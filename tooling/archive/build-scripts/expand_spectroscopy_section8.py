#!/usr/bin/env python3
"""
expand_spectroscopy_section8.py
Provides Section 8 for all 10 units of Chemical Spectroscopy (completing 80 sections).
"""

def get_section8_dict():
    s8 = {}

    # Unit 1: Section 1.8
    s8[1] = {
        "id": "u1-sec8",
        "number": "1.8",
        "title": "Fourier Transform Spectrometry: Interferometry & Apodization Functions",
        "content": r"""<p>Modern infrared and far-infrared spectrometers operate almost universally on the <strong>Fourier Transform (FT)</strong> principle using a Michelson interferometer rather than dispersive gratings. The Michelson interferometer divides an incident beam using a beamsplitter into two arms: one terminating on a fixed mirror and the other on a moving mirror translated at constant velocity \(v\).</p>
<h4 class="content-heading">Optical Retardation & The Interferogram</h4>
<p>The optical path difference between the two beams is the <strong>retardation</strong> \(\delta = 2(x_{\text{moving}} - x_{\text{fixed}})\). When the beams recombine at the beamsplitter, constructive and destructive interference modulates the transmitted intensity. For monochromatic radiation of wavenumber \(\tilde{\nu}\), the detector records an oscillating signal:</p>
\[
I(\delta) = S(\tilde{\nu}) [1 + \cos(2\pi \tilde{\nu} \delta)]
\]
<p>For a polychromatic broadband source, the total interferogram \(I(\delta)\) is the integral over all spectral wavenumbers:</p>
\[
I(\delta) = \int_0^\infty S(\tilde{\nu}) \cos(2\pi \tilde{\nu} \delta) d\tilde{\nu}
\]
<p>At zero optical path difference (\(\delta = 0\)), all frequencies interfere constructively, creating an intense central spike known as the <strong>Centerburst</strong>. At large retardation, the waves rapidly dephase, leaving weak oscillations that encode high-resolution spectral details.</p>
<h4 class="content-heading">The Fourier Inversion & Instrumental Line Shape</h4>
<p>The frequency spectrum \(S(\tilde{\nu})\) is reconstructed via the cosine Fourier transform:</p>
\[
S(\tilde{\nu}) = \int_{-\infty}^{\infty} I(\delta) \cos(2\pi \tilde{\nu} \delta) d\delta
\]
<p>In practice, the mirror cannot travel to infinity; the interferogram is truncated at maximum retardation \(\pm \delta_{\max}\). Truncation is mathematically equivalent to multiplying the infinite interferogram by a rectangular boxcar function \(\Pi(\delta)\). In the frequency domain, this convolves the true spectrum with a sinc function instrumental line shape (ILS):</p>
\[
\text{ILS}(\tilde{\nu}) = 2 \delta_{\max} \frac{\sin(2\pi \tilde{\nu} \delta_{\max})}{2\pi \tilde{\nu} \delta_{\max}} = 2 \delta_{\max} \text{sinc}(2\pi \tilde{\nu} \delta_{\max})
\]
<p>The sinc function possesses substantial secondary lobes ('side-lobes') with negative amplitudes of \(-21.7\%\), which create false ringing artifacts near intense absorption bands.</p>
<h4 class="content-heading">Apodization Functions & Phase Correction</h4>
<p>To suppress side-lobes, the interferogram is multiplied by an <strong>apodization function</strong> \(A(\delta)\) (from the Greek <em>apodos</em>, 'removing the foot') that smoothly rolls off to zero at \(\delta_{\max}\):</p>
<ul>
  <li><strong>Triangular Apodization:</strong> \(A(\delta) = 1 - \frac{|\delta|}{\delta_{\max}}\), yielding an \(\text{sinc}^2\) profile with side-lobes reduced to \(< 5\%\), at the cost of a slight broadening of the FWHM.</li>
  <li><strong>Happ-Genzel Apodization:</strong> \(A(\delta) = 0.54 + 0.46 \cos\left(\frac{\pi \delta}{\delta_{\max}}\right)\).</li>
  <li><strong>Blackman-Harris 3-Term:</strong> Optimal side-lobe suppression below \(0.01\%\).</li>
</ul>
<p>Phase errors caused by electronic amplifier delays and beamsplitter dispersion are numerically corrected using the <strong>Mertz</strong> or <strong>Forman</strong> phase-correction algorithms, yielding pristine absorption spectra.</p>"""
    }

    # Unit 2: Section 2.8
    s8[2] = {
        "id": "u2-sec8",
        "number": "2.8",
        "title": "Microwave Instrumentation, Cavity Resonators & Dielectric Loss Mechanics",
        "content": r"""<p>Microwave spectroscopy encompasses the frequency range from \(3\text{ GHz}\) to \(300\text{ GHz}\) (\(0.1 - 10\text{ cm}^{-1}\)). Because coaxial cables suffer unacceptable attenuation at these frequencies, microwave radiation is guided through hollow rectangular metal <strong>waveguides</strong> and resonant cavity structures.</p>
<h4 class="content-heading">Microwave Radiation Sources & Stark Cells</h4>
<ol>
  <li><strong>Solid-State Generators:</strong> Reflex klystrons and backward wave oscillators (BWOs) have been largely superseded by solid-state <strong>Gunn diodes</strong> and phase-locked microwave frequency synthesizers, providing narrow spectral purity (\(\Delta\nu / \nu < 10^{-8}\)).</li>
  <li><strong>The Stark Absorption Cell:</strong> A long rectangular waveguide (typically \(1 - 3\text{ meters}\)) containing a central isolated metal septum plate. A high-voltage square wave (\(0 - 2\text{ kV}\) at \(100\text{ kHz}\)) is applied to modulate the Stark splitting, enabling phase-sensitive lock-in detection that eliminates low-frequency source drift.</li>
  <li><strong>Detectors:</strong> Low-noise point-contact silicon-tungsten crystal diodes, Schottky barrier diodes, or cryogenic bolometers.</li>
</ol>
<h4 class="content-heading">Dielectric Relaxation & Microwave Heating Physics</h4>
<p>In condensed phases (liquids and solids), microwave radiation interacts with molecular dipoles not through discrete rotational transitions (which are quenched by collisions), but via collective <strong>dielectric relaxation</strong>. The response of the medium is characterized by the complex relative permittivity:</p>
\[
\varepsilon^*(\omega) = \varepsilon'(\omega) - i \varepsilon''(\omega)
\]
<p>where \(\varepsilon'\) is the real dielectric constant (characterizing capacitive energy storage) and \(\varepsilon''\) is the imaginary <strong>dielectric loss factor</strong> (characterizing irreversible thermal dissipation).</p>
<h4 class="content-heading">The Debye Relaxation Formulation</h4>
<p>Peter Debye modeled the rotational relaxation of molecular dipoles in a viscous solvent with rotational correlation time \(\tau_D\):</p>
\[
\varepsilon'(\omega) = \varepsilon_\infty + \frac{\varepsilon_s - \varepsilon_\infty}{1 + \omega^2 \tau_D^2}, \quad \varepsilon''(\omega) = \frac{(\varepsilon_s - \varepsilon_\infty) \omega \tau_D}{1 + \omega^2 \tau_D^2}
\]
<p>where \(\varepsilon_s\) is the static (low-frequency) permittivity and \(\varepsilon_\infty\) is the high-frequency optical permittivity (\(\approx n^2\)). Dielectric loss \(\varepsilon''\) reaches its absolute maximum when \(\omega \tau_D = 1\), i.e., when the electric field frequency matches the reciprocal molecular reorientation time:</p>
\[
f_{\max} = \frac{1}{2\pi \tau_D}
\]
<p>For liquid water at \(25^\circ\text{C}\), \(\tau_D \approx 8.3\text{ ps}\), yielding \(f_{\max} \approx 19\text{ GHz}\). Domestic microwave ovens operate at \(2.45\text{ GHz}\) (\(\lambda = 12.24\text{ cm}\)), where \(\varepsilon''\) is moderate, ensuring uniform penetration depth rather than superficial surface heating.</p>"""
    }

    # Unit 3: Section 3.8
    s8[3] = {
        "id": "u3-sec8",
        "number": "3.8",
        "title": "Normal Coordinate Analysis & Characteristic Functional Group Wavenumbers",
        "content": r"""<p>For a non-linear polyatomic molecule with \(N\) atoms, there exist \(3N - 6\) independent vibrational degrees of freedom (\(3N - 5\) for linear molecules). E. Bright Wilson formalized the exact mathematical treatment of polyatomic vibrations using the <strong>Wilson FG matrix method</strong>.</p>
<h4 class="content-heading">The Wilson FG Secular Matrix Equation</h4>
<p>Internal coordinates \(S\) (bond stretches \(\Delta r\), valence angle bends \(\Delta\theta\), out-of-plane wags \(\Delta\gamma\), and torsions \(\Delta\tau\)) are related to Cartesian displacements through kinetic energy matrix \(\mathbf{G}\) and potential energy matrix \(\mathbf{F}\):</p>
\[
2 T = \dot{\mathbf{S}}^T \mathbf{G}^{-1} \dot{\mathbf{S}}, \quad 2 V = \mathbf{S}^T \mathbf{F} \mathbf{S}
\]
<p>The vibrational frequencies \(\lambda_k = 4\pi^2 c^2 \tilde{\nu}_k^2\) are the eigenvalues of the secular determinant:</p>
\[
|\mathbf{F}\mathbf{G} - \lambda \mathbf{E}| = 0
\]
<p>where \(\mathbf{G}\) elements depend purely on atomic masses and equilibrium molecular geometry, while \(\mathbf{F}\) contains the quadratic harmonic force constants (diagonal stretching force constants \(f_r\), bending force constants \(f_\theta\), and off-diagonal stretch-bend interaction constants).</p>
<h4 class="content-heading">Diagnostic Characteristic Infrared Group Frequencies</h4>
<p>Because many chemical functional groups involve high force constants or light atoms (such as \(\text{-H}\)), their vibrational modes are mechanically decoupled from the rest of the molecular framework, producing highly characteristic absorption bands regardless of the surrounding molecular structure:</p>
<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Functional Group</th>
        <th>Vibrational Mode Assignment</th>
        <th>Typical Wavenumber Range (\(\text{cm}^{-1}\))</th>
        <th>Band Intensity & Characteristics</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Free O-H</strong> (Alcohol, Phenol)</td>
        <td>O-H stretch (unassociated)</td>
        <td>\(3600 - 3650\)</td>
        <td>Sharp, medium (dilute gas/solution)</td>
      </tr>
      <tr>
        <td><strong>H-Bonded O-H</strong></td>
        <td>O-H \(\cdots\) O stretch</td>
        <td>\(3200 - 3500\)</td>
        <td>Very broad, intense</td>
      </tr>
      <tr>
        <td><strong>Carboxylic Acid O-H</strong></td>
        <td>O-H stretch (dimerized)</td>
        <td>\(2500 - 3300\)</td>
        <td>Extremely broad, centered \(\sim 3000\), overlaps C-H</td>
      </tr>
      <tr>
        <td><strong>Aliphatic C-H</strong> (\(sp^3\))</td>
        <td>C-H symmetric & asymmetric stretch</td>
        <td>\(2850 - 2960\)</td>
        <td>Strong to medium, always below \(3000\)</td>
      </tr>
      <tr>
        <td><strong>Aromatic / Alkenyl C-H</strong> (\(sp^2\))</td>
        <td>\(=\text{C-H}\) stretch</td>
        <td>\(3010 - 3100\)</td>
        <td>Sharp, medium, always above \(3000\)</td>
      </tr>
      <tr>
        <td><strong>Alkyne C-H</strong> (\(sp\))</td>
        <td>\(\equiv\text{C-H}\) stretch</td>
        <td>\(3280 - 3320\)</td>
        <td>Sharp, intense</td>
      </tr>
      <tr>
        <td><strong>Nitriles & Alkynes</strong></td>
        <td>\(\text{C}\equiv\text{N}\), \(\text{C}\equiv\text{C}\) stretch</td>
        <td>\(2100 - 2260\)</td>
        <td>Sharp, variable (weak for symmetrical alkynes)</td>
      </tr>
      <tr>
        <td><strong>Ketones & Aldehydes</strong></td>
        <td>\(\text{C=O}\) stretch</td>
        <td>\(1715 - 1730\)</td>
        <td>Very intense, diagnostic</td>
      </tr>
      <tr>
        <td><strong>Esters</strong></td>
        <td>\(\text{C=O}\) stretch / C-O stretch</td>
        <td>\(1735 - 1750\) / \(1150 - 1250\)</td>
        <td>Very intense \(\text{C=O}\); strong C-O band</td>
      </tr>
      <tr>
        <td><strong>Amides (Amide I & II)</strong></td>
        <td>\(\text{C=O}\) stretch / N-H bend + C-N stretch</td>
        <td>\(1640 - 1690\) / \(1510 - 1560\)</td>
        <td>Two strong bands (Amide I and Amide II)</td>
      </tr>
      <tr>
        <td><strong>Aromatic Ring</strong></td>
        <td>C=C ring quadrant stretch</td>
        <td>\(1600, 1585, 1500, 1450\)</td>
        <td>Pair of sharp doublets; out-of-plane bends \(700 - 850\)</td>
      </tr>
    </tbody>
  </table>
</div>
<p>The region below \(1500\text{ cm}^{-1}\), designated the <strong>fingerprint region</strong>, contains complex coupled skeletal vibrations unique to each individual molecule.</p>"""
    }

    # Unit 4: Section 4.8
    s8[4] = {
        "id": "u4-sec8",
        "number": "4.8",
        "title": "Modern Raman Instrumentation, Confocal Microscopy & Anti-Stokes Thermometry",
        "content": r"""<p>The renaissance of Raman spectroscopy in modern chemical and materials analysis is driven by five major technological advances: monochromatic laser sources, holographic notch filters, high-throughput imaging spectrographs, low-noise charge-coupled device (CCD) array detectors, and confocal optical microscopes.</p>
<h4 class="content-heading">Rayleigh Rejection Filters</h4>
<p>Because Rayleigh scattering is \(10^6 - 10^8\) times more intense than Raman scattering, detecting faint Raman lines displaced by just a few tens of wavenumbers requires extraordinary stray-light rejection. Modern instruments replace bulky triple monochromators with:</p>
<ul>
  <li><strong>Holographic Notch Filters:</strong> Attenuate the laser wavelength by an optical density \(> 6.0\) (\(10^{-6}\) transmission) with sub-nanometer bandwidth.</li>
  <li><strong>Edge Steep-Cut Filters:</strong> Block radiation at and below the laser line, permitting transmission of Stokes Raman signals down to \(50\text{ cm}^{-1}\).</li>
  <li><strong>Volume Bragg Gratings (VBG):</strong> Ultra-narrowband rejection filters enabling simultaneous acquisition of both Stokes and anti-Stokes lines down to \(5 - 10\text{ cm}^{-1}\) (low-frequency shear and acoustic modes).</li>
</ul>
<h4 class="content-heading">Confocal Raman Microscopy</h4>
<p>Coupling a research-grade Raman spectrograph to an epifluorescence microscope through a spatial confocal pinhole aperture restricts detection strictly to the diffraction-limited focal volume:</p>
\[
\Delta x_{\text{lateral}} \approx \frac{0.61 \lambda}{\text{NA}} \sim 250 - 500\text{ nm}, \quad \Delta z_{\text{axial}} \approx \frac{1.4 n \lambda}{\text{NA}^2} \sim 1 - 2\ \mu\text{m}
\]
<p>where \(\text{NA}\) is objective numerical aperture and \(n\) is refractive index. By raster-scanning the sample with piezo stages, 3D chemical composition maps of living cells, semiconductor microchips, and pharmaceutical tablets are generated non-destructively.</p>
<h4 class="content-heading">Anti-Stokes Non-Contact Thermometry</h4>
<p>Because the ratio of anti-Stokes to Stokes Raman intensity is governed strictly by the Boltzmann distribution \(I_{\text{AS}} / I_S = (\frac{\nu_0 + \nu_v}{\nu_0 - \nu_v})^4 \exp(-hc\tilde{\nu}_v / k_B T)\), measuring this ratio provides a universal, self-calibrated, non-contact optical thermometer. This technique is widely utilized to map local temperatures inside microelectronic integrated circuits, catalytic microreactors, and laser-heated diamond anvil cells up to thousands of Kelvins.</p>"""
    }

    # Unit 5: Section 5.8
    s8[5] = {
        "id": "u5-sec8",
        "number": "5.8",
        "title": "Inductively Coupled Plasma (ICP-OES & ICP-MS) Atomic Emission Spectrometry",
        "content": r"""<p>While Flame Atomic Absorption Spectroscopy (FAAS) measures atomic absorption at temperatures up to \(2800\text{ K}\), <strong>Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES)</strong> harnesses thermal excitation in an atmospheric argon plasma sustained at extreme temperatures of \(6,000 - 10,000\text{ K}\).</p>
<h4 class="content-heading">The Inductively Coupled Argon Plasma Torch</h4>
<p>An ICP torch consists of three concentric quartz tubes surrounded by a water-cooled copper induction coil connected to a radiofrequency (RF) generator (typically \(27.12\text{ MHz}\) or \(40.68\text{ MHz}\) at \(1 - 1.5\text{ kW}\)):</p>
<ol>
  <li>Argon gas flows tangentially through the outer tube (\(12 - 15\text{ L/min}\)).</li>
  <li>A high-voltage Tesla spark seeds initial seed electrons into the argon stream.</li>
  <li>The oscillating RF magnetic field accelerates the free electrons in closed annular paths, inducing intense ohmic resistance heating that sustains a toroidal, self-perpetuating argon plasma.</li>
  <li>Aerosolized sample solution is injected through the central injector tube directly through the center of the plasma donut.</li>
</ol>
<h4 class="content-heading">Plasma Excitation & Spectroscopic Advantages</h4>
<p>At \(8,000\text{ K}\), the plasma provides distinct physical advantages over chemical flames:</p>
<ul>
  <li><strong>Complete Atomization & High Ionization:</strong> Refractory metal oxides and carbides (\(\text{Zr}, \text{W}, \text{B}, \text{Al}, \text{Ti}\)) dissociate completely into free atoms and singly charged ions (\(\text{M}^+\)). Chemical matrix interferences are virtually eliminated.</li>
  <li><strong>Simultaneous Multi-Element Detection:</strong> Thermally excited atoms and ions emit intense discrete optical lines spanning \(165 - 800\text{ nm}\). Modern Echelle grating polychromators with segmented charge-coupled detectors (SCD) record up to 70 elements simultaneously in a single 30-second measurement.</li>
  <li><strong>Linear Dynamic Range:</strong> The thin, optically transparent analytical zone suppresses self-absorption, yielding a linear calibration range exceeding \(5 - 6\) orders of magnitude (\(0.1\text{ ppb} - 100\text{ ppm}\)).</li>
</ul>
<h4 class="content-heading">ICP Mass Spectrometry (ICP-MS)</h4>
<p>Coupling the ICP torch through water-cooled nickel sampling and skimmer cones into a high-vacuum quadrupole or magnetic sector mass spectrometer (ICP-MS) detects elemental ions directly by their mass-to-charge ratio (\(m/z\)). Detection limits drop by an additional three to four orders of magnitude into the parts-per-trillion (\(\text{ppt}\), \(\text{ng/L}\)) and parts-per-quadrillion (\(\text{ppq}\)) regimes with isotopic precision.</p>"""
    }

    # Unit 6: Section 6.8
    s8[6] = {
        "id": "u6-sec8",
        "number": "6.8",
        "title": "Electronic Spectra of Transition Metal Complexes & Tanabe-Sugano Diagrams",
        "content": r"""<p>The colors and optical spectra of transition metal coordination complexes originate from electronic transitions between \(d\)-orbitals split by the surrounding ligand field. In an octahedral ligand field (\(O_h\)), the fivefold degenerate \(d\)-orbitals split into a lower triply degenerate \(t_{2g}\) set (\(d_{xy}, d_{yz}, d_{zx}\)) and an upper doubly degenerate \(e_g\) set (\(d_{x^2-y^2}, d_{z^2}\)), separated by ligand field splitting energy \(\Delta_o = 10 Dq\).</p>
<h4 class="content-heading">Selection Rules for d-d Transitions</h4>
<ol>
  <li><strong>The Laporte Parity Rule:</strong> In centrosymmetric complexes (such as octahedral \(O_h\)), electric dipole transitions between states of the same parity are forbidden (\(g \not\to g\)). Since all \(d\)-orbitals are gerade (\(g\)), \(d\text{-}d\) transitions are Laporte-forbidden. They appear with low molar absorptivities (\(\varepsilon \approx 1 - 50\text{ L}/(\text{mol}\cdot\text{cm})\)) through <strong>vibronic borrowing</strong> (coupling to non-centrosymmetric ungerade vibrational modes that temporarily destroy the inversion center). In tetrahedral complexes (\(T_d\)), which lack an inversion center, \(p\text{-}d\) orbital mixing increases intensity to \(\varepsilon \approx 100 - 2000\).</li>
  <li><strong>The Spin Selection Rule:</strong> Transitions must conserve spin multiplicity (\(\Delta S = 0\)). Spin-forbidden transitions (such as in high-spin \(d^5\) \(\text{Mn}^{2+}\)) are extremely weak (\(\varepsilon < 0.1\)).</li>
  <li><strong>Charge-Transfer (CT) Bands:</strong> Involve electron transfer between ligand and metal (LMCT or MLCT), are fully Laporte- and spin-allowed, and display immense intensities (\(\varepsilon \sim 10^3 - 10^5\)).</li>
</ol>
<h4 class="content-heading">Tanabe-Sugano Correlation Diagrams</h4>
<p>Yukito Tanabe and Satoru Sugano constructed quantitative correlation diagrams plotting the energy of electronic states \(E / B\) against ligand field strength \(\Delta_o / B\) (where \(B\) is the Racah interelectronic repulsion parameter). On Tanabe-Sugano diagrams:</p>
<ul>
  <li>The ground electronic state is always normalized to the horizontal axis (\(E = 0\)).</li>
  <li>For configurations with \(d^4 - d^7\), a vertical dashed line marks the spin crossover where the ground state abruptly transitions from <strong>high-spin</strong> (weak ligand field) to <strong>low-spin</strong> (strong ligand field, e.g., \({}^5E_g \to {}^1A_{1g}\) in \(d^6\)).</li>
  <li>Observed absorption band energies can be fitted directly to determine both the crystal field splitting \(\Delta_o\) and the nephelauxetic (cloud-expanding) reduction of the Racah parameter \(B\), revealing metal-ligand covalency.</li>
</ul>"""
    }

    # Unit 7: Section 7.8
    s8[7] = {
        "id": "u7-sec8",
        "number": "7.8",
        "title": "Time-Resolved Spectroscopy, TCSPC & Femtosecond Transient Absorption",
        "content": r"""<p>While steady-state spectroscopy measures time-averaged emissions and absorptions, ultrafast time-resolved techniques monitor the dynamic real-time evolution of non-equilibrium transient intermediates, excited states, and radical pairs.</p>
<h4 class="content-heading">1. Time-Correlated Single Photon Counting (TCSPC)</h4>
<p>TCSPC is the premier technique for measuring fluorescence lifetimes in the picosecond to microsecond regime (\(20\text{ ps} - 100\ \mu\text{s}\)) with single-photon counting sensitivity:</p>
<ol>
  <li>A pulsed laser (pulse width \(< 50\text{ ps}\)) excites the sample at high repetition rate (\(10 - 80\text{ MHz}\)).</li>
  <li>A reference photodiode generates a START electrical pulse.</li>
  <li>The emission is attenuated so that at most one fluorescence photon is detected per laser pulse by a microchannel plate photomultiplier tube (MCP-PMT), which generates a STOP pulse.</li>
  <li>A Time-to-Amplitude Converter (TAC) measures the time interval \(\Delta t\) between START and STOP, charging a capacitor proportionally.</li>
  <li>A Multi-Channel Analyzer (MCA) bins the events into a histogram representing the probability distribution of photon emission \(I(t)\).</li>
</ol>
<p>The true fluorescence decay \(F(t)\) is recovered by numerical deconvolution with the instrumental response function (IRF): \(I(t) = \int_0^t \text{IRF}(t') F(t - t') dt'\).</p>
<h4 class="content-heading">2. Femtosecond Pump-Probe Transient Absorption</h4>
<p>To capture chemical bond breaking, electron transfer, and conical intersections on their fundamental vibrational timescales (\(10 - 1000\text{ fs}\)), Ahmed Zewail pioneered femtosecond pump-probe spectroscopy (1999 Nobel Prize):</p>
<ul>
  <li><strong>Pump Pulse:</strong> An ultrashort femtosecond laser pulse (e.g., \(800\text{ nm}\) or harmonic, pulse width \(\sim 35\text{ fs}\)) photoexcites the sample, creating a coherent population in \(S_1\).</li>
  <li><strong>Probe Pulse:</strong> A broadband white-light supercontinuum pulse generated in a sapphire crystal interrogates the sample at a calibrated optical delay time \(t_{\text{delay}} = 2 \Delta x / c\).</li>
</ul>
<p>The recorded differential absorption spectrum \(\Delta A(\lambda, t) = A_{\text{pump on}} - A_{\text{pump off}}\) contains four concurrent photophysical signatures:</p>
<ol>
  <li><strong>Ground State Bleach (GSB, \(\Delta A < 0\)):</strong> Depletion of ground-state molecules reduces absorption at the ground-state band.</li>
  <li><strong>Stimulated Emission (SE, \(\Delta A < 0\)):</strong> Probe photons stimulate emission from \(S_1\) back to \(S_0\), amplifying transmitted probe light.</li>
  <li><strong>Excited State Absorption (ESA, \(\Delta A > 0\)):</strong> Absorption of probe photons by \(S_1\) promoting electrons to higher states \(S_n\).</li>
  <li><strong>Photoproduct Absorption (\(\Delta A > 0\)):</strong> Formation of new chemical species (triplets, radicals, isomerized products).</li>
</ol>"""
    }

    # Unit 8: Section 8.8
    s8[8] = {
        "id": "u8-sec8",
        "number": "8.8",
        "title": "Chiral Shift Reagents, Lanthanide Induced Shifts & Reaction Field Theory",
        "content": r"""<p>Enantiomers in an achiral solvent environment possess identical chemical shifts and coupling constants in \(^1\text{H}\) and \(^{13}\text{C}\) NMR spectra because their internal stereochemical relationships are enantiotopic and related by symmetry.</p>
<h4 class="content-heading">Lanthanide Shift Reagents (LSR)</h4>
<p>In 1969, Hinckley discovered that paramagnetic coordination complexes of trivalent lanthanide ions (primarily Europium \(\text{Eu}^{3+}\) and Praseodymium \(\text{Pr}^{3+}\)) with fluorinated \(\beta\)-diketonate ligands (such as \(\text{Eu(fod)}_3\) or \(\text{Eu(dpm)}_3\)) reversibly coordinate to Lewis-basic functional groups (\(-\text{OH}, -\text{NH}_2, >\text{C=O}, -\text{O-}\)):</p>
\[
\text{Substrate} + \text{LSR} \rightleftharpoons [\text{Substrate} \cdot \text{LSR}]
\]
<p>Fast chemical exchange on the NMR timescale produces a weighted average chemical shift. The paramagnetic lanthanide induces a massive pseudo-contact (dipolar) shift \(\Delta\delta_{\text{dip}}\) governed by the <strong>Bleaney equation</strong>:</p>
\[
\Delta\delta_{\text{dip}} = C_J \frac{\mu_B^2}{k_B^2 T^2} \left[ \frac{3\cos^2\theta - 1}{r^3} \right]
\]
<p>where \(r\) is the distance from the lanthanide metal center to the nucleus, \(\theta\) is the angle relative to the principal magnetic axis of the complex, and \(C_J\) is a constant characteristic of the lanthanide (\(C_J > 0\) for \(\text{Eu}^{3+}\), causing downfield shifts; \(C_J < 0\) for \(\text{Pr}^{3+}\), causing upfield shifts). Because the shift attenuates as \(r^{-3}\), complex overlapping multiplets are spread across many ppm without line broadening.</p>
<h4 class="content-heading">Enantiomeric Excess Determination via Chiral Solvating Agents</h4>
<p>When a chiral shift reagent (such as chiral tris[3-(heptafluoropropylhydroxymethylene)-(+)-camphorato]europium(III), \(\text{Eu(hfc)}_3\)) is added to a racemic mixture of enantiomers (\(R\) and \(S\)):</p>
\[
(R)\text{-Substrate} + \text{Eu(hfc)}_3 \rightleftharpoons \text{Diastereomeric Complex } [(R) \cdot \text{Eu(hfc)}_3]
\]
\[
(S)\text{-Substrate} + \text{Eu(hfc)}_3 \rightleftharpoons \text{Diastereomeric Complex } [(S) \cdot \text{Eu(hfc)}_3]
\]
<p>The resulting complexes are <strong>diastereomers</strong>, possessing different thermodynamic stability constants and different spatial geometries. Consequently, the enantiotopic protons become diastereotopic and exhibit distinct chemical shifts (\(\Delta\Delta\delta \sim 0.05 - 0.5\text{ ppm}\)). Direct integration of the separated peak areas determines the <strong>enantiomeric excess (ee)</strong>:</p>
\[
\text{ee} = \frac{|A_R - A_S|}{A_R + A_S} \times 100\%
\]"""
    }

    # Unit 9: Section 9.8
    s8[9] = {
        "id": "u9-sec8",
        "number": "9.8",
        "title": "TOCSY, HMQC & Triple-Resonance Biomolecular NMR Spectroscopy",
        "content": r"""<p>As molecular complexity scales to large natural products, oligosaccharides, and proteins (\(> 10\text{ kDa}\)), conventional 2D COSY spectra become uninterpretable due to severe peak overlap. Advanced multidimensional pulse sequences resolve these structural ambiguities.</p>
<h4 class="content-heading">1. TOCSY (Total Correlation Spectroscopy)</h4>
<p>Unlike COSY, which only reveals scalar correlations between directly coupled neighboring protons (\(^2J\) and \(^3J\)), TOCSY utilizes a continuous isotropic radiofrequency spin-lock sequence (such as MLEV-17 or DIPSI-2) during the mixing period \(\tau_m\) (\(30 - 120\text{ ms}\)):</p>
<ul>
  <li>During the spin lock, scalar couplings are transformed into an isotropic exchange Hamiltonian: \(\hat{H}_{\text{eff}} = 2\pi \sum J_{ij} \vec{I}_i \cdot \vec{I}_j\).</li>
  <li>Magnetization propagates coherently through the entire scalar coupling network (relay mechanism): \(A \to M \to X \to \dots\).</li>
  <li>All protons belonging to the same continuous spin system (e.g., all protons within a single amino acid sidechain or monosaccharide ring) appear on the same horizontal track, identifying individual spin systems at a glance.</li>
</ul>
<h4 class="content-heading">2. Triple-Resonance 3D NMR of Proteins</h4>
<p>In structural biology, recombinant proteins uniformly labeled with stable isotopes (\(^{13}\text{C}\) and \(^{15}\text{N}\)) are analyzed using 3D triple-resonance pulse sequences that transfer magnetization through large, well-defined one-bond couplings (\(^1J_{NH} \approx 90\text{ Hz}\), \(^1J_{NC\alpha} \approx 11\text{ Hz}\), \(^1J_{C\alpha C'} \approx 55\text{ Hz}\)):</p>
<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Experiment</th>
        <th>Correlated Nuclei (Dimensions)</th>
        <th>Magnetization Transfer Pathway</th>
        <th>Structural Function</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>HNCA</strong></td>
        <td>\(^1\text{H}^N(i) - {}^{15}\text{N}(i) - {}^{13}\text{C}^\alpha(i, i-1)\)</td>
        <td>\(^1\text{H}^N \xrightarrow{J_{NH}} {}^{15}\text{N} \xrightarrow{J_{NC\alpha}} {}^{13}\text{C}^\alpha \xrightarrow{J_{NC\alpha}} {}^{15}\text{N} \xrightarrow{J_{NH}} {}^1\text{H}^N\)</td>
        <td>Correlates amide to both intra-residue \(C^\alpha(i)\) and preceding \(C^\alpha(i-1)\)</td>
      </tr>
      <tr>
        <td><strong>HN(CO)CA</strong></td>
        <td>\(^1\text{H}^N(i) - {}^{15}\text{N}(i) - {}^{13}\text{C}^\alpha(i-1)\)</td>
        <td>\(^1\text{H}^N \to {}^{15}\text{N} \xrightarrow{J_{NCO}} {}^{13}\text{C}'(i-1) \xrightarrow{J_{COC\alpha}} {}^{13}\text{C}^\alpha(i-1) \to \text{detect}\)</td>
        <td>Exclusively detects preceding residue \(C^\alpha(i-1)\)</td>
      </tr>
      <tr>
        <td><strong>HNCO</strong></td>
        <td>\(^1\text{H}^N(i) - {}^{15}\text{N}(i) - {}^{13}\text{C}'(i-1)\)</td>
        <td>\(^1\text{H}^N \to {}^{15}\text{N} \xrightarrow{J_{NCO}} {}^{13}\text{C}'(i-1) \to \text{detect}\)</td>
        <td>Highest sensitivity 3D experiment; correlates amide to preceding carbonyl</td>
      </tr>
    </tbody>
  </table>
</div>
<p>By comparing the pair of \(C^\alpha\) peaks in HNCA with the single preceding \(C^\alpha(i-1)\) peak in HN(CO)CA, spectroscopists step sequentially along the peptide chain like dominoes, completing the complete sequence-specific backbone resonance assignment of intact proteins.</p>"""
    }

    # Unit 10: Section 10.8
    s8[10] = {
        "id": "u10-sec8",
        "number": "10.8",
        "title": "Advanced Pulse EPR (DEER, ESEEM) & Synchrotron Mössbauer Spectroscopy",
        "content": r"""<p>Modern advancements in magnetic and nuclear resonance have pushed experimental boundaries to nanoscale distance measurements and synchrotron brilliance:</p>
<h4 class="content-heading">1. Double Electron-Electron Resonance (DEER / PELDOR)</h4>
<p>While continuous-wave (CW) EPR measures small distances through spectral line broadening, <strong>4-pulse DEER (Double Electron-Electron Resonance)</strong> measures through-space magnetic dipole-dipole coupling between two nitroxide spin labels across macromolecular distances of \(1.5 - 10\text{ nm}\) (\(15 - 100\text{ \AA}\)):</p>
<ol>
  <li>A 3-pulse observer sequence (\(\pi/2 - \tau_1 - \pi - (\tau_1 + t) - \text{echo}\)) monitors the refocused primary spin echo of spin \(A\) at frequency \(\nu_A\).</li>
  <li>A high-power pump pulse at pump frequency \(\nu_B\) selectively flips spin \(B\), modulating the local dipolar field experienced by spin \(A\).</li>
  <li>The dipolar modulation frequency \(\omega_{\text{dip}}\) scales inversely with the cube of the distance:
  \[
  \omega_{\text{dip}}(\theta) = \frac{\mu_0 \mu_B^2 g_A g_B}{4\pi \hbar r^3} (1 - 3\cos^2\theta)
  \]
  </li>
  <li>Tikhonov regularization of the time-domain dipolar oscillations yields the complete probability distribution of distances \(P(r)\) with sub-angstrom precision, revolutionizing structural biology of membrane transporters and protein complexes.</li>
</ol>
<h4 class="content-heading">2. Electron Spin Echo Envelope Modulation (ESEEM & HYSCORE)</h4>
<p>ESEEM applies microwave pulse sequences to measure very weak electron-nuclear hyperfine couplings (\(< 10\text{ MHz}\)) that are completely hidden within inhomogeneous CW-EPR lineshapes. 2D HYSCORE (Hyperfine Sublevel Correlation) separates nuclear frequencies into cross-peaks, identifying coordinating \(^{14}\text{N}\) or \(^{17}\text{O}\) ligands around active-site metal centers.</p>
<h4 class="content-heading">3. Synchrotron Mössbauer Source (Nuclear Forward Scattering)</h4>
<p>Conventional Mössbauer spectroscopy relies on radioactive \(^{57}\text{Co}\) decay sources with limited photon flux and non-directional emission. Third- and fourth-generation synchrotron radiation facilities (such as ESRF, PETRA III, APS, SPring-8) generate monochromatic pulsed X-ray beams tuned to the \(14.4125\text{ keV}\) nuclear resonance of \(^{57}\text{Fe}\):</p>
<ul>
  <li><strong>Nuclear Forward Scattering (NFS):</strong> Intense, highly collimated synchrotron pulses excite the nuclear ensemble coherently, producing a forward-scattered time-delayed 'quantum beat' interference pattern recorded on nanosecond time scales.</li>
  <li><strong>Diamond Anvil Cell Extremes:</strong> The micro-focused beam (\(< 10\ \mu\text{m}\)) permits Mössbauer investigations of iron minerals under core-mantle boundary conditions exceeding \(150\text{ GPa}\) and \(3000\text{ K}\), establishing spin-pairing and oxidation transitions in the Earth's deep interior.</li>
</ul>"""
    }

    return s8

if __name__ == "__main__":
    s8 = get_section8_dict()
    print(f"Generated Section 8 for {len(s8)} units.")
    for u_num, sec in s8.items():
        print(f"Unit {u_num}: Section {sec['number']} - {sec['title']}")
