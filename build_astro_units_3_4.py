import json
import os

u3 = {
    "unitId": 3,
    "title": "Stellar Structure, Evolution & The Hertzsprung-Russell Diagram",
    "subtitle": "Saha Ionization, Jeans Collapse, Main Sequence Scaling & Post-MS Nucleosynthesis",
    "icon": "🌟",
    "summary": "This unit develops the comprehensive physical lifecycle of stars, from molecular cloud collapse to post-main sequence death. We formalize quantitative astronomical photometry, bolometric corrections, and the Morgan-Keenan spectral classification, deriving the Saha ionization equation to elucidate the Balmer maximum in A0 stars. We construct the theoretical Hertzsprung-Russell diagram, deriving mass-luminosity scaling relations ($L \\propto M^{3.5}$) and main-sequence lifetimes. We investigate star formation via the Jeans gravitational instability criterion, trace pre-main sequence Hayashi and Henyey evolutionary tracks, and follow low- and high-mass stars through post-main sequence hydrogen shell burning, red giant expansion, the core helium flash, asymptotic giant branch dredge-up episodes, and terminal supernova core collapse.",
    "keyTakeaways": [
        "Stellar apparent and absolute magnitudes connect via Pogson's logarithmic flux formula $m_1 - m_2 = -2.5\\log_{10}(F_1/F_2)$, with intrinsic luminosities dictated by the Stefan-Boltzmann law $L = 4\\pi R^2 \\sigma T_{\\text{eff}}^4$.",
        "The spectral sequence OBAFGKM reflects stellar surface temperature rather than chemical composition, with line absorption strengths governed by the interplay of the Boltzmann excitation equation and the Saha ionization formula.",
        "Gravitational cloud collapse occurs when thermal gas pressure fails to support self-gravity, satisfying the Jeans mass instability criterion $M > M_J = \\frac{\\pi}{6}\\rho \\left(\\frac{5 k T}{G \\mu m_H \\rho^{1/3}}\\right)^{3/2} \\propto T^{3/2} \\rho^{-1/2}$.",
        "On the main sequence, stars maintain steady core hydrogen fusion with stellar luminosities scaling steeply as $L \\propto M^{3.5}$, leading to nuclear lifetimes $\\tau_{\\text{MS}} \\propto M/L \\propto M^{-2.5}$ where massive stars exhaust their fuel millions of times faster than low-mass dwarfs.",
        "Post-main sequence evolution diverges by mass: low-mass stars ($M < 2 M_\\odot$) undergo an explosive degenerate helium core flash before shedding planetary nebulae, while massive stars ($M > 8 M_\\odot$) burn successive nuclear fuels up to an inert iron core, triggering catastrophic core-collapse supernovae."
    ],
    "sections": [
        {
            "id": "sec-3-1",
            "title": "Stellar Photometry, Magnitudes & Color Indices",
            "content": """
<p>Quantitative measurement of stellar electromagnetic radiation requires rigorous photometric systems that measure radiant energy flux across calibrated spectral passbands.</p>

<h4>Apparent Magnitude & Pogson's Relation</h4>
<p>The human eye perceives light intensity logarithmically (the Weber-Fechner law). In 1856, Norman Pogson formalized the ancient magnitude scale of Hipparchus by defining a difference of 5 magnitudes as corresponding to an exact flux ratio of $100:1$. The difference between two apparent magnitudes $m_1$ and $m_2$ with detected radiant energy fluxes $F_1$ and $F_2$ ($\text{W m}^{-2}$) is:</p>
<div class="equation-box">
$$m_1 - m_2 = -2.5 \\log_{10}\\left(\\frac{F_1}{F_2}\\right)$$
$$m = -2.5 \\log_{10}(F) + C_0$$
</div>
<p>where $C_0$ is the zero-point constant defining the photometric system (traditionally anchored to $\\alpha$ Lyrae / Vega as $m = 0.0$ in all optical bands).</p>

<h4>Absolute Magnitude & Distance Modulus</h4>
<p>The <strong>absolute magnitude ($M$)</strong> is defined as the apparent magnitude a star would have if placed at a standard reference distance of exactly $10\\text{ parsecs}$ ($32.6\\text{ ly}$) in the absence of interstellar extinction:</p>
<div class="equation-box">
$$F(10\\text{ pc}) = \\frac{L}{4\\pi (10\\text{ pc})^2}, \\quad F(d) = \\frac{L}{4\\pi d^2}$$
$$m - M = -2.5 \\log_{10}\\left(\\frac{F(d)}{F(10\\text{ pc})}\\right) = -2.5 \\log_{10}\\left(\\frac{10\\text{ pc}}{d}\\right)^2 = 5 \\log_{10}\\left(\\frac{d}{10\\text{ pc}}\\right)$$
$$\\mu \\equiv m - M = 5 \\log_{10}(d / \\text{pc}) - 5$$
</div>

<h4>Bolometric Magnitude & Luminosity</h4>
<p>The total radiant power emitted by a star integrated across all electromagnetic wavelengths from radio to gamma rays is its <strong>bolometric luminosity ($L$)</strong>. The absolute bolometric magnitude $M_{\\text{bol}}$ is anchored by convention to the Sun ($M_{\\text{bol},\\odot} = +4.74$):</p>
<div class="equation-box">
$$M_{\\text{bol}} - M_{\\text{bol},\\odot} = -2.5 \\log_{10}\\left(\\frac{L}{L_\\odot}\\right)$$
$$L = L_\\odot \\times 10^{-0.4(M_{\\text{bol}} - 4.74)}$$
</div>
<p>Because optical detectors sample only visual photons, the <strong>bolometric correction (BC)</strong> converts visual absolute magnitude $M_V$ to bolometric absolute magnitude: $M_{\\text{bol}} = M_V + \\text{BC}$. BC is always negative by modern convention.</p>

<h4>Color Index & Effective Temperature</h4>
<p>The standard Johnson-Cousins filter system uses broad passbands: Ultraviolet ($U, \\lambda_{\\text{eff}} \\approx 365\\text{ nm}$), Blue ($B, \\lambda_{\\text{eff}} \\approx 440\\text{ nm}$), and Visual ($V, \\lambda_{\\text{eff}} \\approx 550\\text{ nm}$). The <strong>color index</strong> is defined as the magnitude difference between two bands:</p>
<div class="equation-box">
$$B - V = m_B - m_V = -2.5 \\log_{10}\\left(\\frac{F_B}{F_V}\\right) + \\text{const}$$
</div>
<p>By Planck's blackbody law, hotter stars emit predominantly at shorter wavelengths, exhibiting smaller or negative $B-V$ values (e.g., $B-V \\approx -0.3$ for an O-star at $35{,}000\\text{ K}$), whereas cool red dwarfs exhibit large positive values ($B-V \\approx +1.5$ for an M-dwarf at $3{,}000\\text{ K}$). The <strong>effective temperature ($T_{\\text{eff}}$)</strong> is defined by the Stefan-Boltzmann law:</p>
<div class="equation-box">
$$L = 4\\pi R^2 \\sigma T_{\\text{eff}}^4$$
</div>
"""
        },
        {
            "id": "sec-3-2",
            "title": "Spectral Classification & The Saha-Boltzmann Ionization Physics",
            "content": """
<p>Stellar spectra exhibit diverse dark absorption lines superimposed on continuous thermal continua. Annie Jump Cannon and the Harvard Computers categorized stars into the empirical sequence <strong>O, B, A, F, G, K, M</strong>. In 1925, Cecilia Payne-Gaposchkin proved that this sequence represents a monotonic progression in stellar surface temperature rather than differences in elemental composition.</p>

<h4>The Morgan-Keenan (MK) Spectral & Luminosity System</h4>
<table class="data-table">
  <thead>
    <tr><th>Spectral Type</th><th>$T_{\\text{eff}}$ Range (K)</th><th>Color</th><th>Dominant Spectral Line Signatures</th></tr>
  </thead>
  <tbody>
    <tr><td>O</td><td>$> 30{,}000$</td><td>Deep Blue</td><td>Ionized helium (He II), weak H Balmer lines, highly ionized N III, C III</td></tr>
    <tr><td>B</td><td>$10{,}000 - 30{,}000$</td><td>Blue-White</td><td>Neutral helium (He I) max at B2, moderate H Balmer lines, O II, Si II</td></tr>
    <tr><td>A</td><td>$7{,}500 - 10{,}000$</td><td>White</td><td>Hydrogen Balmer lines reach maximum strength at A0 ($T \\approx 9520\\text{ K}$), weak Ca II</td></tr>
    <tr><td>F</td><td>$6{,}000 - 7{,}500$</td><td>Yellow-White</td><td>Weakening Balmer lines, prominent ionized calcium (Ca II H & K lines), Fe I, Fe II</td></tr>
    <tr><td>G</td><td>$5{,}200 - 6{,}000$</td><td>Yellow</td><td>Solar-type; strong Ca II H & K, dominant neutral metal lines (Fe I), CH G-band</td></tr>
    <tr><td>K</td><td>$3{,}700 - 5{,}200$</td><td>Orange</td><td>Strong neutral metal lines, Ca I $\\lambda 4227$, molecular bands of TiO begin to appear</td></tr>
    <tr><td>M</td><td>$2{,}400 - 3{,}700$</td><td>Red</td><td>Very strong molecular absorption bands of Titanium Oxide (TiO), neutral metals</td></tr>
  </tbody>
</table>
<p>Luminosity classes reflect gas density and pressure broadening in the stellar atmosphere: <strong>Ia/Ib</strong> (Supergiants), <strong>II</strong> (Bright Giants), <strong>III</strong> (Regular Giants), <strong>IV</strong> (Subgiants), <strong>V</strong> (Main Sequence Dwarfs, e.g., the Sun is G2V), and <strong>wd</strong> (White Dwarfs).</p>

<h4>The Boltzmann Excitation Formula</h4>
<p>In thermal equilibrium at temperature $T$, the ratio of populations of atoms of the same ionization state occupying energy states $E_A$ and $E_B$ with statistical weights $g_A$ and $g_B$ is governed by Maxwell-Boltzmann statistics:</p>
<div class="equation-box">
$$\\frac{N_B}{N_A} = \\frac{g_B}{g_A} \\exp\\left(-\\frac{E_B - E_A}{k T}\\right)$$
</div>
<p>For hydrogen, the ground state ($n=1$) has $g_1 = 2(1)^2 = 2$ and $E_1 = -13.6\\text{ eV}$. The first excited state ($n=2$) from which optical Balmer absorption originates has $g_2 = 2(2)^2 = 8$ and $E_2 = -3.40\\text{ eV}$, with excitation energy $\\Delta E = 10.20\\text{ eV}$.</p>

<h4>The Saha Ionization Equation</h4>
<p>Megnad Saha (1920) combined quantum statistical mechanics and chemical thermodynamics to determine the ionization equilibrium ratio between ionization stage $j+1$ and stage $j$:</p>
<div class="equation-box">
$$\\frac{N_{j+1}}{N_j} = \\frac{2 k T g_{j+1}}{P_e g_j} \\left(\\frac{2\\pi m_e k T}{h^2}\\right)^{3/2} \\exp\\left(-\\frac{\\chi_j}{k T}\\right)$$
</div>
<p>where $P_e = n_e k T$ is the electron pressure, $m_e$ is electron mass, and $\\chi_j$ is the ionization potential from ground state $j$ to $j+1$ ($\\chi = 13.60\\text{ eV}$ for neutral hydrogen $\\text{H I} \\to \\text{H II}$).</p>

<h4>Explanation of the Balmer Maximum at A0</h4>
<p>The fraction of all hydrogen atoms capable of absorbing a visual Balmer photon is $\\frac{N_{n=2,\\text{H I}}}{N_{\\text{total}}} = \\left(\\frac{N_{n=2}}{N_{\\text{H I}}}\\right) \\left(\\frac{N_{\\text{H I}}}{N_{\\text{H I}} + N_{\\text{H II}}}\\right)$.</p>
<ul>
  <li>At low temperatures ($T < 7{,}000\\text{ K}$, G, K, M stars), hydrogen is almost completely neutral ($N_{\\text{H I}} \\approx N_{\\text{total}}$), but the Boltzmann factor $\\exp(-10.2\\text{ eV}/kT)$ is vanishingly small ($< 10^{-7}$). Virtually all atoms reside in $n=1$, making Balmer absorption weak.</li>
  <li>At high temperatures ($T > 12{,}000\\text{ K}$, B and O stars), thermal collisions vigorously populate $n=2$, but the Saha factor ionizes nearly all hydrogen into bare protons ($N_{\\text{H II}} \\gg N_{\\text{H I}}$). Few neutral atoms remain, weakening the lines.</li>
  <li>The product peaks sharply at $T \\approx 9{,}520\\text{ K}$ (spectral type A0), explaining the prominence of Balmer lines in A-stars.</li>
</ul>
"""
        },
        {
            "id": "sec-3-3",
            "title": "The Hertzsprung-Russell (H-R) Diagram & Mass-Luminosity Scaling",
            "content": """
<p>Independently discovered by Ejnar Hertzsprung (1911) and Henry Norris Russell (1913), the <strong>Hertzsprung-Russell (H-R) diagram</strong> plots stellar luminosity $L/L_\\odot$ (or absolute magnitude $M_V$) against effective surface temperature $T_{\\text{eff}}$ (or spectral type / color index $B-V$), with temperature decreasing to the right.</p>

<h4>Anatomy of the H-R Diagram</h4>
<ul>
  <li><strong>The Main Sequence:</strong> A prominent diagonal band running from hot, luminous blue stars (top left: O stars, $L \\sim 10^5 L_\\odot, T \\sim 40{,}000\\text{ K}$) to cool, dim red dwarfs (bottom right: M stars, $L \\sim 10^{-4} L_\\odot, T \\sim 3{,}000\\text{ K}$). Over $90\\%$ of all observed stars lie on the main sequence, stably fusing hydrogen into helium in their cores.</li>
  <li><strong>Red Giants and Supergiants:</strong> Occupy the upper right ($L \\sim 10^2 - 10^5 L_\\odot, T \\sim 3{,}000 - 5{,}000\\text{ K}$). By the Stefan-Boltzmann law $R = \\sqrt{L / (4\\pi\\sigma T_{\\text{eff}}^4)}$, these stars possess immense physical radii ($R \\sim 10 - 1000 R_\\odot$).</li>
  <li><strong>White Dwarfs:</strong> Occupy the lower left ($L \\sim 10^{-4} - 10^{-2} L_\\odot, T \\sim 10{,}000 - 30{,}000\\text{ K}$). They are exceedingly hot yet faint, implying Earth-like radii ($R \\sim 0.01 R_\\odot$).</li>
</ul>

<h4>The Empirical Mass-Luminosity Relation</h4>
<p>For main-sequence stars in detached, double-lined eclipsing binary systems where masses and luminosities are measured with precision, a steep power-law relation emerges:</p>
<div class="equation-box">
$$\\frac{L}{L_\\odot} \\approx \\left(\\frac{M}{M_\\odot}\\right)^\\alpha$$
</div>
<p>where:</p>
<ul>
  <li>$\\alpha \\approx 4.0$ for $0.43 M_\\odot < M < 2 M_\\odot$</li>
  <li>$\\alpha \\approx 3.5$ for intermediate-mass stars ($2 M_\\odot < M < 20 M_\\odot$)</li>
  <li>$\\alpha \\to 1.0$ for ultra-massive stars ($M > 50 M_\\odot$) as radiation pressure dominates gas pressure ($P_{\\text{rad}} \\gg P_{\\text{gas}}$).</li>
</ul>

<h4>Derivation of Mass-Luminosity Scaling from Stellar Structure</h4>
<p>From hydrostatic equilibrium, $\\frac{P}{R} \\sim \\frac{G M \\rho}{R^2} \\implies P \\sim \\frac{G M^2}{R^4}$. For an ideal gas, $P \\sim \\frac{\\rho k T}{\\mu m_H} \\sim \\frac{M T}{\\mu R^3}$. Equating these gives the interior temperature scaling:</p>
<div class="equation-box">
$$T \\sim \\frac{\\mu G M}{R}$$
</div>
<p>Energy transport via radiative diffusion gives $L \\sim \\frac{R^2 a_{\\text{rad}} c T^3}{\\kappa \\rho} \\frac{T}{R} \\sim \\frac{R T^4}{\\kappa (M/R^3)} \\sim \\frac{R^4 T^4}{\\kappa M}$.</p>
<p>For electron scattering opacity, $\\kappa = \\kappa_{\\text{es}} = \\text{constant}$. Substituting $T \\propto M/R$:</p>
<div class="equation-box">
$$L \\propto \\frac{R^4}{\\kappa M} \\left(\\frac{M}{R}\\right)^4 \\propto \\frac{M^3}{\\kappa} \\implies L \\propto M^3$$
</div>
<p>Taking Kramers' opacity $\\kappa \\propto \\rho T^{-7/2}$ yields an even steeper relation: $L \\propto M^{5.5} R^{-0.5} \\approx M^{3.5}$.</p>

<h4>Main-Sequence Lifetimes</h4>
<p>The total nuclear energy available from core hydrogen fusion is $E_{\\text{nuc}} = f_{\\text{core}} X \\eta_{\\text{fusion}} M c^2$, where $f_{\\text{core}} \\approx 0.10$ and $\\eta_{\\text{fusion}} = 0.0071$ ($0.71\\%$ mass deficit). The main-sequence lifetime $\\tau_{\\text{MS}}$ is:</p>
<div class="equation-box">
$$\\tau_{\\text{MS}} = \\frac{E_{\\text{nuc}}}{L} \\propto \\frac{M}{L} \\propto \\frac{M}{M^{3.5}} = M^{-2.5}$$
$$\\tau_{\\text{MS}} \\approx 10^{10}\\text{ yr} \\left(\\frac{M_\\odot}{M}\\right)^{2.5}$$
</div>
<p>A $10 M_\\odot$ B-star lives only $\\sim 30\\text{ million years}$, while a $0.2 M_\\odot$ red dwarf endures for over a trillion years!</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 3.1: Interactive Hertzsprung-Russell Diagram & Evolutionary Tracks</h4>
  </div>
  <p>Explore thousands of stars plotted across the H-R diagram. Select initial progenitor masses from $0.8 M_\\odot$ to $25 M_\\odot$ and follow real-time evolutionary tracks from the Main Sequence through Red Giant, Horizontal Branch, and supernova or white dwarf cooling phases.</p>
  <div id="astro-hr-diagram-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-3-4",
            "title": "Star Formation & The Jeans Gravitational Collapse Criterion",
            "content": """
<p>Stars condense out of dense, cold interstellar clouds known as <strong>Giant Molecular Clouds (GMCs)</strong> ($T \\sim 10-20\\text{ K}$, $n \\sim 10^3 - 10^6\\text{ cm}^{-3}$, composed predominantly of molecular hydrogen $\\text{H}_2$). Sir James Jeans (1902) formulated the mathematical condition under which self-gravity overcomes internal thermal gas pressure, triggering runaway gravitational collapse.</p>

<h4>Virial Derivation of the Jeans Mass</h4>
<p>By the Virial Theorem, a spherical cloud of mass $M$, radius $R$, uniform density $\\rho$, and temperature $T$ with total particle count $N = \\frac{M}{\\mu m_H}$ collapses if the magnitude of its gravitational potential energy exceeds twice its internal thermal kinetic energy:</p>
<div class="equation-box">
$$|\\Omega| > 2 K$$
</div>
<p>For a homogeneous sphere, $\\Omega = -\\frac{3}{5}\\frac{G M^2}{R}$. The thermal kinetic energy is $K = \\frac{3}{2} N k T = \\frac{3}{2}\\frac{M}{\\mu m_H} k T$.</p>
<p>Setting the threshold $|\\Omega| = 2K$ gives:</p>
<div class="equation-box">
$$\\frac{3}{5}\\frac{G M^2}{R} = 3\\frac{M}{\\mu m_H} k T \\implies \\frac{G M}{R} = \\frac{5 k T}{\\mu m_H}$$
</div>
<p>Expressing radius in terms of density $R = \\left(\\frac{3M}{4\\pi\\rho}\\right)^{1/3}$:</p>
<div class="equation-box">
$$G M \\left(\\frac{4\\pi\\rho}{3M}\\right)^{1/3} = \\frac{5 k T}{\\mu m_H} \\implies M^{2/3} = \\frac{5 k T}{G \\mu m_H} \\left(\\frac{3}{4\\pi\\rho}\\right)^{1/3}$$
$$M_J = \\left(\\frac{5 k T}{G \\mu m_H}\\right)^{3/2} \\left(\\frac{3}{4\\pi\\rho}\\right)^{1/2} \\propto T^{3/2} \\rho^{-1/2}$$
</div>

<h4>The Jeans Length ($\\lambda_J$)</h4>
<p>From linear perturbation analysis of the linearized continuity, Euler, and Poisson fluid equations with wave perturbations $\\delta\\rho \\propto e^{i(\\vec{k}\\cdot\\vec{r} - \\omega t)}$, the acoustic dispersion relation in a self-gravitating medium is:</p>
<div class="equation-box">
$$\\omega^2 = k^2 c_s^2 - 4\\pi G \\rho_0$$
</div>
<p>where $c_s = \\sqrt{\\frac{\\gamma k T}{\\mu m_H}}$ is the isothermal sound speed. If $k^2 c_s^2 < 4\\pi G \\rho_0$, $\\omega^2 < 0$, making $\\omega = \\pm i \\gamma$ imaginary. Density perturbations grow exponentially in time: $\\delta\\rho \\propto e^{\\gamma t}$, driving unstable collapse! The marginal stability wavevector $k_J$ and <strong>Jeans length</strong> $\\lambda_J$ are:</p>
<div class="equation-box">
$$k_J = \\sqrt{\\frac{4\\pi G \\rho_0}{c_s^2}} \\implies \\lambda_J = \\frac{2\\pi}{k_J} = c_s \\sqrt{\\frac{\\pi}{G \\rho_0}} = \\sqrt{\\frac{\\pi k T}{G \\mu m_H \\rho_0}}$$
</div>

<h4>Free-Fall Collapse Timescale</h4>
<p>If thermal pressure is neglected entirely, a pressureless sphere collapses under pure gravity. Integrating the radial equation of motion $\\ddot{r} = -\\frac{G M(r)}{r^2}$ yields the <strong>free-fall timescale ($\\tau_{\\text{ff}}$)</strong>:</p>
<div class="equation-box">
$$\\tau_{\\text{ff}} = \\sqrt{\\frac{3\\pi}{32 G \\rho_0}}$$
</div>
<p>Remarkably, $\\tau_{\\text{ff}}$ depends solely on the initial density $\\rho_0$, entirely independent of the cloud's initial size or total mass! For a typical molecular cloud core with density $\\rho = 10^{-19}\\text{ g cm}^{-3}$ ($n_{\\text{H}_2} \\approx 3 \\times 10^4\\text{ cm}^{-3}$), $\\tau_{\\text{ff}} \\approx 2 \\times 10^5\\text{ years}$.</p>
"""
        },
        {
            "id": "sec-3-5",
            "title": "Protostellar Contraction: The Hayashi & Henyey Tracks",
            "content": """
<p>As a collapsing gas core fragments, it forms an opaque, hydrostatically balanced protostellar core surrounded by an infalling circumstellar envelope and protoplanetary accretion disk.</p>

<h4>The Hayashi Limit & Hayashi Track</h4>
<p>Chushiro Hayashi (1961) proved that for a star of given mass $M$ in hydrostatic equilibrium, there exists a minimum effective temperature below which no stable solution exists. This boundary—the <strong>Hayashi track</strong>—corresponds to a nearly vertical locus on the H-R diagram around $T_{\\text{eff}} \\sim 3{,}000 - 4{,}000\\text{ K}$.</p>
<p>A star on the Hayashi track is:</p>
<ul>
  <li><strong>Fully Convective:</strong> High molecular/atomic opacities in the cool exterior keep the radiative temperature gradient exceedingly steep, enforcing convective transport from core to surface.</li>
  <li><strong>Vertically Descending:</strong> Because the effective temperature remains pinned to the Hayashi boundary while the protostar gravitationally contracts ($R$ shrinks), its surface area drops rapidly. Consequently, its luminosity plummets at roughly constant $T_{\\text{eff}}$:
  $$L = 4\\pi R^2 \\sigma T_{\\text{eff}}^4 \\implies \\frac{dL}{dt} < 0 \\quad (T_{\\text{eff}} \\approx \\text{const})$$
  </li>
</ul>

<h4>The Henyey Track</h4>
<p>For protostars with $M \\gtrsim 0.5 M_\\odot$, contraction raises the core temperature sufficiently to ionize hydrogen and helium, drastically lowering the central opacity (Kramers' opacity $\\kappa \\propto T^{-7/2}$). Convection ceases in the core, establishing a stable <strong>radiative core</strong>. The protostar leaves the Hayashi track and turns horizontally onto the <strong>Henyey track</strong>, moving toward higher effective temperatures at nearly constant luminosity ($L \\approx \\text{const}, T_{\\text{eff}} \\uparrow$) until core hydrogen ignition halts contraction at the Zero-Age Main Sequence (ZAMS).</p>

<h4>The Brown Dwarf Threshold</h4>
<p>If a collapsing protostellar fragment has an initial mass $M < 0.075 M_\\odot$ ($75-80 M_{\\text{Jup}}$), gravitational contraction compresses the core to densities where <strong>non-relativistic electron degeneracy pressure</strong> sets in before central temperatures reach the $\\sim 3 \\times 10^6\\text{ K}$ threshold required for sustained $p$-$p$ hydrogen fusion. Degenerate electron pressure halts further contraction, forever preventing hydrogen ignition. Such failed stars are <strong>brown dwarfs</strong> (spectral types L, T, and Y), briefly burning trace deuterium before cooling indefinitely into cosmic obscurity.</p>
"""
        },
        {
            "id": "sec-3-6",
            "title": "Post-Main Sequence Evolution: Giants, Helium Flash & Supernovae",
            "content": """
<p>When core hydrogen is exhausted, the central nuclear furnace shuts down. What follows is a dramatic sequence of restructuring determined entirely by the star's initial birth mass.</p>

<h4>1. Low- and Intermediate-Mass Stars ($0.8 M_\\odot < M < 8 M_\\odot$)</h4>
<ol>
  <li><strong>Subgiant & Red Giant Branch (RGB):</strong> The inert helium core contracts, releasing gravitational energy that heats a surrounding hydrogen-burning shell. The stellar envelope expands dramatically (mirror principle: core contracts, envelope expands), cooling the surface until the star reaches the Hayashi boundary as a luminous Red Giant ($R \\sim 100 R_\\odot$).</li>
  <li><strong>The Helium Core Flash:</strong> For stars with $M < 2 M_\\odot$, the contracting helium core becomes completely supported by non-relativistic degenerate electron pressure ($P \\propto \\rho^{5/3}$) before reaching the helium ignition temperature ($T \\approx 10^8\\text{ K}$). Because degenerate pressure is independent of temperature ($\partial P / \\partial T = 0$), there is zero thermal expansion to moderate rising nuclear burn rates. When helium ignites via the triple-alpha process ($3\\,^4\\text{He} \\to\\ ^{12}\\text{C}$), a runaway thermal explosion occurs—the <strong>helium core flash</strong>—producing $L_{\\text{flash}} \\sim 10^{11} L_\\odot$ in seconds, which is absorbed by the outer envelope without disrupting the star. The flash ends when thermal energy lifts electron degeneracy.</li>
  <li><strong>Horizontal Branch (HB):</strong> The star burns core helium stably alongside a hydrogen shell.</li>
  <li><strong>Asymptotic Giant Branch (AGB):</strong> Core helium is exhausted, leaving an inert degenerate carbon-oxygen core surrounded by helium- and hydrogen-burning shells. Strong stellar winds and thermal pulses expel the entire outer envelope, illuminating the gas as a colorful <strong>planetary nebula</strong> ($v_{\\text{exp}} \\sim 20-30\\text{ km s}^{-1}$), leaving the hot exposed carbon-oxygen core as a cooling <strong>white dwarf</strong>.</li>
</ol>

<h4>2. Massive Stars ($M > 8 M_\\odot$) and Core-Collapse Supernovae</h4>
<p>Massive stars achieve central temperatures high enough to bypass electron degeneracy and sequentially ignite heavier fuels in an onion-skin core architecture:</p>
<div class="equation-box">
$$\\text{H-burning } (T \\sim 4 \\times 10^7\\text{ K}) \\to \\text{He-burning } (10^8\\text{ K}) \\to \\text{C-burning } (6 \\times 10^8\\text{ K}) \\to \\text{Ne-burning } (1.2 \\times 10^9\\text{ K}) \\to \\text{O-burning } (1.5 \\times 10^9\\text{ K}) \\to \\text{Si-burning } (3 \\times 10^9\\text{ K})$$
</div>
<p>Silicon fusion produces an inert iron-nickel core ($^{56}\\text{Fe}$). Because $^{56}\\text{Fe}$ and $^{62}\\text{Ni}$ possess the highest nuclear binding energy per nucleon ($8.8\\text{ MeV/nucleon}$), any further nuclear fusion is endothermic (absorbs energy). Silicon burning lasts only $\\approx 1\\text{ day}$.</p>
<p>When the inert iron core exceeds the Chandrasekhar limit ($M_{\\text{core}} > 1.44 M_\\odot$), electron degeneracy pressure fails. Catastrophic core collapse ensues within $\\sim 100\\text{ milliseconds}$ through:</p>
<ul>
  <li><strong>Photodisintegration:</strong> Energetic gamma rays shatter iron nuclei into alpha particles and free neutrons: $^{56}\\text{Fe} + \\gamma \\to 13\\,^4\\text{He} + 4n - 124.4\\text{ MeV}$.</li>
  <li><strong>Electron Capture (Neutronization):</strong> Electrons are crushed into protons: $p + e^- \\to n + \\nu_e$.</li>
</ul>
<p>The core collapses until nuclear density is reached ($\\rho_{\\text{nuc}} \\approx 2.7 \\times 10^{14}\\text{ g cm}^{-3}$), where strong repulsive nuclear forces abruptly halt the collapse, launching a colossal hydrodynamic shock wave. Revitalized by intense neutrino heating ($10^{58}$ neutrinos carrying $99\\%$ of the $10^{46}\\text{ J}$ gravitational binding energy), the shock wave blows the stellar mantle apart in a <strong>Type II / Ib / Ic Core-Collapse Supernova</strong>, forging heavy $r$-process elements and leaving a neutron star or black hole remnant.</p>
"""
        }
    ],
    "problems": [
        {
            "id": "prob-3-1",
            "title": "Stellar Radius, Luminosity & Effective Temperature from Gaia & Photometry",
            "statement": "The bright giant star Aldebaran ($\\alpha$ Tauri) has a measured Gaia trigonometric parallax $p = 50.0 \\pm 0.2\\text{ mas}$, an apparent visual magnitude $m_V = +0.85$, a bolometric correction $\\text{BC} = -0.70$, and a measured angular diameter from optical interferometry $\\theta_{\\text{LD}} = 20.58 \\pm 0.05\\text{ mas}$ (milliarcseconds).\\n\\n(a) Calculate the star's distance $d$ in parsecs and its absolute visual magnitude $M_V$.\\n(b) Determine the star's absolute bolometric magnitude $M_{\\text{bol}}$ and true bolometric luminosity $L/L_\\odot$ (taking $M_{\\text{bol},\\odot} = +4.74$).\\n(c) Calculate the star's physical radius $R$ in solar radii ($R_\\odot$).\\n(d) Calculate Aldebaran's effective temperature $T_{\\text{eff}}$ using the Stefan-Boltzmann relation.",
            "solution": """
<h4>(a) Distance & Absolute Visual Magnitude</h4>
<p>The distance is:</p>
<div class="equation-box">
$$d = \\frac{1}{p} = \\frac{1}{0.0500''} = 20.0\\text{ parsecs} = 65.2\\text{ ly}$$
</div>
<p>The distance modulus is $\\mu = 5\\log_{10}(20) - 5 = 5(1.30103) - 5 = 6.505 - 5 = 1.505$. Neglecting minimal local extinction ($A_V \\approx 0$):</p>
<div class="equation-box">
$$M_V = m_V - \\mu = 0.85 - 1.505 = -0.655$$
</div>

<h4>(b) Bolometric Magnitude & Luminosity</h4>
<p>With $\\text{BC} = -0.70$:</p>
<div class="equation-box">
$$M_{\\text{bol}} = M_V + \\text{BC} = -0.655 + (-0.70) = -1.355$$
</div>
<p>Comparing to the solar value $M_{\\text{bol},\\odot} = +4.74$:</p>
<div class="equation-box">
$$\\log_{10}\\left(\\frac{L}{L_\\odot}\\right) = -0.4 (M_{\\text{bol}} - M_{\\text{bol},\\odot}) = -0.4 (-1.355 - 4.74) = -0.4 (-6.095) = 2.438$$
$$\\frac{L}{L_\\odot} = 10^{2.438} \\approx 274.2 L_\\odot$$
</div>

<h4>(c) Physical Radius from Interferometric Angular Diameter</h4>
<p>The angular diameter is $\\theta = 20.58\\text{ mas} = 20.58 \\times 10^{-3} \\times \\left(\\frac{\\pi}{180 \\times 3600}\\right) \\approx 9.977 \\times 10^{-8}\\text{ radians}$.</p>
<p>The physical diameter $2R$ is:</p>
<div class="equation-box">
$$2R = \\theta \\times d = (9.977 \\times 10^{-8}\\text{ rad}) \\times (20.0 \\times 3.0857 \\times 10^{16}\\text{ m}) \\approx 6.160 \\times 10^{10}\\text{ m}$$
$$R = 3.080 \\times 10^{10}\\text{ m}$$
</div>
<p>In solar units ($R_\\odot = 6.957 \\times 10^8\\text{ m}$):</p>
<div class="equation-box">
$$\\frac{R}{R_\\odot} = \\frac{3.080 \\times 10^{10}}{6.957 \\times 10^8} \\approx 44.27 R_\\odot$$
</div>

<h4>(d) Effective Temperature</h4>
<p>From the Stefan-Boltzmann law $L = 4\\pi R^2 \\sigma T_{\\text{eff}}^4$:</p>
<div class="equation-box">
$$\\frac{L}{L_\\odot} = \\left(\\frac{R}{R_\\odot}\\right)^2 \\left(\\frac{T_{\\text{eff}}}{T_{\\text{eff},\\odot}}\\right)^4$$
$$274.2 = (44.27)^2 \\left(\\frac{T_{\\text{eff}}}{5778\\text{ K}}\\right)^4 = 1959.8 \\left(\\frac{T_{\\text{eff}}}{5778}\\right)^4$$
$$\\left(\\frac{T_{\\text{eff}}}{5778}\\right)^4 = \\frac{274.2}{1959.8} \\approx 0.1399 \\implies \\frac{T_{\\text{eff}}}{5778} = (0.1399)^{1/4} \\approx 0.6117$$
$$T_{\\text{eff}} = 0.6117 \\times 5778\\text{ K} \\approx 3534\\text{ K}$$
</div>
<p>Aldebaran is a K5III red giant star with $R \\approx 44.3 R_\\odot$, $L \\approx 274 L_\\odot$, and cool surface temperature $T_{\\text{eff}} \\approx 3534\\text{ K}$.</p>
"""
        },
        {
            "id": "prob-3-2",
            "title": "Atmospheric Ionization Fraction: The Saha-Boltzmann Balmer Maximum",
            "statement": "In the atmosphere of an A0V star with effective temperature $T = 9520\\text{ K}$ and electron pressure $P_e = 20.0\\text{ N m}^{-2}$ ($200\\text{ dyn cm}^{-2}$):\\n\\n(a) Calculate the ratio of singly ionized to neutral hydrogen $N_{\\text{II}}/N_{\\text{I}}$ using the Saha equation with ionization energy $\\chi = 13.60\\text{ eV}$, $g_{\\text{I}} = 2$, and $g_{\\text{II}} = 1$.\\n(b) Using the Boltzmann formula, compute the fraction of neutral hydrogen atoms in the $n=2$ excited state $N_2/N_{\\text{I}}$ ($E_1 = -13.60\\text{ eV}, E_2 = -3.40\\text{ eV}, g_1 = 2, g_2 = 8$).\\n(c) Find the total fraction of all hydrogen atoms capable of Balmer absorption: $f = \\frac{N_2}{N_{\\text{total}}} = \\left(\\frac{N_2}{N_{\\text{I}}}\\right)\\left(\\frac{N_{\\text{I}}}{N_{\\text{total}}}\\right)$.",
            "solution": """
<h4>(a) Saha Equation Calculation</h4>
<p>At $T = 9520\\text{ K}$, thermal energy is $k T = (1.3807 \\times 10^{-23}\\text{ J/K})(9520\\text{ K}) = 1.3144 \\times 10^{-19}\\text{ J} \\approx 0.8204\\text{ eV}$.</p>
<p>The Saha equation is:</p>
<div class="equation-box">
$$\\frac{N_{\\text{II}}}{N_{\\text{I}}} = \\frac{2 k T g_{\\text{II}}}{P_e g_{\\text{I}}} \\left(\\frac{2\\pi m_e k T}{h^2}\\right)^{3/2} \\exp\\left(-\\frac{\\chi}{k T}\\right)$$
</div>
<p>Evaluating the quantum volume factor:</p>
<div class="equation-box">
$$\\frac{2\\pi m_e k T}{h^2} = \\frac{2\\pi (9.1094 \\times 10^{-31}\\text{ kg})(1.3144 \\times 10^{-19}\\text{ J})}{(6.6261 \\times 10^{-34}\\text{ J s})^2} = \\frac{7.5235 \\times 10^{-49}}{4.3905 \\times 10^{-67}} \\approx 1.7136 \\times 10^{18}\\text{ m}^{-2}$$
$$\\left(\\frac{2\\pi m_e k T}{h^2}\\right)^{3/2} = (1.7136 \\times 10^{18})^{3/2} \\approx 2.2432 \\times 10^{27}\\text{ m}^{-3}$$
</div>
<p>Evaluating the prefactor with $g_{\\text{II}}/g_{\\text{I}} = 1/2$ and $P_e = 20.0\\text{ N m}^{-2}$:</p>
<div class="equation-box">
$$\\frac{2 k T}{P_e} \\frac{g_{\\text{II}}}{g_{\\text{I}}} = \\frac{2 (1.3144 \\times 10^{-19})}{20.0} \\times \\frac{1}{2} = 6.572 \\times 10^{-21}\\text{ m}^3$$
$$\\text{Prefactor} = (6.572 \\times 10^{-21}\\text{ m}^3)(2.2432 \\times 10^{27}\\text{ m}^{-3}) \\approx 1.474 \\times 10^7$$
</div>
<p>Evaluating the exponential Boltzmann ionization factor:</p>
<div class="equation-box">
$$\\frac{\\chi}{k T} = \\frac{13.60\\text{ eV}}{0.8204\\text{ eV}} \\approx 16.577 \\implies \\exp(-16.577) \\approx 6.320 \\times 10^{-8}$$
$$\\frac{N_{\\text{II}}}{N_{\\text{I}}} = 1.474 \\times 10^7 \\times 6.320 \\times 10^{-8} \\approx 0.9316$$
</div>
<p>Hydrogen is roughly half-ionized: $N_{\\text{I}} / N_{\\text{total}} = \\frac{1}{1 + N_{\\text{II}}/N_{\\text{I}}} = \\frac{1}{1 + 0.9316} = \\frac{1}{1.9316} \\approx 0.5177$ ($51.8\\%$ neutral).</p>

<h4>(b) Boltzmann Excitation Fraction</h4>
<p>For excitation from $n=1$ to $n=2$ with $\\Delta E = 10.20\\text{ eV}$, $g_1 = 2$, $g_2 = 8$:</p>
<div class="equation-box">
$$\\frac{N_2}{N_{\\text{I}}} \\approx \\frac{N_2}{N_1} = \\frac{g_2}{g_1} \\exp\\left(-\\frac{\\Delta E}{k T}\\right) = \\frac{8}{2} \\exp\\left(-\\frac{10.20\\text{ eV}}{0.8204\\text{ eV}}\\right) = 4 \\exp(-12.433) = 4 \\times (3.985 \\times 10^{-6}) \\approx 1.594 \\times 10^{-5}$$
</div>

<h4>(c) Net Balmer Absorption Fraction</h4>
<p>The total fraction of all hydrogen atoms in the state capable of Balmer absorption is:</p>
<div class="equation-box">
$$f = \\frac{N_2}{N_{\\text{total}}} = \\left(\\frac{N_2}{N_{\\text{I}}}\\right) \\left(\\frac{N_{\\text{I}}}{N_{\\text{total}}}\\right) = (1.594 \\times 10^{-5}) \\times (0.5177) \\approx 8.25 \\times 10^{-6}$$
</div>
<p>While only $\\sim 8$ in every million hydrogen atoms are in $n=2$ at any instant, because hydrogen is overwhelmingly abundant and the oscillator strength of the H$\\alpha$ line is large, this fraction produces the strongest Balmer absorption lines across the entire stellar classification spectrum!</p>
"""
        },
        {
            "id": "prob-3-3",
            "title": "Jeans Mass & Gravitational Free-Fall Collapse in Molecular Clouds",
            "statement": "A dense spherical core inside the Orion Molecular Cloud has temperature $T = 15.0\\text{ K}$ and number density $n = 2.0 \\times 10^4\\text{ cm}^{-3}$ of molecular hydrogen ($\\text{H}_2$), with mean molecular weight $\\mu = 2.30$.\\n\\n(a) Calculate the mass density $\\rho_0$ in $\\text{kg m}^{-3}$ and the isothermal sound speed $c_s$.\\n(b) Compute the Jeans length $\\lambda_J$ in parsecs and AU.\\n(c) Calculate the Jeans mass $M_J$ in solar masses ($M_\\odot$).\\n(d) Calculate the free-fall collapse time $\\tau_{\\text{ff}}$ in years.",
            "solution": """
<h4>(a) Mass Density & Sound Speed</h4>
<p>The mass density is:</p>
<div class="equation-box">
$$\\rho_0 = n \\mu m_H = (2.0 \\times 10^{10}\\text{ m}^{-3}) \\times (2.30 \\times 1.6735 \\times 10^{-27}\\text{ kg}) \\approx 7.698 \\times 10^{-17}\\text{ kg m}^{-3} = 7.70 \\times 10^{-20}\\text{ g cm}^{-3}$$
</div>
<p>The isothermal sound speed is:</p>
<div class="equation-box">
$$c_s = \\sqrt{\\frac{k T}{\\mu m_H}} = \\sqrt{\\frac{(1.3807 \\times 10^{-23}\\text{ J/K})(15.0\\text{ K})}{2.30 \\times 1.6735 \\times 10^{-27}\\text{ kg}}} = \\sqrt{\\frac{2.071 \\times 10^{-22}}{3.849 \\times 10^{-27}}} = \\sqrt{5.381 \\times 10^4} \\approx 232.0\\text{ m s}^{-1}$$
</div>

<h4>(b) Jeans Length</h4>
<p>The Jeans length is $\\lambda_J = c_s \\sqrt{\\frac{\\pi}{G \\rho_0}}$:</p>
<div class="equation-box">
$$\\lambda_J = 232.0 \\times \\sqrt{\\frac{\\pi}{(6.6743 \\times 10^{-11})(7.698 \\times 10^{-17})}} = 232.0 \\times \\sqrt{\\frac{3.14159}{5.138 \\times 10^{-27}}} = 232.0 \\times \\sqrt{6.114 \\times 10^{26}} = 232.0 \\times (2.473 \\times 10^{13}) \\approx 5.737 \\times 10^{15}\\text{ m}$$
</div>
<p>In AU ($1\\text{ AU} = 1.496 \\times 10^{11}\\text{ m}$) and parsecs ($1\\text{ pc} = 3.086 \\times 10^{16}\\text{ m}$):</p>
<div class="equation-box">
$$\\lambda_J = \\frac{5.737 \\times 10^{15}}{1.496 \\times 10^{11}} \\approx 38{,}350\\text{ AU} = \\frac{5.737 \\times 10^{15}}{3.086 \\times 10^{16}} \\approx 0.186\\text{ pc}$$
</div>

<h4>(c) Jeans Mass</h4>
<p>The mass contained within a Jeans sphere of diameter $\\lambda_J$ (radius $R_J = \\lambda_J/2$) is:</p>
<div class="equation-box">
$$M_J = \\frac{4}{3}\\pi \\left(\\frac{\\lambda_J}{2}\\right)^3 \\rho_0 = \\frac{\\pi}{6} \\lambda_J^3 \\rho_0 = \\frac{\\pi}{6} (5.737 \\times 10^{15}\\text{ m})^3 (7.698 \\times 10^{-17}\\text{ kg m}^{-3})$$
$$M_J = 0.5236 \\times (1.888 \\times 10^{47}) \\times (7.698 \\times 10^{-17}) \\approx 7.61 \\times 10^{30}\\text{ kg}$$
</div>
<p>In solar masses ($M_\\odot = 1.989 \\times 10^{30}\\text{ kg}$):</p>
<div class="equation-box">
$$M_J = \\frac{7.61 \\times 10^{30}}{1.989 \\times 10^{30}} \\approx 3.83 M_\\odot$$
</div>

<h4>(d) Free-Fall Collapse Time</h4>
<p>The free-fall time is:</p>
<div class="equation-box">
$$\\tau_{\\text{ff}} = \\sqrt{\\frac{3\\pi}{32 G \\rho_0}} = \\sqrt{\\frac{3\\pi}{32 (6.6743 \\times 10^{-11})(7.698 \\times 10^{-17})}} = \\sqrt{\\frac{9.4248}{1.644 \\times 10^{-25}}} = \\sqrt{5.733 \\times 10^{25}} \\approx 7.572 \\times 10^{12}\\text{ seconds}$$
</div>
<p>Converting to years ($1\\text{ yr} = 3.1558 \\times 10^7\\text{ s}$):</p>
<div class="equation-box">
$$\\tau_{\\text{ff}} = \\frac{7.572 \\times 10^{12}\\text{ s}}{3.1558 \\times 10^7\\text{ s/yr}} \\approx 239{,}900\\text{ years} \\approx 2.4 \\times 10^5\\text{ years}$$
</div>
<p>Any dense clump exceeding $3.8 M_\\odot$ in this cloud is gravitationally unstable and will collapse into protostellar cores in roughly $240{,}000\\text{ years}$.</p>
"""
        }
    ]
}

u4 = {
    "unitId": 4,
    "title": "Stellar Remnants: White Dwarfs, Neutron Stars & Black Holes",
    "subtitle": "Fermi Degeneracy, Chandrasekhar Limit, TOV Equation & Relativistic Geodesics",
    "icon": "🕳️",
    "summary": "This unit explores the exotic physics of stellar corpses supported not by thermal pressure, but by quantum degeneracy and general relativistic spacetime curvature. We begin by solving the Lane-Emden equation for polytropic stellar models. We formulate the thermodynamics of completely degenerate Fermi-Dirac electron gases, deriving the celebrated mass-radius relation ($R \\propto M^{-1/3}$) and the exact relativistic Chandrasekhar mass limit ($M_{\\text{Ch}} \\approx 1.44 M_\\odot$). We progress to neutron stars supported by nuclear degeneracy, deriving the general relativistic Tolman-Oppenheimer-Volkoff (TOV) hydrostatic equilibrium equation. We analyze pulsars as rotating magnetic dipole radiators, quantifying spin-down luminosities, braking indices, and characteristic ages. Finally, we explore stellar-mass black holes via the Schwarzschild metric, deriving event horizons, photon spheres, and the innermost stable circular orbit (ISCO).",
    "keyTakeaways": [
        "White dwarfs are supported by non-relativistic electron degeneracy pressure with equation of state $P \\propto \\rho^{5/3}$ ($n=3/2$ polytrope), exhibiting the counterintuitive property that more massive white dwarfs possess smaller physical radii ($R \\propto M^{-1/3}$).",
        "At high central densities, electrons become ultra-relativistic ($v \\approx c$), softening the equation of state to $P \\propto \\rho^{4/3}$ ($n=3$ polytrope), which sets an absolute ceiling on white dwarf mass: the Chandrasekhar limit $M_{\\text{Ch}} \\approx 1.44 M_\\odot$.",
        "Neutron stars collapse to nuclear densities ($\\sim 10^{14}\\text{ g cm}^{-3}$), requiring general relativistic hydrostatic equilibrium governed by the Tolman-Oppenheimer-Volkoff (TOV) equation, yielding maximum stable masses $M_{\\text{TOV}} \\sim 2.1-2.3 M_\\odot$.",
        "Pulsars are rapidly spinning, highly magnetized neutron stars ($B \\sim 10^{12}\\text{ G}$) losing rotational kinetic energy via magnetic dipole radiation at rate $\\dot{E} \\propto \\Omega^4$, with characteristic ages $\\tau_c = P / (2\\dot{P})$.",
        "Remnants exceeding the TOV limit collapse into Schwarzschild black holes bounded by an event horizon at $R_s = \\frac{2GM}{c^2}$, encircled by a photon sphere at $r = 1.5 R_s$ and an Innermost Stable Circular Orbit (ISCO) at $r = 3 R_s$ ($6GM/c^2$)."
    ],
    "sections": [
        {
            "id": "sec-4-1",
            "title": "Polytropic Stellar Models & The Lane-Emden Differential Equation",
            "content": """
<p>In many astrophysical regimes—such as completely convective stars, degenerate white dwarfs, and neutron stars—the pressure depends solely on the local density according to a power-law <strong>polytropic equation of state</strong>:</p>
<div class="equation-box">
$$P(r) = K \\rho(r)^{\\gamma} = K \\rho(r)^{1 + 1/n}$$
</div>
<p>where $K$ is the polytropic constant, $\\gamma = 1 + 1/n$ is the polytropic exponent, and $n$ is the <strong>polytropic index</strong> ($n = \\frac{1}{\\gamma - 1}$).</p>

<h4>Derivation of the Lane-Emden Equation</h4>
<p>Combine the hydrostatic equation $\\frac{dP}{dr} = -\\frac{G M(r)\\rho}{r^2}$ with mass conservation $\\frac{dM(r)}{dr} = 4\\pi r^2 \\rho$ by dividing by $\\rho$, multiplying by $r^2$, and differentiating with respect to $r$:</p>
<div class="equation-box">
$$\\frac{1}{r^2} \\frac{d}{dr}\\left(\\frac{r^2}{\\rho} \\frac{dP}{dr}\\right) = -4\\pi G \\rho$$
</div>
<p>Define dimensionless variables for density and radius anchored to the central density $\\rho_c$:</p>
<div class="equation-box">
$$\\rho(r) = \\rho_c \\theta(\\xi)^n, \\quad P(r) = P_c \\theta(\\xi)^{n+1}$$
$$r = \\alpha \\xi \\quad \\text{with characteristic radial scale } \\alpha = \\left[\\frac{(n+1) K \\rho_c^{1/n - 1}}{4\\pi G}\\right]^{1/2}$$
</div>
<p>Substituting into the combined hydrostatic equation yields the celebrated <strong>Lane-Emden equation of index $n$</strong>:</p>
<div class="equation-box">
$$\\frac{1}{\\xi^2} \\frac{d}{d\\xi}\\left(\\xi^2 \\frac{d\\theta}{d\\xi}\\right) = -\\theta^n$$
</div>
<p>subject to central boundary conditions $\\theta(0) = 1$ (since $\\rho(0) = \\rho_c$) and $\\theta'(0) = 0$ (zero gravitational force at the center).</p>

<h4>Analytical Solutions</h4>
<p>Exact closed-form analytical solutions exist for three integer indices:</p>
<ul>
  <li><strong>$n = 0$ (Uniform incompressible sphere, $\\rho = \\text{const}$):</strong>
  $$\\theta(\\xi) = 1 - \\frac{\\xi^2}{6}, \\quad \\xi_1 = \\sqrt{6} \\approx 2.449$$
  </li>
  <li><strong>$n = 1$ (Linear gas):</strong>
  $$\\theta(\\xi) = \\frac{\\sin\\xi}{\\xi}, \\quad \\xi_1 = \\pi \\approx 3.142$$
  </li>
  <li><strong>$n = 5$ (Infinitely extended sphere):</strong>
  $$\\theta(\\xi) = \\left(1 + \\frac{\\xi^2}{3}\\right)^{-1/2}, \\quad \\xi_1 = \\infty$$
  </li>
</ul>
<p>For all other indices (notably $n = 3/2$ for non-relativistic degeneracy and $n = 3$ for relativistic degeneracy), the equation is solved numerically. The surface occurs at the first zero $\\xi = \\xi_1$ where $\\theta(\\xi_1) = 0$.</p>
"""
        },
        {
            "id": "sec-4-2",
            "title": "Quantum Mechanics of Completely Degenerate Electron Gases",
            "content": """
<p>In a white dwarf, stellar matter is compressed to extreme densities ($\rho \\sim 10^5 - 10^9\\text{ g cm}^{-3}$). Under these conditions, atoms are completely pressure-ionized into bare nuclei surrounded by a sea of free electrons. The average separation between electrons becomes comparable to their quantum mechanical de Broglie wavelengths, and Fermi-Dirac quantum statistics completely dominates thermal pressure.</p>

<h4>Fermi Energy & Fermi Momentum</h4>
<p>Electrons are spin-$1/2$ fermions subject to the Pauli Exclusion Principle: each quantum phase-space cell $h^3 = (2\\pi\\hbar)^3$ accommodates at most 2 electrons (spin up and spin down). In the zero-temperature limit ($T \\to 0$, valid since $k T \\ll E_F$ even at $10^7\\text{ K}$), electrons pack the Fermi sphere up to a maximum momentum $p_F$:</p>
<div class="equation-box">
$$n_e = 2 \\int_0^{p_F} \\frac{4\\pi p^2 dp}{h^3} = \\frac{8\\pi}{3 h^3} p_F^3 = \\frac{p_F^3}{3\\pi^2 \\hbar^3}$$
$$p_F = \\hbar (3\\pi^2 n_e)^{1/3}$$
</div>
<p>For fully ionized matter with mass fraction of hydrogen $X$, helium $Y$, and metals $Z$, the electron number density is $n_e = \\frac{\\rho}{\\mu_e m_u}$, where the mean molecular weight per electron is $\\mu_e = \\frac{2}{1+X} \\approx 2.0$ for pure helium, carbon, or oxygen.</p>

<h4>1. Non-Relativistic Degeneracy Pressure ($p_F \\ll m_e c$)</h4>
<p>When electron velocities are non-relativistic ($v = p/m_e$), the pressure is computed from the momentum flux tensor $P = \\frac{1}{3}\\int_0^{p_F} p v \\, n(p) dp$:</p>
<div class="equation-box">
$$P_e = \\frac{1}{3 m_e} \\frac{8\\pi}{h^3} \\int_0^{p_F} p^4 dp = \\frac{8\\pi}{15 m_e h^3} p_F^5 = \\frac{(3\\pi^2)^{2/3} \\hbar^2}{5 m_e} n_e^{5/3}$$
$$P_e = \\frac{(3\\pi^2)^{2/3} \\hbar^2}{5 m_e (\\mu_e m_u)^{5/3}} \\rho^{5/3} = K_1 \\rho^{5/3}$$
</div>
<p>This corresponds exactly to a <strong>polytrope of index $n = 3/2$</strong> ($\\gamma = 5/3$). Crucially, $P_e$ is completely independent of temperature $T$! A white dwarf does not shrink as it radiates heat and cools.</p>

<h4>2. Ultra-Relativistic Degeneracy Pressure ($p_F \\gg m_e c$)</h4>
<p>At extreme densities ($\\rho \\gtrsim 10^6\\text{ g cm}^{-3}$), the Fermi momentum approaches and exceeds $m_e c$. Electrons move at speeds near the speed of light ($v \\approx c$):</p>
<div class="equation-box">
$$P_e = \\frac{c}{3} \\frac{8\\pi}{h^3} \\int_0^{p_F} p^3 dp = \\frac{8\\pi c}{12 h^3} p_F^4 = \\frac{(3\\pi^2)^{1/3} \\hbar c}{4} n_e^{4/3}$$
$$P_e = \\frac{(3\\pi^2)^{1/3} \\hbar c}{4 (\\mu_e m_u)^{4/3}} \\rho^{4/3} = K_2 \\rho^{4/3}$$
</div>
<p>The polytropic index shifts to <strong>$n = 3$</strong> ($\\gamma = 4/3$). The equation of state 'softens' dramatically from $\\rho^{5/3}$ to $\\rho^{4/3}$, which will destabilize the star.</p>
"""
        },
        {
            "id": "sec-4-3",
            "title": "White Dwarfs & Exact Derivation of the Chandrasekhar Mass Limit",
            "content": """
<p>In 1930, on his voyage from India to England at the age of nineteen, Subrahmanyan Chandrasekhar applied relativistic Fermi-Dirac statistics to stellar polytropes, making the revolutionary discovery that there exists an absolute upper mass limit beyond which an electron-degenerate star cannot exist.</p>

<h4>1. The Non-Relativistic Mass-Radius Relation ($n = 3/2$)</h4>
<p>For any polytrope of index $n$, the mass and radius scale with central density $\\rho_c$ as:</p>
<div class="equation-box">
$$R = \\alpha \\xi_1 \\propto K^{1/2} \\rho_c^{\\frac{1-n}{2n}}, \\quad M = 4\\pi \\alpha^3 \\rho_c \\omega_n \\propto K^{3/2} \\rho_c^{\\frac{3-n}{2n}}$$
</div>
<p>For non-relativistic degenerate electrons ($n = 3/2$):</p>
<div class="equation-box">
$$R \\propto \\rho_c^{-1/6}, \\quad M \\propto \\rho_c^{1/2} \\implies \\rho_c \\propto M^2$$
$$R \\propto (M^2)^{-1/6} = M^{-1/3}$$
</div>
<p>Substituting the physical constants for $\\mu_e = 2$:</p>
<div class="equation-box">
$$R_{\\text{WD}} \\approx 0.0126 R_\\odot \\left(\\frac{\\mu_e}{2}\\right)^{-5/3} \\left(\\frac{M}{M_\\odot}\\right)^{-1/3} \\approx 8{,}700\\text{ km} \\left(\\frac{M_\\odot}{M}\\right)^{1/3}$$
</div>
<p>More massive white dwarfs are physically smaller and denser! Adding mass compresses the star to higher densities to generate the requisite degeneracy pressure.</p>

<h4>2. Exact Derivation of the Chandrasekhar Limit ($n = 3$)</h4>
<p>As the mass $M$ increases, the radius shrinks, driving the central density $\\rho_c$ up until electrons become ultra-relativistic, transitioning the star into an $n = 3$ polytrope ($P = K_2 \\rho^{4/3}$). For $n = 3$:</p>
<div class="equation-box">
$$\\frac{3-n}{2n} = \\frac{3-3}{6} = 0 \\implies M \\propto \\rho_c^0 = \\text{independent of } \\rho_c!$$
</div>
<p>The mass of an $n=3$ polytrope is a single unique eigenvalue:</p>
<div class="equation-box">
$$M_{\\text{Ch}} = 4\\pi \\alpha^3 \\rho_c \\omega_3 = 4\\pi \\left[\\frac{(3+1) K_2}{4\\pi G}\\right]^{3/2} \\omega_3 = \\frac{\\omega_3}{\\sqrt{4\\pi}} \\left(\\frac{4 K_2}{G}\\right)^{3/2}$$
</div>
<p>From the numerical integration of the Lane-Emden equation for $n=3$, the boundary values are $\\xi_1 = 6.89685$ and $\\omega_3 = -\\xi_1^2 \\theta'(\\xi_1) = 2.01824$. Substituting $K_2 = \\frac{(3\\pi^2)^{1/3} \\hbar c}{4 (\\mu_e m_u)^{4/3}}$:</p>
<div class="equation-box">
$$M_{\\text{Ch}} = \\frac{\\omega_3}{4\\pi} \\left(\\frac{h c}{G}\\right)^{3/2} \\left(\\frac{1}{\\mu_e m_u}\\right)^2$$
</div>
<p>Inserting fundamental physical constants ($h, c, G, m_u$):</p>
<div class="equation-box">
$$M_{\\text{Ch}} \\approx \\frac{5.83}{\\mu_e^2} M_\\odot$$
</div>
<p>For carbon-oxygen white dwarfs with $\\mu_e = 2.00$:</p>
<div class="equation-box">
$$M_{\\text{Ch}} \\approx \\frac{5.83}{4.00} M_\\odot \\approx 1.44 M_\\odot$$
</div>
<p>If a white dwarf accretes matter from a binary companion pushing its mass beyond $1.44 M_\\odot$, relativistic electron degeneracy pressure is mathematically incapable of supporting it. The star either undergoes runaway thermonuclear detonation (Type Ia Supernova) or collapses into a neutron star.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 4.1: Relativistic Electron Degeneracy & Chandrasekhar Mass Limit Solver</h4>
  </div>
  <p>Vary the central density $\\rho_c$ across 6 orders of magnitude to observe the transition from non-relativistic ($P \\propto \\rho^{5/3}$) to ultra-relativistic ($P \\propto \\rho^{4/3}$) electron degeneracy, watching the stellar radius shrink and asymptotic mass stall at exactly $1.44 M_\\odot$.</p>
  <div id="astro-chandrasekhar-limit-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-4-4",
            "title": "Neutron Stars & The Relativistic Tolman-Oppenheimer-Volkoff (TOV) Equation",
            "content": """
<p>When an iron stellar core collapses beyond the Chandrasekhar limit, electrons and protons are crushed together via inverse beta decay: $p + e^- \\to n + \\nu_e$. The resulting remnant is a <strong>neutron star</strong>—a gigantic macroscopic atomic nucleus of mass $M \\sim 1.4 - 2.0 M_\\odot$ compressed into a radius of merely $R \\sim 10-12\\text{ km}$ with core densities $\\rho \\sim 3-8 \\times 10^{14}\\text{ g cm}^{-3}$.</p>

<h4>The Need for General Relativity: Compactness Parameter</h4>
<p>The gravitational compactness parameter $\\Xi$ measures the severity of spacetime curvature:</p>
<div class="equation-box">
$$\\Xi = \\frac{R_s}{R} = \\frac{2 G M}{R c^2}$$
</div>
<p>For the Earth, $\\Xi \\sim 10^{-9}$; for the Sun, $\\Xi \\sim 4 \\times 10^{-6}$. For a $1.4 M_\\odot, 11\\text{ km}$ neutron star:</p>
<div class="equation-box">
$$\\Xi = \\frac{2 (6.674 \\times 10^{-11})(2.78 \\times 10^{30})}{(11{,}000)(3 \\times 10^8)^2} \\approx \\frac{3.71 \\times 10^{20}}{9.9 \\times 10^{20}} \\approx 0.38$$
</div>
<p>Spacetime curvature is massive ($R \\approx 2.6 R_s$). Newtonian gravity fails completely, requiring Einstein's General Relativity.</p>

<h4>Derivation of the Tolman-Oppenheimer-Volkoff (TOV) Equation</h4>
<p>Starting with the spherically symmetric static Schwarzschild metric $ds^2 = -e^{2\\Phi(r)} c^2 dt^2 + e^{2\\Lambda(r)} dr^2 + r^2 d\\Omega^2$ and solving Einstein's field equations $G^\\mu_\\nu = \\frac{8\\pi G}{c^4} T^\\mu_\\nu$ with a perfect fluid stress-energy tensor $T^\\mu_\\nu = \\text{diag}(-\\rho c^2, P, P, P)$ yields the <strong>Tolman-Oppenheimer-Volkoff (TOV) equation of relativistic hydrostatic equilibrium</strong> (1939):</p>
<div class="equation-box">
$$\\frac{dP}{dr} = -\\frac{G M(r)\\rho(r)}{r^2} \\left[1 + \\frac{P(r)}{\\rho(r) c^2}\\right] \\left[1 + \\frac{4\\pi r^3 P(r)}{M(r) c^2}\\right] \\left[1 - \\frac{2 G M(r)}{r c^2}\\right]^{-1}$$
</div>
<p>Notice the three relativistic correction bracket terms:</p>
<ol>
  <li>$\\left[1 + \\frac{P}{\\rho c^2}\\right]$: In General Relativity, pressure itself possesses effective mass-energy ($E = m c^2$), contributing directly to gravitational attraction! High pressure intensifies gravity.</li>
  <li>$\\left[1 + \\frac{4\\pi r^3 P}{M(r) c^2}\\right]$: Accounts for the enclosed pressure work contributing to the total active gravitational mass.</li>
  <li>$\\left[1 - \\frac{2 G M(r)}{r c^2}\\right]^{-1}$: The metric spatial curvature correction ($e^{2\\Lambda}$), amplifying the local gravitational gradient as $r$ approaches the Schwarzschild radius.</li>
</ol>

<h4>The Tolman-Oppenheimer-Volkoff Mass Limit</h4>
<p>Because pressure self-gravitates in General Relativity, increasing the central density eventually increases inward gravitational pull faster than outward degenerate pressure. Even with the strong repulsive nuclear force (meson exchange between neutrons), there exists a rigorous upper limit for neutron stars:</p>
<div class="equation-box">
$$M_{\\text{TOV}} \\approx 2.1 - 2.3 M_\\odot$$
</div>
<p>Any core remnant exceeding $M_{\\text{TOV}}$ (such as the primary object in binary merger GW170817) cannot stabilize and collapses into a black hole.</p>
"""
        },
        {
            "id": "sec-4-5",
            "title": "Pulsars & Rotating Magnetized Dipole Radiators",
            "content": """
<p>Discovered in 1967 by Jocelyn Bell Burnell and Antony Hewish as periodic radio beeps ($P = 1.337\\text{ s}$), pulsars were identified by Thomas Gold and Franco Pacini as rapidly rotating, highly magnetized neutron stars.</p>

<h4>Conservation of Magnetic Flux & Magnetic Field Strength</h4>
<p>During core collapse, the progenitor's magnetic field is trapped within the highly conducting collapsing plasma. By Alfvén's theorem of flux freezing, total magnetic flux is conserved: $\\Phi_B = B R^2 = \\text{const}$. If a progenitor of radius $R_0 = 10^6\\text{ km}$ and field $B_0 = 100\\text{ G}$ collapses to $R = 10\\text{ km}$:</p>
<div class="equation-box">
$$B = B_0 \\left(\\frac{R_0}{R}\\right)^2 = 100\\text{ G} \\times \\left(\\frac{10^6}{10}\\right)^2 = 100 \\times 10^{10} = 10^{12}\\text{ Gauss} = 10^8\\text{ Tesla}$$
</div>
<p>Neutron stars possess the strongest magnetic fields in the cosmos (up to $10^{14}-10^{15}\\text{ G}$ in <em>magnetars</em>).</p>

<h4>Magnetic Dipole Radiation & Spin-Down Power</h4>
<p>A neutron star spinning with angular frequency $\\Omega = 2\\pi/P$ with magnetic dipole moment $\\vec{m}$ ($m = B_p R^3$) inclined at magnetic obliquity angle $\\alpha$ relative to its rotation axis emits magnetic dipole radiation into space at a rate governed by electrodynamics:</p>
<div class="equation-box">
$$\\dot{E}_{\\text{dipole}} = -\\frac{2}{3 c^3} |\\ddot{\\vec{m}}|^2 = -\\frac{2}{3 c^3} (m \\Omega^2 \\sin\\alpha)^2 = -\\frac{2 B_p^2 R^6 \\Omega^4 \\sin^2\\alpha}{3 c^3}$$
</div>
<p>This radiant power is extracted directly from the star's rotational kinetic energy $E_{\\text{rot}} = \\frac{1}{2} I \\Omega^2$ (where $I \\approx 0.4 M R^2 \\sim 10^{45}\\text{ g cm}^2$ is the moment of inertia):</p>
<div class="equation-box">
$$\\dot{E}_{\\text{rot}} = \\frac{d}{dt}\\left(\\frac{1}{2} I \\Omega^2\\right) = I \\Omega \\dot{\\Omega} = -\\frac{4\\pi^2 I \\dot{P}}{P^3}$$
</div>
<p>Equating $\\dot{E}_{\\text{rot}} = \\dot{E}_{\\text{dipole}}$:</p>
<div class="equation-box">
$$I \\Omega \\dot{\\Omega} \\propto \\Omega^4 \\implies \\dot{\\Omega} \\propto -\\Omega^n \\quad \\text{with braking index } n = 3$$
</div>

<h4>Characteristic Age & Surface Magnetic Field Determination</h4>
<p>From the observable period $P$ and its measured spin-down rate $\\dot{P} = dP/dt > 0$:</p>
<div class="equation-box">
$$\\tau_c = \\frac{P}{2\\dot{P}} \\quad (\\text{Pulsar Characteristic Age})$$
$$B_p = \\left[\\frac{3 c^3 I P \\dot{P}}{8\\pi^2 R^6 \\sin^2\\alpha}\\right]^{1/2} \\approx 3.2 \\times 10^{19} \\sqrt{P \\dot{P}} \\text{ Gauss}$$
</div>
<p>For the Crab Pulsar ($P = 0.033\\text{ s}, \\dot{P} = 4.2 \\times 10^{-13}\\text{ s/s}$), $\\tau_c \\approx 1240\\text{ years}$ (closely matching the historical supernova of 1054 CE) and $B_p \\approx 3.8 \\times 10^{12}\\text{ G}$.</p>

<div class="sim-embed-card">
  <div class="sim-header">
    <span class="sim-badge">Interactive 60-FPS Simulation</span>
    <h4>Simulation 4.2: Rotating Pulsar Lighthouse & Relativistic Magnetosphere</h4>
  </div>
  <p>Rotate the magnetized neutron star in 3D, change the magnetic inclination angle $\\alpha$ and spin period $P$, and watch the lighthouse emission cones sweep across the line of sight to generate periodic radio pulses.</p>
  <div id="astro-pulsar-lighthouse-sim" class="astro-sim-mount" style="width:100%; height:460px;"></div>
</div>
"""
        },
        {
            "id": "sec-4-6",
            "title": "Stellar Black Holes: Schwarzschild Metric, Geodesics & ISCO",
            "content": """
<p>When the mass of a collapsing stellar core exceeds the TOV limit ($M > 2.3 M_\\odot$), no known physical force can oppose gravity. The core undergoes complete gravitational collapse to a spacetime singularity, cloaked behind an <strong>event horizon</strong>.</p>

<h4>The Schwarzschild Spacetime Metric</h4>
<p>Karl Schwarzschild (1916) found the exact static, spherically symmetric vacuum solution to Einstein's Field Equations:</p>
<div class="equation-box">
$$ds^2 = -\\left(1 - \\frac{2GM}{c^2 r}\\right) c^2 dt^2 + \\left(1 - \\frac{2GM}{c^2 r}\\right)^{-1} dr^2 + r^2(d\\theta^2 + \\sin^2\\theta d\\phi^2)$$
</div>
<p>The metric coefficient $g_{00} = -(1 - R_s/r)$ vanishes and $g_{rr} = (1 - R_s/r)^{-1}$ diverges at the <strong>Schwarzschild radius</strong>:</p>
<div class="equation-box">
$$R_s = \\frac{2GM}{c^2} \\approx 2.953 \\left(\\frac{M}{M_\\odot}\\right) \\text{ km}$$
</div>
<p>For a stellar black hole of $10 M_\\odot$, $R_s \\approx 29.5\\text{ km}$.</p>

<h4>Gravitational Redshift & Time Dilation</h4>
<p>A clock at rest at coordinate radius $r$ ticks at proper time $d\\tau = \\sqrt{-g_{00}} dt = \\sqrt{1 - R_s/r} dt$. Light emitted at radius $r_e$ with frequency $\\nu_e$ is received by an observer at infinity with frequency $\\nu_\\infty$:</p>
<div class="equation-box">
$$\\frac{\\nu_\\infty}{\\nu_e} = \\sqrt{1 - \\frac{R_s}{r_e}} \\implies 1 + z = \\frac{1}{\\sqrt{1 - R_s/r_e}}$$
</div>
<p>As an infalling source reaches the event horizon ($r_e \\to R_s$), $z \\to \\infty$: emitted photons red-shift to infinite wavelength, and the object appears frozen and dimmed to blackness.</p>

<h4>Geodesics, Photon Sphere & The ISCO</h4>
<p>Particle orbits in the equatorial plane ($\\theta = \\pi/2$) obey the effective potential equation $\\frac{1}{2}\\left(\\frac{dr}{d\\tau}\\right)^2 + V_{\\text{eff}}(r) = \\frac{\\mathcal{E}^2 - c^2}{2}$:</p>
<div class="equation-box">
$$V_{\\text{eff}}(r) = -\\frac{GM}{r} + \\frac{L^2}{2 r^2} - \\frac{G M L^2}{c^2 r^3}$$
</div>
<p>Notice the general relativistic term $-\\frac{G M L^2}{c^2 r^3}$, which pulls particles inward at small radii, absent in Newtonian physics.</p>
<ul>
  <li><strong>The Photon Sphere ($r_{\\text{ph}} = 1.5 R_s = 3GM/c^2$):</strong> The radius at which photons can execute unstable circular orbits. Light emitted tangentially here circles the black hole.</li>
  <li><strong>Innermost Stable Circular Orbit (ISCO, $r_{\\text{ISCO}} = 3 R_s = 6GM/c^2$):</strong> Inside $6GM/c^2$, circular orbits of massive particles become dynamically unstable ($d^2 V_{\\text{eff}}/dr^2 < 0$). Matter in an accretion disk spirals into the horizon.</li>
</ul>

<h4>Accretion Efficiency & X-Ray Binaries</h4>
<p>The binding energy of a particle at the ISCO of a Schwarzschild black hole is:</p>
<div class="equation-box">
$$\\mathcal{E}_{\\text{ISCO}} = c^2 \\sqrt{\\frac{8}{9}} \\approx 0.9428 c^2 \\implies \\Delta E = (1 - 0.9428) m c^2 \\approx 0.0572 m c^2$$
</div>
<p>Accretion onto a non-rotating black hole converts $\\eta \\approx 5.7\\%$ of rest-mass energy into radiation (for a maximally rotating Kerr black hole, $\\eta \\approx 42.3\\%$!), dwarfing nuclear fusion ($\\eta \\approx 0.7\\%$). This immense efficiency powers Galactic X-ray binaries (Cygnus X-1) and quasars.</p>
"""
        }
    ],
    "problems": [
        {
            "id": "prob-4-1",
            "title": "White Dwarf Mass-Radius Scaling from the Lane-Emden n=3/2 Polytrope",
            "statement": "A non-relativistic carbon-oxygen white dwarf has mass $M = 0.85 M_\\odot$ and composition with $\\mu_e = 2.00$. It is modeled as a polytrope of index $n = 3/2$ with Lane-Emden boundary parameters $\\xi_1 = 3.65375$ and $\\omega_{3/2} = -\\xi_1^2 \\theta'(\\xi_1) = 2.71406$.\\n\\n(a) Compute the polytropic constant $K_1$ in SI units from electron degeneracy theory.\\n(b) Calculate the star's central density $\\rho_c$ in $\\text{kg m}^{-3}$ and $\\text{g cm}^{-3}$.\\n(c) Determine the physical radius $R$ in km and in solar radii ($R_\\odot$).\\n(d) Calculate the central pressure $P_c$ in $\\text{N m}^{-2}$.",
            "solution": """
<h4>(a) Polytropic Constant $K_1$</h4>
<p>From non-relativistic electron degeneracy:</p>
<div class="equation-box">
$$K_1 = \\frac{(3\\pi^2)^{2/3} \\hbar^2}{5 m_e (\\mu_e m_u)^{5/3}}$$
$$\\hbar = 1.05457 \\times 10^{-34}\\text{ J s}, \\quad m_e = 9.10938 \\times 10^{-31}\\text{ kg}, \\quad m_u = 1.66054 \\times 10^{-27}\\text{ kg}$$
$$(3\\pi^2)^{2/3} = (29.6088)^{2/3} \\approx 9.5707$$
$$\\mu_e m_u = 2 \\times 1.66054 \\times 10^{-27} = 3.3211 \\times 10^{-27}\\text{ kg} \\implies (\\mu_e m_u)^{5/3} \\approx 4.887 \\times 10^{-45}$$
$$K_1 = \\frac{9.5707 \\times (1.05457 \\times 10^{-34})^2}{5 \\times (9.10938 \\times 10^{-31}) \\times (4.887 \\times 10^{-45})} = \\frac{1.0644 \\times 10^{-67}}{2.2257 \\times 10^{-74}} \\approx 4.782 \\times 10^6\\text{ SI units (m}^4\\text{ s}^{-2}\\text{ kg}^{-2/3}\\text{)}$$
</div>

<h4>(b) Central Density $\\rho_c$</h4>
<p>For an $n = 3/2$ polytrope, total mass relates to central density by:</p>
<div class="equation-box">
$$M = 4\\pi \\alpha^3 \\rho_c \\omega_{3/2} = 4\\pi \\left[\\frac{2.5 K_1 \\rho_c^{-1/3}}{4\\pi G}\\right]^{3/2} \\rho_c \\omega_{3/2} = 4\\pi \\left(\\frac{2.5 K_1}{4\\pi G}\\right)^{3/2} \\omega_{3/2} \\rho_c^{1/2}$$
$$\\rho_c^{1/2} = \\frac{M}{4\\pi \\omega_{3/2}} \\left(\\frac{4\\pi G}{2.5 K_1}\\right)^{3/2}$$
</div>
<p>With $M = 0.85 M_\\odot = 0.85 \\times 1.989 \\times 10^{30}\\text{ kg} = 1.69065 \\times 10^{30}\\text{ kg}$:</p>
<div class="equation-box">
$$\\frac{4\\pi G}{2.5 K_1} = \\frac{4\\pi (6.6743 \\times 10^{-11})}{2.5 \\times 4.782 \\times 10^6} = \\frac{8.3872 \\times 10^{-10}}{1.1955 \\times 10^7} \\approx 7.0157 \\times 10^{-17}$$
$$(7.0157 \\times 10^{-17})^{3/2} \\approx 5.8763 \\times 10^{-25}$$
$$\\rho_c^{1/2} = \\frac{1.69065 \\times 10^{30}}{4\\pi \\times 2.71406} \\times 5.8763 \\times 10^{-25} = (4.957 \\times 10^{28}) \\times (5.8763 \\times 10^{-25}) \\approx 29{,}129$$
$$\\rho_c = (29{,}129)^2 \\approx 8.485 \\times 10^8\\text{ kg m}^{-3} = 8.485 \\times 10^5\\text{ g cm}^{-3}$$
</div>

<h4>(c) Physical Stellar Radius</h4>
<p>The scale length $\\alpha$ is:</p>
<div class="equation-box">
$$\\alpha = \\left[\\frac{2.5 K_1 \\rho_c^{-1/3}}{4\\pi G}\\right]^{1/2} = \\left[\\frac{2.5 \\times 4.782 \\times 10^6 \\times (8.485 \\times 10^8)^{-1/3}}{4\\pi \\times 6.6743 \\times 10^{-11}}\\right]^{1/2}$$
$$(8.485 \\times 10^8)^{-1/3} = \\frac{1}{946.8} \\approx 1.0562 \\times 10^{-3}$$
$$\\alpha = \\left[\\frac{1.2627 \\times 10^4}{8.3872 \\times 10^{-10}}\\right]^{1/2} = (1.5055 \\times 10^{13})^{1/2} \\approx 3.880 \\times 10^6\\text{ m} = 3880\\text{ km}$$
$$R = \\alpha \\xi_1 = 3880\\text{ km} \\times 3.65375 \\approx 14{,}177\\text{ km}$$
$$\\frac{R}{R_\\odot} = \\frac{1.418 \\times 10^7\\text{ m}}{6.957 \\times 10^8\\text{ m}} \\approx 0.0204 R_\\odot$$
</div>

<h4>(d) Central Pressure</h4>
<p>From the polytropic equation of state:</p>
<div class="equation-box">
$$P_c = K_1 \\rho_c^{5/3} = (4.782 \\times 10^6) \\times (8.485 \\times 10^8)^{5/3} = (4.782 \\times 10^6) \\times (7.625 \\times 10^{14}) \\approx 3.65 \\times 10^{21}\\text{ N m}^{-2}$$
</div>
<p>The central pressure exceeds 36 billion atmospheres, supported exclusively by non-relativistic degenerate electron Fermi quantum momentum.</p>
"""
        },
        {
            "id": "prob-4-2",
            "title": "Neutron Star Centrifugal Breakup Limit & Pulsar Spin-Down Energetics",
            "statement": "A newborn neutron star has mass $M = 1.40 M_\\odot = 2.785 \\times 10^{30}\\text{ kg}$ and radius $R = 11.5\\text{ km}$.\\n\\n(a) Derive the centrifugal mass-shedding breakup period $P_{\\text{break}}$ and maximum spin frequency $\\nu_{\\text{max}}$.\\n(b) The pulsar is observed with period $P = 33.39\\text{ ms}$ and spin-down rate $\\dot{P} = 4.21 \\times 10^{-13}\\text{ s s}^{-1}$. Calculate the spin-down luminosity $\\dot{E}$ assuming moment of inertia $I = 1.20 \\times 10^{38}\\text{ kg m}^2$.\\n(c) Compute the pulsar's characteristic spin-down age $\\tau_c$ in years.\\n(d) Calculate the dipole magnetic field strength $B_p$ at the magnetic poles.",
            "solution": """
<h4>(a) Centrifugal Breakup Period</h4>
<p>At the equator, centrifugal acceleration $\\Omega^2 R$ equals surface gravity $\\frac{GM}{R^2}$:</p>
<div class="equation-box">
$$\\Omega_{\\text{break}}^2 R = \\frac{G M}{R^2} \\implies \\Omega_{\\text{break}} = \\sqrt{\\frac{G M}{R^3}}$$
$$\\Omega_{\\text{break}} = \\sqrt{\\frac{(6.6743 \\times 10^{-11})(2.785 \\times 10^{30})}{(11{,}500)^3}} = \\sqrt{\\frac{1.8587 \\times 10^{20}}{1.5209 \\times 10^{12}}} = \\sqrt{1.222 \\times 10^8} \\approx 11{,}055\\text{ rad s}^{-1}$$
$$\\nu_{\\text{max}} = \\frac{\\Omega_{\\text{break}}}{2\\pi} = \\frac{11{,}055}{6.28318} \\approx 1759\\text{ Hz}$$
$$P_{\\text{break}} = \\frac{1}{\\nu_{\\text{max}}} \\approx 0.568\\text{ ms}$$
</div>
<p>A neutron star can rotate up to $\\approx 1760$ times per second before centrifugal force tears it apart.</p>

<h4>(b) Spin-Down Luminosity</h4>
<p>With $P = 0.03339\\text{ s}$, the angular frequency is $\\Omega = \\frac{2\\pi}{0.03339} \\approx 188.18\\text{ rad s}^{-1}$.</p>
<div class="equation-box">
$$\\dot{E} = -4\\pi^2 I \\frac{\\dot{P}}{P^3} = -4\\pi^2 (1.20 \\times 10^{38}\\text{ kg m}^2) \\frac{4.21 \\times 10^{-13}\\text{ s/s}}{(0.03339\\text{ s})^3}$$
$$P^3 = (0.03339)^3 \\approx 3.7226 \\times 10^{-5}\\text{ s}^3$$
$$\\dot{E} = \\frac{39.478 \\times 1.20 \\times 10^{38} \\times 4.21 \\times 10^{-13}}{3.7226 \\times 10^{-5}} = \\frac{1.9945 \\times 10^{27}}{3.7226 \\times 10^{-5}} \\approx 5.36 \\times 10^{31}\\text{ Watts}$$
</div>
<p>In solar luminosities ($L_\\odot = 3.828 \\times 10^{26}\\text{ W}$):</p>
<div class="equation-box">
$$\\dot{E} = \\frac{5.36 \\times 10^{31}\\text{ W}}{3.828 \\times 10^{26}\\text{ W}} \\approx 140{,}000 L_\\odot$$
</div>
<p>The rotational braking power exceeds $10^5$ times the entire radiant power of the Sun, energizing the surrounding synchrotron nebula.</p>

<h4>(c) Characteristic Age</h4>
<p>The spin-down age is:</p>
<div class="equation-box">
$$\\tau_c = \\frac{P}{2\\dot{P}} = \\frac{0.03339\\text{ s}}{2 \\times (4.21 \\times 10^{-13}\\text{ s/s})} = \\frac{0.03339}{8.42 \\times 10^{-13}} \\approx 3.965 \\times 10^{10}\\text{ seconds}$$
$$\\tau_c = \\frac{3.965 \\times 10^{10}\\text{ s}}{3.15576 \\times 10^7\\text{ s/yr}} \\approx 1256\\text{ years}$$
</div>

<h4>(d) Polar Magnetic Field Strength</h4>
<p>From the dipole formula $B_p = 3.2 \\times 10^{19} \\sqrt{P \\dot{P}}\\text{ Gauss}$:</p>
<div class="equation-box">
$$P \\dot{P} = 0.03339 \\times (4.21 \\times 10^{-13}) = 1.4057 \\times 10^{-14}$$
$$\\sqrt{P \\dot{P}} = \\sqrt{1.4057 \\times 10^{-14}} \\approx 1.1856 \\times 10^{-7}$$
$$B_p = 3.2 \\times 10^{19} \\times (1.1856 \\times 10^{-7}) \\approx 3.79 \\times 10^{12}\\text{ Gauss} = 3.79 \\times 10^8\\text{ Tesla}$$
</div>
<p>The surface magnetic field is nearly four trillion Gauss.</p>
"""
        },
        {
            "id": "prob-4-3",
            "title": "ISCO Orbital Dynamics & Gravitational Redshift Around a Stellar Black Hole",
            "statement": "An X-ray binary contains a stellar black hole of mass $M = 12.0 M_\\odot$ accreting gas from an OB supergiant companion.\\n\\n(a) Compute the Schwarzschild radius $R_s$ and photon sphere radius $r_{\\text{ph}}$ in kilometers.\\n(b) Determine the radius of the Innermost Stable Circular Orbit (ISCO) $r_{\\text{ISCO}}$ and the orbital frequency $\\nu_{\\text{ISCO}}$ in Hz observed at infinity.\\n(c) Calculate the gravitational redshift factor $z_g$ for an iron K$\\alpha$ X-ray line (rest energy $E_0 = 6.40\\text{ keV}$) emitted from stationary gas at $r = 1.20 R_s$.\\n(d) Compute the energy efficiency $\\eta$ of accretion onto this Schwarzschild black hole.",
            "solution": """
<h4>(a) Schwarzschild Radius & Photon Sphere</h4>
<p>With $M = 12.0 M_\\odot = 12.0 \\times 1.989 \\times 10^{30}\\text{ kg} = 2.3868 \\times 10^{31}\\text{ kg}$:</p>
<div class="equation-box">
$$R_s = \\frac{2 G M}{c^2} = \\frac{2 (6.6743 \\times 10^{-11})(2.3868 \\times 10^{31})}{(2.9979 \\times 10^8)^2} = \\frac{3.186 \\times 10^{21}}{8.9875 \\times 10^{16}} \\approx 35.45\\text{ km}$$
</div>
<p>The photon sphere radius is:</p>
<div class="equation-box">
$$r_{\\text{ph}} = 1.5 R_s = 1.5 \\times 35.45\\text{ km} \\approx 53.18\\text{ km}$$
</div>

<h4>(b) ISCO Radius & Orbital Frequency</h4>
<p>The ISCO occurs at $r_{\\text{ISCO}} = 3 R_s$:</p>
<div class="equation-box">
$$r_{\\text{ISCO}} = 3 \\times 35.45\\text{ km} = 106.35\\text{ km} = 1.0635 \\times 10^5\\text{ m}$$
</div>
<p>In General Relativity, the coordinate angular orbital frequency of a circular equatorial geodesic around a Schwarzschild black hole is identical to Kepler's formula: $\\Omega = \\sqrt{\\frac{GM}{r^3}}$.</p>
<div class="equation-box">
$$\\Omega_{\\text{ISCO}} = \\sqrt{\\frac{(6.6743 \\times 10^{-11})(2.3868 \\times 10^{31})}{(1.0635 \\times 10^5)^3}} = \\sqrt{\\frac{1.593 \\times 10^{21}}{1.203 \\times 10^{15}}} = \\sqrt{1.324 \\times 10^6} \\approx 1150.7\\text{ rad s}^{-1}$$
$$\\nu_{\\text{ISCO}} = \\frac{\\Omega_{\\text{ISCO}}}{2\\pi} = \\frac{1150.7}{6.28318} \\approx 183.1\\text{ Hz}$$
</div>
<p>Accretion matter at the inner edge whips around the black hole 183 times per second, generating characteristic Quasi-Periodic Oscillations (QPOs) in observed X-ray flux.</p>

<h4>(c) Gravitational Redshift of Iron K$\\alpha$ Line</h4>
<p>At $r = 1.20 R_s$, the redshift factor is:</p>
<div class="equation-box">
$$1 + z_g = \\left(1 - \\frac{R_s}{r}\\right)^{-1/2} = \\left(1 - \\frac{1}{1.20}\\right)^{-1/2} = \\left(1 - 0.8333\\right)^{-1/2} = (0.1667)^{-1/2} = \\sqrt{6.0} \\approx 2.4495$$
$$z_g = 1.4495$$
</div>
<p>The observed energy of the Iron K$\\alpha$ photon at infinity is:</p>
<div class="equation-box">
$$E_{\\text{obs}} = \\frac{E_0}{1 + z_g} = \\frac{6.40\\text{ keV}}{2.4495} \\approx 2.61\\text{ keV}$$
</div>
<p>The line is strongly shifted from $6.40\\text{ keV}$ down into a broad, relativistic asymmetric profile centered near $2.61\\text{ keV}$.</p>

<h4>(d) Accretion Radiative Efficiency</h4>
<p>The specific energy of a particle at the ISCO is $\\mathcal{E}_{\\text{ISCO}} = c^2 \\sqrt{8/9} = \\frac{2\\sqrt{2}}{3} c^2 \\approx 0.94281 c^2$.</p>
<div class="equation-box">
$$\\eta = 1 - \\frac{\\mathcal{E}_{\\text{ISCO}}}{c^2} = 1 - 0.94281 = 0.05719 \\approx 5.72\\%$$
</div>
<p>The gravitational accretion onto a non-rotating stellar black hole releases $5.72\\%$ of the accreted rest mass as intense thermal X-ray radiation, over 8 times more efficient than hydrogen nuclear fusion ($0.71\\%$).</p>
"""
        }
    ]
}

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/astro_u3.json', 'w') as f:
    json.dump(u3, f, indent=2)
print("astro_u3.json written successfully")

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/astro_u4.json', 'w') as f:
    json.dump(u4, f, indent=2)
print("astro_u4.json written successfully")
