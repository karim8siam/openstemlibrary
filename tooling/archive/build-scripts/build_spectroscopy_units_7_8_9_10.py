#!/usr/bin/env python3
"""
build_spectroscopy_units_7_8_9_10.py
Builds Units 7, 8, 9, and 10 for Chemical Spectroscopy.
Unit 7: Photophysical Relaxation: Fluorescence, Phosphorescence & Chiroptical Spectroscopy
Unit 8: Nuclear Magnetic Resonance (NMR) I: Larmor Precession, Relaxation & Proton Chemical Shifts
Unit 9: Nuclear Magnetic Resonance (NMR) II: Spin-Spin Coupling, Decoupling & 2D Pulse Sequences
Unit 10: Electron Spin Resonance (ESR/EPR) & Mössbauer Spectroscopy
"""

import json

def get_units_7_8_9_10():
    units = []

    # =========================================================================
    # UNIT 7: Photophysical Relaxation: Fluorescence, Phosphorescence & Chiroptical Spectroscopy
    # =========================================================================
    u7 = {
        "id": "unit7",
        "number": 7,
        "title": "Unit 7: Photophysical Relaxation: Fluorescence, Phosphorescence & Chiroptical Spectroscopy",
        "description": "Jablonski diagram, radiative and non-radiative photophysical pathways, internal conversion (IC), intersystem crossing (ISC), fluorescence and phosphorescence kinetics, quantum yields, Stern-Volmer quenching, Förster resonance energy transfer (FRET), Circular Dichroism (CD), and Optical Rotatory Dispersion (ORD).",
        "simulations": [
            {
                "id": "sim_spec_jablonski_photophysics",
                "title": "Jablonski Diagram & Photophysical Dynamics",
                "description": "Interactive 60 FPS simulator modeling photoexcitation and relaxation kinetics on a live Jablonski diagram. Pulse excitation light, track molecular transitions through internal conversion, fluorescence, intersystem crossing to triplet T1, and phosphorescence, and vary quencher concentration [Q] to observe real-time Stern-Volmer fluorescence quenching."
            }
        ],
        "sections": [
            {
                "id": "u7-sec1",
                "number": "7.1",
                "title": "The Jablonski Diagram & Timescale Hierarchy of Photophysics",
                "content": r"""<p>The electronic absorption of a photon promotes a molecule from its ground singlet state \(S_0\) to an electronically excited singlet state (\(S_1, S_2 \dots\)) in \(\sim 10^{-15}\text{ s}\). The subsequent dissipation of electronic energy is represented on the <strong>Jablonski diagram</strong>, which categorizes transitions into radiative (accompanied by photon emission) and non-radiative (dissipated as thermal vibrational energy to the solvent bath):</p>
<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Photophysical Process</th>
        <th>Transition Scheme</th>
        <th>Radiative?</th>
        <th>Typical Rate Constant (\(k\))</th>
        <th>Characteristic Timescale</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Light Absorption</strong></td>
        <td>\(S_0 + h\nu \to S_1, S_2\)</td>
        <td>Yes</td>
        <td>-</td>
        <td>\(10^{-15}\text{ s}\) (1 femtosecond)</td>
      </tr>
      <tr>
        <td><strong>Vibrational Relaxation (VR)</strong></td>
        <td>\(S_n(v) \to S_n(0)\)</td>
        <td>No</td>
        <td>\(10^{12} - 10^{14}\text{ s}^{-1}\)</td>
        <td>\(10^{-14} - 10^{-12}\text{ s}\) (sub-picosecond)</td>
      </tr>
      <tr>
        <td><strong>Internal Conversion (IC)</strong></td>
        <td>\(S_n \to S_{n-1}\)</td>
        <td>No</td>
        <td>\(10^{11} - 10^{13}\text{ s}^{-1}\)</td>
        <td>\(10^{-13} - 10^{-11}\text{ s}\)</td>
      </tr>
      <tr>
        <td><strong>Fluorescence</strong></td>
        <td>\(S_1 \to S_0 + h\nu_f\)</td>
        <td>Yes</td>
        <td>\(10^7 - 10^9\text{ s}^{-1}\)</td>
        <td>\(10^{-9} - 10^{-7}\text{ s}\) (1 – 100 nanoseconds)</td>
      </tr>
      <tr>
        <td><strong>Intersystem Crossing (ISC)</strong></td>
        <td>\(S_1 \to T_1\)</td>
        <td>No</td>
        <td>\(10^6 - 10^9\text{ s}^{-1}\)</td>
        <td>\(10^{-9} - 10^{-6}\text{ s}\)</td>
      </tr>
      <tr>
        <td><strong>Phosphorescence</strong></td>
        <td>\(T_1 \to S_0 + h\nu_p\)</td>
        <td>Yes</td>
        <td>\(10^{-2} - 10^4\text{ s}^{-1}\)</td>
        <td>\(10^{-4} - 10^2\text{ s}\) (milliseconds to seconds)</td>
      </tr>
      <tr>
        <td><strong>Triplet Non-Radiative Decay</strong></td>
        <td>\(T_1 \to S_0\)</td>
        <td>No</td>
        <td>\(10^{-1} - 10^3\text{ s}^{-1}\)</td>
        <td>\(10^{-3} - 10^1\text{ s}\)</td>
      </tr>
    </tbody>
  </table>
</div>
<h4 class="content-heading">Kasha's Rule & The Stokes Shift</h4>
<p>Because internal conversion from higher singlet states \(S_n \to S_1\) and vibrational relaxation to \(S_1(v=0)\) occur on sub-picosecond timescales—orders of magnitude faster than fluorescence emission (\(\sim 10^{-9}\text{ s}\))—photon emission occurs almost exclusively from the lowest vibrational level of the lowest excited state \(S_1\). This empirical fact is known as <strong>Kasha's rule</strong>.</p>
<p>As a direct result of rapid vibrational relaxation in both the excited state before emission and in the ground state following emission, the fluorescence emission spectrum is red-shifted (lower energy, longer wavelength) relative to the absorption spectrum. This energetic displacement is the <strong>Stokes shift</strong>.</p>"""
            },
            {
                "id": "u7-sec2",
                "number": "7.2",
                "title": "Fluorescence Kinetics, Quantum Yields & Lifetimes",
                "content": r"""<p>Following instantaneous pulse excitation creating initial excited state population \([S_1]_0\), the rate of disappearance of \(S_1\) is governed by first-order decay kinetics encompassing radiative and non-radiative paths:</p>
\[
-\frac{d[S_1]}{dt} = (k_r + k_{nr}) [S_1]
\]
<p>where \(k_r\) is the radiative rate constant of fluorescence and \(k_{nr} = k_{IC} + k_{ISC}\) is the sum of non-radiative decay rate constants.</p>
<h4 class="content-heading">Fluorescence Lifetime (\(\tau_f\))</h4>
<p>Integrating the rate equation yields exponential population decay:</p>
\[
[S_1](t) = [S_1]_0 \exp\left(-\frac{t}{\tau_f}\right), \quad \tau_f = \frac{1}{k_r + k_{nr}} = \frac{1}{\sum k_i}
\]
<p>where \(\tau_f\) is the <strong>observed fluorescence lifetime</strong>. In the hypothetical absence of all non-radiative pathways (\(k_{nr} = 0\)), the decay time is the <strong>natural radiative lifetime</strong> \(\tau_0\):</p>
\[
\tau_0 = \frac{1}{k_r}
\]
<p>The natural lifetime \(\tau_0\) can be calculated directly from the ground-state absorption band using the <strong>Strickler-Berg formula</strong>:</p>
\[
\frac{1}{\tau_0} = 2.88 \times 10^{-9} n^2 \langle \tilde{\nu}_f^{-3} \rangle^{-1} \int \frac{\varepsilon(\tilde{\nu})}{\tilde{\nu}} d\tilde{\nu}
\]
<h4 class="content-heading">Fluorescence Quantum Yield (\(\Phi_f\))</h4>
<p>The fluorescence quantum yield \(\Phi_f\) is defined as the fraction of absorbed photons that result in the emission of a fluorescence photon:</p>
\[
\Phi_f = \frac{\text{Photons Emitted}}{\text{Photons Absorbed}} = \frac{k_r}{k_r + k_{nr}} = \frac{\tau_f}{\tau_0}
\]
<p>Because \(k_{nr} \ge 0\), the observed lifetime is always shorter than the natural lifetime (\(\tau_f \le \tau_0\)), and the quantum yield is always bounded by unity (\(0 \le \Phi_f \le 1\)).</p>"""
            },
            {
                "id": "u7-sec3",
                "number": "7.3",
                "title": "Intersystem Crossing, Triplet States & Phosphorescence",
                "content": r"""<p>Intersystem crossing (ISC) is an isoenergetic non-radiative transition between electronic states of different spin multiplicity, primarily from singlet \(S_1\) (\(S=0\)) to triplet \(T_1\) (\(S=1\)). In the non-relativistic Hamiltonian, transitions between states of different spin multiplicity are strictly forbidden (\(\Delta S = 0\)).</p>
<h4 class="content-heading">Spin-Orbit Coupling Mechanism & El-Sayed's Rules</h4>
<p>Intersystem crossing is enabled by spin-orbit coupling \(\hat{H}_{SO} = \sum \xi_i \vec{l}_i \cdot \vec{s}_i\), which mixes pure singlet and triplet wavefunctions:</p>
\[
\langle T_1 | \hat{H}_{SO} | S_1 \rangle \neq 0
\]
<p>El-Sayed formulated empirical selection rules governing the rate of intersystem crossing:</p>
<blockquote>
  <strong>El-Sayed's Rules:</strong> Intersystem crossing is orders of magnitude faster if it involves a change in molecular orbital type (\(^1(n, \pi^*) \leftrightarrow {}^3(\pi, \pi^*)\) or \(^1(\pi, \pi^*) \leftrightarrow {}^3(n, \pi^*)\)) than if it occurs between states of the same orbital type (\(^1(\pi, \pi^*) \leftrightarrow {}^3(\pi, \pi^*)\) or \(^1(n, \pi^*) \leftrightarrow {}^3(n, \pi^*)\)).
</blockquote>
<h4 class="content-heading">The Heavy-Atom Effect</h4>
<p>Because the spin-orbit parameter \(\xi\) scales as \(Z^4\), substituting heavy halogen atoms (Br, I) or transition metals (Pt, Ir, Ru) into the molecular scaffold (internal heavy-atom effect) or solvent matrix (external heavy-atom effect) dramatically accelerates ISC by up to \(10^6\)-fold, quenching fluorescence while enhancing phosphorescence.</p>
<h4 class="content-heading">Phosphorescence Kinetics</h4>
<p>Once populated, the triplet state \(T_1\) is trapped: radiative relaxation to the ground singlet state \(S_0\) (\(T_1 \to S_0 + h\nu_p\)) is spin-forbidden. Consequently, the radiative rate constant \(k_p\) is extraordinarily small (\(10^{-2} - 10^3\text{ s}^{-1}\)), resulting in long emission lifetimes (\(\tau_p \sim 10^{-3} - 10\text{ seconds}\)). In fluid solution at room temperature, phosphorescence is usually quenched by dissolved paramagnetic molecular oxygen (\(^3\Sigma_g^-\)) via triplet-triplet energy transfer; it is readily observed in rigid frozen glasses or deoxygenated matrices.</p>"""
            },
            {
                "id": "u7-sec4",
                "number": "7.4",
                "title": "Fluorescence Quenching & The Stern-Volmer Equation",
                "content": r"""<p>Fluorescence quenching denotes any bimolecular process that reduces the fluorescence intensity of a fluorophore \(M^*\). Quenching mechanisms fall into two primary physical categories:</p>
<h4 class="content-heading">1. Dynamic (Collisional) Quenching</h4>
<p>In dynamic quenching, the excited fluorophore \(M^*\) collides with a quencher molecule \(Q\) during the lifetime of the excited state, dissipating energy non-radiatively with bimolecular rate constant \(k_q\):</p>
\[
M^* + Q \xrightarrow{k_q} M + Q + \text{heat}
\]
<p>In the presence of quencher \([Q]\), the rate of deactivation of \(M^*\) becomes:</p>
\[
-\frac{d[M^*]}{dt} = (k_r + k_{nr} + k_q [Q]) [M^*]
\]
<p>The fluorescence quantum yield in the presence of quencher is \(\Phi_f = \frac{k_r}{k_r + k_{nr} + k_q [Q]}\). The ratio of unquenched fluorescence intensity \(F_0\) to quenched intensity \(F\) yields the <strong>Stern-Volmer equation</strong>:</p>
\[
\frac{F_0}{F} = \frac{\Phi_{f,0}}{\Phi_f} = \frac{\tau_0}{\tau} = 1 + \tau_0 k_q [Q] = 1 + K_{SV} [Q]
\]
<p>where \(K_{SV} = k_q \tau_0\) is the <strong>Stern-Volmer quenching constant</strong>, and \(\tau_0 = (k_r + k_{nr})^{-1}\) is the unquenched lifetime. A plot of \(F_0 / F\) versus \([Q]\) yields a straight line with slope \(K_{SV}\) and intercept 1. In dynamic quenching, the fluorescence lifetime decreases proportionally: \(\frac{\tau_0}{\tau} = \frac{F_0}{F}\).</p>
<h4 class="content-heading">2. Static Quenching</h4>
<p>In static quenching, a non-fluorescent ground-state complex forms between fluorophore and quencher with association constant \(K_S\): \(M + Q \rightleftharpoons [MQ]\). Only uncomplexed fluorophore molecules emit light. The intensity ratio is:</p>
\[
\frac{F_0}{F} = 1 + K_S [Q]
\]
<p>Crucially, because complexed molecules do not emit, the lifetime of the remaining uncomplexed fluorophores is completely unaffected: \(\frac{\tau_0}{\tau} = 1\). This lifetime invariance provides the unambiguous experimental criterion for distinguishing static from dynamic quenching.</p>"""
            },
            {
                "id": "u7-sec5",
                "number": "7.5",
                "title": "Förster Resonance Energy Transfer (FRET) & Molecular Rulers",
                "content": r"""<p>Förster Resonance Energy Transfer (FRET) is a non-radiative, through-space dipole-dipole energy transfer process in which an excited donor fluorophore \(D^*\) transfers electronic excitation energy to an acceptor chromophore \(A\):</p>
\[
D^* + A \to D + A^*
\]
<p>The rate of energy transfer \(k_{ET}\) derived by Theodor Förster is inversely proportional to the <strong>sixth power</strong> of the donor-acceptor separation distance \(r\):</p>
\[
k_{ET}(r) = \frac{1}{\tau_D} \left(\frac{R_0}{r}\right)^6
\]
<p>where \(\tau_D\) is the donor fluorescence lifetime in the absence of acceptor, and \(R_0\) is the <strong>Förster critical distance</strong> (the distance at which energy transfer efficiency is exactly \(50\%\)):</p>
\[
R_0^6 = \frac{9000 (\ln 10) \kappa^2 \Phi_D}{128 \pi^5 N_A n^4} J(\lambda)
\]
<ul>
  <li>\(\kappa^2\): Orientation factor between donor and acceptor transition dipole vectors (for isotropic dynamic tumbling, \(\kappa^2 = 2/3\)).</li>
  <li>\(\Phi_D\): Donor fluorescence quantum yield.</li>
  <li>\(n\): Refractive index of the medium.</li>
  <li>\(J(\lambda) = \int_0^\infty F_D(\lambda) \varepsilon_A(\lambda) \lambda^4 d\lambda\): Spectral overlap integral between normalized donor emission \(F_D(\lambda)\) and acceptor molar absorptivity \(\varepsilon_A(\lambda)\).</li>
</ul>
<h4 class="content-heading">FRET Efficiency & Distance Measurement</h4>
<p>The energy transfer efficiency \(E\) is defined as:</p>
\[
E = \frac{k_{ET}}{k_{ET} + \tau_D^{-1}} = \frac{R_0^6}{R_0^6 + r^6} = 1 - \frac{F_{DA}}{F_D} = 1 - \frac{\tau_{DA}}{\tau_D}
\]
<p>Because typical Förster distances range from \(20 - 70\text{ \AA}\) (\(2 - 7\text{ nm}\)), which perfectly matches the dimensions of biological macromolecules, FRET functions as a 'spectroscopic ruler' for measuring sub-nanometer conformational changes in proteins, nucleic acids, and macromolecular assemblies.</p>"""
            },
            {
                "id": "u7-sec6",
                "number": "7.6",
                "title": "Circular Dichroism (CD) & Optical Rotatory Dispersion (ORD)",
                "content": r"""<p>Chiroptical spectroscopy probes the differential interaction of chiral molecules with circularly polarized light:</p>
<h4 class="content-heading">1. Circular Dichroism (CD)</h4>
<p>Circular Dichroism measures the differential absorption of left-circularly polarized (LCP) and right-circularly polarized (RCP) light by a chiral medium:</p>
\[
\Delta A = A_L - A_R = (\varepsilon_L - \varepsilon_R) b c = \Delta \varepsilon b c
\]
<p>where \(\Delta\varepsilon = \varepsilon_L - \varepsilon_R\) is the molar circular dichroism (\(\text{L}/(\text{mol}\cdot\text{cm})\)). In passing through the sample, unequal absorption transforms linearly polarized light into elliptically polarized light with ellipticity \(\theta\) (radians):</p>
\[
\theta = \frac{\ln 10}{4} (A_L - A_R) = \frac{\ln 10}{4} \Delta A
\]
<p>In degrees, \(\theta\ (\text{deg}) = 32.982 \Delta A\). The <strong>molar ellipticity</strong> \([\theta]\) (\(\text{deg}\cdot\text{cm}^2/\text{dmol}\)) is universally reported:</p>
\[
[\theta] = 3298.2 \Delta\varepsilon
\]
<h4 class="content-heading">2. Optical Rotatory Dispersion (ORD)</h4>
<p>Optical Rotatory Dispersion measures the rotation angle \(\alpha(\lambda)\) of the plane of linearly polarized light as a function of wavelength. Circular birefringence arises from differential refractive indices \(n_L \neq n_R\):</p>
\[
\alpha = \frac{\pi}{\lambda} (n_L - n_R) b
\]
<h4 class="content-heading">The Cotton Effect & Kramers-Kronig Transforms</h4>
<p>Near an absorption band of a chiral chromophore, CD and ORD exhibit anomalous dispersion known as the <strong>Cotton effect</strong>. If \(\Delta\varepsilon > 0\), the Cotton effect is positive (peak at higher wavelength, trough at lower in ORD). CD and ORD are mathematically connected by the <strong>Kramers-Kronig relations</strong>: measuring CD over all absorption bands uniquely determines the ORD curve.</p>"""
            },
            {
                "id": "u7-sec7",
                "number": "7.7",
                "title": "Protein Secondary Structure Deconvolution by Far-UV CD",
                "content": r"""<p>In the far-ultraviolet region (\(190 - 250\text{ nm}\)), CD spectra are dominated by the electronic transitions of the peptide amide backbone (\(n \to \pi^*\) at \(\sim 222\text{ nm}\) and exciton-split \(\pi \to \pi^*\) at \(\sim 208\text{ nm}\) and \(192\text{ nm}\)). The spatial arrangement of consecutive amide dipoles produces distinctive CD signatures:</p>
<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Secondary Structure Motif</th>
        <th>Characteristic Spectral Features</th>
        <th>Representative Molar Ellipticity \([\theta]\)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>\(\alpha\)-Helix</strong></td>
        <td>Two negative minima at \(222\text{ nm}\) and \(208\text{ nm}\); strong positive peak at \(193\text{ nm}\)</td>
        <td>\([\theta]_{222} \approx -35000\text{ deg}\cdot\text{cm}^2/\text{dmol}\)</td>
      </tr>
      <tr>
        <td><strong>\(\beta\)-Sheet</strong></td>
        <td>Single negative minimum at \(217 - 218\text{ nm}\); positive peak at \(195\text{ nm}\)</td>
        <td>\([\theta]_{217} \approx -15000\text{ deg}\cdot\text{cm}^2/\text{dmol}\)</td>
      </tr>
      <tr>
        <td><strong>\(\beta\)-Turn</strong></td>
        <td>Weak positive peak at \(205\text{ nm}\); negative band at \(190\text{ nm}\)</td>
        <td>Variable</td>
      </tr>
      <tr>
        <td><strong>Random Coil (Unfolded)</strong></td>
        <td>Strong negative band near \(198 - 200\text{ nm}\); near-zero ellipticity above \(215\text{ nm}\)</td>
        <td>\([\theta]_{198} \approx -20000\text{ deg}\cdot\text{cm}^2/\text{dmol}\)</td>
      </tr>
    </tbody>
  </table>
</div>
<h4 class="content-heading">Quantitative Deconvolution Algorithms</h4>
<p>The experimental CD spectrum of a protein \([\theta](\lambda)\) is modeled as a linear combination of basis spectra \([\theta]_k(\lambda)\) weighted by secondary structure fractions \(f_k\):</p>
\[
[\theta](\lambda) = \sum_k f_k [\theta]_k(\lambda), \quad \text{subject to } \sum_k f_k = 1, \ f_k \ge 0
\]
<p>Algorithms such as CONTINLL, SELCON3, and CDSSTR solve this constrained matrix inversion using reference sets of structurally solved proteins, providing rapid assessment of protein folding, thermal stability, and ligand-induced conformational shifts.</p>"""
            }
        ],
        "problems": [
            {
                "id": "u7-prob1",
                "number": 1,
                "title": "Calculation of Fluorescence Quantum Yield and Radiative Rate Constants",
                "difficulty": "Foundational",
                "statement": r"""A fluorescent dye in aqueous buffer has an observed fluorescence lifetime of \(\tau_f = 4.20\text{ ns}\) and a fluorescence quantum yield of \(\Phi_f = 0.650\).
(a) Calculate the radiative rate constant \(k_r\).
(b) Calculate the total non-radiative rate constant \(k_{nr}\).
(c) Determine the natural radiative lifetime \(\tau_0\) of the fluorophore.""",
                "solution": r"""<p><strong>Step (a): Radiative rate constant kr</strong></p>
<p>From the definitions of quantum yield and lifetime:</p>
\[
\Phi_f = k_r \tau_f \implies k_r = \frac{\Phi_f}{\tau_f}
\]
\[
k_r = \frac{0.650}{4.20 \times 10^{-9}\text{ s}} = 1.548 \times 10^8\text{ s}^{-1}
\]
<p><strong>Step (b): Non-radiative rate constant knr</strong></p>
<p>The total decay rate is \(\tau_f^{-1} = k_r + k_{nr}\):</p>
\[
k_r + k_{nr} = \frac{1}{4.20 \times 10^{-9}\text{ s}} = 2.381 \times 10^8\text{ s}^{-1}
\]
\[
k_{nr} = 2.381 \times 10^8 - 1.548 \times 10^8 = 8.33 \times 10^7\text{ s}^{-1}
\]
<p><strong>Step (c): Natural radiative lifetime tau_0</strong></p>
\[
\tau_0 = \frac{1}{k_r} = \frac{1}{1.548 \times 10^8\text{ s}^{-1}} = 6.46 \times 10^{-9}\text{ s} = 6.46\text{ ns}
\]
<p>Equivalently:</p>
\[
\tau_0 = \frac{\tau_f}{\Phi_f} = \frac{4.20\text{ ns}}{0.650} = 6.46\text{ ns}
\]"""
            },
            {
                "id": "u7-prob2",
                "number": 2,
                "title": "Stern-Volmer Quenching Analysis of Tryptophan by Acrylamide",
                "difficulty": "Intermediate",
                "statement": r"""The fluorescence of a tryptophan residue in a protein (\(\tau_0 = 3.20\text{ ns}\)) is quenched by addition of acrylamide. Fluorescence intensities are measured as a function of acrylamide concentration \([Q]\):
\([Q] = 0.00\text{ M}\): \(F = 100.0\)
\([Q] = 0.02\text{ M}\): \(F = 80.0\)
\([Q] = 0.05\text{ M}\): \(F = 62.5\)
\([Q] = 0.10\text{ M}\): \(F = 45.5\)
\([Q] = 0.20\text{ M}\): \(F = 29.4\)
(a) Plot or calculate the Stern-Volmer quenching constant \(K_{SV}\).
(b) Calculate the bimolecular quenching rate constant \(k_q\) in \(\text{M}^{-1}\text{s}^{-1}\).
(c) Compare \(k_q\) with the diffusion-controlled limit in water (\(k_{\text{diff}} \approx 7 \times 10^9\text{ M}^{-1}\text{s}^{-1}\)) and evaluate whether the tryptophan residue is solvent-exposed or buried.""",
                "solution": r"""<p><strong>Step (a): Stern-Volmer analysis</strong></p>
<p>Calculate \(F_0 / F\) for each point:</p>
<ul>
  <li>\([Q] = 0.02\text{ M}\): \(F_0/F = 100.0 / 80.0 = 1.250\) \(\implies K_{SV} = (1.250 - 1) / 0.02 = 12.50\text{ M}^{-1}\)</li>
  <li>\([Q] = 0.05\text{ M}\): \(F_0/F = 100.0 / 62.5 = 1.600\) \(\implies K_{SV} = (1.600 - 1) / 0.05 = 12.00\text{ M}^{-1}\)</li>
  <li>\([Q] = 0.10\text{ M}\): \(F_0/F = 100.0 / 45.5 = 2.198\) \(\implies K_{SV} = (2.198 - 1) / 0.10 = 11.98\text{ M}^{-1}\)</li>
  <li>\([Q] = 0.20\text{ M}\): \(F_0/F = 100.0 / 29.4 = 3.401\) \(\implies K_{SV} = (3.401 - 1) / 0.20 = 12.01\text{ M}^{-1}\)</li>
</ul>
<p>The average Stern-Volmer quenching constant is:</p>
\[
K_{SV} = 12.1\text{ M}^{-1}
\]
<p><strong>Step (b): Bimolecular quenching rate constant kq</strong></p>
\[
k_q = \frac{K_{SV}}{\tau_0} = \frac{12.1\text{ M}^{-1}}{3.20 \times 10^{-9}\text{ s}} = 3.78 \times 10^9\text{ M}^{-1}\text{s}^{-1}
\]
<p><strong>Step (c): Exposure evaluation</strong></p>
<p>The calculated rate constant \(k_q = 3.78 \times 10^9\text{ M}^{-1}\text{s}^{-1}\) is on the order of the diffusion-controlled limit in aqueous solution (\(\approx 7 \times 10^9\text{ M}^{-1}\text{s}^{-1}\)). This near-diffusion-controlled efficiency indicates that the tryptophan indole ring is located on the outer surface of the folded protein, readily accessible to collisional encounters with neutral acrylamide quenchers in solution.</p>"""
            },
            {
                "id": "u7-prob3",
                "number": 3,
                "title": "FRET Efficiency and Inter-Domain Distance Measurement in Protein",
                "difficulty": "Intermediate",
                "statement": r"""A FRET pair consisting of Cy3 (donor) and Cy5 (acceptor) has a calibrated Förster distance \(R_0 = 54.0\text{ \AA}\).
In a dual-labeled protein, the fluorescence lifetime of the Cy3 donor is measured:
In the absence of acceptor: \(\tau_D = 2.40\text{ ns}\).
In the presence of the Cy5 acceptor: \(\tau_{DA} = 0.72\text{ ns}\).
(a) Calculate the FRET efficiency \(E\).
(b) Calculate the inter-dye distance \(r\) in Angstroms (\(\text{\AA}\)).
(c) Upon addition of an allosteric inhibitor, \(\tau_{DA}\) increases to \(1.80\text{ ns}\). Calculate the new inter-dye distance and explain the conformational change.""",
                "solution": r"""<p><strong>Step (a): FRET efficiency calculation</strong></p>
\[
E = 1 - \frac{\tau_{DA}}{\tau_D} = 1 - \frac{0.72\text{ ns}}{2.40\text{ ns}} = 1 - 0.300 = 0.700 = 70.0\%
\]
<p><strong>Step (b): Initial inter-dye distance r</strong></p>
\[
E = \frac{R_0^6}{R_0^6 + r^6} \implies \frac{1}{E} = 1 + \left(\frac{r}{R_0}\right)^6 \implies \left(\frac{r}{R_0}\right)^6 = \frac{1 - E}{E}
\]
\[
\left(\frac{r}{R_0}\right)^6 = \frac{1 - 0.700}{0.700} = \frac{0.300}{0.700} = 0.42857
\]
\[
r = R_0 (0.42857)^{1/6} = 54.0\text{ \AA} \times (0.8688) = 46.9\text{ \AA}
\]
<p><strong>Step (c): Inhibited conformation distance</strong></p>
\[
E_{\text{inhib}} = 1 - \frac{1.80}{2.40} = 1 - 0.750 = 0.250 = 25.0\%
\]
\[
\left(\frac{r_{\text{inhib}}}{R_0}\right)^6 = \frac{1 - 0.250}{0.250} = \frac{0.750}{0.250} = 3.000
\]
\[
r_{\text{inhib}} = 54.0\text{ \AA} \times (3.000)^{1/6} = 54.0\text{ \AA} \times (1.2009) = 64.8\text{ \AA}
\]
<p>The inter-dye distance increased from \(46.9\text{ \AA}\) to \(64.8\text{ \AA}\) (\(\Delta r = +17.9\text{ \AA}\)), revealing that the inhibitor induces a major conformational opening that separates the two labeled protein domains.</p>"""
            },
            {
                "id": "u7-prob4",
                "number": 4,
                "title": "Molar Ellipticity Conversion and Helix Content Estimation by CD",
                "difficulty": "Intermediate",
                "statement": r"""A \(0.150\text{ mg/mL}\) solution of a 150-residue globular protein (mean residue weight \(\text{MRW} = 110.0\text{ g/mol}\)) is analyzed in a \(0.100\text{ cm}\) pathlength CD cuvette.
At \(\lambda = 222\text{ nm}\), the recorded instrument ellipticity is \(\theta = -12.5\text{ millidegrees}\).
(a) Calculate the mean residue molar ellipticity \([\theta]_{222}\) in \(\text{deg}\cdot\text{cm}^2/\text{dmol}\).
(b) Estimate the percentage \(\alpha\)-helical content \(f_H\) using the empirical formula:
\[
f_H = \frac{[\theta]_{222} - [\theta]_C}{[\theta]_H - [\theta]_C}
\]
where \([\theta]_H = -40000(1 - 2.5/n_r)\text{ deg}\cdot\text{cm}^2/\text{dmol}\) for a 100% helix (\(n_r = 150\)), and \([\theta]_C = -3000\text{ deg}\cdot\text{cm}^2/\text{dmol}\) for a random coil.""",
                "solution": r"""<p><strong>Step (a): Mean residue molar ellipticity calculation</strong></p>
<p>The mean residue molar ellipticity is defined as:</p>
\[
[\theta] = \frac{\theta\ (\text{deg}) \times \text{MRW}}{10 \times c\ (\text{g/cm}^3) \times b\ (\text{cm})}
\]
<p>Parameters:</p>
<ul>
  <li>\(\theta = -12.5\text{ mdeg} = -0.0125\text{ deg}\)</li>
  <li>\(\text{MRW} = 110.0\text{ g/mol}\)</li>
  <li>\(c = 0.150\text{ mg/mL} = 0.150 \times 10^{-3}\text{ g/cm}^3\)</li>
  <li>\(b = 0.100\text{ cm}\)</li>
</ul>
\[
[\theta]_{222} = \frac{(-0.0125)(110.0)}{10 \times (0.150 \times 10^{-3}) \times 0.100} = \frac{-1.375}{1.50 \times 10^{-4}} = -9167\text{ deg}\cdot\text{cm}^2/\text{dmol}
\]
<p><strong>Step (b): Alpha-helix percentage content</strong></p>
\[
[\theta]_H = -40000 \left(1 - \frac{2.5}{150}\right) = -40000(1 - 0.01667) = -40000(0.98333) = -39333\text{ deg}\cdot\text{cm}^2/\text{dmol}
\]
\[
[\theta]_C = -3000\text{ deg}\cdot\text{cm}^2/\text{dmol}
\]
\[
f_H = \frac{-9167 - (-3000)}{-39333 - (-3000)} = \frac{-6167}{-36333} = 0.1697 \approx 17.0\%
\]
<p>The protein contains approximately \(17.0\%\) \(\alpha\)-helical secondary structure.</p>"""
            },
            {
                "id": "u7-prob5",
                "number": 5,
                "title": "Kinetics of Triplet State Phosphorescence and Oxygen Quenching",
                "difficulty": "Intermediate",
                "statement": r"""A polycyclic aromatic hydrocarbon has a triplet state radiative decay rate constant \(k_p = 0.25\text{ s}^{-1}\) and an intrinsic non-radiative decay rate constant \(k_{TS} = 0.75\text{ s}^{-1}\).
(a) Calculate the phosphorescence quantum yield \(\Phi_p\) and lifetime \(\tau_p\) in a rigid degassed matrix at \(77\text{ K}\) assuming unity intersystem crossing (\(\Phi_{ISC} = 1.0\)).
(b) In aerated liquid solution at \(298\text{ K}\), dissolved molecular oxygen has concentration \([O_2] = 2.1 \times 10^{-4}\text{ M}\) and quenches the triplet state with rate constant \(k_q = 2.5 \times 10^9\text{ M}^{-1}\text{s}^{-1}\). Calculate the phosphorescence lifetime and quantum yield in the presence of dissolved oxygen.
(c) By what factor is phosphorescence quenched by air?""",
                "solution": r"""<p><strong>Step (a): Degassed matrix at 77 K</strong></p>
\[
\tau_{p,0} = \frac{1}{k_p + k_{TS}} = \frac{1}{0.25 + 0.75} = \frac{1}{1.00\text{ s}^{-1}} = 1.00\text{ second}
\]
\[
\Phi_{p,0} = \Phi_{ISC} \frac{k_p}{k_p + k_{TS}} = 1.0 \times \frac{0.25}{1.00} = 0.250 = 25.0\%
\]
<p><strong>Step (b): Aerated liquid solution at 298 K</strong></p>
<p>The oxygen quenching rate is:</p>
\[
R_{\text{quench}} = k_q [O_2] = (2.5 \times 10^9\text{ M}^{-1}\text{s}^{-1})(2.1 \times 10^{-4}\text{ M}) = 5.25 \times 10^5\text{ s}^{-1}
\]
<p>The total decay rate in the presence of oxygen is:</p>
\[
k_{\text{tot}} = k_p + k_{TS} + k_q [O_2] = 1.00 + 5.25 \times 10^5 \approx 5.25 \times 10^5\text{ s}^{-1}
\]
\[
\tau_p = \frac{1}{5.25 \times 10^5\text{ s}^{-1}} = 1.905 \times 10^{-6}\text{ s} = 1.905\ \mu\text{s}
\]
\[
\Phi_p = \Phi_{ISC} \frac{k_p}{k_{\text{tot}}} = 1.0 \times \frac{0.25}{5.25 \times 10^5} = 4.76 \times 10^{-7}
\]
<p><strong>Step (c): Quenching factor</strong></p>
\[
\frac{\Phi_{p,0}}{\Phi_p} = \frac{0.25}{4.76 \times 10^{-7}} = 5.25 \times 10^5
\]
<p>Phosphorescence is quenched by more than five hundred thousand-fold by dissolved oxygen!</p>"""
            },
            {
                "id": "u7-prob6",
                "number": 6,
                "title": "Determination of Static vs Dynamic Quenching by Variable Temperature",
                "difficulty": "Foundational",
                "statement": r"""A fluorophore is quenched by a synthetic quencher at two different temperatures, and the Stern-Volmer constant \(K_{SV}\) is measured:
At \(T = 20^\circ\text{C}\) (\(293\text{ K}\)): \(K_{SV} = 345\text{ M}^{-1}\)
At \(T = 50^\circ\text{C}\) (\(323\text{ K}\)): \(K_{SV} = 192\text{ M}^{-1}\)
(a) Determine whether the quenching mechanism is predominantly dynamic or static.
(b) Explain the thermodynamic rationale for how temperature distinguishes the two mechanisms.""",
                "solution": r"""<p><strong>Step (a): Mechanism identification</strong></p>
<p>As the temperature increases from \(20^\circ\text{C}\) to \(50^\circ\text{C}\), the Stern-Volmer quenching constant decreases from \(345\text{ M}^{-1}\) to \(192\text{ M}^{-1}\).</p>
<p>This temperature dependence proves that the quenching is predominantly <strong>static quenching</strong>.</p>
<p><strong>Step (b): Physical rationale</strong></p>
<ul>
  <li><strong>Dynamic Quenching:</strong> Relies on diffusion. As temperature rises, viscosity decreases and molecular velocities increase, increasing the diffusion coefficient \(D \propto T / \eta\). Therefore, the bimolecular rate constant \(k_q\) and \(K_{SV} = k_q \tau_0\) <em>increase</em> with temperature.</li>
  <li><strong>Static Quenching:</strong> Relies on ground-state complex formation with stability constant \(K_S\). Complex formation is exothermic (\(\Delta H^\circ < 0\)). As temperature rises, thermal agitation dissociates the weakly bound complex according to the van 't Hoff equation, causing \(K_S\) and \(K_{SV}\) to <em>decrease</em> with temperature.</li>
</ul>"""
            },
            {
                "id": "u7-prob7",
                "number": 7,
                "title": "Quantum Yield Measurement by Relative Actinometry",
                "difficulty": "Intermediate",
                "statement": r"""The fluorescence quantum yield of a newly synthesized organic fluorophore (X) is measured relative to a quinine sulfate reference standard (R, \(\Phi_R = 0.540\) in \(0.1\text{ M}\ \text{H}_2\text{SO}_4\), \(n_R = 1.333\)).
Both solutions are prepared with identical absorbance at excitation wavelength \(\lambda_{\text{ex}} = 350\text{ nm}\): \(A_X = A_R = 0.045\) in a \(1.00\text{ cm}\) cell.
Fluorophore X is dissolved in ethanol (\(n_X = 1.361\)).
Integrated fluorescence emission intensities are:
Reference (Quinine Sulfate): \(I_R = 1.450 \times 10^6\text{ counts}\)
Unknown Sample X: \(I_X = 2.120 \times 10^6\text{ counts}\)
(a) Calculate the absolute fluorescence quantum yield \(\Phi_X\).
(b) Why is it imperative to keep the solution absorbance below \(0.05\) during relative quantum yield measurements?""",
                "solution": r"""<p><strong>Step (a): Relative quantum yield formula</strong></p>
<p>The comparative quantum yield equation is:</p>
\[
\Phi_X = \Phi_R \times \left(\frac{I_X}{I_R}\right) \times \left(\frac{A_R}{A_X}\right) \times \left(\frac{n_X^2}{n_R^2}\right)
\]
<p>Since \(A_R = A_X = 0.045\), the absorbance ratio is unity:</p>
\[
\Phi_X = 0.540 \times \left(\frac{2.120 \times 10^6}{1.450 \times 10^6}\right) \times (1.000) \times \left(\frac{1.361^2}{1.333^2}\right)
\]
\[
\frac{I_X}{I_R} = \frac{2.120}{1.450} = 1.4621
\]
\[
\frac{n_X^2}{n_R^2} = \frac{1.8523}{1.7769} = 1.0424
\]
\[
\Phi_X = 0.540 \times 1.4621 \times 1.0424 = 0.823
\]
<p>The quantum yield of sample X is \(0.823\) (\(82.3\%\)).</p>
<p><strong>Step (b): Low absorbance requirement</strong></p>
<p>The fraction of light absorbed is \(f_{\text{abs}} = 1 - 10^{-A} = 1 - e^{-2.303 A}\). For small \(A\) (\(A \le 0.05\)), expanding the exponential gives \(f_{\text{abs}} \approx 2.303 A\), making absorbed power strictly linear with absorbance.</p>
<p>At higher absorbances (\(A > 0.1\)), inner filter effects occur: non-linear excitation attenuation along the cuvette path and self-absorption of emitted photons severely distort fluorescence intensity.</p>"""
            }
        ]
    }
    units.append(u7)

    # =========================================================================
    # UNIT 8: Nuclear Magnetic Resonance (NMR) I: Larmor Precession, Relaxation & Proton Chemical Shifts
    # =========================================================================
    u8 = {
        "id": "unit8",
        "number": 8,
        "title": "Unit 8: Nuclear Magnetic Resonance (NMR) I: Larmor Precession, Relaxation & Proton Chemical Shifts",
        "description": "Nuclear spin angular momentum, nuclear Zeeman interaction, nuclear g-factor, Boltzmann population differences, Larmor precession, phenomenological Bloch equations, longitudinal (T1) and transverse (T2) relaxation, Fourier transform NMR (FT-NMR), nuclear shielding tensors, proton chemical shifts, inductive and resonance influences, magnetic anisotropy and ring currents, and chemical exchange dynamics.",
        "simulations": [
            {
                "id": "sim_spec_nmr_larmor_bloch_precession",
                "title": "Nuclear Larmor Precession & Bloch Relaxation (FID)",
                "description": "Interactive 60 FPS simulator modeling nuclear spin magnetization precession and relaxation on the Bloch sphere. Apply 90-degree and 180-degree RF pulses, watch the macroscopic magnetization vector M precess at Larmor frequency, trace the Free Induction Decay (FID) signal oscilloscope, and adjust T1 and T2 relaxation times."
            }
        ],
        "sections": [
            {
                "id": "u8-sec1",
                "number": "8.1",
                "title": "Nuclear Spin Angular Momentum & Nuclear Zeeman Splitting",
                "content": r"""<p>Atomic nuclei possessing an odd number of protons, an odd number of neutrons, or both, exhibit intrinsic nuclear spin angular momentum \(\vec{I}\). The magnitude of \(\vec{I}\) and its projection along a quantization \(z\)-axis are quantized:</p>
\[
|\vec{I}| = \hbar \sqrt{I(I+1)}, \quad I_z = m_I \hbar \quad (m_I = -I, -I+1, \dots, +I)
\]
<p>where \(I\) is the nuclear spin quantum number (\(I = 1/2\) for \(^1\text{H}, ^{13}\text{C}, ^{19}\text{F}, ^{31}\text{P}\); \(I = 1\) for \(^2\text{H}, ^{14}\text{N}\); \(I = 0\) for \(^{12}\text{C}, ^{16}\text{O}\)).</p>
<h4 class="content-heading">Nuclear Magnetic Dipole Moment</h4>
<p>The spinning nuclear charge produces a collinear magnetic dipole moment \(\vec{\mu}_N\):</p>
\[
\vec{\mu}_N = \gamma_N \vec{I} = g_N \mu_N \frac{\vec{I}}{\hbar}
\]
<p>where \(\gamma_N\) is the <strong>gyromagnetic ratio</strong> (a fundamental constant characteristic of each nuclide), \(g_N\) is the nuclear \(g\)-factor, and \(\mu_N = \frac{e\hbar}{2m_p} = 5.05078 \times 10^{-27}\text{ J/T}\) is the nuclear magneton. For the proton (\(^1\text{H}\)), \(\gamma_H = 2.67522 \times 10^8\text{ rad}/(\text{s}\cdot\text{T})\) (\(\frac{\gamma_H}{2\pi} = 42.577\text{ MHz/T}\)).</p>
<h4 class="content-heading">The Nuclear Zeeman Interaction</h4>
<p>Placing the nucleus in a static magnetic field \(\vec{B}_0 = B_0 \hat{z}\) produces the Zeeman Hamiltonian:</p>
\[
\hat{H}_Z = -\vec{\mu}_N \cdot \vec{B}_0 = -\gamma_N \hbar B_0 \hat{I}_z
\]
<p>The energy eigenvalues for magnetic quantum numbers \(m_I\) are:</p>
\[
E(m_I) = -\gamma_N \hbar B_0 m_I
\]
<p>For a spin \(I = 1/2\) nucleus (\(^1\text{H}\)), the field splits the state into two energy levels:</p>
<ul>
  <li>Lower state (\(\alpha\), \(m_I = +1/2\)): aligned with the field, \(E_\alpha = -\frac{1}{2}\gamma_N \hbar B_0\)</li>
  <li>Upper state (\(\beta\), \(m_I = -1/2\)): aligned against the field, \(E_\beta = +\frac{1}{2}\gamma_N \hbar B_0\)</li>
</ul>
<p>The energy separation is:</p>
\[
\Delta E = E_\beta - E_\alpha = \gamma_N \hbar B_0 = h \nu_0
\]
<p>Resonance absorption occurs at the <strong>Larmor frequency</strong>: \(\nu_0 = \frac{\gamma_N}{2\pi} B_0\). For protons in a \(7.046\text{ T}\) magnet, \(\nu_0 = 300\text{ MHz}\); in a \(14.092\text{ T}\) magnet, \(\nu_0 = 600\text{ MHz}\).</p>"""
            },
            {
                "id": "u8-sec2",
                "number": "8.2",
                "title": "Boltzmann Populations & Classical Larmor Precession",
                "content": r"""<p>The energetic splitting \(\Delta E = \hbar\omega_0\) in NMR is extraordinarily small compared to thermal energy at room temperature (\(\Delta E \approx 10^{-25}\text{ J} \ll k_B T \approx 4 \times 10^{-21}\text{ J}\)).</p>
<h4 class="content-heading">Fractional Boltzmann Excess</h4>
<p>According to the Maxwell-Boltzmann distribution:</p>
\[
\frac{N_\beta}{N_\alpha} = \exp\left(-\frac{\Delta E}{k_B T}\right) = \exp\left(-\frac{\gamma_N \hbar B_0}{k_B T}\right)
\]
<p>Expanding the exponential in a first-order Taylor series (\(e^{-x} \approx 1 - x\)):</p>
\[
\frac{N_\alpha - N_\beta}{N_\alpha + N_\beta} \approx \frac{\gamma_N \hbar B_0}{2 k_B T}
\]
<p>For protons at \(300\text{ MHz}\) (\(B_0 = 7.05\text{ T}\)) at \(T = 300\text{ K}\):</p>
\[
\frac{\gamma_N \hbar B_0}{2 k_B T} \approx 2.4 \times 10^{-5}
\]
<p>Out of two million proton spins, only about 48 excess spins populate the lower state! This minute population bias generates the macroscopic net magnetization vector \(\vec{M}_0 = \sum \vec{\mu}_i = \frac{N \gamma_N^2 \hbar^2 I(I+1)}{3 k_B T} \vec{B}_0\) and explains why NMR requires high magnetic fields and signal averaging.</p>
<h4 class="content-heading">Classical Torque & Larmor Precession</h4>
<p>Classically, the static magnetic field exerts a torque \(\vec{\tau} = \vec{M} \times \vec{B}_0\) on the macroscopic magnetization vector. Since torque equals the time rate of change of angular momentum \(\vec{L} = \vec{M} / \gamma\):</p>
\[
\frac{d\vec{M}}{dt} = \gamma_N (\vec{M} \times \vec{B}_0)
\]
<p>This differential equation describes a steady precession of \(\vec{M}\) around \(\vec{B}_0\) at angular frequency \(\vec{\omega}_0 = -\gamma_N \vec{B}_0\).</p>"""
            },
            {
                "id": "u8-sec3",
                "number": "8.3",
                "title": "Spin Relaxation: Bloch Equations, T1 and T2",
                "content": r"""<p>In 1946, Felix Bloch formulated the phenomenological differential equations governing the time evolution of magnetization \(\vec{M}(t) = (M_x, M_y, M_z)\) undergoing precession and relaxation back toward thermal equilibrium \(\vec{M}_0 = (0, 0, M_0)\):</p>
\[
\frac{dM_z}{dt} = \gamma_N (\vec{M} \times \vec{B})_z - \frac{M_z - M_0}{T_1}
\]
\[
\frac{dM_x}{dt} = \gamma_N (\vec{M} \times \vec{B})_x - \frac{M_x}{T_2}
\]
\[
\frac{dM_y}{dt} = \gamma_N (\vec{M} \times \vec{B})_y - \frac{M_y}{T_2}
\]
<h4 class="content-heading">Longitudinal (Spin-Lattice) Relaxation Time (\(T_1\))</h4>
<p>Relaxation along the \(z\)-axis requires exchanging energy between the nuclear spin system and the thermal surrounding environment ('lattice'). Following a \(180^\circ\) inversion pulse (\(M_z(0) = -M_0\)):</p>
\[
M_z(t) = M_0 \left(1 - 2 e^{-t / T_1}\right)
\]
<p>\(T_1\) is measured using the <strong>inversion-recovery pulse sequence</strong> (\(180^\circ - \tau - 90^\circ - \text{acquire}\)).</p>
<h4 class="content-heading">Transverse (Spin-Spin) Relaxation Time (\(T_2\))</h4>
<p>Relaxation in the \(xy\)-plane represents the irreversible loss of phase coherence among precessing spins due to local magnetic field fluctuations, with no net energy exchange with the lattice:</p>
\[
M_{xy}(t) = M_{xy}(0) e^{-t / T_2}
\]
<p>The natural linewidth FWHM of an NMR Lorentzian peak is inversely proportional to \(T_2\): \(\Delta \nu_{1/2} = \frac{1}{\pi T_2^*}\), where \(\frac{1}{T_2^*} = \frac{1}{T_2} + \frac{\gamma \Delta B_0}{2}\) accounts for magnet inhomogeneity.</p>"""
            },
            {
                "id": "u8-sec4",
                "number": "8.4",
                "title": "The Chemical Shift & Nuclear Shielding Tensors",
                "content": r"""<p>If all protons resonated at the exact same Larmor frequency, NMR would be useless to chemists. Fortunately, nuclei are surrounded by orbiting electron clouds. In an external field \(\vec{B}_0\), the electrons circulate, generating a small local induced magnetic field \(\vec{B}_{\text{ind}} = -\boldsymbol{\sigma} \vec{B}_0\) that opposes the applied field.</p>
<p>The effective magnetic field experienced at the nucleus is:</p>
\[
B_{\text{local}} = B_0(1 - \sigma)
\]
<p>where \(\sigma\) is the dimensionless <strong>nuclear shielding constant</strong> (typically \(\sim 10^{-6}\) for protons, \(\sim 10^{-4}\) for \(^{13}\text{C}\)). The resonance frequency becomes:</p>
\[
\nu = \frac{\gamma_N}{2\pi} B_0 (1 - \sigma)
\]
<h4 class="content-heading">Ramsey's Equation for Shielding</h4>
<p>Norman Ramsey derived the quantum mechanical expression for \(\sigma\), separating it into two opposing terms:</p>
\[
\sigma = \sigma_d + \sigma_p
\]
<ol>
  <li><strong>Diamagnetic Shielding (\(\sigma_d > 0\)):</strong> Arises from the circulation of electrons in ground-state orbitals (Lamb formula). It opposes \(B_0\), shielding the nucleus and shifting the resonance upfield. Dominated by s-electron density.</li>
  <li><strong>Paramagnetic Deshielding (\(\sigma_p < 0\)):</strong> Arises from magnetic-field-induced mixing of low-lying excited electronic states with the ground state, creating orbital angular momentum that reinforces \(B_0\). Dominates heavy nuclei (\(^{13}\text{C}, ^{31}\text{P}, ^{19}\text{F}\)) possessing p and d valence electrons.</li>
</ol>
<h4 class="content-heading">The Delta (\(\delta\)) Chemical Shift Scale</h4>
<p>Because absolute frequency shifts \(\Delta\nu\) scale linearly with applied field \(B_0\), the universal dimensionless chemical shift \(\delta\) (parts per million, \(\text{ppm}\)) is defined relative to tetramethylsilane (\(\text{TMS}\), \(\text{Si(CH}_3)_4\)):</p>
\[
\delta = \frac{\nu_{\text{sample}} - \nu_{\text{TMS}}}{\nu_{\text{spectrometer}}} \times 10^6 = \frac{\sigma_{\text{TMS}} - \sigma_{\text{sample}}}{1 - \sigma_{\text{TMS}}} \approx (\sigma_{\text{TMS}} - \sigma_{\text{sample}}) \times 10^6
\]
<p>The \(\delta\) scale is completely independent of the operating magnetic field strength of the spectrometer.</p>"""
            },
            {
                "id": "u8-sec5",
                "number": "8.5",
                "title": "Electronic Influences on 1H Chemical Shifts",
                "content": r"""<p>Proton chemical shifts in organic molecules span a characteristic range of \(0 - 14\text{ ppm}\), determined by the local electronic environment:</p>
<h4 class="content-heading">1. Electronegativity & Inductive Effects</h4>
<p>Electronegative substituents (F, Cl, Br, O, N) withdraw electron density through \(\sigma\)-bonds, reducing diamagnetic shielding (\(\sigma_d\)) around adjacent protons. Less shielded protons experience a stronger effective field and resonate <strong>downfield</strong> (higher \(\delta\)):</p>
<ul>
  <li>\(\text{CH}_4\): \(\delta = 0.23\text{ ppm}\)</li>
  <li>\(\text{CH}_3\text{I}\): \(\delta = 2.16\text{ ppm}\)</li>
  <li>\(\text{CH}_3\text{Br}\): \(\delta = 2.68\text{ ppm}\)</li>
  <li>\(\text{CH}_3\text{Cl}\): \(\delta = 3.05\text{ ppm}\)</li>
  <li>\(\text{CH}_3\text{F}\): \(\delta = 4.26\text{ ppm}\)</li>
</ul>
<p>The inductive deshielding effect attenuates rapidly with distance, becoming negligible beyond three bonds.</p>
<h4 class="content-heading">2. Carbon Hybridization</h4>
<p>Higher s-character increases the electronegativity of the carbon atom: \(sp^3\ (25\% s) < sp^2\ (33\% s) < sp\ (50\% s)\). However, chemical shifts do not follow simple electronegativity because magnetic anisotropy dominates \(sp^2\) and \(sp\) carbons:</p>
<ul>
  <li>Aliphatic \(sp^3\) (\(\text{-CH}_3, \text{-CH}_2\text{-}\)): \(\delta = 0.8 - 1.8\text{ ppm}\)</li>
  <li>Alkyne acetylenic \(sp\) (\(\text{-C}\equiv\text{C-H}\)): \(\delta = 2.0 - 3.0\text{ ppm}\) (anomalously shielded!)</li>
  <li>Alkene vinylic \(sp^2\) (\(>\text{C}=\text{CH}_2\)): \(\delta = 4.5 - 6.5\text{ ppm}\)</li>
  <li>Aromatic \(sp^2\) (\(\text{Ar-H}\)): \(\delta = 6.5 - 8.5\text{ ppm}\)</li>
  <li>Aldehyde carbonyl (\(\text{-CHO}\)): \(\delta = 9.5 - 10.5\text{ ppm}\)</li>
  <li>Carboxylic acid (\(\text{-COOH}\)): \(\delta = 10.5 - 13.0\text{ ppm}\)</li>
</ul>"""
            },
            {
                "id": "u8-sec6",
                "number": "8.6",
                "title": "Magnetic Anisotropy & Aromatic Ring Currents",
                "content": r"""<p>Chemical bonds with non-spherical electron distributions (double bonds, triple bonds, aromatic rings) possess <strong>anisotropic magnetic susceptibility</strong> (\(\Delta\chi = \chi_\parallel - \chi_\perp \neq 0\)). The secondary field generated by circulating electrons depends dramatically on spatial orientation:</p>
<p>The McConnell equation describes the dipolar shielding shift at distance \(R\) and angle \(\theta\) relative to the symmetry axis:</p>
\[
\Delta\sigma = \frac{\Delta\chi}{12 \pi R^3} (1 - 3\cos^2\theta)
\]
<h4 class="content-heading">Aromatic Ring Currents (Diatropic)</h4>
<p>In benzene (\(\text{C}_6\text{H}_6\)), the applied field \(B_0\) perpendicular to the ring plane drives a circulation of the \(6\pi\) aromatic electrons around the ring perimeter (Paulings ring current model). By Lenz's law, the induced magnetic field opposes \(B_0\) in the ring interior, but loops around and <strong>reinforces \(B_0\)</strong> at the ring periphery where aromatic protons reside!</p>
<p>Consequently, benzene protons experience an additional downfield deshielding of \(\Delta\delta \approx +1.5 - 2.0\text{ ppm}\), shifting them to \(\delta = 7.27\text{ ppm}\). In [18]annulene, outer protons reside in the deshielding zone (\(\delta = 9.3\text{ ppm}\)), while inner protons reside in the intense shielding cone (\(\delta = -3.0\text{ ppm}\)), confirming diatropic ring currents.</p>
<h4 class="content-heading">Acetylenic Shielding Cone</h4>
<p>In terminal alkynes (\(\text{R-C}\equiv\text{C-H}\)), the cylindrical \(\pi\)-electrons circulate freely around the triple bond axis when \(B_0\) is parallel to the bond. The induced field opposes \(B_0\) along the bond axis, placing the acetylenic proton in an intense shielding cone that shifts its resonance upfield to \(\delta \approx 2.0 - 2.5\text{ ppm}\).</p>"""
            },
            {
                "id": "u8-sec7",
                "number": "8.7",
                "title": "Chemical Exchange Dynamics & Eyring Activation Barriers",
                "content": r"""<p>Protons attached to heteroatoms (\(\text{-OH}, \text{-NH}_2, \text{-COOH}\)) and molecules undergoing conformational exchange (e.g., chair-chair flip of cyclohexane or amide rotation of dimethylformamide) undergo dynamic chemical exchange between distinct magnetic sites \(A\) and \(B\) with lifetimes \(\tau_A\) and \(\tau_B\).</p>
<h4 class="content-heading">Timescale Regimes of NMR Exchange</h4>
<p>The appearance of the spectrum depends on the exchange rate \(k = \tau^{-1}\) relative to the chemical shift frequency difference \(\Delta\nu = |\nu_A - \nu_B|\) (in Hz):</p>
<ol>
  <li><strong>Slow Exchange (\(k \ll \Delta\nu\)):</strong> The exchange process is frozen on the NMR timescale. Two distinct, sharp peaks appear at \(\nu_A\) and \(\nu_B\).</li>
  <li><strong>Intermediate Exchange & Coalescence (\(k \approx \Delta\nu\)):</strong> As temperature increases, the two peaks broaden and migrate toward each other, eventually merging into a single flat-topped peak at the <strong>coalescence temperature (\(T_c\))</strong>. At coalescence, the rate constant for an uncoupled two-site exchange with equal populations is:
  \[
  k_c = \frac{\pi \Delta\nu}{\sqrt{2}} \approx 2.22 \Delta\nu
  \]
  </li>
  <li><strong>Fast Exchange (\(k \gg \Delta\nu\)):</strong> The exchange is rapid. A single sharp peak appears at the population-weighted average chemical shift: \(\nu_{\text{avg}} = p_A \nu_A + p_B \nu_B\).</li>
</ol>
<h4 class="content-heading">Eyring Activation Barrier Calculation</h4>
<p>Measuring the coalescence temperature \(T_c\) and frequency difference \(\Delta\nu\) enables the determination of the Gibbs free energy of activation \(\Delta G^\ddagger\) for the conformational or chemical exchange process using the Eyring equation:</p>
\[
\Delta G^\ddagger = R T_c \left[ 23.76 + \ln\left(\frac{T_c}{k_c}\right) \right] = R T_c \left[ 22.96 + \ln\left(\frac{T_c}{\Delta\nu}\right) \right]
\]"""
            }
        ],
        "problems": [
            {
                "id": "u8-prob1",
                "number": 1,
                "title": "Larmor Precession Frequencies for 1H and 13C in a 14.1 Tesla Magnet",
                "difficulty": "Foundational",
                "statement": r"""A high-field NMR spectrometer operates with a superconducting magnet having magnetic field strength \(B_0 = 14.092\text{ Tesla}\).
Gyromagnetic ratios:
\(\gamma(^1\text{H}) = 2.67522 \times 10^8\text{ rad}/(\text{s}\cdot\text{T})\)
\(\gamma(^{13}\text{C}) = 6.72828 \times 10^7\text{ rad}/(\text{s}\cdot\text{T})\)
\(\gamma(^{31}\text{P}) = 1.08291 \times 10^8\text{ rad}/(\text{s}\cdot\text{T})\)
(a) Calculate the Larmor precession frequency (in MHz) for \(^1\text{H}\), \(^{13}\text{C}\), and \(^{31}\text{P}\).
(b) Calculate the fractional Boltzmann excess population \((N_\alpha - N_\beta)/N_{\text{total}}\) for \(^1\text{H}\) at \(T = 298\text{ K}\).""",
                "solution": r"""<p><strong>Step (a): Larmor frequency calculations</strong></p>
\[
\nu_0 = \frac{\gamma B_0}{2\pi}
\]
<ol>
  <li>For \(^1\text{H}\):
  \[
  \nu_0(^1\text{H}) = \frac{(2.67522 \times 10^8\text{ rad/s}\cdot\text{T})(14.092\text{ T})}{2\pi} = \frac{3.76992 \times 10^9}{6.283185} = 600.00 \times 10^6\text{ Hz} = 600.0\text{ MHz}
  \]
  </li>
  <li>For \(^{13}\text{C}\):
  \[
  \nu_0(^{13}\text{C}) = \frac{(6.72828 \times 10^7)(14.092)}{2\pi} = \frac{9.48149 \times 10^8}{6.283185} = 150.90 \times 10^6\text{ Hz} = 150.9\text{ MHz}
  \]
  </li>
  <li>For \(^{31}\text{P}\):
  \[
  \nu_0(^{31}\text{P}) = \frac{(1.08291 \times 10^8)(14.092)}{2\pi} = \frac{1.52604 \times 10^9}{6.283185} = 242.88 \times 10^6\text{ Hz} = 242.9\text{ MHz}
  \]
  </li>
</ol>
<p><strong>Step (b): Fractional Boltzmann population excess</strong></p>
\[
\frac{N_\alpha - N_\beta}{N_{\text{total}}} \approx \frac{\gamma \hbar B_0}{2 k_B T} = \frac{h \nu_0}{2 k_B T}
\]
\[
h \nu_0 = (6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(6.00 \times 10^8\text{ s}^{-1}) = 3.9756 \times 10^{-25}\text{ J}
\]
\[
2 k_B T = 2(1.38065 \times 10^{-23}\text{ J/K})(298\text{ K}) = 8.2287 \times 10^{-21}\text{ J}
\]
\[
\frac{N_\alpha - N_\beta}{N_{\text{total}}} = \frac{3.9756 \times 10^{-25}}{8.2287 \times 10^{-21}} = 4.83 \times 10^{-5} \approx 48\text{ ppm}
\]
<p>Out of 1,000,000 proton spins, only 48 excess spins populate the lower energy state.</p>"""
            },
            {
                "id": "u8-prob2",
                "number": 2,
                "title": "Inversion-Recovery Determination of Longitudinal Relaxation Time T1",
                "difficulty": "Intermediate",
                "statement": r"""In an inversion-recovery experiment (\(180^\circ - \tau - 90^\circ\)), the longitudinal magnetization recovers according to:
\[
M_z(\tau) = M_0 \left(1 - 2 e^{-\tau / T_1}\right)
\]
For a methyl proton signal, the detected signal passes through a null (zero intensity) at delay \(\tau_{\text{null}} = 1.386\text{ seconds}\).
(a) Derive the relationship between \(\tau_{\text{null}}\) and \(T_1\).
(b) Calculate \(T_1\) for these protons.
(c) What percentage of full equilibrium magnetization \(M_0\) has recovered at delay \(\tau = 5 \times T_1\)?""",
                "solution": r"""<p><strong>Step (a): Derivation of tau_null relation</strong></p>
<p>At the null point, \(M_z(\tau_{\text{null}}) = 0\):</p>
\[
M_0 \left(1 - 2 e^{-\tau_{\text{null}} / T_1}\right) = 0 \implies 2 e^{-\tau_{\text{null}} / T_1} = 1 \implies e^{-\tau_{\text{null}} / T_1} = \frac{1}{2}
\]
\[
-\frac{\tau_{\text{null}}}{T_1} = \ln\left(\frac{1}{2}\right) = -\ln 2 \implies \tau_{\text{null}} = T_1 \ln 2 \approx 0.69315 T_1
\]
<p><strong>Step (b): Calculation of T1</strong></p>
\[
T_1 = \frac{\tau_{\text{null}}}{\ln 2} = \frac{1.386\text{ s}}{0.69315} = 2.000\text{ seconds}
\]
<p><strong>Step (c): Recovery at tau = 5 T1</strong></p>
\[
M_z(5 T_1) = M_0 \left(1 - 2 e^{-5}\right) = M_0 (1 - 2 \times 0.006738) = M_0 (1 - 0.01348) = 0.9865 M_0 = 98.65\%
\]
<p>This explains the universal spectroscopic rule of waiting a relaxation delay of \(d_1 \ge 5 T_1\) between pulses for quantitative NMR integration.</p>"""
            },
            {
                "id": "u8-prob3",
                "number": 3,
                "title": "Chemical Shift Conversion from Hz to ppm across Spectrometer Fields",
                "difficulty": "Foundational",
                "statement": r"""A proton resonance is observed at a frequency shift of \(\Delta\nu = 1450.0\text{ Hz}\) downfield from TMS on a \(400.0\text{ MHz}\) spectrometer.
(a) Calculate the chemical shift \(\delta\) in \(\text{ppm}\).
(b) If the same sample is analyzed on a \(600.0\text{ MHz}\) spectrometer, what will be its chemical shift \(\delta\) in \(\text{ppm}\)?
(c) What will be the frequency separation \(\Delta\nu\) in Hz from TMS on the \(600.0\text{ MHz}\) spectrometer?""",
                "solution": r"""<p><strong>Step (a): Chemical shift on 400 MHz spectrometer</strong></p>
\[
\delta = \frac{\Delta\nu\ (\text{Hz})}{\nu_0\ (\text{MHz})} = \frac{1450.0\text{ Hz}}{400.0\text{ MHz}} = 3.625\text{ ppm}
\]
<p><strong>Step (b): Chemical shift on 600 MHz spectrometer</strong></p>
<p>Because the chemical shift \(\delta\) in ppm is a dimensionless property of the local molecular shielding environment (\(\delta = 10^6(\sigma_{\text{TMS}} - \sigma)\)), it is completely invariant with magnetic field strength:</p>
\[
\delta = 3.625\text{ ppm}
\]
<p><strong>Step (c): Frequency separation on 600 MHz spectrometer</strong></p>
\[
\Delta\nu = \delta \times \nu_0 = 3.625\text{ ppm} \times 600.0\text{ MHz} = 2175.0\text{ Hz}
\]
<p>The line is displaced by \(2175\text{ Hz}\) from TMS, illustrating how higher fields expand the dispersion in Hz.</p>"""
            },
            {
                "id": "u8-prob4",
                "number": 4,
                "title": "Ring Current Deshielding in Benzene via McConnell Equation",
                "difficulty": "Intermediate",
                "statement": r"""In benzene (\(\text{C}_6\text{H}_6\)), circulation of \(6\pi\) electrons induces an anisotropic magnetic susceptibility \(\Delta\chi = \chi_\parallel - \chi_\perp = -60.0 \times 10^{-30}\text{ cm}^3/\text{molecule}\).
A benzene proton is located in the ring plane (\(\theta = 90^\circ\)) at distance \(R = 2.45\text{ \AA}\) from the ring center.
(a) Using the McConnell equation \(\Delta\sigma = \frac{\Delta\chi}{12 \pi R^3}(1 - 3\cos^2\theta)\), calculate the ring current contribution to the shielding constant \(\Delta\sigma\).
(b) Determine the corresponding chemical shift contribution \(\Delta\delta\) in \(\text{ppm}\).
(c) If a non-aromatic cyclohexenyl proton resonates at \(\delta = 5.60\text{ ppm}\), what chemical shift is predicted for benzene?""",
                "solution": r"""<p><strong>Step (a): McConnell equation calculation</strong></p>
<p>At \(\theta = 90^\circ\), \(\cos(90^\circ) = 0 \implies 1 - 3\cos^2\theta = 1\).</p>
<p>Parameters:</p>
<ul>
  <li>\(\Delta\chi = -60.0 \times 10^{-30}\text{ cm}^3 = -60.0 \times 10^{-36}\text{ m}^3\)</li>
  <li>\(R = 2.45 \times 10^{-8}\text{ cm} \implies R^3 = 1.4706 \times 10^{-23}\text{ cm}^3\)</li>
</ul>
\[
\Delta\sigma = \frac{\Delta\chi}{12 \pi R^3} = \frac{-60.0 \times 10^{-30}\text{ cm}^3}{12 \pi (1.4706 \times 10^{-23}\text{ cm}^3)} = \frac{-60.0 \times 10^{-30}}{5.544 \times 10^{-22}} = -1.082 \times 10^{-6}
\]
<p><strong>Step (b): Chemical shift shift Delta delta</strong></p>
\[
\Delta\delta = -\Delta\sigma \times 10^6 = -(-1.082 \times 10^{-6}) \times 10^6 = +1.082\text{ ppm}
\]
<p>The ring current deshields the benzene protons by \(\approx +1.08\text{ ppm}\).</p>
<p><strong>Step (c): Predicted benzene chemical shift</strong></p>
\[
\delta_{\text{benzene}} = \delta_{\text{alkene}} + \Delta\delta = 5.60 + 1.08 = 6.68\text{ ppm}
\]
<p>Accounting for localized bond anisotropy and slight polarization brings the value into close agreement with the experimental value (\(\delta = 7.27\text{ ppm}\)).</p>"""
            },
            {
                "id": "u8-prob5",
                "number": 5,
                "title": "Coalescence Temperature and Rotational Barrier in Dimethylformamide",
                "difficulty": "Intermediate",
                "statement": r"""In \(N,N\)-dimethylformamide (\(\text{H-C}(=\text{O})-\text{N(CH}_3)_2\)), restricted rotation around the partial C-N double bond renders the two methyl groups non-equivalent at low temperature.
On a \(500.0\text{ MHz}\) NMR spectrometer:
At \(-20^\circ\text{C}\), two sharp methyl singlets are observed at \(\delta_A = 2.97\text{ ppm}\) and \(\delta_B = 2.79\text{ ppm}\).
Upon heating, the two singlets coalesce into a single broad peak at coalescence temperature \(T_c = 118.0^\circ\text{C}\) (\(391.15\text{ K}\)).
(a) Calculate the chemical shift frequency difference \(\Delta\nu\) in Hz at \(500\text{ MHz}\).
(b) Determine the rate constant of C-N bond rotation \(k_c\) at the coalescence temperature.
(c) Calculate the Gibbs free energy of activation \(\Delta G^\ddagger\) for C-N bond rotation in \(\text{kJ/mol}\).""",
                "solution": r"""<p><strong>Step (a): Frequency difference Delta nu</strong></p>
\[
\Delta\delta = 2.97 - 2.79 = 0.18\text{ ppm}
\]
\[
\Delta\nu = \Delta\delta \times \nu_0 = 0.18\text{ ppm} \times 500.0\text{ MHz} = 90.0\text{ Hz}
\]
<p><strong>Step (b): Rate constant at coalescence</strong></p>
<p>For an uncoupled two-site exchange with equal populations:</p>
\[
k_c = \frac{\pi \Delta\nu}{\sqrt{2}} = \frac{\pi (90.0)}{\sqrt{2}} = 199.9\text{ s}^{-1} \approx 200\text{ s}^{-1}
\]
<p><strong>Step (c): Activation barrier Delta G_ddagger</strong></p>
<p>Using the Eyring equation at \(T_c = 391.15\text{ K}\):</p>
\[
k_c = \frac{k_B T_c}{h} \exp\left(-\frac{\Delta G^\ddagger}{R T_c}\right) \implies \Delta G^\ddagger = R T_c \ln\left(\frac{k_B T_c}{h k_c}\right)
\]
\[
\frac{k_B T_c}{h} = \frac{(1.38065 \times 10^{-23})(391.15)}{6.62607 \times 10^{-34}} = 8.150 \times 10^{12}\text{ s}^{-1}
\]
\[
\frac{k_B T_c}{h k_c} = \frac{8.150 \times 10^{12}}{199.9} = 4.077 \times 10^{10}
\]
\[
\ln(4.077 \times 10^{10}) = 24.431
\]
\[
\Delta G^\ddagger = (8.31446\text{ J/mol}\cdot\text{K})(391.15\text{ K})(24.431) = 79456\text{ J/mol} = 79.46\text{ kJ/mol} \approx 19.0\text{ kcal/mol}
\]
<p>This barrier of \(\approx 79.5\text{ kJ/mol}\) reflects the substantial \(\sim 40\%\) double-bond character of the amide resonance contributor (\(>\text{N}^+=\text{C-O}^-\)).</p>"""
            },
            {
                "id": "u8-prob6",
                "number": 6,
                "title": "Transverse Relaxation T2 and Linewidth in Paramagnetic Solutions",
                "difficulty": "Foundational",
                "statement": r"""The \(^1\text{H}\) NMR resonance of a small organic molecule has a natural linewidth of \(\Delta\nu_{1/2} = 0.50\text{ Hz}\) in degassed \(\text{CDCl}_3\).
Upon adding trace paramagnetic \(\text{Mn}^{2+}\) ions, dipolar relaxation broadens the line to \(\Delta\nu_{1/2} = 32.0\text{ Hz}\).
(a) Calculate the transverse relaxation time \(T_2^*\) before and after adding \(\text{Mn}^{2+}\).
(b) Explain why paramagnetic metal ions cause such severe line broadening in NMR.""",
                "solution": r"""<p><strong>Step (a): Calculation of T2*</strong></p>
<p>The Lorentzian linewidth FWHM is related to \(T_2^*\) by:</p>
\[
\Delta\nu_{1/2} = \frac{1}{\pi T_2^*} \implies T_2^* = \frac{1}{\pi \Delta\nu_{1/2}}
\]
<ul>
  <li>Before \(\text{Mn}^{2+}\):
  \[
  T_2^* = \frac{1}{\pi (0.50\text{ Hz})} = \frac{1}{1.5708} = 0.637\text{ seconds}
  \]
  </li>
  <li>After \(\text{Mn}^{2+}\):
  \[
  T_2^* = \frac{1}{\pi (32.0\text{ Hz})} = \frac{1}{100.53} = 0.00995\text{ seconds} \approx 9.95\text{ ms}
  \]
  </li>
</ul>
<p><strong>Step (b): Mechanism of paramagnetic broadening</strong></p>
<p>Unpaired electrons possess a magnetic moment \(\mu_e = g_e \mu_B\) that is approximately 658 times larger than the nuclear magnetic moment of the proton (\(\mu_B / \mu_N \approx m_p / m_e \approx 1836\)).</p>
<p>Because through-space dipolar relaxation scales with the square of the magnetic moment (\(\propto \mu^2 \propto \gamma^2\)), fluctuating local magnetic fields generated by paramagnetic \(\text{Mn}^{2+}\) (\(S = 5/2\)) enhance nuclear relaxation by a factor of \(\sim 10^6\), dramatically shortening \(T_2\) and broadening the resonance.</p>"""
            },
            {
                "id": "u8-prob7",
                "number": 7,
                "title": "Hydrogen Bonding and Concentration-Dependent Chemical Shift of Ethanol",
                "difficulty": "Intermediate",
                "statement": r"""The hydroxyl proton (\(\text{-OH}\)) of ethanol (\(\text{CH}_3\text{CH}_2\text{OH}\)) exhibits a chemical shift that varies strongly with concentration in non-polar \(\text{CCl}_4\) solvent:
In neat liquid ethanol: \(\delta = 5.25\text{ ppm}\)
In \(1.0\text{ M}\) solution: \(\delta = 3.80\text{ ppm}\)
Extrapolated to infinite dilution: \(\delta = 0.70\text{ ppm}\)
(a) Explain why the chemical shift shifts upfield by over \(4.5\text{ ppm}\) upon dilution.
(b) Why does the \(\text{-OH}\) proton usually appear as a broad singlet at room temperature without showing scalar coupling to the adjacent \(\text{-CH}_2\text{-}\) protons?
(c) How can the scalar coupling between \(\text{-OH}\) and \(\text{-CH}_2\text{-}\) (triplet \(\text{-OH}\)) be experimentally unmasked?""",
                "solution": r"""<p><strong>Step (a): Explanation of dilution shift</strong></p>
<p>In concentrated ethanol, extensive intermolecular hydrogen bonding (\(\text{R-O-H}\cdots\text{O(H)-R}\)) occurs. Hydrogen bond formation draws the bonding electron pair toward the oxygen atom, severely deshielding the bridging proton and shifting its resonance downfield to \(\delta = 5.25\text{ ppm}\).</p>
<p>Upon progressive dilution in inert \(\text{CCl}_4\), hydrogen-bonded oligomers dissociate into isolated monomeric ethanol molecules. Free monomeric \(\text{-OH}\) has full electron density around the proton, restoring diamagnetic shielding and shifting the signal upfield to \(\delta = 0.70\text{ ppm}\).</p>
<p><strong>Step (b): Broad singlet appearance</strong></p>
<p>In standard samples, trace acidic or basic impurities (including trace moisture) catalyze rapid intermolecular proton exchange:</p>
\[
\text{EtOH}^* + \text{EtOH} \rightleftharpoons \text{EtOH} + \text{EtOH}^*
\]
<p>Because the lifetime of a proton on any given ethanol molecule is much shorter than the reciprocal coupling constant (\(\tau_{\text{ex}} \ll 1/J \approx 0.2\text{ s}\)), the proton experiences an average spin state of the neighboring methylene group, collapsing the multiplet into a single exchange-broadened singlet.</p>
<p><strong>Step (c): Experimental unmasking of scalar coupling</strong></p>
<p>To slow down exchange and observe the vicinal \(^3J_{HH} \approx 5\text{ Hz}\) coupling (triplet \(\text{-OH}\) and doublet of quartets for \(\text{-CH}_2\text{-}\)):</p>
<ul>
  <li>Use an ultra-pure, anhydrous polar aprotic solvent that forms strong hydrogen bonds (e.g., dry \(\text{DMSO-}d_6\)). DMSO solvates the \(\text{-OH}\) proton in a stable monomeric complex, shutting down intermolecular exchange.</li>
  <li>Alternatively, cool the sample to low temperatures (\(< -40^\circ\text{C}\)) to freeze the exchange kinetics.</li>
</ul>"""
            }
        ]
    }
    units.append(u8)

    # =========================================================================
    # UNIT 9: Nuclear Magnetic Resonance (NMR) II: Spin-Spin Coupling, Decoupling & 2D Pulse Sequences
    # =========================================================================
    u9 = {
        "id": "unit9",
        "number": 9,
        "title": "Unit 9: Nuclear Magnetic Resonance (NMR) II: Spin-Spin Coupling, Decoupling & 2D Pulse Sequences",
        "description": "Mechanisms of indirect scalar J-coupling, Fermi contact interaction, first-order multiplets and Pascal's triangle, Karplus relation and dihedral angles, second-order strongly coupled spin systems (AB and AMX roof effects), broadband heteronuclear decoupling, 13C NMR and DEPT editing, Nuclear Overhauser Effect (NOE), and multidimensional NMR (2D COSY, NOESY, HSQC, HMBC).",
        "simulations": [
            {
                "id": "sim_spec_nmr_spin_spin_splitting_2d",
                "title": "Scalar J-Coupling & 2D COSY Cross-Peaks",
                "description": "Interactive 60 FPS simulator demonstrating scalar J-coupling multiplet trees and 2D COSY correlation spectroscopy. Adjust coupling constant J, vary dihedral angle phi to test the Karplus equation, switch between AX (doublet/doublet) and AX3 (triplet/quartet) spin systems, and examine corresponding diagonal and cross peaks in the simulated 2D COSY contour map."
            }
        ],
        "sections": [
            {
                "id": "u9-sec1",
                "number": "9.1",
                "title": "Mechanism of Indirect Scalar Spin-Spin Coupling (J-Coupling)",
                "content": r"""<p>While through-space dipolar magnetic interactions average to zero in isotropic liquids due to rapid molecular tumbling, an indirect magnetic interaction persists transmitted through the chemical bonding electrons. This is <strong>scalar spin-spin coupling (\(J\)-coupling)</strong>.</p>
<h4 class="content-heading">The Ramsey-Fermi Contact Mechanism</h4>
<p>The primary quantum mechanical mechanism mediating \(J\)-coupling across covalent bonds is the <strong>Fermi contact interaction</strong>:</p>
<ol>
  <li>The nuclear spin of nucleus \(A\) (\(\vec{I}_A\)) polarizes the spin of an electron in its immediate vicinity via contact hyperfine interaction with s-electron density at the nucleus (\(|\psi(0)|^2\)).</li>
  <li>By the Pauli exclusion principle, the paired electron in the covalent \(\sigma\)-bond must have antiparallel spin.</li>
  <li>This polarized bonding electron interacts via Fermi contact with the second nucleus \(B\) (\(\vec{I}_B\)), effectively communicating the spin state of \(A\) to \(B\).</li>
</ol>
<p>The scalar coupling Hamiltonian is formulated as:</p>
\[
\hat{H}_J = 2\pi J_{AB} \hat{\vec{I}}_A \cdot \hat{\vec{I}}_B = h J_{AB} \left(\hat{I}_{Ax}\hat{I}_{Bx} + \hat{I}_{Ay}\hat{I}_{By} + \hat{I}_{Az}\hat{I}_{Bz}\right)
\]
<p>Crucially, the scalar coupling constant \(J_{AB}\) is expressed in <strong>Hertz (Hz)</strong> and is strictly independent of the spectrometer magnetic field \(B_0\). One-bond couplings (\(^1J\)) are typically positive and large (e.g., \(^1J_{CH} \approx 125 - 250\text{ Hz}\)); two-bond geminal couplings (\(^2J\)) are typically negative (\(-12\text{ Hz}\)); three-bond vicinal couplings (\(^3J\)) are positive (\(0 - 18\text{ Hz}\)).</p>"""
            },
            {
                "id": "u9-sec2",
                "number": "9.2",
                "title": "First-Order Multiplets & Pascal's Triangle Rules",
                "content": r"""<p>A spin system is classified as <strong>first-order</strong> when the chemical shift separation \(\Delta\nu\) between coupled nuclei is much larger than their coupling constant \(J\):</p>
\[
\frac{\Delta\nu}{J} \ge 10
\]
<h4 class="content-heading">Multiplicity & The 2nI + 1 Rule</h4>
<p>When a nucleus couples to \(n\) magnetically equivalent neighboring nuclei of spin \(I\), its resonance is split into a multiplet containing:</p>
\[
M = 2nI + 1 \quad \text{peaks}
\]
<p>For coupling to spin \(I = 1/2\) nuclei (protons), this simplifies to the familiar <strong>\((n + 1)\) rule</strong>:</p>
<ul>
  <li>\(n = 0\): Singlet (1)</li>
  <li>\(n = 1\): Doublet (1:1), separated by \(J\)</li>
  <li>\(n = 2\): Triplet (1:2:1), adjacent peaks separated by \(J\)</li>
  <li>\(n = 3\): Quartet (1:3:3:1), adjacent peaks separated by \(J\)</li>
  <li>\(n = 4\): Quintet (1:4:6:4:1)</li>
  <li>\(n = 5\): Sextet (1:5:10:10:5:1)</li>
  <li>\(n = 6\): Septet (1:6:15:20:15:6:1)</li>
</ul>
<p>The relative intensities of the multiplet lines correspond exactly to the binomial coefficients of <strong>Pascal's triangle</strong>: \(\binom{n}{k} = \frac{n!}{k!(n-k)!}\).</p>
<h4 class="content-heading">Coupling Trees for Non-Equivalent Nuclei</h4>
<p>When a nucleus couples to two non-equivalent sets of nuclei with different coupling constants (e.g., \(J_{AM} \neq J_{AX}\)), successive splitting yields composite multiplet trees: a doublet of doublets (\(dd\)), doublet of triplets (\(dt\)), or doublet of doublets of doublets (\(ddd\)).</p>"""
            },
            {
                "id": "u9-sec3",
                "number": "9.3",
                "title": "The Karplus Relation & Dihedral Angle Conformational Calculus",
                "content": r"""<p>In 1959, Martin Karplus demonstrated that vicinal three-bond coupling constants \(^3J_{HH}\) across a \(\text{H-C-C-H}\) fragment depend strictly on the dihedral (torsional) angle \(\phi\) between the two \(\text{C-H}\) bonds:</p>
\[
^3J_{HH}(\phi) = A \cos^2\phi + B \cos\phi + C
\]
<p>Typical empirical coefficients for aliphatic hydrocarbons are \(A = 7.0\text{ Hz}\), \(B = -1.0\text{ Hz}\), and \(C = 5.0\text{ Hz}\), giving:</p>
\[
^3J_{HH}(\phi) = 7.0 \cos^2\phi - 1.0 \cos\phi + 5.0
\]
<h4 class="content-heading">Structural Implications of the Karplus Curve</h4>
<ul>
  <li><strong>Anti-periplanar (\(\phi = 180^\circ\)):</strong> Maximum orbital overlap between C-H \(\sigma\)-orbitals: \(\cos(180^\circ) = -1 \implies {}^3J \approx 7 + 1 + 5 = 13\text{ Hz}\) (can reach \(14 - 18\text{ Hz}\)). In cyclohexane chairs, <em>diaxial</em> coupling is large: \(^3J_{aa} \approx 10 - 14\text{ Hz}\).</li>
  <li><strong>Syn-periplanar (\(\phi = 0^\circ\)):</strong> Moderate orbital overlap: \(\cos(0^\circ) = 1 \implies {}^3J \approx 7 - 1 + 5 = 11\text{ Hz}\) (typically \(8 - 10\text{ Hz}\)). In alkenes, <em>cis</em>-coupling: \(^3J_{cis} \approx 7 - 11\text{ Hz}\).</li>
  <li><strong>Gauche / Orthogonal (\(\phi = 90^\circ\)):</strong> Minimal orbital overlap: \(\cos(90^\circ) = 0 \implies {}^3J \approx 5\text{ Hz}\) (at \(\phi = 90^\circ\), \(^3J\) drops to \(0 - 2\text{ Hz}\)). In cyclohexanes, <em>axial-equatorial</em> and <em>diequatorial</em> couplings are small: \(^3J_{ae} \approx {}^3J_{ee} \approx 2 - 5\text{ Hz}\).</li>
</ul>
<p>The Karplus equation is the cornerstone of conformational analysis in organic stereochemistry and protein backbone NMR (where \(^3J_{H^N H^\alpha}\) determines the peptide \(\phi\) dihedral angle).</p>"""
            },
            {
                "id": "u9-sec4",
                "number": "9.4",
                "title": "Second-Order (Strongly Coupled) Spin Systems: The AB Pattern",
                "content": r"""<p>When the chemical shift separation between coupled nuclei becomes comparable to the coupling constant (\(\Delta\nu / J < 10\)), the first-order approximation breaks down completely. The spin system transitions into a <strong>strongly coupled second-order system</strong>.</p>
<h4 class="content-heading">Quantum Mechanical Matrix Solution of the AB System</h4>
<p>For two coupled spin-1/2 nuclei \(A\) and \(B\) with chemical shifts \(\nu_A, \nu_B\) and coupling \(J\), the Hamiltonian matrix in the product basis \(\{ |\alpha\alpha\rangle, |\alpha\beta\rangle, |\beta\alpha\rangle, |\beta\beta\rangle \}\) is:</p>
\[
\hat{H} = \begin{pmatrix}
\bar{\nu} + \frac{1}{4}J & 0 & 0 & 0 \\
0 & \frac{1}{2}\Delta\nu - \frac{1}{4}J & \frac{1}{2}J & 0 \\
0 & \frac{1}{2}J & -\frac{1}{2}\Delta\nu - \frac{1}{4}J & 0 \\
0 & 0 & 0 & -\bar{\nu} + \frac{1}{4}J
\end{pmatrix}
\]
<p>The inner \(2\times 2\) block mixes states \(|\alpha\beta\rangle\) and \(|\beta\alpha\rangle\). Diagonalizing this block with mixing angle \(\theta\), where \(\tan(2\theta) = J / \Delta\nu\):</p>
<p>The spectrum consists of four lines: two outer lines (1 and 4) and two inner lines (2 and 3):</p>
\[
\nu_1 - \nu_2 = \nu_3 - \nu_4 = J
\]
\[
\nu_1 - \nu_3 = \nu_2 - \nu_4 = \sqrt{\Delta\nu^2 + J^2} - J
\]
<h4 class="content-heading">The 'Roof Effect'</h4>
<p>The relative intensities of the four lines are given by:</p>
\[
I_1 : I_2 : I_3 : I_4 = (1 - \sin 2\theta) : (1 + \sin 2\theta) : (1 + \sin 2\theta) : (1 - \sin 2\theta)
\]
<p>where \(\sin 2\theta = \frac{J}{\sqrt{\Delta\nu^2 + J^2}}\). The inner lines are amplified while the outer lines shrink, causing the multiplet to 'tilt' inward toward the coupled partner like a slanted roof (the <strong>roof effect</strong>). As \(\Delta\nu / J \to 0\), the outer lines vanish completely and the inner lines coalesce into a single singlet.</p>"""
            },
            {
                "id": "u9-sec5",
                "number": "9.5",
                "title": "Carbon-13 (13C) NMR & DEPT Spectral Editing",
                "content": r"""<p>Carbon-13 (\(^{13}\text{C}\)) is a spin-1/2 nucleus with low natural abundance (\(1.108\%\)) and a lower gyromagnetic ratio (\(\gamma_C \approx 0.25 \gamma_H\)). Its inherent sensitivity is \(\approx 1.76 \times 10^{-4}\) relative to \(^1\text{H}\). However, the chemical shift range spans \(0 - 220\text{ ppm}\), providing superior spectral dispersion without peak overlap.</p>
<h4 class="content-heading">1. Broadband Proton Decoupling (\(^{13}\text{C}\{^1\text{H}\}\))</h4>
<p>In standard \(^{13}\text{C}\) acquisitions, high-power composite RF irradiation is applied at the proton resonance frequency (broadband decoupling, e.g., WALTZ-16). This induces rapid proton spin flips, completely collapsing all \(^1J_{CH}\) multiplets into single sharp singlets for each chemically non-equivalent carbon atom.</p>
<h4 class="content-heading">2. The Nuclear Overhauser Effect (NOE) Enhancement</h4>
<p>Proton decoupling saturates proton transitions, driving through-space dipolar cross-relaxation that perturbs \(^{13}\text{C}\) populations. The maximum theoretical NOE signal enhancement is:</p>
\[
\eta = \frac{\gamma_H}{2\gamma_C} \approx \frac{2.675 \times 10^8}{2(6.728 \times 10^7)} \approx 1.988 \implies \text{Total Intensity} = 1 + \eta \approx 2.988
\]
<p>Protonated carbons gain nearly a 3-fold intensity boost. Quaternary carbons without directly attached protons experience minimal NOE and long \(T_1\) times, resulting in much smaller peaks.</p>
<h4 class="content-heading">3. DEPT (Distortionless Enhancement by Polarization Transfer)</h4>
<p>DEPT uses polarization transfer from sensitive protons to coupled carbons via variable read pulse angle \(\theta\):</p>
<ul>
  <li><strong>DEPT-45 (\(\theta = 45^\circ\)):</strong> All protonated carbons (\(\text{CH}, \text{CH}_2, \text{CH}_3\)) appear positive.</li>
  <li><strong>DEPT-90 (\(\theta = 90^\circ\)):</strong> Only \(\text{CH}\) (methine) carbons appear positive; \(\text{CH}_2\) and \(\text{CH}_3\) are completely invisible.</li>
  <li><strong>DEPT-135 (\(\theta = 135^\circ\)):</strong> \(\text{CH}\) and \(\text{CH}_3\) appear <strong>positive (pointing up)</strong>; \(\text{CH}_2\) (methylene) appears <strong>negative (pointing down / inverted)</strong>. Quaternary carbons are absent from all DEPT spectra.</li>
</ul>"""
            },
            {
                "id": "u9-sec6",
                "number": "9.6",
                "title": "Two-Dimensional NMR Principles: Evolution & Acquisition",
                "content": r"""<p>Two-dimensional (2D) NMR, pioneered by Jean Jeener and Richard Ernst (1991 Nobel Prize), expands spectroscopic information across two frequency axes \((F_1, F_2)\). Every 2D pulse sequence consists of four fundamental time intervals:</p>
\[
\text{Preparation} \longrightarrow \text{Evolution } (t_1) \longrightarrow \text{Mixing } (\tau_m) \longrightarrow \text{Detection } (t_2)
\]
<ol>
  <li><strong>Preparation:</strong> Magnetization is initialized at thermal equilibrium and tipped into the transverse plane by an RF pulse.</li>
  <li><strong>Evolution (\(t_1\)):</strong> Spins precess freely at their characteristic frequencies \(\omega_1\). The interval \(t_1\) is systematically incremented in \(N_1\) discrete steps.</li>
  <li><strong>Mixing:</strong> A pulse or delay period during which coherence or magnetization is transferred between coupled or spatially proximate spins via scalar coupling (\(J\)) or dipolar cross-relaxation (NOE).</li>
  <li><strong>Detection (\(t_2\)):</strong> The Free Induction Decay (FID) \(S(t_1, t_2)\) is recorded as a function of real time \(t_2\).</li>
</ol>
<h4 class="content-heading">2D Fourier Transformation</h4>
<p>A double Fourier transformation converts the time-domain matrix \(S(t_1, t_2)\) into a 2D frequency spectrum \(F(\omega_1, \omega_2)\):</p>
\[
F(\omega_1, \omega_2) = \int_0^\infty \int_0^\infty S(t_1, t_2) e^{-i\omega_1 t_1} e^{-i\omega_2 t_2} dt_1 dt_2
\]"""
            },
            {
                "id": "u9-sec7",
                "number": "9.7",
                "title": "Homonuclear & Heteronuclear 2D Sequences: COSY, NOESY, HSQC & HMBC",
                "content": r"""<p>Modern organic structure elucidation relies on four cornerstone 2D experiments:</p>
<h4 class="content-heading">1. COSY (Correlation Spectroscopy)</h4>
<p>Homonuclear \(^1\text{H}-^1\text{H}\) experiment (\(90^\circ - t_1 - 90^\circ - \text{acquire}\)).</p>
<ul>
  <li><strong>Diagonal Peaks (\(F_1 = F_2\)):</strong> Replicate the conventional 1D \(^1\text{H}\) spectrum.</li>
  <li><strong>Cross Peaks (\(F_1 \neq F_2\)):</strong> Appear symmetrically off the diagonal at coordinates \((\delta_A, \delta_B)\) and \((\delta_B, \delta_A)\) if and only if protons \(A\) and \(B\) share scalar coupling (\(^2J\) or \(^3J\)). Tracing cross-peaks establishes the complete carbon-proton connectivity backbone.</li>
</ul>
<h4 class="content-heading">2. NOESY (Nuclear Overhauser Effect Spectroscopy)</h4>
<p>Homonuclear \(^1\text{H}-^1\text{H}\) experiment utilizing dipolar cross-relaxation during mixing time \(\tau_m\). Cross-peaks indicate spatial proximity through space (\(r < 5\text{ \AA}\)), independent of intervening chemical bonds. Indispensable for establishing stereochemistry and 3D protein structures.</p>
<h4 class="content-heading">3. HSQC (Heteronuclear Single Quantum Coherence)</h4>
<p>Heteronuclear \(^1\text{H}-^{13}\text{C}\) experiment correlating protons with the exact carbon atom to which they are directly attached via one-bond coupling (\(^1J_{CH} \approx 140\text{ Hz}\)). Each peak indicates a direct \(\text{C-H}\) bond.</p>
<h4 class="content-heading">4. HMBC (Heteronuclear Multiple Bond Correlation)</h4>
<p>Heteronuclear \(^1\text{H}-^{13}\text{C}\) experiment tuned for long-range two- and three-bond couplings (\(^2J_{CH}, {}^3J_{CH} \approx 5 - 10\text{ Hz}\)), with one-bond couplings suppressed. Crucial for connecting quaternary carbons (carbonyls, aromatics, fully substituted centers) across heteroatoms where proton-proton COSY connectivity terminates.</p>"""
            }
        ],
        "problems": [
            {
                "id": "u9-prob1",
                "number": 1,
                "title": "Multiplet Splitting Tree Analysis for Ethyl Group",
                "difficulty": "Foundational",
                "statement": r"""In the \(^1\text{H}\) NMR spectrum of bromoethane (\(\text{CH}_3\text{CH}_2\text{Br}\)) recorded at \(400.0\text{ MHz}\):
The methyl group (\(\text{-CH}_3\)) appears at \(\delta = 1.68\text{ ppm}\).
The methylene group (\(\text{-CH}_2\text{-}\)) appears at \(\delta = 3.42\text{ ppm}\).
The vicinal scalar coupling constant is \(^3J = 7.4\text{ Hz}\).
(a) Determine the multiplicity and relative line intensities for the methyl and methylene resonances.
(b) Calculate the frequency difference \(\Delta\nu\) in Hz between the centers of the two multiplets.
(c) Evaluate the ratio \(\Delta\nu / J\) and verify whether this spin system can be treated as first-order (\(A_3 X_2\)).""",
                "solution": r"""<p><strong>Step (a): Multiplicities and intensities</strong></p>
<ul>
  <li><strong>Methyl group (\(\text{-CH}_3\)):</strong> Adjacent to \(n=2\) methylene protons. Multiplicity \(= n + 1 = 2 + 1 = 3\) (<strong>triplet</strong>). Relative line intensities from Pascal's triangle: <strong>1 : 2 : 1</strong>, spaced by \(J = 7.4\text{ Hz}\).</li>
  <li><strong>Methylene group (\(\text{-CH}_2\text{-}\)):</strong> Adjacent to \(n=3\) methyl protons. Multiplicity \(= n + 1 = 3 + 1 = 4\) (<strong>quartet</strong>). Relative line intensities from Pascal's triangle: <strong>1 : 3 : 3 : 1</strong>, spaced by \(J = 7.4\text{ Hz}\).</li>
</ul>
<p><strong>Step (b): Chemical shift separation Delta nu</strong></p>
\[
\Delta\delta = 3.42 - 1.68 = 1.74\text{ ppm}
\]
\[
\Delta\nu = \Delta\delta \times \nu_0 = 1.74\text{ ppm} \times 400.0\text{ MHz} = 696.0\text{ Hz}
\]
<p><strong>Step (c): First-order criterion evaluation</strong></p>
\[
\frac{\Delta\nu}{J} = \frac{696.0\text{ Hz}}{7.4\text{ Hz}} = 94.1
\]
<p>Since \(\frac{\Delta\nu}{J} = 94.1 \gg 10\), the spin system strictly satisfies the first-order condition (\(A_3 X_2\)). Multiplet intensities conform to Pascal's triangle without visible second-order distortion.</p>"""
            },
            {
                "id": "u9-prob2",
                "number": 2,
                "title": "Conformational Analysis of Cyclohexane Derivative via Karplus Relation",
                "difficulty": "Intermediate",
                "statement": r"""A substituted cyclohexane ring possesses a proton \(H_A\) on carbon C1 coupled to two adjacent protons on carbon C2: one axial proton \(H_{2a}\) and one equatorial proton \(H_{2e}\).
In the chair conformation:
The dihedral angle between \(H_A\) and \(H_{2a}\) is \(\phi_1 = 180^\circ\) (anti-periplanar).
The dihedral angle between \(H_A\) and \(H_{2e}\) is \(\phi_2 = 60^\circ\) (gauche).
Using the Karplus equation:
\[
^3J(\phi) = 8.5 \cos^2\phi - 0.5 \cos\phi + 2.0\text{ Hz}
\]
(a) Calculate the theoretical coupling constants \(^3J_{A, 2a}\) and \(^3J_{A, 2e}\).
(b) Describe the resulting multiplet pattern observed for proton \(H_A\).
(c) If proton \(H_A\) were equatorial instead of axial, what would be the two dihedral angles to \(H_{2a}\) and \(H_{2e}\), and what would be the predicted coupling constants?""",
                "solution": r"""<p><strong>Step (a): Coupling constant calculations for axial HA</strong></p>
<ol>
  <li>For \(H_A(\text{ax}) - H_{2a}(\text{ax})\) (\(\phi_1 = 180^\circ\)):
  \[
  \cos(180^\circ) = -1 \implies \cos^2(180^\circ) = 1
  \]
  \[
  ^3J_{aa} = 8.5(1) - 0.5(-1) + 2.0 = 8.5 + 0.5 + 2.0 = 11.0\text{ Hz}
  \]
  </li>
  <li>For \(H_A(\text{ax}) - H_{2e}(\text{eq})\) (\(\phi_2 = 60^\circ\)):
  \[
  \cos(60^\circ) = 0.5 \implies \cos^2(60^\circ) = 0.25
  \]
  \[
  ^3J_{ae} = 8.5(0.25) - 0.5(0.5) + 2.0 = 2.125 - 0.25 + 2.0 = 3.875\text{ Hz} \approx 3.9\text{ Hz}
  \]
  </li>
</ol>
<p><strong>Step (b): Multiplet appearance</strong></p>
<p>Proton \(H_A\) couples to two non-equivalent protons with distinct coupling constants (\(11.0\text{ Hz}\) and \(3.9\text{ Hz}\)).</p>
<p>The resulting signal is a <strong>doublet of doublets (\(dd\))</strong> with line positions at: \(\pm \frac{11.0}{2} \pm \frac{3.9}{2}\), consisting of four lines of equal intensity (1:1:1:1).</p>
<p><strong>Step (c): Equatorial HA case</strong></p>
<p>If \(H_A\) is equatorial:</p>
<ul>
  <li>Dihedral angle to \(H_{2a}\) is \(\phi \approx 60^\circ \implies {}^3J_{ea} \approx 3.9\text{ Hz}\).</li>
  <li>Dihedral angle to \(H_{2e}\) is \(\phi \approx 60^\circ \implies {}^3J_{ee} \approx 3.9\text{ Hz}\).</li>
</ul>
<p>Both couplings are small (\(\approx 3.9\text{ Hz}\)), producing an apparent <strong>triplet</strong> with small splitting. This stark difference between a large diaxial coupling (\(11\text{ Hz}\)) and small equatorial couplings (\(3.9\text{ Hz}\)) is the foundational rule for determining axial versus equatorial stereochemistry in six-membered rings.</p>"""
            },
            {
                "id": "u9-prob3",
                "number": 3,
                "title": "Quantum Mechanical Analysis of an AB Strongly Coupled Quartet",
                "difficulty": "Advanced",
                "statement": r"""A geminal methylene group (\(-\text{CH}_2-\)) in a rigid bicyclic lactone forms an strongly coupled \(AB\) spin system recorded on a \(300.0\text{ MHz}\) spectrometer.
The spectrum consists of four lines:
Line 1: \(848.0\text{ Hz}\)
Line 2: \(836.0\text{ Hz}\)
Line 3: \(818.0\text{ Hz}\)
Line 4: \(806.0\text{ Hz}\)
(a) Determine the scalar coupling constant \(J_{AB}\).
(b) Calculate the true chemical shift difference \(\Delta\nu = |\nu_A - \nu_B|\) in Hz and in ppm.
(c) Calculate the true chemical shifts \(\delta_A\) and \(\delta_B\).
(d) Calculate the theoretical intensity ratio \(I_{\text{inner}} / I_{\text{outer}}\) reflecting the roof effect.""",
                "solution": r"""<p><strong>Step (a): Scalar coupling constant J_AB</strong></p>
<p>In an \(AB\) quartet, the outer-to-inner line separations equal \(J_{AB}\):</p>
\[
\nu_1 - \nu_2 = 848.0 - 836.0 = 12.0\text{ Hz}
\]
\[
\nu_3 - \nu_4 = 818.0 - 806.0 = 12.0\text{ Hz}
\]
\[
J_{AB} = 12.0\text{ Hz}
\]
<p><strong>Step (b): True chemical shift difference Delta nu</strong></p>
<p>The separation between alternating lines relates to \(\Delta\nu\) by:</p>
\[
\nu_1 - \nu_3 = \nu_2 - \nu_4 = 848.0 - 818.0 = 30.0\text{ Hz} = \sqrt{\Delta\nu^2 + J^2} - J
\]
\[
\sqrt{\Delta\nu^2 + J^2} = 30.0 + J = 30.0 + 12.0 = 42.0\text{ Hz}
\]
\[
\Delta\nu^2 + J^2 = (42.0)^2 = 1764.0\text{ Hz}^2
\]
\[
\Delta\nu^2 = 1764.0 - 12.0^2 = 1764.0 - 144.0 = 1620.0\text{ Hz}^2
\]
\[
\Delta\nu = \sqrt{1620.0} = 40.25\text{ Hz}
\]
<p>In ppm on a \(300.0\text{ MHz}\) spectrometer:</p>
\[
\Delta\delta = \frac{40.25\text{ Hz}}{300.0\text{ MHz}} = 0.134\text{ ppm}
\]
<p><strong>Step (c): True chemical shifts delta_A and delta_B</strong></p>
<p>The center of gravity of the multiplet is:</p>
\[
\nu_{\text{mid}} = \frac{848.0 + 806.0}{2} = 827.0\text{ Hz} \implies \delta_{\text{mid}} = \frac{827.0}{300.0} = 2.7567\text{ ppm}
\]
\[
\nu_A = \nu_{\text{mid}} + \frac{\Delta\nu}{2} = 827.0 + 20.12 = 847.12\text{ Hz} \implies \delta_A = \frac{847.12}{300.0} = 2.824\text{ ppm}
\]
\[
\nu_B = \nu_{\text{mid}} - \frac{\Delta\nu}{2} = 827.0 - 20.12 = 806.88\text{ Hz} \implies \delta_B = \frac{806.88}{300.0} = 2.690\text{ ppm}
\]
<p><strong>Step (d): Theoretical intensity ratio (roof effect)</strong></p>
\[
\sin 2\theta = \frac{J}{\sqrt{\Delta\nu^2 + J^2}} = \frac{12.0}{42.0} = 0.2857
\]
\[
\frac{I_{\text{inner}}}{I_{\text{outer}}} = \frac{1 + \sin 2\theta}{1 - \sin 2\theta} = \frac{1 + 0.2857}{1 - 0.2857} = \frac{1.2857}{0.7143} = 1.800
\]
<p>The inner peaks (lines 2 and 3) are \(1.8\) times taller than the outer peaks (lines 1 and 4), producing the characteristic inward roof slant.</p>"""
            },
            {
                "id": "u9-prob4",
                "number": 4,
                "title": "DEPT-135 and DEPT-90 Carbon Multiplicity Assignment",
                "difficulty": "Foundational",
                "statement": r"""A compound with molecular formula \(\text{C}_6\text{H}_{12}\text{O}\) produces six distinct peaks in its broadband decoupled \(^{13}\text{C}\{^1\text{H}\}\) NMR spectrum:
C1: \(208.5\text{ ppm}\)
C2: \(52.3\text{ ppm}\)
C3: \(38.4\text{ ppm}\)
C4: \(24.8\text{ ppm}\)
C5: \(22.5\text{ ppm}\)
C6: \(14.1\text{ ppm}\)
DEPT spectral editing reveals:
In DEPT-90: Only the peak at \(52.3\text{ ppm}\) is observed (pointing up).
In DEPT-135: Peaks at \(52.3\text{ ppm}\), \(22.5\text{ ppm}\), and \(14.1\text{ ppm}\) point up (positive); peaks at \(38.4\text{ ppm}\) and \(24.8\text{ ppm}\) point down (negative); the peak at \(208.5\text{ ppm}\) is absent.
(a) Determine the carbon multiplicity (quaternary \(\text{C}\), \(\text{CH}\), \(\text{CH}_2\), or \(\text{CH}_3\)) for each of the six carbon signals.
(b) Propose the constitutional formula and name of the compound.""",
                "solution": r"""<p><strong>Step (a): Carbon multiplicity assignments</strong></p>
<ol>
  <li><strong>C1 (\(208.5\text{ ppm}\)):</strong> Absent in both DEPT-90 and DEPT-135. High chemical shift indicates a carbonyl carbon. It is a <strong>quaternary carbon (\(\text{C}_{\text{quat}}\))</strong> (specifically a ketone carbonyl \(\text{C=O}\)).</li>
  <li><strong>C2 (\(52.3\text{ ppm}\)):</strong> Present in DEPT-90 (up) and DEPT-135 (up). Only methine carbons appear in DEPT-90. It is a <strong>\(\text{CH}\) (methine) group</strong>.</li>
  <li><strong>C3 (\(38.4\text{ ppm}\)):</strong> Absent in DEPT-90; negative (pointing down) in DEPT-135. Methylene carbons invert in DEPT-135. It is a <strong>\(\text{CH}_2\) (methylene) group</strong>.</li>
  <li><strong>C4 (\(24.8\text{ ppm}\)):</strong> Absent in DEPT-90; negative (pointing down) in DEPT-135. It is a <strong>\(\text{CH}_2\) (methylene) group</strong>.</li>
  <li><strong>C5 (\(22.5\text{ ppm}\)):</strong> Absent in DEPT-90; positive (pointing up) in DEPT-135. Since it is absent in DEPT-90, it must be a <strong>\(\text{CH}_3\) (methyl) group</strong>.</li>
  <li><strong>C6 (\(14.1\text{ ppm}\)):</strong> Absent in DEPT-90; positive (pointing up) in DEPT-135. It is a <strong>\(\text{CH}_3\) (methyl) group</strong>.</li>
</ol>
<p>Summary of carbon inventory: \(1 \times \text{C=O} + 1 \times \text{CH} + 2 \times \text{CH}_2 + 2 \times \text{CH}_3 = \text{C}_6\text{H}_{12}\text{O}\).</p>
<p><strong>Step (b): Proposed structure</strong></p>
<p>The molecular formula has unsaturation index \(\text{DBE} = 6 - \frac{12}{2} + 1 = 1\), fully accounted for by the ketone carbonyl (\(\text{C=O}\)).</p>
<p>The presence of two methyl groups, two methylene groups, one methine group, and one ketone carbonyl establishes the structure as:</p>
\[
\text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH}(\text{CH}_3)-\text{CHO} \quad \text{or} \quad \text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CO}-\text{CH}(\text{CH}_3)_2 \quad (\text{etc.})
\]
<p>With an acyclic ketone at \(208.5\text{ ppm}\) and only 6 carbons: <strong>2-Hexanone</strong> has \(3 \times \text{CH}_2, 2 \times \text{CH}_3\); whereas <strong>3-Methyl-2-pentanone</strong> possesses: \(\text{C=O}\) (C1), \(\text{CH}\) (C2), \(\text{CH}_2\) (C3), and two \(\text{CH}_3\) groups, perfectly matching the inventory! Thus, the molecule is <strong>3-methylpentan-2-one</strong> (or 2-methylpentan-3-one).</p>"""
            },
            {
                "id": "u9-prob5",
                "number": 5,
                "title": "NOESY Distance Quantification and Stereochemical Assignment",
                "difficulty": "Advanced",
                "statement": r"""In a stereochemical investigation of a rigid bicyclic lactam, the Nuclear Overhauser Effect cross-peak volume \(V_{ij}\) scales with internuclear distance as \(V_{ij} \propto r_{ij}^{-6}\).
A fixed reference distance between two geminal methylene protons is known to be \(r_{\text{ref}} = 1.78\text{ \AA}\), giving a reference NOESY cross-peak volume of \(V_{\text{ref}} = 4.50 \times 10^5\text{ units}\).
A cross-peak between bridgehead proton \(H_X\) and methyl ester proton \(H_Y\) has an integrated volume of \(V_{XY} = 8.20 \times 10^3\text{ units}\).
(a) Derive the distance formula: \(r_{XY} = r_{\text{ref}} \left(\frac{V_{\text{ref}}}{V_{XY}}\right)^{1/6}\).
(b) Calculate the distance \(r_{XY}\) in Angstroms.
(c) Molecular modeling indicates that if the methyl ester is in the *endo* configuration, the distance is predicted to be \(\approx 2.5\text{ \AA}\); if *exo*, the distance is predicted to be \(\approx 3.5\text{ \AA}\). Determine the stereochemical configuration of the compound.""",
                "solution": r"""<p><strong>Step (a): Derivation of distance formula</strong></p>
<p>According to the through-space dipolar cross-relaxation rate in the isolated spin-pair approximation (ISPA):</p>
\[
V_{ij} = k \cdot r_{ij}^{-6} \implies r_{ij} = \left(\frac{k}{V_{ij}}\right)^{1/6}
\]
<p>Taking the ratio with the reference pair:</p>
\[
\frac{V_{XY}}{V_{\text{ref}}} = \left(\frac{r_{\text{ref}}}{r_{XY}}\right)^6 \implies \left(\frac{r_{XY}}{r_{\text{ref}}}\right)^6 = \frac{V_{\text{ref}}}{V_{XY}} \implies r_{XY} = r_{\text{ref}} \left(\frac{V_{\text{ref}}}{V_{XY}}\right)^{1/6}
\]
<p><strong>Step (b): Distance calculation</strong></p>
\[
\frac{V_{\text{ref}}}{V_{XY}} = \frac{4.50 \times 10^5}{8.20 \times 10^3} = 54.878
\]
\[
(54.878)^{1/6} = 1.9482
\]
\[
r_{XY} = 1.78\text{ \AA} \times 1.9482 = 3.468\text{ \AA} \approx 3.47\text{ \AA}
\]
<p><strong>Step (c): Stereochemical assignment</strong></p>
<p>The experimentally derived distance \(r_{XY} = 3.47\text{ \AA}\) matches the predicted distance for the *exo* isomer (\(\approx 3.5\text{ \AA}\)) within \(1\%\) error, and is drastically larger than the *endo* expectation (\(2.5\text{ \AA}\), which would yield \(V_{XY} \sim 7.2 \times 10^4\)).</p>
<p>Therefore, the compound is unequivocally assigned as the <strong>*exo* stereoisomer</strong>.</p>"""
            },
            {
                "id": "u9-prob6",
                "number": 6,
                "title": "Complete 2D NMR Structural Assembly: COSY and HSQC Connectivity",
                "difficulty": "Advanced",
                "statement": r"""An unknown fragrant ester (\(\text{C}_5\text{H}_{10}\text{O}_2\)) is analyzed by 1D and 2D NMR.
Spectral data:
1. \(^1\text{H}\) NMR:
   Signal A: \(\delta = 4.08\text{ ppm}\) (triplet, \(J = 6.8\text{ Hz}\), \(2\text{H}\))
   Signal B: \(\delta = 2.05\text{ ppm}\) (singlet, \(3\text{H}\))
   Signal C: \(\delta = 1.65\text{ ppm}\) (sextet, \(J = 6.8\text{ Hz}\), \(2\text{H}\))
   Signal D: \(\delta = 0.95\text{ ppm}\) (triplet, \(J = 6.8\text{ Hz}\), \(3\text{H}\))
2. 2D COSY cross-peaks:
   Cross-peak between Signal A and Signal C.
   Cross-peak between Signal C and Signal D.
   Signal B shows zero COSY cross-peaks.
3. 2D HSQC correlations:
   Signal A correlates with carbon at \(\delta = 66.2\text{ ppm}\).
   Signal B correlates with carbon at \(\delta = 20.8\text{ ppm}\).
   Signal C correlates with carbon at \(\delta = 22.0\text{ ppm}\).
   Signal D correlates with carbon at \(\delta = 10.3\text{ ppm}\).
   (Uncorrelated carbonyl carbon at \(\delta = 171.2\text{ ppm}\)).
(a) Deduce the spin system and connectivity from the COSY correlations.
(b) Assemble the complete chemical structure and name the ester.""",
                "solution": r"""<p><strong>Step (a): Analysis of spin systems</strong></p>
<ol>
  <li><strong>Spin System 1 (A-C-D):</strong>
    <ul>
      <li>Signal A (\(\delta = 4.08\text{ ppm}\), \(2\text{H}\), triplet) couples to C. Its downfield shift (\(4.08\text{ ppm}\)) and carbon shift (\(66.2\text{ ppm}\)) indicate a methylene group directly bonded to the ester oxygen: \(\text{-O-CH}_2\text{-}\).</li>
      <li>Signal C (\(\delta = 1.65\text{ ppm}\), \(2\text{H}\), sextet) couples to both A (\(2\text{H}\)) and D (\(3\text{H}\)), giving \(n=5\) neighbors \(\implies\) sextet. It is a central methylene: \(\text{-CH}_2\text{-}\).</li>
      <li>Signal D (\(\delta = 0.95\text{ ppm}\), \(3\text{H}\), triplet) couples to C (\(2\text{H}\)). It is a terminal methyl group: \(\text{-CH}_3\).</li>
    </ul>
    COSY connectivity: \(\text{-O-CH}_2(\text{A})-\text{CH}_2(\text{C})-\text{CH}_3(\text{D})\). This establishes an intact <strong>propyl group</strong> attached to oxygen (\(\text{-O-CH}_2\text{CH}_2\text{CH}_3\)).
  </li>
  <li><strong>Spin System 2 (B):</strong>
    <ul>
      <li>Signal B (\(\delta = 2.05\text{ ppm}\), \(3\text{H}\), sharp singlet). Shows zero COSY cross-peaks, meaning it has no protons on adjacent carbons. Its chemical shift (\(2.05\text{ ppm}\)) is characteristic of an acetyl methyl group attached directly to a carbonyl: \(\text{CH}_3-\text{C(=O)-}\).</li>
    </ul>
  </li>
  <li><strong>Carbonyl group:</strong>
    The quaternary carbon at \(\delta = 171.2\text{ ppm}\) is an ester carbonyl (\(\text{-COO-}\)).
  </li>
</ol>
<p><strong>Step (b): Structural assembly</strong></p>
<p>Combining the acetyl group (\(\text{CH}_3\text{CO-}\)) and the propoxy group (\(\text{-OCH}_2\text{CH}_2\text{CH}_3\)):</p>
\[
\text{CH}_3-\text{C}(=\text{O})-\text{O}-\text{CH}_2-\text{CH}_2-\text{CH}_3
\]
<p>The compound is uniquely and conclusively identified as <strong>propyl acetate</strong> (propyl ethanoate).</p>"""
            },
            {
                "id": "u9-prob7",
                "number": 7,
                "title": "Pulse Angle and Nutation Calculation in FT-NMR",
                "difficulty": "Foundational",
                "statement": r"""In a modern Fourier Transform NMR spectrometer, an RF pulse is applied on-resonance with magnetic field amplitude \(B_1 = 5.87 \times 10^{-4}\text{ Tesla}\).
For protons with gyromagnetic ratio \(\gamma = 2.67522 \times 10^8\text{ rad}/(\text{s}\cdot\text{T})\):
(a) Calculate the nutation frequency \(\omega_1 = \gamma B_1\) in \(\text{rad/s}\) and in kHz.
(b) Calculate the duration \(t_{90}\) (in microseconds, \(\mu\text{s}\)) required for a \(90^\circ\) (\(\pi/2\) radian) flip angle.
(c) What pulse duration \(t_{180}\) is required for an inversion pulse (\(180^\circ\))?""",
                "solution": r"""<p><strong>Step (a): Nutation frequency</strong></p>
\[
\omega_1 = \gamma B_1 = (2.67522 \times 10^8\text{ rad/s}\cdot\text{T})(5.87 \times 10^{-4}\text{ T}) = 1.57035 \times 10^5\text{ rad/s}
\]
<p>In kHz:</p>
\[
f_1 = \frac{\omega_1}{2\pi} = \frac{1.57035 \times 10^5}{6.283185} = 2.4993 \times 10^4\text{ Hz} \approx 25.0\text{ kHz}
\]
<p><strong>Step (b): 90-degree pulse duration</strong></p>
<p>The tip angle is \(\theta = \omega_1 t_p\):</p>
\[
\theta = \frac{\pi}{2} \implies t_{90} = \frac{\pi / 2}{\omega_1} = \frac{1.570796}{1.57035 \times 10^5\text{ s}^{-1}} = 1.000 \times 10^{-5}\text{ s} = 10.0\ \mu\text{s}
\]
<p><strong>Step (c): 180-degree pulse duration</strong></p>
\[
t_{180} = 2 \times t_{90} = 2 \times 10.0\ \mu\text{s} = 20.0\ \mu\text{s}
\]
<p>A \(10\ \mu\text{s}\) pulse tips the magnetization into the transverse plane, while a \(20\ \mu\text{s}\) pulse fully inverts it.</p>"""
            }
        ]
    }
    units.append(u9)

    # =========================================================================
    # UNIT 10: Electron Spin Resonance (ESR/EPR) & Mössbauer Spectroscopy
    # =========================================================================
    u10 = {
        "id": "unit10",
        "number": 10,
        "title": "Unit 10: Electron Spin Resonance (ESR/EPR) & Mössbauer Spectroscopy",
        "description": "Physical principles of Electron Spin Resonance (ESR/EPR), electron Zeeman interaction, g-tensor anisotropy, isotropic and anisotropic hyperfine coupling, McConnell relation for radical spin densities, transition metal zero-field splitting, spin labeling, Mössbauer recoil-free fraction, isomer shift, electric quadrupole splitting, and magnetic hyperfine Zeeman splitting.",
        "simulations": [
            {
                "id": "sim_spec_esr_mossbauer_hyperfine",
                "title": "ESR/EPR Hyperfine & Mössbauer Spectroscopy",
                "description": "Interactive 60 FPS dual-mode simulator for advanced magnetic and nuclear resonance. Mode A (ESR): modulate hyperfine coupling constant a to view first-derivative ESR multiplets (1:3:3:1 methyl radical) and verify the McConnell relation. Mode B (Mössbauer): adjust Doppler velocity, isomer shift delta, quadrupole splitting, and internal magnetic field to observe the 57Fe transmission sextet."
            }
        ],
        "sections": [
            {
                "id": "u10-sec1",
                "number": "10.1",
                "title": "Physical Foundations of Electron Spin Resonance (ESR/EPR)",
                "content": r"""<p>Electron Spin Resonance (ESR), also designated Electron Paramagnetic Resonance (EPR), detects transitions between magnetic energy levels of chemical species possessing one or more <strong>unpaired electrons</strong> (\(S \ge 1/2\)), such as organic free radicals, radical ions, triplet states, and transition metal complexes.</p>
<h4 class="content-heading">The Electron Zeeman Hamiltonian</h4>
<p>An unpaired electron possesses spin angular momentum \(\vec{S}\) (\(S = 1/2\)) and a collinear magnetic dipole moment \(\vec{\mu}_e\):</p>
\[
\vec{\mu}_e = -g_e \mu_B \vec{S} / \hbar
\]
<p>where \(g_e = 2.00231930436\) is the free electron \(g\)-factor and \(\mu_B = \frac{e\hbar}{2m_e} = 9.27401 \times 10^{-24}\text{ J/T}\) is the Bohr magneton. Note that \(\mu_B\) is approximately 658 times larger than the nuclear magneton \(\mu_N\), rendering ESR spectroscopy intrinsically far more sensitive than NMR.</p>
<p>In a static magnetic field \(\vec{B}_0 = B_0 \hat{z}\), the electron Zeeman Hamiltonian is:</p>
\[
\hat{H}_{EZ} = -\vec{\mu}_e \cdot \vec{B}_0 = g \mu_B B_0 \hat{S}_z
\]
<p>The energy eigenvalues for \(M_S = \pm 1/2\) are:</p>
\[
E(M_S) = g \mu_B B_0 M_S \implies E_\beta = +\frac{1}{2}g\mu_B B_0, \quad E_\alpha = -\frac{1}{2}g\mu_B B_0
\]
<p>The resonant energy splitting is:</p>
\[
\Delta E = h\nu = g \mu_B B_0
\]
<h4 class="content-heading">Microwave Bands & First-Derivative Detection</h4>
<p>Unlike NMR where frequency is swept at fixed field, in ESR the microwave frequency is kept constant inside a high-\(Q\) resonant cavity while the magnetic field \(B_0\) is swept. Standard operational microwave bands include:</p>
<ul>
  <li><strong>X-band:</strong> \(\nu \approx 9.5\text{ GHz}\) (\(\lambda \approx 3.2\text{ cm}\)), resonant field \(B_0 \approx 0.34\text{ T}\) (\(3400\text{ Gauss}\)).</li>
  <li><strong>Q-band:</strong> \(\nu \approx 34\text{ GHz}\) (\(\lambda \approx 8.8\text{ mm}\)), resonant field \(B_0 \approx 1.2\text{ T}\).</li>
  <li><strong>W-band:</strong> \(\nu \approx 94\text{ GHz}\), resonant field \(B_0 \approx 3.4\text{ T}\).</li>
</ul>
<p>Phase-sensitive detection with small magnetic field modulation (\(100\text{ kHz}\)) is universally employed, causing ESR spectra to be recorded as the <strong>first derivative of absorption</strong> (\(dA/dB\) vs \(B\)).</p>"""
            },
            {
                "id": "u10-sec2",
                "number": "10.2",
                "title": "The g-Tensor & Deviations from Free Electron Spin",
                "content": r"""<p>In real chemical systems, spin-orbit coupling \(\hat{H}_{SO} = \lambda \vec{L} \cdot \vec{S}\) mixes excited electronic states into the ground state, generating unquenched orbital angular momentum that shifts the effective \(g\)-factor away from the free-electron value \(g_e = 2.0023\):</p>
\[
g = g_e + \Delta g = g_e - \frac{2 \lambda}{\Delta E_{\text{el}}}
\]
<p>where \(\lambda\) is the spin-orbit coupling constant of the atom and \(\Delta E_{\text{el}}\) is the energy separation to the excited state:</p>
<ul>
  <li>If the unpaired electron resides in an orbital that is <em>less than half-full</em> (e.g., \(d^1\) in \(\text{Ti}^{3+}\), \(\text{VO}^{2+}\)), \(\lambda > 0\), causing \(g < g_e\) (typically \(1.90 - 1.98\)).</li>
  <li>If the unpaired electron resides in an orbital that is <em>more than half-full</em> (e.g., \(d^9\) in \(\text{Cu}^{2+}\)), \(\lambda < 0\), causing \(g > g_e\) (typically \(2.05 - 2.30\)).</li>
  <li>For organic free radicals where the electron is delocalized over carbon \(2p\) \(\pi\)-orbitals (\(\lambda\) is very small), \(g \approx 2.0025 - 2.0060\), very close to \(g_e\).</li>
</ul>
<h4 class="content-heading">g-Tensor Anisotropy</h4>
<p>In frozen solutions or single crystals, the \(g\)-factor is a second-rank tensor represented in its principal axis frame by three values \((g_{xx}, g_{yy}, g_{zz})\):</p>
<ul>
  <li><strong>Isotropic (Liquids):</strong> Rapid tumbling averages the tensor to a scalar: \(g_{\text{iso}} = \frac{1}{3}(g_{xx} + g_{yy} + g_{zz})\).</li>
  <li><strong>Axial Symmetry:</strong> \(g_{xx} = g_{yy} = g_\perp\), \(g_{zz} = g_\parallel\).</li>
  <li><strong>Rhombic Symmetry:</strong> \(g_{xx} \neq g_{yy} \neq g_{zz}\).</li>
</ul>"""
            },
            {
                "id": "u10-sec3",
                "number": "10.3",
                "title": "Hyperfine Coupling & Nuclear Spin Interactions",
                "content": r"""<p>When the unpaired electron interacts magnetically with nearby magnetic nuclei possessing nuclear spin \(I\) (e.g., \(^1\text{H}\) with \(I=1/2\), \(^{14}\text{N}\) with \(I=1\)), the energy levels split into <strong>hyperfine components</strong>.</p>
<h4 class="content-heading">Hyperfine Hamiltonian & Energy Levels</h4>
<p>The isotropic spin Hamiltonian incorporating Zeeman and scalar Fermi contact hyperfine interactions is:</p>
\[
\hat{H} = g \mu_B B_0 \hat{S}_z + a \hat{\vec{S}} \cdot \hat{\vec{I}} \approx g \mu_B B_0 \hat{S}_z + a \hat{S}_z \hat{I}_z
\]
<p>where \(a\) is the isotropic <strong>hyperfine splitting constant</strong> (expressed in Gauss, Tesla, or MHz). The energy eigenvalues are:</p>
\[
E(M_S, M_I) = g \mu_B B_0 M_S + a M_S M_I
\]
<h4 class="content-heading">ESR Selection Rules & Line Counts</h4>
<p>The electric dipole selection rules for microwave absorption are:</p>
\[
\Delta M_S = \pm 1, \quad \Delta M_I = 0 \quad (\text{the nuclear spin cannot flip during an electron transition})
\]
<p>For an electron coupled to a single nucleus of spin \(I\), the resonant field condition is:</p>
\[
B_{\text{res}} = B_0 - \frac{a}{g \mu_B} M_I = B_0 - a' M_I
\]
<p>The spectrum splits into \(2I + 1\) equally spaced lines of identical intensity.</p>
<ul>
  <li>Coupling to a single proton (\(I = 1/2\)): \(2(1/2) + 1 = 2\) lines (<strong>doublet</strong>, 1:1), separated by \(a\).</li>
  <li>Coupling to a single \(^{14}\text{N}\) nucleus (\(I = 1\), as in nitroxide spin labels): \(2(1) + 1 = 3\) lines (<strong>triplet</strong>, 1:1:1), separated by \(a_N\).</li>
  <li>Coupling to \(n\) equivalent protons (\(I = 1/2\)): \(n + 1\) lines with binomial intensities matching Pascal's triangle. For the methyl radical (\(\cdot\text{CH}_3\)), coupling to 3 equivalent protons yields \(3 + 1 = 4\) lines (<strong>quartet</strong>, 1:3:3:1) separated by \(a_H = 23.0\text{ G}\).</li>
</ul>"""
            },
            {
                "id": "u10-sec4",
                "number": "10.4",
                "title": "Radical Spin Densities & The McConnell Relation",
                "content": r"""<p>In planar conjugated organic \(\pi\)-radicals (e.g., benzene radical anion \(\text{C}_6\text{H}_6^{\bullet-}\) or naphthalene radical anion), the unpaired electron resides in a delocalized \(\pi\)-molecular orbital. Because \(\pi\)-orbitals possess a nodal plane containing all the carbon and hydrogen nuclei, the direct \(\pi\)-electron probability density at the proton nucleus is strictly zero: \(|\psi_\pi(0)|^2 = 0\).</p>
<h4 class="content-heading">The McConnell Equation</h4>
<p>Despite this nodal plane, substantial proton hyperfine splitting is observed (\(a_H = 3.75\text{ G}\) in benzene anion). Harden McConnell proved that this splitting arises from <strong>spin polarization</strong> of the \(\text{C-H}\) \(\sigma\)-bond electrons:</p>
<p>Exchange interaction between the unpaired \(\pi\)-electron on carbon and the \(\sigma\)-electron of the \(\text{C-H}\) bond favors parallel spins. Consequently, the \(\sigma\)-electron residing near carbon has spin parallel to the \(\pi\)-electron, forcing the paired \(\sigma\)-electron near the hydrogen nucleus to have <em>antiparallel</em> spin, inducing a net negative spin density at the proton.</p>
<p>The resulting isotropic proton hyperfine splitting \(a_H\) is directly proportional to the \(\pi\)-spin density \(\rho_\pi\) on the adjacent carbon atom, formalized by the <strong>McConnell equation</strong>:</p>
\[
a_H = Q \cdot \rho_\pi
\]
<p>where \(Q\) is the semi-empirical McConnell proportionality constant (typically \(Q \approx -22.5\text{ Gauss} = -2.25\text{ mT}\)), and \(\rho_\pi\) is the spin density on carbon (\(\sum_i \rho_{\pi, i} = 1\)).</p>
<p>For the benzene radical anion (\(\text{C}_6\text{H}_6^{\bullet-}\)), the unpaired electron is shared equally among all 6 carbons by symmetry: \(\rho_\pi = 1/6\):</p>
\[
|a_H| = \frac{|Q|}{6} = \frac{22.5\text{ G}}{6} = 3.75\text{ G}
\]
<p>The ESR spectrum of \(\text{C}_6\text{H}_6^{\bullet-}\) displays a symmetric septet of 7 lines (\(n+1 = 6+1=7\)) with intensity ratios 1:6:15:20:15:6:1, confirming the McConnell relation.</p>"""
            },
            {
                "id": "u10-sec5",
                "number": "10.5",
                "title": "Transition Metal ESR, Kramers' Degeneracy & Spin Labeling",
                "content": r"""<p>Transition metal ions frequently possess multiple unpaired d-electrons (\(S > 1/2\)). The combined effects of crystal fields and spin-orbit coupling give rise to <strong>zero-field splitting (ZFS)</strong>, governed by the spin Hamiltonian:</p>
\[
\hat{H}_{\text{ZFS}} = D \left( \hat{S}_z^2 - \frac{1}{3} S(S+1) \right) + E (\hat{S}_x^2 - \hat{S}_y^2)
\]
<p>where \(D\) is the axial zero-field splitting parameter and \(E\) is the rhombic parameter.</p>
<h4 class="content-heading">Kramers' Theorem</h4>
<blockquote>
  <strong>Kramers' Theorem:</strong> Any quantum system with an odd number of electrons (half-integer total spin \(S = 1/2, 3/2, 5/2 \dots\)) must possess at least twofold degeneracy for every energy state in the absence of an external magnetic field (Kramers doublet).
</blockquote>
<p>Consequently, half-integer spin systems (e.g., \(\text{Cu}^{2+}\) with \(S=1/2\), \(\text{Fe}^{3+}\) high-spin with \(S=5/2\), \(\text{Mn}^{2+}\) with \(S=5/2\)) always exhibit observable ESR spectra at conventional microwave frequencies. In contrast, integer spin systems (e.g., \(\text{Fe}^{2+}\) with \(S=2\), \(\text{Ni}^{2+}\) with \(S=1\)) often have large zero-field splittings exceeding the microwave photon energy (\(D > h\nu\)), rendering them 'ESR-silent' at standard X-band.</p>
<h4 class="content-heading">Spin Labeling of Biomembranes</h4>
<p>Diamagnetic biological macromolecules (proteins, lipid bilayers) lack unpaired electrons. In <strong>spin labeling</strong>, a stable nitroxide free radical (e.g., TEMPO or MTSSL) containing an \(>\text{N}-\text{O}^\bullet\) moiety is site-specifically tethered. The \(^{14}\text{N}\) hyperfine triplet lineshape reports on the rotational correlation time \(\tau_c\), providing real-time measurements of membrane fluidity and protein conformational flexibility.</p>"""
            },
            {
                "id": "u10-sec6",
                "number": "10.6",
                "title": "Physical Foundations of Mössbauer Spectroscopy",
                "content": r"""<p>Discovered by Rudolf Mössbauer in 1957 (1961 Nobel Prize), Mössbauer spectroscopy probes resonant nuclear \(\gamma\)-ray absorption and fluorescence between nuclear ground and isomeric excited states, most prominently in \(^{57}\text{Fe}\) and \(^{119}\text{Sn}\).</p>
<h4 class="content-heading">The Nuclear Recoil Problem</h4>
<p>When an isolated free nucleus of mass \(M\) emits a \(\gamma\)-ray photon of energy \(E_\gamma\), conservation of momentum requires the nucleus to recoil with momentum \(p_{\text{recoil}} = E_\gamma / c\). The recoil kinetic energy \(E_R\) imparted to the nucleus is:</p>
\[
E_R = \frac{p^2}{2M} = \frac{E_\gamma^2}{2 M c^2}
\]
<p>For the \(14.41\text{ keV}\) transition of \(^{57}\text{Fe}\), \(E_R \approx 1.95 \times 10^{-3}\text{ eV}\). Because the natural Heisenberg linewidth of the nuclear excited state (\(\tau = 141\text{ ns}\)) is extraordinarily narrow:</p>
\[
\Gamma = \frac{\hbar}{\tau} = \frac{1.055 \times 10^{-34}\text{ J}\cdot\text{s}}{1.41 \times 10^{-7}\text{ s}} = 4.67 \times 10^{-9}\text{ eV}
\]
<p>The recoil energy is roughly \(400,000\) times larger than the linewidth (\(E_R \gg \Gamma\)). The emitted photon energy (\(E_\gamma - E_R\)) is severely deficient, and cannot be absorbed by a second stationary nucleus which requires \((E_\gamma + E_R)\). In free atoms, resonant nuclear absorption is completely impossible!</p>
<h4 class="content-heading">The Recoil-Free Mössbauer Effect</h4>
<p>Mössbauer discovered that when the emitting and absorbing nuclei are bound in a solid crystalline lattice at low temperatures, the recoil momentum can be transferred to the <strong>entire macroscopic crystal lattice</strong> (\(M_{\text{crystal}} \sim 10^{20} M_{\text{nucleus}}\)):</p>
\[
E_{R, \text{crystal}} = \frac{E_\gamma^2}{2 M_{\text{crystal}} c^2} \approx 0
\]
<p>The fraction of \(\gamma\)-ray emissions that occur completely recoil-free (without exciting lattice phonons) is the <strong>Lamb-Mössbauer factor</strong> \(f\):</p>
\[
f = \exp\left(-\frac{E_\gamma^2 \langle x^2 \rangle}{\hbar^2 c^2}\right) = \exp(-k^2 \langle x^2 \rangle)
\]
<p>where \(\langle x^2 \rangle\) is the mean-square vibrational displacement of the nucleus. Recoil-free emission preserves the ultranarrow natural linewidth \(\Gamma \sim 10^{-9}\text{ eV}\), enabling resolving powers of \(R = \frac{E_\gamma}{\Gamma} \sim \frac{14400}{4.67 \times 10^{-9}} \approx 3 \times 10^{12}\), the sharpest spectroscopic resonance in physics!</p>
<h4 class="content-heading">Doppler Velocity Modulation</h4>
<p>Because linewidths are on the order of \(10^{-8}\text{ eV}\), scanning through resonances cannot be accomplished with monochromators. Instead, the radioactive source is mechanically translated with Doppler velocity \(v\) (\(\text{mm/s}\)):</p>
\[
\Delta E_{\text{Doppler}} = E_\gamma \frac{v}{c}
\]
<p>A velocity of just \(1.0\text{ mm/s}\) shifts the \(\gamma\)-ray energy by \(4.8 \times 10^{-8}\text{ eV}\), easily scanning the entire resonance profile.</p>"""
            },
            {
                "id": "u10-sec7",
                "number": "10.7",
                "title": "Hyperfine Interactions in Mössbauer: Isomer Shift, Quadrupole & Magnetic Splitting",
                "content": r"""<p>The extreme resolution of the Mössbauer effect allows direct measurement of hyperfine electromagnetic interactions between the nucleus and surrounding electrons. Three primary hyperfine parameters characterize a Mössbauer spectrum:</p>
<h4 class="content-heading">1. The Isomer Shift (\(\delta\))</h4>
<p>The isomer shift arises from the electrostatic Coulomb monopole interaction between the finite nuclear charge radius \(R\) and the s-electron charge density at the nucleus \(|\psi(0)|^2\):</p>
\[
\delta = \frac{2\pi}{3} Z e^2 \left( \langle R_e^2 \rangle - \langle R_g^2 \rangle \right) \left[ |\psi_{\text{abs}}(0)|^2 - |\psi_{\text{source}}(0)|^2 \right]
\]
<p>For \(^{57}\text{Fe}\), the nuclear radius contracts upon excitation: \((\langle R_e^2 \rangle - \langle R_g^2 \rangle) < 0\). Therefore, higher s-electron density produces a <strong>more negative</strong> isomer shift. Because d-electrons shield s-electrons from the nucleus, \(\delta\) reports directly on iron oxidation and spin states:</p>
<ul>
  <li>High-spin \(\text{Fe}^{2+}\) (\(d^6\)): Maximum d-electron shielding \(\implies\) low \(|\psi(0)|^2\) \(\implies\) \(\delta \approx +0.8 - +1.4\text{ mm/s}\).</li>
  <li>High-spin \(\text{Fe}^{3+}\) (\(d^5\)): Lower d-shielding \(\implies\) higher \(|\psi(0)|^2\) \(\implies\) \(\delta \approx +0.3 - +0.6\text{ mm/s}\).</li>
  <li>Low-spin \(\text{Fe}^{2+}\) (\(d^6\)) / \(\text{Fe}^{3+}\) (\(d^5\)): Strong \(\pi\)-backbonding withdraws d-electrons \(\implies\) \(\delta \approx 0.0 - +0.3\text{ mm/s}\).</li>
</ul>
<h4 class="content-heading">2. Electric Quadrupole Splitting (\(\Delta E_Q\))</h4>
<p>If the nuclear spin satisfies \(I > 1/2\), the nucleus possesses an electric quadrupole moment \(eQ\). In the presence of a non-spherical electric field gradient (EFG) tensor with principal component \(V_{zz} = \frac{\partial^2 V}{\partial z^2}\), the \(I = 3/2\) excited state of \(^{57}\text{Fe}\) splits into two sublevels (\(M_I = \pm 3/2\) and \(M_I = \pm 1/2\)):</p>
\[
\Delta E_Q = \frac{e Q V_{zz}}{2} \sqrt{1 + \frac{\eta^2}{3}}
\]
<p>The ground state (\(I = 1/2\)) remains unsplit. The spectrum displays a symmetric <strong>two-line doublet</strong> separated by \(\Delta E_Q\) (\(\text{mm/s}\)), diagnostic of electronic asymmetry and coordination geometry.</p>
<h4 class="content-heading">3. Magnetic Hyperfine Zeeman Splitting</h4>
<p>In ferromagnetic, antiferromagnetic, or slowly relaxing paramagnetic materials, an internal magnetic field \(\vec{B}_{\text{int}}\) (typically \(30 - 55\text{ Tesla}\)) removes all \(M_I\) degeneracies. The ground state (\(I=1/2\)) splits into 2 levels; the excited state (\(I=3/2\)) splits into 4 levels. Transitions satisfying \(\Delta M_I = 0, \pm 1\) produce a characteristic <strong>six-line sextet</strong> with intensity ratios 3 : 2 : 1 : 1 : 2 : 3.</p>"""
            }
        ],
        "problems": [
            {
                "id": "u10-prob1",
                "number": 1,
                "title": "ESR Resonance Field at X-Band and Q-Band Frequencies",
                "difficulty": "Foundational",
                "statement": r"""A stable organic nitroxide free radical has an isotropic \(g\)-factor of \(g = 2.0060\).
Bohr magneton: \(\mu_B = 9.27401 \times 10^{-24}\text{ J/T}\), Planck's constant: \(h = 6.62607 \times 10^{-34}\text{ J}\cdot\text{s}\).
(a) Calculate the resonant magnetic field \(B_0\) (in Tesla and Gauss) when measured in an X-band spectrometer at frequency \(\nu = 9.500\text{ GHz}\).
(b) Calculate the resonant magnetic field \(B_0\) when measured in a Q-band spectrometer at frequency \(\nu = 34.000\text{ GHz}\).
(c) By what factor does spectral dispersion in magnetic field increase at Q-band compared to X-band?""",
                "solution": r"""<p><strong>Step (a): Resonant field at X-band</strong></p>
<p>The ESR resonance condition is \(h\nu = g\mu_B B_0\):</p>
\[
B_0 = \frac{h\nu}{g\mu_B}
\]
\[
h\nu = (6.62607 \times 10^{-34}\text{ J}\cdot\text{s})(9.500 \times 10^9\text{ s}^{-1}) = 6.29477 \times 10^{-24}\text{ J}
\]
\[
g\mu_B = 2.0060 \times (9.27401 \times 10^{-24}\text{ J/T}) = 1.86037 \times 10^{-23}\text{ J/T}
\]
\[
B_0 = \frac{6.29477 \times 10^{-24}}{1.86037 \times 10^{-23}} = 0.33836\text{ Tesla}
\]
<p>In Gauss (\(1\text{ T} = 10000\text{ Gauss}\)):</p>
\[
B_0 = 3383.6\text{ Gauss}
\]
<p><strong>Step (b): Resonant field at Q-band</strong></p>
\[
h\nu = (6.62607 \times 10^{-34})(34.000 \times 10^9) = 2.25286 \times 10^{-23}\text{ J}
\]
\[
B_0 = \frac{2.25286 \times 10^{-23}}{1.86037 \times 10^{-23}} = 1.2110\text{ Tesla} = 12110\text{ Gauss}
\]
<p><strong>Step (c): Dispersion factor</strong></p>
\[
\frac{B_0(\text{Q-band})}{B_0(\text{X-band})} = \frac{34.000\text{ GHz}}{9.500\text{ GHz}} = 3.579
\]
<p>Field dispersion increases by \(\approx 3.58\)-fold at Q-band, allowing subtle \(g\)-tensor anisotropies to be clearly resolved from field-independent hyperfine couplings.</p>"""
            },
            {
                "id": "u10-prob2",
                "number": 2,
                "title": "ESR Hyperfine Multiplet Analysis of Methyl and Ethyl Radicals",
                "difficulty": "Intermediate",
                "statement": r"""Predict the ESR hyperfine splitting pattern (number of lines, line spacing, and relative binomial intensities) for:
(a) The methyl radical (\(\cdot\text{CH}_3\)), with three equivalent protons and \(a_H = 23.0\text{ Gauss}\).
(b) The ethyl radical (\(\cdot\text{CH}_2\text{CH}_3\)), possessing two \(\alpha\)-protons (\(a_\alpha = 22.4\text{ G}\)) and three \(\beta\)-protons (\(a_\beta = 26.9\text{ G}\)).
(c) Total spectral width (separation between outermost lines) for each radical.""",
                "solution": r"""<p><strong>Step (a): Methyl radical (·CH3)</strong></p>
<p>The unpaired electron couples to \(n = 3\) equivalent protons (\(I = 1/2\)).</p>
<p>Number of lines: \(n + 1 = 3 + 1 = 4\) (<strong>quartet</strong>).</p>
<p>Relative intensities from Pascal's triangle: <strong>1 : 3 : 3 : 1</strong>.</p>
<p>Line spacing: \(\Delta B = a_H = 23.0\text{ Gauss}\).</p>
<p>Total width: \((4 - 1) \times 23.0 = 3 \times 23.0 = 69.0\text{ Gauss}\).</p>
<p><strong>Step (b): Ethyl radical (·CH2CH3)</strong></p>
<p>The unpaired electron couples to two non-equivalent sets of protons:</p>
<ol>
  <li>Coupling to 2 \(\alpha\)-protons: splits the resonance into a triplet (1 : 2 : 1) with spacing \(a_\alpha = 22.4\text{ G}\).</li>
  <li>Coupling to 3 \(\beta\)-protons: splits each of the triplet lines into a quartet (1 : 3 : 3 : 1) with spacing \(a_\beta = 26.9\text{ G}\).</li>
</ol>
<p>Total number of lines: \((2 + 1)(3 + 1) = 3 \times 4 = 12\text{ lines}\) (a <strong>triplet of quartets</strong>).</p>
<p><strong>Step (c): Total width of ethyl radical spectrum</strong></p>
\[
\text{Width} = 2 a_\alpha + 3 a_\beta = 2(22.4\text{ G}) + 3(26.9\text{ G}) = 44.8 + 80.7 = 125.5\text{ Gauss}
\]"""
            },
            {
                "id": "u10-prob3",
                "number": 3,
                "title": "Spin Density Calculation in Naphthalene Radical Anion via McConnell Equation",
                "difficulty": "Intermediate",
                "statement": r"""The naphthalene radical anion (\(\text{C}_{10}\text{H}_8^{\bullet-}\)) has \(D_{2h}\) molecular symmetry.
Protons are divided into two chemically distinct sets:
Four \(\alpha\)-protons (positions 1, 4, 5, 8) with hyperfine coupling constant \(|a_\alpha| = 4.90\text{ Gauss}\).
Four \(\beta\)-protons (positions 2, 3, 6, 7) with hyperfine coupling constant \(|a_\beta| = 1.83\text{ Gauss}\).
Using McConnell's proportionality constant \(Q = -22.5\text{ Gauss}\):
(a) Calculate the experimental \(\pi\)-spin densities \(\rho_\alpha\) and \(\rho_\beta\) on the respective carbon atoms.
(b) Verify that the sum of spin densities over the eight peripheral carbons is consistent with total spin \(\sum \rho_i \approx 1\).
(c) State the total number of lines expected in the ESR spectrum of the naphthalene radical anion.""",
                "solution": r"""<p><strong>Step (a): Spin density calculations</strong></p>
<p>According to the McConnell equation \(a_H = Q \cdot \rho_\pi \implies \rho_\pi = |a_H| / |Q|\):</p>
\[
\rho_\alpha = \frac{4.90\text{ G}}{22.5\text{ G}} = 0.2178 \approx 0.218
\]
\[
\rho_\beta = \frac{1.83\text{ G}}{22.5\text{ G}} = 0.0813 \approx 0.081
\]
<p><strong>Step (b): Sum of spin densities</strong></p>
<p>Naphthalene possesses four \(\alpha\)-carbons and four \(\beta\)-carbons:</p>
\[
\sum \rho_{\pi} = 4 \rho_\alpha + 4 \rho_\beta = 4(0.2178) + 4(0.0813) = 0.8712 + 0.3252 = 1.1964
\]
<p>The remaining bridgehead carbons (C9, C10) carry negative spin densities (\(\rho_9 = \rho_{10} \approx -0.098\)) due to \(\sigma\text{-}\pi\) exchange polarization, giving total sum \(\sum_{i=1}^{10} \rho_i = 1.196 - 2(0.098) = 1.000\), exactly verifying the normalization.</p>
<p><strong>Step (c): Total number of lines</strong></p>
<p>The spectrum consists of coupling to 4 equivalent \(\alpha\)-protons and 4 equivalent \(\beta\)-protons:</p>
\[
N_{\text{lines}} = (2 \times 4 \times \frac{1}{2} + 1)(2 \times 4 \times \frac{1}{2} + 1) = (4 + 1)(4 + 1) = 5 \times 5 = 25\text{ lines}
\]
<p>A quintet of quintets containing 25 lines is observed.</p>"""
            },
            {
                "id": "u10-prob4",
                "number": 4,
                "title": "Copper(II) Complex g-Values and Axial ESR Hyperfine Analysis",
                "difficulty": "Advanced",
                "statement": r"""A square-planar copper(II) complex (\(\text{Cu}^{2+}\), \(3d^9\), \(S = 1/2\)) is analyzed in frozen solution at \(77\text{ K}\).
Copper has nuclear spin \(I = 3/2\) (\(100\%\) abundance of \(^{63}\text{Cu}\) and \(^{65}\text{Cu}\)).
The axial ESR spectrum yields:
Parallel region: \(g_\parallel = 2.240\), hyperfine splitting \(A_\parallel = 165\text{ Gauss}\).
Perpendicular region: \(g_\perp = 2.055\), hyperfine splitting \(A_\perp = 25\text{ Gauss}\).
(a) How many hyperfine lines are observed in the parallel (\(g_\parallel\)) and perpendicular (\(g_\perp\)) manifolds?
(b) Explain why \(g_\parallel > g_\perp > g_e\).
(c) At X-band frequency \(\nu = 9.400\text{ GHz}\), calculate the center field \(B_\parallel\) and the positions of the four parallel lines in Gauss.""",
                "solution": r"""<p><strong>Step (a): Number of hyperfine lines</strong></p>
<p>Since \(I = 3/2\), coupling splits the electronic transition into:</p>
\[
2I + 1 = 2(3/2) + 1 = 4\text{ lines (quartet)}
\]
<p>Both the parallel manifold and the perpendicular manifold are split into 4 lines of equal intensity.</p>
<p><strong>Step (b): Explanation of g-value shifts</strong></p>
<p>For a \(d^9\) configuration in a square-planar crystal field, the hole resides in the \(d_{x^2-y^2}\) orbital. Spin-orbit coupling with filled lower orbitals shifts the \(g\)-factors:</p>
\[
g_\parallel = g_e - \frac{8\lambda}{\Delta E(d_{xy} \to d_{x^2-y^2})}, \quad g_\perp = g_e - \frac{2\lambda}{\Delta E(d_{xz, yz} \to d_{x^2-y^2})}
\]
<p>Because the \(d\)-shell is more than half-full, the effective spin-orbit coupling constant is negative: \(\lambda = -830\text{ cm}^{-1} < 0\). Therefore, both \(g\)-values exceed \(g_e\). The factor of 8 in \(g_\parallel\) versus 2 in \(g_\perp\) ensures \(g_\parallel > g_\perp > g_e\).</p>
<p><strong>Step (c): Line positions in parallel manifold</strong></p>
\[
B_\parallel = \frac{h\nu}{g_\parallel \mu_B} = \frac{(6.62607 \times 10^{-34})(9.400 \times 10^9)}{2.240 \times (9.27401 \times 10^{-24})} = \frac{6.2285 \times 10^{-24}}{2.07738 \times 10^{-23}} = 0.29983\text{ T} = 2998.3\text{ G}
\]
<p>The four lines appear at \(B = B_\parallel - A_\parallel M_I\) for \(M_I = +3/2, +1/2, -1/2, -3/2\):</p>
<ul>
  <li>\(M_I = +3/2\): \(B_1 = 2998.3 - 1.5(165) = 2998.3 - 247.5 = 2750.8\text{ G}\)</li>
  <li>\(M_I = +1/2\): \(B_2 = 2998.3 - 0.5(165) = 2998.3 - 82.5 = 2915.8\text{ G}\)</li>
  <li>\(M_I = -1/2\): \(B_3 = 2998.3 + 0.5(165) = 2998.3 + 82.5 = 3080.8\text{ G}\)</li>
  <li>\(M_I = -3/2\): \(B_4 = 2998.3 + 1.5(165) = 2998.3 + 247.5 = 3245.8\text{ G}\)</li>
</ul>"""
            },
            {
                "id": "u10-prob5",
                "number": 5,
                "title": "Mössbauer Recoil Energy and Recoil-Free Fraction Calculation",
                "difficulty": "Intermediate",
                "statement": r"""For the \(14.41\text{ keV}\) \(\gamma\)-ray transition of \(^{57}\text{Fe}\) (nuclear mass \(M = 56.935\text{ u} = 9.454 \times 10^{-26}\text{ kg}\)):
(a) Calculate the recoil energy \(E_R\) (in \(\text{eV}\) and Joules) of a free unconstrained \(^{57}\text{Fe}\) atom.
(b) Compare \(E_R\) with the natural linewidth \(\Gamma = 4.67 \times 10^{-9}\text{ eV}\).
(c) In metallic iron at \(300\text{ K}\), the mean-square vibrational displacement is \(\langle x^2 \rangle = 0.0048\text{ \AA}^2 = 4.8 \times 10^{-23}\text{ m}^2\). Calculate the wavevector \(k = E_\gamma / (\hbar c)\) and determine the Lamb-Mössbauer recoil-free fraction \(f\).""",
                "solution": r"""<p><strong>Step (a): Recoil energy of free ⁵⁷Fe atom</strong></p>
\[
E_\gamma = 14.41\text{ keV} = 14410\text{ eV} = (14410)(1.60218 \times 10^{-19}\text{ J}) = 2.3087 \times 10^{-15}\text{ J}
\]
\[
E_R = \frac{E_\gamma^2}{2 M c^2}
\]
\[
E_\gamma^2 = (2.3087 \times 10^{-15})^2 = 5.3303 \times 10^{-30}\text{ J}^2
\]
\[
2 M c^2 = 2 (9.454 \times 10^{-26}\text{ kg})(2.99792 \times 10^8\text{ m/s})^2 = 2 (9.454 \times 10^{-26})(8.98755 \times 10^{16}) = 1.6994 \times 10^{-8}\text{ J}
\]
\[
E_R = \frac{5.3303 \times 10^{-30}\text{ J}^2}{1.6994 \times 10^{-8}\text{ J}} = 3.1365 \times 10^{-22}\text{ J}
\]
<p>In electron-volts:</p>
\[
E_R = \frac{3.1365 \times 10^{-22}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} = 1.958 \times 10^{-3}\text{ eV} = 1.958\text{ meV}
\]
<p><strong>Step (b): Comparison with natural linewidth</strong></p>
\[
\frac{E_R}{\Gamma} = \frac{1.958 \times 10^{-3}\text{ eV}}{4.67 \times 10^{-9}\text{ eV}} = 4.19 \times 10^5
\]
<p>The recoil energy is over 400,000 times larger than the natural resonance width, precluding any resonance in the gas phase.</p>
<p><strong>Step (c): Lamb-Mössbauer recoil-free fraction f</strong></p>
\[
k = \frac{E_\gamma}{\hbar c} = \frac{2.3087 \times 10^{-15}\text{ J}}{(1.05457 \times 10^{-34}\text{ J}\cdot\text{s})(2.99792 \times 10^8\text{ m/s})} = \frac{2.3087 \times 10^{-15}}{3.1615 \times 10^{-26}} = 7.3025 \times 10^{10}\text{ m}^{-1}
\]
\[
k^2 = (7.3025 \times 10^{10})^2 = 5.3327 \times 10^{21}\text{ m}^{-2}
\]
\[
k^2 \langle x^2 \rangle = (5.3327 \times 10^{21}\text{ m}^{-2})(4.8 \times 10^{-23}\text{ m}^2) = 0.2560
\]
\[
f = e^{-k^2 \langle x^2 \rangle} = e^{-0.2560} = 0.774 = 77.4\%
\]
<p>In solid iron at room temperature, over \(77\%\) of all \(\gamma\)-rays are emitted completely recoil-free, producing an intense Mössbauer absorption line.</p>"""
            },
            {
                "id": "u10-prob6",
                "number": 6,
                "title": "Mössbauer Isomer Shift and Quadrupole Splitting of Iron Complexes",
                "difficulty": "Intermediate",
                "statement": r"""A bioinorganic chemist records the \(^{57}\text{Fe}\) Mössbauer spectra of two non-heme iron proteins at \(77\text{ K}\) relative to an \(\alpha\text{-Fe}\) foil standard:
Protein Sample 1: Displays a doublet with centroid (isomer shift) \(\delta_1 = +0.38\text{ mm/s}\) and quadrupole splitting \(\Delta E_{Q1} = 0.65\text{ mm/s}\).
Protein Sample 2: Displays a doublet with centroid \(\delta_2 = +1.15\text{ mm/s}\) and quadrupole splitting \(\Delta E_{Q2} = 2.80\text{ mm/s}\).
(a) Convert the isomer shift difference \(\Delta\delta = \delta_2 - \delta_1\) into an equivalent energy difference in \(\text{eV}\).
(b) Assign the oxidation state and spin state of the iron active site in Sample 1 and Sample 2.
(c) Explain why Sample 2 exhibits such a massive quadrupole splitting (\(2.80\text{ mm/s}\)) compared to Sample 1.""",
                "solution": r"""<p><strong>Step (a): Energy conversion of Doppler velocity</strong></p>
\[
\Delta v = 1.15 - 0.38 = 0.77\text{ mm/s} = 0.77 \times 10^{-3}\text{ m/s}
\]
\[
\Delta E = E_\gamma \frac{\Delta v}{c} = 14410\text{ eV} \times \frac{0.77 \times 10^{-3}\text{ m/s}}{2.99792 \times 10^8\text{ m/s}} = 14410 \times (2.568 \times 10^{-12}) = 3.70 \times 10^{-8}\text{ eV}
\]
<p><strong>Step (b): Oxidation and spin state assignments</strong></p>
<ul>
  <li><strong>Sample 1 (\(\delta = +0.38\text{ mm/s}, \Delta E_Q = 0.65\text{ mm/s}\)):</strong>
    The isomer shift of \(+0.38\text{ mm/s}\) is characteristic of <strong>high-spin \(\text{Fe}^{3+}\) (\(d^5, S=5/2\))</strong>. The five d-electrons spherically distribute across all five d-orbitals (\(t_{2g}^3 e_g^2\)), producing low valence EFG and small quadrupole splitting.
  </li>
  <li><strong>Sample 2 (\(\delta = +1.15\text{ mm/s}, \Delta E_Q = 2.80\text{ mm/s}\)):</strong>
    The large isomer shift of \(+1.15\text{ mm/s}\) indicates high d-electron shielding (lower s-density), diagnostic of <strong>high-spin \(\text{Fe}^{2+}\) (\(d^6, S=2\))</strong>.
  </li>
</ul>
<p><strong>Step (c): Physical explanation of large quadrupole splitting in Fe(II)</strong></p>
<p>In high-spin \(\text{Fe}^{3+}\) (\(d^5\)), the half-filled shell has spherical orbital symmetry (\(^6S\) state); the electric field gradient arises solely from distant ligand charges (lattice EFG). In contrast, high-spin \(\text{Fe}^{2+}\) (\(d^6\)) has an extra electron in one of the \(t_{2g}\) orbitals (e.g., \(d_{xy}^2 d_{xz}^1 d_{yz}^1\)). This creates an asymmetric valence electron distribution close to the nucleus, generating a massive valence electric field gradient that produces \(\Delta E_Q \sim 2.8\text{ mm/s}\).</p>"""
            },
            {
                "id": "u10-prob7",
                "number": 7,
                "title": "Magnetic Hyperfine Field Determination from Mössbauer Sextet",
                "difficulty": "Advanced",
                "statement": r"""At room temperature (\(298\text{ K}\)), metallic iron (\(\alpha\text{-Fe}\)) is ferromagnetic and produces a symmetric Mössbauer sextet centered at \(\delta = 0.00\text{ mm/s}\).
The outermost lines (lines 1 and 6, corresponding to \(M_I = -1/2 \to -3/2\) and \(+1/2 \to +3/2\)) appear at Doppler velocities \(v_1 = -5.312\text{ mm/s}\) and \(v_6 = +5.312\text{ mm/s}\), giving an overall splitting of \(\Delta v_{16} = 10.624\text{ mm/s}\).
For \(^{57}\text{Fe}\):
Ground-state nuclear magnetic moment: \(\mu_g = +0.09062 \mu_N\) (\(I_g = 1/2\)).
Excited-state nuclear magnetic moment: \(\mu_e = -0.1549 \mu_N\) (\(I_e = 3/2\)).
Nuclear magneton: \(\mu_N = 5.05078 \times 10^{-27}\text{ J/T}\).
\(\gamma\)-ray energy: \(E_\gamma = 14.41\text{ keV}\).
(a) Express \(\Delta v_{16}\) in terms of \(\mu_g\), \(\mu_e\), and internal magnetic field \(B_{\text{int}}\).
(b) Calculate the magnitude of the internal magnetic field \(B_{\text{int}}\) in metallic iron in Tesla.""",
                "solution": r"""<p><strong>Step (a): Sextet outer splitting formula</strong></p>
<p>The Zeeman energy shifts for the nuclear levels are:</p>
\[
E_g(M_g) = -\frac{\mu_g}{I_g} B_{\text{int}} M_g = -2 \mu_g B_{\text{int}} M_g
\]
\[
E_e(M_e) = -\frac{\mu_e}{I_e} B_{\text{int}} M_e = -\frac{2}{3} \mu_e B_{\text{int}} M_e
\]
<p>The transition energy between \(M_g = -1/2\) and \(M_e = -3/2\) (Line 6) is:</p>
\[
\Delta E_6 = E_\gamma + E_e(-3/2) - E_g(-1/2) = E_\gamma + \mu_e B_{\text{int}} - \mu_g B_{\text{int}}
\]
<p>The transition energy between \(M_g = +1/2\) and \(M_e = +3/2\) (Line 1) is:</p>
\[
\Delta E_1 = E_\gamma + E_e(+3/2) - E_g(+1/2) = E_\gamma - \mu_e B_{\text{int}} + \mu_g B_{\text{int}}
\]
<p>The total energy splitting between outer lines 1 and 6 is:</p>
\[
\Delta E_{16} = \Delta E_6 - \Delta E_1 = 2 (|\mu_e| + \mu_g) B_{\text{int}}
\]
<p>Equating this to Doppler velocity energy: \(\Delta E_{16} = E_\gamma \frac{\Delta v_{16}}{c}\):</p>
\[
2 (|\mu_e| + \mu_g) B_{\text{int}} = E_\gamma \frac{\Delta v_{16}}{c}
\]
<p><strong>Step (b): Internal magnetic field calculation</strong></p>
\[
\Delta E_{16} = 14410\text{ eV} \times \frac{10.624 \times 10^{-3}\text{ m/s}}{2.99792 \times 10^8\text{ m/s}} = 14410 \times (3.5438 \times 10^{-11})\text{ eV} = 5.1066 \times 10^{-7}\text{ eV}
\]
<p>Convert to Joules:</p>
\[
\Delta E_{16} = (5.1066 \times 10^{-7}\text{ eV})(1.60218 \times 10^{-19}\text{ J/eV}) = 8.1817 \times 10^{-26}\text{ J}
\]
<p>Nuclear magnetic moments in SI units:</p>
\[
|\mu_e| + \mu_g = (0.1549 + 0.09062) \mu_N = 0.24552 \mu_N
\]
\[
|\mu_e| + \mu_g = 0.24552 \times (5.05078 \times 10^{-27}\text{ J/T}) = 1.24007 \times 10^{-27}\text{ J/T}
\]
<p>Now calculate \(B_{\text{int}}\):</p>
\[
B_{\text{int}} = \frac{\Delta E_{16}}{2 (|\mu_e| + \mu_g)} = \frac{8.1817 \times 10^{-26}\text{ J}}{2(1.24007 \times 10^{-27}\text{ J/T})} = \frac{8.1817 \times 10^{-26}}{2.48014 \times 10^{-27}} = 32.99\text{ Tesla} \approx 33.0\text{ Tesla}
\]
<p>The internal magnetic hyperfine field experienced by \(^{57}\text{Fe}\) nuclei in ferromagnetic iron is an astounding **33.0 Tesla** (330,000 Gauss), generated primarily by Fermi contact interaction with polarized core s-electrons.</p>"""
            }
        ]
    }
    units.append(u10)

    return units

if __name__ == "__main__":
    units = get_units_7_8_9_10()
    print(f"Successfully generated Units 7-10. Total units: {len(units)}")
    for u in units:
        print(f"Unit {u['number']}: {len(u['sections'])} sections, {len(u['problems'])} problems.")
