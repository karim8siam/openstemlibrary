#!/usr/bin/env python3
"""
expand_spectroscopy_problem8.py
Provides Problem 8 for all 10 units of Chemical Spectroscopy (completing 80 problems).
"""

def get_problem8_dict():
    p8 = {}

    # Unit 1: Problem 1.8
    p8[1] = {
        "id": "u1-prob8",
        "number": 8,
        "title": "Apodization Function Side-Lobe Suppression and Spectral Resolution Trade-Off",
        "difficulty": "Advanced",
        "statement": r"""In a Fourier transform infrared spectrometer with maximum mirror retardation \(\delta_{\max} = 1.00\text{ cm}\):
(a) For un-apodized (boxcar) truncation, the instrumental line shape is \(\text{ILS}(\tilde{\nu}) = 2\delta_{\max}\text{sinc}(2\pi \tilde{\nu}\delta_{\max})\).
Calculate the nominal FWHM resolution \(\Delta\tilde{\nu}_{\text{box}}\) and the relative amplitude of the first negative side-lobe (\(\%\)).
(b) When triangular apodization is applied, \(\text{ILS}(\tilde{\nu}) = \delta_{\max}\text{sinc}^2(\pi \tilde{\nu}\delta_{\max})\).
Calculate the new FWHM resolution \(\Delta\tilde{\nu}_{\text{tri}}\) and the relative amplitude of the first side-lobe.
(c) Discuss the fundamental spectroscopic trade-off between spectral resolution and side-lobe suppression.""",
        "solution": r"""<p><strong>Step (a): Boxcar truncation parameters</strong></p>
<p>For a boxcar truncation window of length \(2\delta_{\max}\):</p>
\[
\text{ILS}_{\text{box}}(\tilde{\nu}) \propto \frac{\sin(2\pi \tilde{\nu} \delta_{\max})}{2\pi \tilde{\nu} \delta_{\max}}
\]
<p>The Full Width at Half Maximum (FWHM) occurs where \(\text{sinc}(x) = 0.5\), which gives \(x \approx 1.8954\) radians:</p>
\[
2\pi (\Delta\tilde{\nu}_{\text{box}} / 2) \delta_{\max} = 1.8954 \implies \Delta\tilde{\nu}_{\text{box}} = \frac{1.8954}{\pi \delta_{\max}} = \frac{0.6033}{\delta_{\max}}
\]
\[
\Delta\tilde{\nu}_{\text{box}} = \frac{0.6033}{1.00\text{ cm}} = 0.603\text{ cm}^{-1}
\]
<p>The first minimum occurs at \(2\pi \tilde{\nu} \delta_{\max} = \pi \implies \tilde{\nu} = \frac{1}{2\delta_{\max}}\). The first negative side-lobe peak occurs at \(2\pi \tilde{\nu} \delta_{\max} \approx 4.4934\) radians:</p>
\[
\text{Amplitude} = \frac{\sin(4.4934)}{4.4934} = \frac{-0.9761}{4.4934} = -0.2172 = -21.72\%
\]
<p>The un-apodized spectrum displays prominent side-lobes with \(21.7\%\) negative amplitude!</p>
<p><strong>Step (b): Triangular apodization parameters</strong></p>
<p>For triangular apodization:</p>
\[
\text{ILS}_{\text{tri}}(\tilde{\nu}) \propto \left[ \frac{\sin(\pi \tilde{\nu} \delta_{\max})}{\pi \tilde{\nu} \delta_{\max}} \right]^2
\]
<p>The FWHM occurs where \(\text{sinc}^2(y) = 0.5 \implies \text{sinc}(y) = \frac{1}{\sqrt{2}} \approx 0.7071\), giving \(y \approx 1.3916\):</p>
\[
\pi (\Delta\tilde{\nu}_{\text{tri}} / 2) \delta_{\max} = 1.3916 \implies \Delta\tilde{\nu}_{\text{tri}} = \frac{2 \times 1.3916}{\pi \delta_{\max}} = \frac{0.8859}{\delta_{\max}} = 0.886\text{ cm}^{-1}
\]
<p>The first secondary maximum occurs at \(y \approx 4.4934\):</p>
\[
\text{Amplitude} = (-0.2172)^2 = +0.0472 = +4.72\%
\]
<p><strong>Step (c): Spectroscopic trade-off</strong></p>
<p>Triangular apodization dramatically suppresses the side-lobes from \(-21.7\%\) down to \(+4.7\%\), eliminating false ringing artifacts. However, this suppression broadens the spectral linewidth from \(0.603\text{ cm}^{-1}\) to \(0.886\text{ cm}^{-1}\) (a resolution loss of \(\approx 47\%\)). Choosing an apodization function represents a deliberate optimization between artifact suppression and spectral resolving power.</p>"""
    }

    # Unit 2: Problem 2.8
    p8[2] = {
        "id": "u2-prob8",
        "number": 8,
        "title": "Debye Rotational Correlation Time and Optimal Microwave Loss Frequency",
        "difficulty": "Intermediate",
        "statement": r"""Liquid water at \(T = 298\text{ K}\) has a viscosity of \(\eta = 0.890\text{ mPa}\cdot\text{s}\) (\(8.90 \times 10^{-4}\text{ kg}/(\text{m}\cdot\text{s})\)) and an effective hydrodynamic radius of \(a = 1.45\text{ \AA}\).
(a) Using the Stokes-Einstein-Debye relation:
\[
\tau_D = \frac{4\pi \eta a^3}{k_B T}
\]
calculate the rotational correlation time \(\tau_D\) of water molecules in picoseconds.
(b) Calculate the critical frequency \(f_{\max} = \frac{1}{2\pi \tau_D}\) (in GHz) at which the dielectric loss factor \(\varepsilon''\) reaches its theoretical maximum.
(c) Explain why domestic microwave ovens are engineered to operate at \(2.45\text{ GHz}\) rather than at \(f_{\max}\).""",
        "solution": r"""<p><strong>Step (a): Calculation of Debye correlation time tau_D</strong></p>
<p>Parameters in SI units:</p>
<ul>
  <li>\(\eta = 8.90 \times 10^{-4}\text{ kg}/(\text{m}\cdot\text{s})\)</li>
  <li>\(a = 1.45 \times 10^{-10}\text{ m} \implies a^3 = 3.0486 \times 10^{-30}\text{ m}^3\)</li>
  <li>\(k_B T = (1.38065 \times 10^{-23}\text{ J/K})(298\text{ K}) = 4.1143 \times 10^{-21}\text{ J}\)</li>
</ul>
\[
\tau_D = \frac{4\pi (8.90 \times 10^{-4})(3.0486 \times 10^{-30})}{4.1143 \times 10^{-21}} = \frac{3.410 \times 10^{-32}}{4.1143 \times 10^{-21}} = 8.288 \times 10^{-12}\text{ s} \approx 8.29\text{ ps}
\]
<p><strong>Step (b): Maximum dielectric loss frequency</strong></p>
\[
f_{\max} = \frac{1}{2\pi \tau_D} = \frac{1}{2\pi (8.288 \times 10^{-12}\text{ s})} = \frac{1}{5.2076 \times 10^{-11}} = 1.920 \times 10^{10}\text{ Hz} = 19.2\text{ GHz}
\]
<p><strong>Step (c): Why 2.45 GHz is selected</strong></p>
<p>If microwave ovens operated at \(f_{\max} \approx 19.2\text{ GHz}\), the dielectric loss factor \(\varepsilon''\) would be extremely high. The electromagnetic radiation would be absorbed completely in the first millimeter of food (shallow penetration depth \(d_p < 1\text{ mm}\)), charring the surface while leaving the interior cold and raw.</p>
<p>Operating at \(2.45\text{ GHz}\) places the system on the lower slope of the Debye loss curve, where \(\varepsilon'' \approx 12\). This provides a penetration depth of \(d_p \approx 1.5 - 3\text{ cm}\), allowing microwaves to penetrate deeply into the bulk food matrix for rapid, uniform volumetric heating.</p>"""
    }

    # Unit 3: Problem 3.8
    p8[3] = {
        "id": "u3-prob8",
        "number": 8,
        "title": "Carbonyl Stretching Frequency Modulations: Ring Strain vs Conjugation",
        "difficulty": "Intermediate",
        "statement": r"""The fundamental carbonyl stretching wavenumber \(\tilde{\nu}_{\text{C=O}}\) in cyclic ketones varies systematically with ring size:
1. Cyclohexanone (6-membered): \(\tilde{\nu} = 1715\text{ cm}^{-1}\)
2. Cyclopentanone (5-membered): \(\tilde{\nu} = 1745\text{ cm}^{-1}\)
3. Cyclobutanone (4-membered): \(\tilde{\nu} = 1780\text{ cm}^{-1}\)
4. Cyclopropenone (3-membered): \(\tilde{\nu} = 1850\text{ cm}^{-1}\)
In contrast, \(\alpha,\beta\)-unsaturated cyclohex-2-en-1-one absorbs at \(\tilde{\nu} = 1685\text{ cm}^{-1}\).
(a) Explain why decreasing ring size increases the \(\text{C=O}\) force constant and stretching wavenumber using carbon hybridization arguments.
(b) Explain why conjugation with an adjacent \(\text{C=C}\) double bond lowers \(\tilde{\nu}_{\text{C=O}}\) to \(1685\text{ cm}^{-1}\).
(c) Predict the approximate carbonyl stretching frequency of cyclobut-2-en-1-one.""",
        "solution": r"""<p><strong>Step (a): Ring strain and hybridization effect</strong></p>
<p>As the ring size decreases from 6 to 3, the internal \(\text{C-C-C}\) bond angle at the carbonyl carbon is constrained to smaller values (\(120^\circ \to 108^\circ \to 90^\circ \to 60^\circ\)).</p>
<p>According to <strong>Coulson's theorem</strong> (\(1 + \lambda_i \lambda_j \cos\theta_{ij} = 0\)), decreasing the bond angle between the ring \(\text{C-C}\) bonds forces them to divert more p-character into the ring (\(\lambda^2 > 3\)).</p>
<p>To conserve total s-character (\(\sum f_s = 1\)), the exocyclic \(\sigma\)-bond to oxygen is forced to accept higher s-character (approaching \(sp\) hybridization). Higher s-character shortens the \(\text{C=O}\) \(\sigma\)-bond, increases the bond force constant \(k\), and raises the vibrational frequency: \(\tilde{\nu} \propto \sqrt{k/\mu}\), shifting \(\tilde{\nu}_{\text{C=O}}\) progressively from \(1715\text{ cm}^{-1}\) to \(1850\text{ cm}^{-1}\).</p>
<p><strong>Step (b): Conjugation effect</strong></p>
<p>Conjugation with an adjacent double bond allows resonance delocalization:</p>
\[
>\text{C=C-C=O} \longleftrightarrow >\text{C}^+-\text{C=C-O}^-
\]
<p>The dipolar resonance contributor introduces single-bond character into the carbonyl group, reducing the \(\pi\)-bond order from \(2.0\) to \(\approx 1.85\). This lowers the force constant \(k\), shifting the stretching band downfield by \(\sim 30 - 40\text{ cm}^{-1}\) to \(1685\text{ cm}^{-1}\).</p>
<p><strong>Step (c): Prediction for cyclobut-2-en-1-one</strong></p>
<p>In cyclobut-2-en-1-one, both effects operate simultaneously:</p>
<ul>
  <li>4-membered ring strain: \(+65\text{ cm}^{-1}\) relative to acyclic ketone (\(1715 \to 1780\text{ cm}^{-1}\))</li>
  <li>\(\alpha,\beta\)-conjugation: \(-30\text{ cm}^{-1}\)</li>
</ul>
\[
\tilde{\nu}_{\text{predicted}} \approx 1780 - 30 = 1750\text{ cm}^{-1}
\]
<p>Experimental measurement gives \(1752\text{ cm}^{-1}\), verifying the additive predictive power of physical organic spectroscopy.</p>"""
    }

    # Unit 4: Problem 4.8
    p8[4] = {
        "id": "u4-prob8",
        "number": 8,
        "title": "Confocal Raman Lateral and Axial Resolution under High-NA Oil Immersion",
        "difficulty": "Advanced",
        "statement": r"""A confocal Raman microscope operates with laser excitation wavelength \(\lambda = 532.0\text{ nm}\) and a \(100\times\) oil-immersion objective lens with numerical aperture \(\text{NA} = 1.40\) (immersion oil refractive index \(n = 1.518\)).
(a) Calculate the diffraction-limited lateral spatial resolution \(\Delta r_{\text{lateral}}\) according to the Abbe-Rayleigh criterion:
\[
\Delta r_{\text{lateral}} = \frac{0.61 \lambda}{\text{NA}}
\]
(b) Calculate the theoretical axial depth resolution (optical sectioning thickness) \(\Delta z_{\text{axial}}\):
\[
\Delta z_{\text{axial}} = \frac{1.4 n \lambda}{\text{NA}^2}
\]
(c) Calculate the confocal focal sampling volume \(V_{\text{voxel}} \approx \frac{4}{3}\pi \left(\frac{\Delta r}{2}\right)^2 \left(\frac{\Delta z}{2}\right)\) in femtoliters (\(\text{fL} = 10^{-15}\text{ L}\)).""",
        "solution": r"""<p><strong>Step (a): Lateral resolution</strong></p>
\[
\Delta r_{\text{lateral}} = \frac{0.61 (532.0\text{ nm})}{1.40} = \frac{324.52}{1.40} = 231.8\text{ nm} \approx 0.232\ \mu\text{m}
\]
<p><strong>Step (b): Axial resolution</strong></p>
\[
\Delta z_{\text{axial}} = \frac{1.4 n \lambda}{\text{NA}^2} = \frac{1.4 (1.518)(532.0\text{ nm})}{(1.40)^2} = \frac{1130.6}{1.96} = 576.8\text{ nm} \approx 0.577\ \mu\text{m}
\]
<p><strong>Step (c): Confocal sampling volume (voxel)</strong></p>
<p>The semi-axes of the focal ellipsoid are \(r_x = r_y = \Delta r / 2 = 1.159 \times 10^{-5}\text{ cm}\) and \(r_z = \Delta z / 2 = 2.884 \times 10^{-5}\text{ cm}\):</p>
\[
V_{\text{voxel}} = \frac{4}{3}\pi r_x^2 r_z = \frac{4}{3}\pi (1.159 \times 10^{-5}\text{ cm})^2 (2.884 \times 10^{-5}\text{ cm})
\]
\[
V_{\text{voxel}} = \frac{4}{3}\pi (1.343 \times 10^{-10})(2.884 \times 10^{-5}) = 1.622 \times 10^{-14}\text{ cm}^3
\]
<p>Since \(1\text{ cm}^3 = 1\text{ mL} = 10^{-3}\text{ L} = 10^{12}\text{ fL}\):</p>
\[
V_{\text{voxel}} = (1.622 \times 10^{-14})(10^{12}\text{ fL}) = 0.0162\text{ fL} = 16.2\text{ attoliters}
\]
<p>Confocal Raman spectroscopy samples a tiny volume of only 16 attoliters, enabling chemical depth-profiling of single living cells and microscopic mineral inclusions.</p>"""
    }

    # Unit 5: Problem 5.8
    p8[5] = {
        "id": "u5-prob8",
        "number": 8,
        "title": "Trace Arsenic Quantification by ICP-OES Standard Addition Method",
        "difficulty": "Intermediate",
        "statement": r"""To eliminate severe matrix enhancement effects in industrial wastewater analysis, arsenic (\(\text{As}\)) is quantified by ICP-OES at \(\lambda = 193.696\text{ nm}\) using the method of standard additions.
Equal \(20.0\text{ mL}\) aliquots of the wastewater sample are spiked with varying volumes of an arsenic standard solution (\(50.0\text{ mg/L}\)) and diluted to \(50.0\text{ mL}\):
Flask 0 (Unspiked): \(0.00\text{ mL}\) standard added \(\implies\) Emission \(I_0 = 1250\text{ counts}\)
Flask 1: \(0.50\text{ mL}\) standard added (\(0.50\text{ mg/L}\) added) \(\implies\) Emission \(I_1 = 2150\text{ counts}\)
Flask 2: \(1.00\text{ mL}\) standard added (\(1.00\text{ mg/L}\) added) \(\implies\) Emission \(I_2 = 3050\text{ counts}\)
Flask 3: \(2.00\text{ mL}\) standard added (\(2.00\text{ mg/L}\) added) \(\implies\) Emission \(I_3 = 4850\text{ counts}\)
(a) Determine the linear regression slope \(m\) and intercept \(b\) of emission versus added concentration \(C_{\text{add}}\).
(b) Calculate the concentration of arsenic in the diluted measurement solution.
(c) Calculate the concentration of arsenic in the original undiluted wastewater sample in \(\text{mg/L}\) (\(\text{ppm}\)).""",
                "solution": r"""<p><strong>Step (a): Linear regression analysis</strong></p>
<p>The standard addition data pairs \((C_{\text{add}}, I)\):</p>
<ul>
  <li>\((0.00, 1250)\)</li>
  <li>\((0.50, 2150)\)</li>
  <li>\((1.00, 3050)\)</li>
  <li>\((2.00, 4850)\)</li>
</ul>
<p>The slope is strictly:</p>
\[
m = \frac{\Delta I}{\Delta C} = \frac{2150 - 1250}{0.50} = \frac{900}{0.50} = 1800\text{ counts}/(\text{mg/L})
\]
\[
b = I_0 = 1250\text{ counts}
\]
<p><strong>Step (b): Diluted measurement concentration</strong></p>
<p>At the x-intercept of the standard additions line (\(I = 0\)):</p>
\[
0 = m C_x + b \implies C_{\text{diluted}} = \frac{b}{m} = \frac{1250\text{ counts}}{1800\text{ counts}/(\text{mg/L})} = 0.6944\text{ mg/L}
\]
<p><strong>Step (c): Original wastewater concentration</strong></p>
<p>Account for the dilution factor (\(20.0\text{ mL} \to 50.0\text{ mL}\)):</p>
\[
\text{Dilution Factor} = \frac{50.0\text{ mL}}{20.0\text{ mL}} = 2.50
\]
\[
C_{\text{original}} = C_{\text{diluted}} \times 2.50 = 0.6944\text{ mg/L} \times 2.50 = 1.736\text{ mg/L} \approx 1.74\text{ ppm}
\]
<p>The arsenic concentration in the wastewater is \(1.74\text{ mg/L}\).</p>"""
    }

    # Unit 6: Problem 6.8
    p8[6] = {
        "id": "u6-prob8",
        "number": 6,
        "title": "Extraction of 10Dq and Racah B from Tanabe-Sugano Diagram for Cr(III)",
        "difficulty": "Advanced",
        "statement": r"""The electronic absorption spectrum of the octahedral complex \([\text{Cr(NH}_3)_6]^{3+}\) (\(d^3\) electron configuration, ground state \(^4A_{2g}\)) exhibits two spin-allowed \(d\text{-}d\) absorption bands:
Band 1: \(\tilde{\nu}_1 = 21550\text{ cm}^{-1}\) (assigned to \(^4T_{2g} \leftarrow {}^4A_{2g}\))
Band 2: \(\tilde{\nu}_2 = 28500\text{ cm}^{-1}\) (assigned to \(^4T_{1g}(F) \leftarrow {}^4A_{2g}\))
(a) Explain why the first transition directly gives the crystal field splitting parameter \(\Delta_o = 10Dq\).
(b) In ligand field theory for \(d^3\), the energy of the second transition is given by:
\[
\tilde{\nu}_2 = \frac{1}{2} (15B + 3\Delta_o) - \frac{1}{2}\sqrt{(15B - \Delta_o)^2 + 48 B \Delta_o}
\]
Alternatively, using the Tanabe-Sugano approximation: \(\tilde{\nu}_2 - \tilde{\nu}_1 = \frac{9B \Delta_o}{\Delta_o + 9B}\) or the direct secular relation:
\[
B = \frac{2\tilde{\nu}_1^2 + \tilde{\nu}_2^2 - 3\tilde{\nu}_1\tilde{\nu}_2}{15\tilde{\nu}_2 - 27\tilde{\nu}_1}
\]
Calculate the Racah parameter \(B\) for \([\text{Cr(NH}_3)_6]^{3+}\).
(c) Given the free gaseous ion Racah parameter \(B_0 = 918\text{ cm}^{-1}\) for \(\text{Cr}^{3+}\), calculate the nephelauxetic parameter \(\beta = B / B_0\) and interpret its chemical meaning.""",
                "solution": r"""<p><strong>Step (a): Direct assignment of Delta_o</strong></p>
<p>For a \(d^3\) ion in an octahedral field, the \(t_{2g}^3\) ground state is \(^4A_{2g}\). The lowest excited state \(t_{2g}^2 e_g^1\) with identical spin multiplicity is \(^4T_{2g}\).</p>
<p>Because the interelectronic repulsion energy for \(^4T_{2g}\) and \(^4A_{2g}\) is identical (both have repulsion energy \(3A - 15B\)), the energy difference is strictly independent of Racah parameters:</p>
\[
E(^4T_{2g}) - E(^4A_{2g}) = 10Dq = \Delta_o
\]
\[
\Delta_o = 21550\text{ cm}^{-1}
\]
<p><strong>Step (b): Calculation of Racah parameter B</strong></p>
<p>Using the secular determinant expression for \(d^3\):</p>
\[
B = \frac{2\tilde{\nu}_1^2 + \tilde{\nu}_2^2 - 3\tilde{\nu}_1\tilde{\nu}_2}{15\tilde{\nu}_2 - 27\tilde{\nu}_1}
\]
<p>Evaluate numerator:</p>
<ul>
  <li>\(2\tilde{\nu}_1^2 = 2(21550)^2 = 2(4.644025 \times 10^8) = 9.28805 \times 10^8\)</li>
  <li>\(\tilde{\nu}_2^2 = (28500)^2 = 8.12250 \times 10^8\)</li>
  <li>\(3\tilde{\nu}_1\tilde{\nu}_2 = 3(21550)(28500) = 3(6.14175 \times 10^8) = 1.842525 \times 10^9\)</li>
  <li>Numerator \(= 9.28805 \times 10^8 + 8.12250 \times 10^8 - 18.42525 \times 10^8 = -1.0147 \times 10^8\)</li>
</ul>
<p>Evaluate denominator:</p>
<ul>
  <li>\(15\tilde{\nu}_2 = 15(28500) = 427500\)</li>
  <li>\(27\tilde{\nu}_1 = 27(21550) = 581850\)</li>
  <li>Denominator \(= 427500 - 581850 = -154350\)</li>
</ul>
\[
B = \frac{-1.0147 \times 10^8}{-154350} = 657.4\text{ cm}^{-1} \approx 657\text{ cm}^{-1}
\]
<p><strong>Step (c): Nephelauxetic parameter beta</strong></p>
\[
\beta = \frac{B}{B_0} = \frac{657.4\text{ cm}^{-1}}{918.0\text{ cm}^{-1}} = 0.716 = 71.6\%
\]
<p>The parameter \(\beta = 0.72 < 1.0\) reflects the <strong>nephelauxetic effect</strong> (electron cloud expansion). Overlap of metal \(d\)-orbitals with ammonia ligand lone pairs partially delocalizes the electrons, reducing effective nuclear charge and interelectronic repulsion by \(\approx 28\%\), direct spectroscopic proof of covalent metal-ligand bonding.</p>"""
    }

    # Unit 7: Problem 7.8
    p8[7] = {
        "id": "u7-prob8",
        "number": 8,
        "title": "Biexponential Fluorescence Lifetime Deconvolution in TCSPC",
        "difficulty": "Intermediate",
        "statement": r"""A fluorescent sensor exhibits biexponential decay in Time-Correlated Single Photon Counting (TCSPC) due to coexistence of open and closed conformations in equilibrium:
\[
I(t) = a_1 e^{-t / \tau_1} + a_2 e^{-t / \tau_2}
\]
Deconvolution fitting of the decay histogram yields:
Pre-exponential amplitudes: \(a_1 = 3500\text{ counts}\), \(a_2 = 1500\text{ counts}\).
Lifetimes: \(\tau_1 = 1.20\text{ ns}\), \(\tau_2 = 4.80\text{ ns}\).
(a) Calculate the amplitude-weighted (intensity-averaged) mean fluorescence lifetime:
\[
\langle \tau \rangle_{\text{amp}} = \frac{a_1 \tau_1 + a_2 \tau_2}{a_1 + a_2}
\]
(b) Calculate the fractional contribution \(f_i\) of each species to the steady-state emission:
\[
f_i = \frac{a_i \tau_i}{\sum a_j \tau_j}
\]
(c) Calculate the intensity-weighted mean lifetime \(\langle \tau \rangle_{\text{int}} = f_1 \tau_1 + f_2 \tau_2\).""",
        "solution": r"""<p><strong>Step (a): Amplitude-weighted lifetime</strong></p>
\[
a_1 + a_2 = 3500 + 1500 = 5000\text{ counts}
\]
\[
a_1 \tau_1 = 3500 \times 1.20\text{ ns} = 4200\text{ counts}\cdot\text{ns}
\]
\[
a_2 \tau_2 = 1500 \times 4.80\text{ ns} = 7200\text{ counts}\cdot\text{ns}
\]
\[
\langle \tau \rangle_{\text{amp}} = \frac{4200 + 7200}{5000} = \frac{11400}{5000} = 2.28\text{ ns}
\]
<p><strong>Step (b): Fractional steady-state contributions</strong></p>
<p>Total steady-state photon emission is proportional to \(\int_0^\infty I(t)dt = a_1 \tau_1 + a_2 \tau_2 = 11400\text{ counts}\cdot\text{ns}\):</p>
\[
f_1 = \frac{a_1 \tau_1}{a_1 \tau_1 + a_2 \tau_2} = \frac{4200}{11400} = 0.3684 = 36.84\%
\]
\[
f_2 = \frac{a_2 \tau_2}{a_1 \tau_1 + a_2 \tau_2} = \frac{7200}{11400} = 0.6316 = 63.16\%
\]
<p>Notice that even though species 1 represents \(70\%\) of the molecules initially excited (\(a_1 / (a_1+a_2) = 0.70\)), species 2 contributes \(63.2\%\) of all emitted steady-state light because its lifetime is 4 times longer!</p>
<p><strong>Step (c): Intensity-weighted mean lifetime</strong></p>
\[
\langle \tau \rangle_{\text{int}} = f_1 \tau_1 + f_2 \tau_2 = (0.3684)(1.20\text{ ns}) + (0.6316)(4.80\text{ ns}) = 0.4421 + 3.0317 = 3.474\text{ ns} \approx 3.47\text{ ns}
\]"""
    }

    # Unit 8: Problem 8.8
    p8[8] = {
        "id": "u8-prob8",
        "number": 8,
        "title": "Enantiomeric Excess Determination of Chiral Amine by Eu(hfc)3",
        "difficulty": "Foundational",
        "statement": r"""A sample of non-racemic 1-phenylethylamine (\(\text{PhCH(CH}_3)\text{NH}_2\)) is treated with the chiral lanthanide shift reagent \(\text{Eu(hfc)}_3\) in \(\text{CDCl}_3\).
In the uncomplexed amine, the methyl doublet appears at \(\delta = 1.38\text{ ppm}\).
Upon adding \(0.15\text{ equivalents}\) of \(\text{Eu(hfc)}_3\), pseudo-contact shifts separate the methyl resonance into two baseline-resolved doublets:
\((R)\)-enantiomer methyl: \(\delta = 2.45\text{ ppm}\), integrated area \(A_R = 184.0\text{ mm}^2\).
\((S)\)-enantiomer methyl: \(\delta = 2.20\text{ ppm}\), integrated area \(A_S = 46.0\text{ mm}^2\).
(a) Calculate the enantiomeric excess (\(\% \text{ ee}\)) of the amine sample.
(b) Determine the mole percent of the \((R)\) and \((S)\) enantiomers in the mixture.
(c) Explain the physical origin of the chemical shift splitting \(\Delta\Delta\delta = 0.25\text{ ppm}\).""",
        "solution": r"""<p><strong>Step (a): Enantiomeric excess (ee) calculation</strong></p>
\[
\% \text{ ee} = \frac{|A_R - A_S|}{A_R + A_S} \times 100\% = \frac{184.0 - 46.0}{184.0 + 46.0} \times 100\% = \frac{138.0}{230.0} \times 100\% = 60.0\%
\]
<p>The sample has an enantiomeric excess of \(60.0\%\) \((R)\).</p>
<p><strong>Step (b): Mole percentages</strong></p>
\[
\text{Mole } \% (R) = \frac{A_R}{A_R + A_S} \times 100\% = \frac{184.0}{230.0} \times 100\% = 80.0\%
\]
\[
\text{Mole } \% (S) = \frac{A_S}{A_R + A_S} \times 100\% = \frac{46.0}{230.0} \times 100\% = 20.0\%
\]
<p>(Checking: \(80.0\% - 20.0\% = 60.0\%\) ee).</p>
<p><strong>Step (c): Origin of diastereomeric chemical shift difference</strong></p>
<p>In an achiral solvent, \((R)\)-amine and \((S)\)-amine are enantiomers, and their protons reside in enantiotopic magnetic environments that yield strictly identical chemical shifts.</p>
<p>When the enantiomerically pure chiral shift reagent \(\text{Eu(hfc)}_3\) coordinates to the amine nitrogen, it forms two distinct complexes: \([(R)\text{-amine} \cdot \text{Eu(hfc)}_3]\) and \([(S)\text{-amine} \cdot \text{Eu(hfc)}_3]\).</p>
<p>These two complexes are <strong>diastereomers</strong>. Because diastereomers have different 3D spatial conformations, the methyl group protons experience different distances \(r\) and angles \(\theta\) relative to the paramagnetic \(\text{Eu}^{3+}\) ion. By Bleaney's equation, this induces unequal pseudo-contact shifts (\(\Delta\Delta\delta = 0.25\text{ ppm}\)), completely resolving the enantiomers.</p>"""
    }

    # Unit 9: Problem 9.8
    p8[9] = {
        "id": "u9-prob8",
        "number": 8,
        "title": "Sequential 3D HNCA / HN(CO)CA Backbone Walking in a Protein",
        "difficulty": "Advanced",
        "statement": r"""In a 3D NMR structural investigation of a \(^{15}\text{N}, ^{13}\text{C}\)-labeled protein, two consecutive residues in a \(\beta\)-strand are analyzed:
At amide strip 1 (\(H^N = 8.42\text{ ppm}\), \(N = 120.5\text{ ppm}\)):
HNCA shows two peaks: \(C^\alpha = 56.4\text{ ppm}\) (strong) and \(C^\alpha = 61.8\text{ ppm}\) (weak).
HN(CO)CA shows a single peak: \(C^\alpha = 61.8\text{ ppm}\).
At amide strip 2 (\(H^N = 9.15\text{ ppm}\), \(N = 124.8\text{ ppm}\)):
HNCA shows two peaks: \(C^\alpha = 61.8\text{ ppm}\) (strong) and \(C^\alpha = 53.2\text{ ppm}\) (weak).
HN(CO)CA shows a single peak: \(C^\alpha = 53.2\text{ ppm}\).
(a) Explain how HNCA and HN(CO)CA distinguish intra-residue \(C^\alpha(i)\) from inter-residue \(C^\alpha(i-1)\).
(b) Determine which residue precedes which: does strip 1 precede strip 2, or does strip 2 precede strip 1?
(c) Given typical \(C^\alpha\) chemical shift statistics: Alanine (\(53.2\text{ ppm}\)), Valine (\(61.8\text{ ppm}\)), Leucine (\(56.4\text{ ppm}\)), deduce the sequential amino acid dipeptide sequence.""",
                "solution": r"""<p><strong>Step (a): Distinction between intra- and inter-residue C_alpha</strong></p>
<ul>
  <li><strong>HNCA:</strong> Transfers magnetization from \(H^N(i) - N(i)\) to both intra-residue \(C^\alpha(i)\) (via \(^1J_{NC\alpha} \approx 11\text{ Hz}\)) and preceding inter-residue \(C^\alpha(i-1)\) (via \(^2J_{NC\alpha} \approx 7\text{ Hz}\)). Both peaks appear, with the intra-residue peak usually stronger.</li>
  <li><strong>HN(CO)CA:</strong> Transfers magnetization through the intervening carbonyl carbon: \(H^N(i) \to N(i) \to C'(i-1) \to C^\alpha(i-1)\). It <em>strictly</em> and exclusively detects the preceding residue \(C^\alpha(i-1)\).</li>
</ul>
<p>Therefore, by comparing the two experiments: the peak appearing in both HNCA and HN(CO)CA is definitively \(C^\alpha(i-1)\); the peak appearing exclusively in HNCA is \(C^\alpha(i)\).</p>
<p><strong>Step (b): Directional sequence connectivity</strong></p>
<ul>
  <li>For Strip 2: \(C^\alpha(i) = 61.8\text{ ppm}\), and preceding \(C^\alpha(i-1) = 53.2\text{ ppm}\).</li>
  <li>For Strip 1: \(C^\alpha(i) = 56.4\text{ ppm}\), and preceding \(C^\alpha(i-1) = 61.8\text{ ppm}\).</li>
</ul>
<p>Notice that the intra-residue \(C^\alpha(i)\) of Strip 2 (\(61.8\text{ ppm}\)) matches the preceding \(C^\alpha(i-1)\) of Strip 1!</p>
<p>This establishes unambiguous sequential connectivity: <strong>Strip 2 precedes Strip 1</strong>.</p>
<p><strong>Step (c): Tripeptide sequence deduction</strong></p>
<ul>
  <li>Preceding residue to Strip 2: \(C^\alpha = 53.2\text{ ppm} \implies\) <strong>Alanine (Ala)</strong></li>
  <li>Strip 2 residue: \(C^\alpha = 61.8\text{ ppm} \implies\) <strong>Valine (Val)</strong></li>
  <li>Strip 1 residue: \(C^\alpha = 56.4\text{ ppm} \implies\) <strong>Leucine (Leu)</strong></li>
</ul>
<p>The tripeptide sequence is conclusively determined as: <strong>\(\text{-Ala-Val-Leu-}\)</strong>.</p>"""
    }

    # Unit 10: Problem 10.8
    p8[10] = {
        "id": "u10-prob8",
        "number": 8,
        "title": "Nanometer Distance Measurement by 4-Pulse DEER Dipolar Modulation",
        "difficulty": "Advanced",
        "statement": r"""A homodimeric membrane protein is site-specifically labeled with two MTSL nitroxide spin labels (\(g_A = g_B = 2.006\)).
In a 4-pulse DEER experiment at \(Q\)-band at \(50\text{ K}\), time-domain dipolar oscillations are observed in the primary spin echo:
The period of the dipolar modulation is measured as \(T_{\text{dip}} = 200.0\text{ ns}\) (\(\nu_{\text{dip}} = 5.00\text{ MHz}\)).
The dipolar coupling frequency for perpendicular orientation (\(\theta = 90^\circ\)) is given by:
\[
\nu_{\text{dip}} = \frac{\mu_0 \mu_B^2 g_A g_B}{4\pi h r^3} = \frac{52.04}{r^3\ (\text{nm}^3)}\ \text{MHz}
\]
(a) Calculate the inter-spin distance \(r\) between the two nitroxide labels in nanometers (\(\text{nm}\)) and Angstroms (\(\text{\AA}\)).
(b) If the protein undergoes a conformational expansion that doubles the distance (\(r' = 2r\)), what will be the new dipolar oscillation frequency \(\nu_{\text{dip}}'\) and period \(T_{\text{dip}}'\)?
(c) State the upper practical distance limit for DEER measurements and explain what physical mechanism imposes this limit.""",
        "solution": r"""<p><strong>Step (a): Inter-spin distance calculation</strong></p>
\[
\nu_{\text{dip}} = \frac{52.04}{r^3} \implies r^3 = \frac{52.04}{\nu_{\text{dip}}\ (\text{MHz})}
\]
\[
r^3 = \frac{52.04}{5.00} = 10.408\text{ nm}^3
\]
\[
r = (10.408)^{1/3} = 2.183\text{ nm} = 21.83\text{ \AA}
\]
<p>The distance between the two nitroxide spin labels is \(2.18\text{ nm}\) (\(21.8\text{ \AA}\)).</p>
<p><strong>Step (b): Effect of distance doubling</strong></p>
<p>Because dipolar coupling scales inversely with the cube of distance (\(\propto r^{-3}\)):</p>
\[
\nu_{\text{dip}}' = \frac{\nu_{\text{dip}}}{2^3} = \frac{5.00\text{ MHz}}{8} = 0.625\text{ MHz}
\]
\[
T_{\text{dip}}' = \frac{1}{\nu_{\text{dip}}'} = \frac{1}{0.625 \times 10^6\text{ s}^{-1}} = 1.60 \times 10^{-6}\text{ s} = 1.60\ \mu\text{s} = 1600\text{ ns}
\]
<p><strong>Step (c): Upper distance limit of DEER</strong></p>
<p>The practical upper distance limit for standard DEER is \(\sim 8 - 10\text{ nm}\) (\(80 - 100\text{ \AA}\)).</p>
<p>This limit is imposed by <strong>phase memory relaxation (\(T_m\))</strong> of the electron spin echo in frozen solution. To observe at least one full cycle of the dipolar oscillation, the dipolar period \(T_{\text{dip}}\) cannot exceed the time window before the electron spin echo decays into baseline noise due to matrix proton nuclear spin diffusion (\(T_m \sim 3 - 5\ \mu\text{s}\)). Perdeuteration of the solvent and protein extends \(T_m\) up to \(15\ \mu\text{s}\), extending the distance limit to \(\sim 12 - 16\text{ nm}\).</p>"""
    }

    return p8

if __name__ == "__main__":
    p8 = get_problem8_dict()
    print(f"Generated Problem 8 for {len(p8)} units.")
    for u_num, prob in p8.items():
        print(f"Unit {u_num}: Problem {prob['number']} - {prob['title']}")
