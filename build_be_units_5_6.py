import json

unit5 = {
    "id": "unit-5",
    "number": 5,
    "title": "Feedback in Amplifiers & Waveform Oscillators",
    "description": "Rigorous foundation of feedback theory across all four topological variants (voltage-series, voltage-shunt, current-series, current-shunt); Barkhausen criterion; comprehensive mathematical derivations of LC (Colpitts, Hartley), RC (Phase-Shift, Wien Bridge), and high-Q Quartz Crystal oscillators; complete university exam problems.",
    "sections": [
        {
            "id": "u5-sec1",
            "title": "Principles of Negative Feedback & Four Topological Variants",
            "content": """<h4>1. Fundamental Feedback Equation & Closed-Loop Desensitivity</h4>
<p>In a feedback amplifier, a fraction $\\beta$ of the output signal is sampled and combined with the external input source $x_s$. For <strong>negative (degenerative) feedback</strong>, the feedback signal is subtracted in phase from the source signal:</p>
<div class="math-display">
$$x_i = x_s - x_f = x_s - \\beta x_o$$
</div>
<p>The open-loop amplifier provides gain $A = x_o / x_i$. Substituting into the transfer relation:</p>
<div class="math-display">
$$x_o = A (x_s - \\beta x_o) \\implies x_o (1 + A\\beta) = A x_s$$
</div>
<p>Thus, the <strong>closed-loop gain $A_f$</strong> is:</p>
<div class="math-display">
$$A_f = \\frac{x_o}{x_s} = \\frac{A}{1 + A\\beta}$$
</div>
<p>The term $D = 1 + A\\beta$ is called the <strong>desensitivity factor</strong> or <strong>amount of feedback</strong> ($F = 20 \\log_{10}|1 + A\\beta|\\,\\text{dB}$). When loop gain $A\\beta \\gg 1$:</p>
<div class="math-display">
$$A_f \\approx \\frac{A}{A\\beta} = \\frac{1}{\\beta}$$
</div>
<p>The closed-loop gain becomes virtually independent of internal transistor parameters, device aging, temperature fluctuations, and supply voltages, governed solely by stable passive feedback resistors.</p>

<h4>2. Advantages of Negative Feedback</h4>
<ul>
<li><strong>Gain Stabilization:</strong> Differentiating $A_f = A / (1 + A\\beta)$:
<div class="math-display">
$$\\frac{d A_f}{A_f} = \\frac{1}{1 + A\\beta} \\left( \\frac{dA}{A} \\right)$$
</div>
Internal open-loop variations are attenuated by the factor $(1 + A\\beta)$.</li>
<li><strong>Bandwidth Extension:</strong> High-frequency cutoff extends while low-frequency cutoff drops:
<div class="math-display">
$$f_{H,f} = f_H (1 + A\\beta), \\quad f_{L,f} = \\frac{f_L}{1 + A\\beta} \\implies BW_f \\approx BW (1 + A\\beta)$$
</div>
The Gain-Bandwidth product remains constant ($A_f \\cdot BW_f = A \\cdot BW$).</li>
<li><strong>Harmonic Distortion Reduction:</strong> Nonlinear harmonic distortion generated within the amplifier is reduced to $D_f = D / (1 + A\\beta)$.</li>
<li><strong>Noise Reduction:</strong> Internally generated spurious noise $N$ is reduced to $N_f = N / (1 + A\\beta)$.</li>
</ul>

<h4>3. The Four Feedback Topologies</h4>
<p>Feedback networks are classified by how the output is sampled (voltage or current) and how feedback is injected at the input (series voltage or shunt current):</p>
<table class="data-table" style="width:100%; border-collapse:collapse; margin:16px 0;">
<thead>
<tr style="background:rgba(255,255,255,0.05); text-align:left;">
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Topology</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Output Sample</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Input Mix</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Input Impedance $Z_{in,f}$</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Output Impedance $Z_{out,f}$</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Voltage-Series (Series-Shunt)</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Voltage (Parallel)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Series (Voltage)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$Z_{in} (1 + A\\beta)$ (Increased)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$Z_{out} / (1 + A\\beta)$ (Decreased)</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Voltage-Shunt (Shunt-Shunt)</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Voltage (Parallel)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Shunt (Current)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$Z_{in} / (1 + A\\beta)$ (Decreased)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$Z_{out} / (1 + A\\beta)$ (Decreased)</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Current-Series (Series-Series)</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Current (Series)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Series (Voltage)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$Z_{in} (1 + A\\beta)$ (Increased)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$Z_{out} (1 + A\\beta)$ (Increased)</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Current-Shunt (Shunt-Series)</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Current (Series)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Shunt (Current)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$Z_{in} / (1 + A\\beta)$ (Decreased)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$Z_{out} (1 + A\\beta)$ (Increased)</td>
</tr>
</tbody>
</table>"""
        },
        {
            "id": "u5-sec2",
            "title": "Barkhausen Criterion & LC Tuned Oscillators (Colpitts & Hartley)",
            "content": """<h4>1. Barkhausen Criterion for Sustained Oscillations</h4>
<p>An electronic oscillator generates continuous sinusoidal AC waveforms without any external AC input signal, converting DC supply energy into AC oscillation. In a feedback loop where feedback is positive:</p>
<div class="math-display">
$$A_f = \\frac{A}{1 - A\\beta}$$
</div>
<p>To sustain steady, unattenuated oscillations at a specific frequency $\\omega_0$, the <strong>Barkhausen Criteria</strong> must be fulfilled:
<ol>
<li><strong>Magnitude Condition:</strong> The loop gain magnitude must equal unity:
<div class="math-display">
$$|A \\beta| = 1$$
</div>
(To initiate oscillation from thermal noise, $|A\\beta| > 1$ initially; nonlinear amplitude limiting stabilizes $|A\\beta| = 1$ in steady state).</li>
<li><strong>Phase Condition:</strong> The total net phase shift around the closed loop must be an integer multiple of $360^\\circ$ (or $0^\\circ$):
<div class="math-display">
$$\\angle (A \\beta) = 0^\\circ \\quad \\text{or} \\quad 2\\pi n \\quad (n = 0, 1, 2, \\dots)$$
</div>
If the active amplifier introduces a $180^\\circ$ phase shift (such as a Common Emitter BJT), the feedback network must introduce an additional $180^\\circ$ phase shift at $\\omega_0$.</li>
</ol>
</p>

<h4>2. Hartley LC Oscillator</h4>
<p>The Hartley oscillator employs a tapped inductive voltage divider ($L_1, L_2$) in parallel with a single tuning capacitor $C$. If mutual inductance between the coil segments is $M$, the effective inductance is $L_{eq} = L_1 + L_2 + 2M$.</p>
<p>The natural resonant frequency of oscillation is:</p>
<div class="math-display">
$$f_0 = \\frac{1}{2\\pi \\sqrt{L_{eq} C}} = \\frac{1}{2\\pi \\sqrt{(L_1 + L_2 + 2M) C}}$$
</div>
<p>The feedback fraction is determined by the inductive tap ratio:</p>
<div class="math-display">
$$\\beta = \\frac{L_1 + M}{L_2 + M}$$
</div>
<p>For sustained oscillations, the minimum required transistor current gain is:</p>
<div class="math-display">
$$h_{fe} \\ge \\frac{L_1 + M}{L_2 + M} \\approx \\frac{L_1}{L_2}$$
</div>

<h4>3. Colpitts LC Oscillator</h4>
<p>The Colpitts oscillator replaces the tapped inductor with a capacitive voltage divider ($C_1, C_2$) in parallel with a single continuous inductor $L$. The series combination of $C_1$ and $C_2$ forms the equivalent tank capacitance:</p>
<div class="math-display">
$$C_{eq} = \\frac{C_1 C_2}{C_1 + C_2}$$
</div>
<p>The oscillation frequency is derived from tank resonance:</p>
<div class="math-display">
$$f_0 = \\frac{1}{2\\pi \\sqrt{L C_{eq}}} = \\frac{1}{2\\pi \\sqrt{L \\left(\\frac{C_1 C_2}{C_1 + C_2}\\right)}}$$
</div>
<p>The feedback voltage fed to the base is tapped across $C_1$, while output is taken across $C_2$. The feedback factor magnitude is:</p>
<div class="math-display">
$$\\beta = \\frac{C_2}{C_1}$$
</div>
<p>To satisfy $|A\\beta| \\ge 1$, the minimum amplifier gain condition is:</p>
<div class="math-display">
$$A_v \\ge \\frac{C_1}{C_2} \\implies h_{fe} \\ge \\frac{C_1}{C_2}$$
</div>
<p>Because capacitors can be fabricated with higher precision and less stray magnetic coupling than tapped inductors, the Colpitts oscillator offers superior frequency stability in high-frequency RF communications.</p>"""
        },
        {
            "id": "u5-sec3",
            "title": "RC Audio Oscillators: RC Phase-Shift & Wien Bridge",
            "content": """<h4>1. RC Phase-Shift Oscillator</h4>
<p>At audio frequencies ($20\\,\\text{Hz} - 200\\,\\text{kHz}$), inductors become excessively bulky, heavy, and lossy. RC feedback networks are preferred.</p>
<p>A CE transistor amplifier introduces a $180^\\circ$ phase shift. To achieve the requisite $360^\\circ$ total loop phase shift, a cascade of three identical $RC$ high-pass filter sections is inserted in the feedback loop. Each section contributes a $60^\\circ$ phase advance at the oscillation frequency $\\omega_0$.</p>
<p>Applying mesh analysis to the three-stage ladder network:</p>
<div class="math-display">
$$\\beta(s) = \\frac{v_f}{v_o} = \\frac{s^3 R^3 C^3}{s^3 R^3 C^3 + 6 s^2 R^2 C^2 + 5 s R C + 1}$$
</div>
<p>Setting $s = j\\omega$ and requiring the imaginary part of the denominator to vanish for zero net phase difference ($\angle \\beta = -180^\circ$ relative to inverting input):</p>
<div class="math-display">
$$-(j\\omega)^3 R^3 C^3 + 5 j\\omega R C = 0 \\implies -\\omega^2 R^2 C^2 + 5 = 0 \\quad (\\text{ignoring } \\omega = 0)$$
</div>
<p>Taking loading into account across the ladder yields:</p>
<div class="math-display">
$$1 - 6 \\omega_0^2 R^2 C^2 = 0 \\implies f_0 = \\frac{1}{2\\pi R C \\sqrt{6}}$$
</div>
<p>Evaluating the attenuation of the network at this frequency:</p>
<div class="math-display">
$$\\beta(j\\omega_0) = -\\frac{1}{29}$$
</div>
<p>To satisfy Barkhausen's criterion $|A\\beta| \\ge 1$:</p>
<div class="math-display">
$$|A_v| \\ge 29$$
</div>
<p>The amplifier must maintain a voltage gain of at least $29$ to overcome the passive $RC$ ladder attenuation and sustain audio oscillations.</p>

<h4>2. Wien Bridge Oscillator</h4>
<p>The Wien Bridge oscillator is the premier laboratory standard for pure low-distortion audio sinusoidal generation. It employs a four-arm AC bridge consisting of:
<ul>
<li>A series $R-C$ branch in series with a parallel $R-C$ branch (the frequency-selective lead-lag arm).</li>
<li>A resistive divider branch ($R_1, R_2$) that sets the closed-loop non-inverting gain.</li>
</ul>
</p>
<p>The transfer function of the lead-lag network is:</p>
<div class="math-display">
$$\\beta(s) = \\frac{Z_p}{Z_s + Z_p} = \\frac{ \\frac{R}{1 + sRC} }{ \\left( R + \\frac{1}{sRC} \\right) + \\frac{R}{1 + sRC} } = \\frac{sRC}{s^2 R^2 C^2 + 3 sRC + 1}$$
</div>
<p>Substituting $s = j\\omega$:</p>
<div class="math-display">
$$\\beta(j\\omega) = \\frac{j\\omega RC}{(1 - \\omega^2 R^2 C^2) + 3 j\\omega RC}$$
</div>
<p>For the phase shift to be strictly $0^\\circ$ (real $\\beta$), the imaginary term in the denominator must equal zero:</p>
<div class="math-display">
$$1 - \\omega_0^2 R^2 C^2 = 0 \\implies f_0 = \\frac{1}{2\\pi R C}$$
</div>
<p>At resonance $\\omega = \\omega_0$:</p>
<div class="math-display">
$$\\beta(j\\omega_0) = \\frac{j}{3j} = \\frac{1}{3}$$
</div>
<p>Because the network introduces zero phase shift, a non-inverting operational amplifier or two-stage CE amplifier is used. To meet $|A\\beta| = 1$:</p>
<div class="math-display">
$$A_v = 1 + \\frac{R_f}{R_1} \\ge 3 \\implies R_f \\ge 2 R_1$$
</div>
<p>Automatic gain control using a tungsten filament bulb, thermistor, or JFET channel in the negative feedback arm stabilizes the amplitude and suppresses harmonic distortion below $0.01\\%$.</p>"""
        },
        {
            "id": "u5-sec4",
            "title": "Quartz Crystal Oscillators: Piezoelectricity, Equivalent Circuit & Q-Factor",
            "content": """<h4>1. Piezoelectric Effect in Natural and Synthetic Quartz</h4>
<p>Quartz ($\text{SiO}_2$) exhibits the <strong>direct piezoelectric effect</strong>: applying mechanical stress or compressive force across specific crystallographic axes produces electric polarization and charges on opposite faces. Conversely, by the <strong>inverse piezoelectric effect</strong>, applying an alternating voltage creates mechanical vibrations and acoustic standing waves within the quartz plate.</p>
<p>When the frequency of the applied AC voltage matches the mechanical resonant frequency of the wafer (determined by thickness $t$, cut angle like AT-cut, and acoustic velocity $v_a$):</p>
<div class="math-display">
$$f_0 = \\frac{v_a}{2 t}$$
</div>
<p>The crystal vibrates with extreme mechanical amplitude and exhibits electrical resonance with unmatched frequency stability.</p>

<h4>2. Electrical Equivalent Circuit of a Crystal</h4>
<p>Electrically, a mounted quartz crystal is represented by the Butterworth-Van Dyke (BVD) model:
<ul>
<li><strong>$L$ (Motional Inductance):</strong> Represents the vibrating mechanical mass/inertia of the quartz wafer (very large: hundreds of millihenries to tens of henries).</li>
<li><strong>$C_s$ (Motional Capacitance):</strong> Represents the mechanical compliance/elasticity of the crystal (very small: femtofarads to picofarads, $\\sim 0.01\\text{ to }0.1\\,\\text{pF}$).</li>
<li><strong>$R$ (Motional Resistance):</strong> Represents internal mechanical friction and acoustic losses (small: $10\\,\\Omega \\text{ to } 100\\,\\Omega$).</li>
<li><strong>$C_p$ (Parallel Electrostatic Capacitance):</strong> Represents the physical capacitance formed by the metal mounting electrodes sandwiching the dielectric quartz slab (typically $3\\text{ to }8\\,\\text{pF}$, where $C_p \\gg C_s$).</li>
</ul>
</p>

<h4>3. Series and Parallel Resonant Frequencies</h4>
<p>Because the crystal contains both series and parallel reactive branches, it possesses two closely spaced resonant frequencies:
<ol>
<li><strong>Series Resonant Frequency ($f_s$):</strong> Occurs when the motional branch impedance drops to minimum (pure resistance $R$):
<div class="math-display">
$$f_s = \\frac{1}{2\\pi \\sqrt{L C_s}}$$
</div>
At $f_s$, the crystal exhibits very low series impedance, operating as a series bandpass filter.</li>
<li><strong>Parallel (Anti-resonant) Frequency ($f_p$):</strong> Occurs when the net inductive reactance of the motional branch resonates with parallel electrostatic capacitance $C_p$:
<div class="math-display">
$$C_{total} = \\frac{C_s C_p}{C_s + C_p}$$
</div>
<div class="math-display">
$$f_p = \\frac{1}{2\\pi \\sqrt{L C_{total}}} = f_s \\sqrt{1 + \\frac{C_s}{C_p}} \\approx f_s \\left( 1 + \\frac{C_s}{2 C_p} \\right)$$
</div>
Between $f_s$ and $f_p$, the crystal reactance is strictly inductive ($X_L > X_C$), enabling it to replace inductors in Pierce or Colpitts oscillator circuits.</li>
</ol>
</p>

<h4>4. Quality Factor $Q$ and Unsurpassed Frequency Stability</h4>
<p>The figure of merit of a resonator is its <strong>Quality Factor $Q$</strong>:</p>
<div class="math-display">
$$Q = \\frac{\\omega_s L}{R} = \\frac{1}{R} \\sqrt{\\frac{L}{C_s}}$$
</div>
<p>While traditional LC resonant tanks achieve $Q \\approx 50 \\text{ to } 200$, quartz crystals achieve $Q = 10,000 \\text{ to } 1,000,000$ because motional inductance $L$ is colossal while resistance $R$ is tiny. This gigantic $Q$-factor makes the phase-frequency slope $d\\phi/df$ extraordinarily steep, ensuring clock frequency drift is kept below $1\\text{ part per million (ppm)}$ per year in digital microprocessors and telecommunications transmitters.</p>"""
        }
    ],
    "problems": [
        {
            "id": "u5-prob1",
            "title": "Negative Feedback Gain Desensitivity & Bandwidth Extension",
            "statement": "An open-loop amplifier has a midband voltage gain of A = 2000 \\pm 150 (a 7.5% variation due to transistor manufacturing tolerances) and a high-frequency cutoff of f_H = 50\\,\\text{kHz}. A negative feedback network with feedback factor \\beta = 0.02 is incorporated. Calculate: (a) The nominal closed-loop gain A_f, (b) The percentage variation in closed-loop gain \\Delta A_f / A_f, (c) The new high-frequency cutoff f_{H,f}, and (d) The closed-loop gain in decibels.",
            "solution": """<p><strong>Step 1: Calculate Closed-Loop Gain $A_f$</strong></p>
<div class="math-display">
$$1 + A\\beta = 1 + (2000 \\times 0.02) = 1 + 40 = 41$$
</div>
<div class="math-display">
$$A_f = \\frac{A}{1 + A\\beta} = \\frac{2000}{41} \\approx 48.78$$
</div>

<p><strong>Step 2: Calculate Percentage Variation in Closed-Loop Gain</strong></p>
<p>Using the desensitivity relation:</p>
<div class="math-display">
$$\\frac{\\Delta A_f}{A_f} = \\frac{1}{1 + A\\beta} \\left( \\frac{\\Delta A}{A} \\right) = \\frac{1}{41} \\times 7.5\\% = \\frac{7.5\\%}{41} \\approx 0.183\\%$$
</div>
<p>The variation is stabilized by a factor of 41, dropping from $\\pm 7.5\\%$ to under $\\pm 0.19\\%$.</p>

<p><strong>Step 3: Calculate New High-Frequency Cutoff $f_{H,f}$</strong></p>
<div class="math-display">
$$f_{H,f} = f_H (1 + A\\beta) = 50\\,\\text{kHz} \\times 41 = 2050\\,\\text{kHz} = 2.05\\,\\text{MHz}$$
</div>
<p>The bandwidth has expanded more than 40-fold from $50\\,\\text{kHz}$ to $2.05\\,\\text{MHz}$.</p>

<p><strong>Step 4: Calculate Closed-Loop Gain in Decibels</strong></p>
<div class="math-display">
$$A_f(\\text{dB}) = 20 \\log_{10}(48.78) \\approx 20 \\times 1.6882 = 33.76\\,\\text{dB}$$
</div>"""
        },
        {
            "id": "u5-prob2",
            "title": "Colpitts Oscillator Frequency & Feedback Factor Analysis",
            "statement": "A transistorized Colpitts oscillator operates with tank capacitors C_1 = 0.001\\,\\mu\\text{F}$ and C_2 = 0.01\\,\\mu\\text{F}$, and an inductor L = 15\\,\\mu\\text{H}$. Calculate: (a) The equivalent tank capacitance C_{eq}, (b) The oscillation frequency f_0, (c) The feedback factor \\beta, and (d) The minimum transistor voltage gain A_v required to sustain continuous oscillation.",
            "solution": """<p><strong>Step 1: Calculate Equivalent Capacitance $C_{eq}$</strong></p>
<p>Converting to nanofarads: $C_1 = 1\\,\\text{nF}$, $C_2 = 10\\,\\text{nF}$:</p>
<div class="math-display">
$$C_{eq} = \\frac{C_1 C_2}{C_1 + C_2} = \\frac{1 \\times 10}{1 + 10} = \\frac{10}{11}\\,\\text{nF} \\approx 0.9091\\,\\text{nF} = 9.091 \\times 10^{-10}\\,\\text{F}$$
</div>

<p><strong>Step 2: Calculate Oscillation Frequency $f_0$</strong></p>
<div class="math-display">
$$f_0 = \\frac{1}{2\\pi \\sqrt{L C_{eq}}} = \\frac{1}{2\\pi \\sqrt{(15 \\times 10^{-6}\\,\\text{H}) \\times (9.091 \\times 10^{-10}\\,\\text{F})}}$$
</div>
<div class="math-display">
$$L C_{eq} = 1.3636 \\times 10^{-14}\\,\\text{s}^2 \\implies \\sqrt{L C_{eq}} = 1.1677 \\times 10^{-7}\\,\\text{s}$$
</div>
<div class="math-display">
$$f_0 = \\frac{1}{2\\pi \\times 1.1677 \\times 10^{-7}} = \\frac{1}{7.337 \\times 10^{-7}} \\approx 1.363 \\times 10^6\\,\\text{Hz} = 1.363\\,\\text{MHz}$$
</div>

<p><strong>Step 3: Calculate Feedback Factor $\\beta$ and Minimum Gain $A_v$</strong></p>
<div class="math-display">
$$\\beta = \\frac{C_1}{C_2} = \\frac{1\\,\\text{nF}}{10\\,\\text{nF}} = 0.1$$
</div>
<p>To satisfy $|A\\beta| \\ge 1$:</p>
<div class="math-display">
$$|A_v| \\ge \\frac{1}{\\beta} = \\frac{C_2}{C_1} = \\frac{10}{1} = 10$$
</div>
<p>The amplifier must provide a voltage gain of at least $10$ to overcome capacitive attenuation.</p>"""
        },
        {
            "id": "u5-prob3",
            "title": "Wien Bridge Audio Oscillator Design for Variable Audio Range",
            "statement": "Design a Wien Bridge oscillator using an operational amplifier to generate a variable audio sine wave from f_{min} = 100\\,\\text{Hz} to f_{max} = 10\\,\\text{kHz}$. A dual-ganged variable capacitor with range C = 100\\,\\text{pF} to 1000\\,\\text{pF} is used. If feedback resistor R_1 = 10\\,\\text{k}\\Omega: (a) Determine the required resistor values R for the lead-lag network across two switched frequency bands, (b) Calculate the minimum value of feedback resistor R_f to ensure oscillation, and (c) Explain the role of back-to-back zener diodes across R_f.",
            "solution": """<p><strong>Step 1: Calculate Resistance $R$ for the High-Frequency Band ($1\\,\\text{kHz} - 10\\,\\text{kHz}$)</strong></p>
<p>At $f_{max} = 10\\,\\text{kHz}$ with minimum capacitance $C_{min} = 100\\,\\text{pF}$:</p>
<div class="math-display">
$$R = \\frac{1}{2\\pi f_{max} C_{min}} = \\frac{1}{2\\pi \\times 10^4 \\times 100 \\times 10^{-12}} = \\frac{1}{2\\pi \\times 10^{-6}} = \\frac{10^6}{6.283} \\approx 159.15\\,\\text{k}\\Omega$$
</div>

<p><strong>Step 2: Calculate Resistance for the Low-Frequency Band ($100\\,\\text{Hz} - 1\\,\\text{kHz}$)</strong></p>
<p>At $f_{min} = 100\\,\\text{Hz}$ with maximum capacitance $C_{max} = 1000\\,\\text{pF} = 1\\,\\text{nF}$:</p>
<div class="math-display">
$$R_{low} = \\frac{1}{2\\pi f C} = \\frac{1}{2\\pi \\times 100 \\times 10^{-9}} \\approx 1.591\\,\\text{M}\\Omega$$
</div>

<p><strong>Step 3: Calculate Minimum Feedback Resistor $R_f$</strong></p>
<p>For a non-inverting op-amp Wien bridge oscillator, gain must be $A_v = 1 + R_f / R_1 \\ge 3$:</p>
<div class="math-display">
$$\\frac{R_f}{R_1} \\ge 2 \\implies R_f \\ge 2 \\times 10\\,\\text{k}\\Omega = 20\\,\\text{k}\\Omega$$
</div>

<p><strong>Step 4: Function of Zener Amplitude Limiter</strong></p>
<p>To initiate oscillation from startup noise, $R_f$ is chosen slightly larger than $20\\,\\text{k}\\Omega$ (e.g., $22\\,\\text{k}\\Omega$, giving $A_v = 3.2 > 3$). Back-to-back zener diodes placed in parallel with a portion of $R_f$ turn on when output amplitude exceeds the zener breakdown voltage, dynamically shunting $R_f$ down until the average loop gain settles at exactly $|A\\beta| = 1.000$, ensuring zero waveform clipping and ultra-low THD.</p>"""
        }
    ]
}

unit6 = {
    "id": "unit-6",
    "number": 6,
    "title": "Modulation, Demodulation & Superheterodyne Radio Communication",
    "description": "Comprehensive mathematical theory of wireless telecommunications: baseband transmission constraints and antenna dimensions; full spectrum, power, and efficiency derivations for Amplitude Modulation (AM); diode envelope detection; Frequency Modulation (FM) and Carson's rule; complete architectural engineering of the Superheterodyne Radio Receiver.",
    "sections": [
        {
            "id": "u6-sec1",
            "title": "Need for Modulation & Baseband Transmission Constraints",
            "content": """<h4>1. Physical Limitations of Direct Baseband Transmission</h4>
<p>In telecommunications, information signals (speech: $300\\,\\text{Hz} - 3.4\\,\\text{kHz}$; high-fidelity audio: $20\\,\\text{Hz} - 20\\,\\text{kHz}$; video: $0 - 5\\,\\text{MHz}$) are low-frequency electrical signals collectively termed <strong>baseband signals</strong>. Directly transmitting these signals electromagnetically over free space is practically impossible due to fundamental physical laws:
<ol>
<li><strong>Antenna Dimensions:</strong> For efficient radiation of electromagnetic energy without severe impedance reflection, an antenna must have physical dimensions comparable to at least a quarter wavelength $(\\lambda / 4)$ of the transmitted wave. For an audio wave at $f = 15\\,\\text{kHz}$:
<div class="math-display">
$$\\lambda = \\frac{c}{f} = \\frac{3 \\times 10^8\\,\\text{m/s}}{15 \\times 10^3\\,\\text{s}^{-1}} = 20,000\\,\\text{m} = 20\\,\\text{km}$$
</div>
<div class="math-display">
$$\\frac{\\lambda}{4} = \\frac{20\\,\\text{km}}{4} = 5\\,\\text{km} \\quad (\\text{a 5-kilometer tall antenna is mechanically impossible})$$
</div>
By modulating onto a high-frequency carrier (e.g., $f_c = 100\\,\\text{MHz}$), $\\lambda = 3\\,\\text{m}$ and $\\lambda / 4 = 75\\,\\text{cm}$, which is easily fabricated on portable handheld devices.</li>
<li><strong>Radiated Power:</strong> The power radiated by a linear antenna of length $l$ scales inversely with the fourth power of wavelength:
<div class="math-display">
$$P_{rad} \\propto \\left( \\frac{l}{\\lambda} \\right)^2 \\propto l^2 f^2$$
</div>
Low frequencies radiate virtually zero power into the surrounding ether.</li>
<li><strong>Signal Multiplexing:</strong> If all radio stations broadcast unmodulated audio in the $20\\,\\text{Hz} - 20\\,\\text{kHz}$ band, all signals would overlap simultaneously, creating an unintelligible din. Modulation shifts each signal to a unique carrier frequency band (Frequency Division Multiplexing - FDM).</li>
</ol>
</p>"""
        },
        {
            "id": "u6-sec2",
            "title": "Amplitude Modulation (AM): Spectrum, Power Distribution & Efficiency",
            "content": """<h4>1. Time-Domain Representation and Modulation Index</h4>
<p>In Amplitude Modulation (AM), the instantaneous amplitude of a high-frequency sinusoidal carrier $v_c(t) = V_c \\cos(\\omega_c t)$ is varied in direct linear proportion to the instantaneous value of the modulating message signal $v_m(t) = V_m \\cos(\\omega_m t)$:</p>
<div class="math-display">
$$v_{AM}(t) = [V_c + v_m(t)] \\cos(\\omega_c t) = [V_c + V_m \\cos(\\omega_m t)] \\cos(\\omega_c t)$$
</div>
<p>Factoring out carrier amplitude $V_c$:</p>
<div class="math-display">
$$v_{AM}(t) = V_c [1 + m_a \\cos(\\omega_m t)] \\cos(\\omega_c t)$$
</div>
<p>where the <strong>Modulation Index $m_a$</strong> is:</p>
<div class="math-display">
$$m_a = \\frac{V_m}{V_c} = \\frac{V_{max} - V_{min}}{V_{max} + V_{min}}$$
</div>
<ul>
<li><strong>Under-modulation ($m_a < 1$):</strong> Carrier envelope never reaches zero; signal is cleanly recovered by simple diode envelope detectors.</li>
<li><strong>Critical modulation ($m_a = 1$):</strong> Envelope touches zero at troughs without clipping. Maximum unclipped transmission efficiency.</li>
<li><strong>Over-modulation ($m_a > 1$):</strong> Envelope crosses zero and inverts phase, causing severe harmonic envelope distortion and adjacent-channel splatter.</li>
</ul>

<h4>2. Frequency Spectrum & Transmission Bandwidth</h4>
<p>Expanding $v_{AM}(t)$ trigonometrically using $\\cos A \\cos B = \\frac{1}{2}[\\cos(A+B) + \\cos(A-B)]$:</p>
<div class="math-display">
$$v_{AM}(t) = V_c \\cos(\\omega_c t) + \\frac{m_a V_c}{2} \\cos((\\omega_c + \\omega_m) t) + \\frac{m_a V_c}{2} \\cos((\\omega_c - \\omega_m) t)$$
</div>
<p>The AM signal consists of exactly three distinct spectral components:
<ol>
<li><strong>Carrier Component:</strong> Frequency $f_c$, peak amplitude $V_c$.</li>
<li><strong>Upper Sideband (USB):</strong> Frequency $f_c + f_m$, peak amplitude $m_a V_c / 2$.</li>
<li><strong>Lower Sideband (LSB):</strong> Frequency $f_c - f_m$, peak amplitude $m_a V_c / 2$.</li>
</ol>
</p>
<p>The transmission bandwidth required for double-sideband full-carrier AM is:</p>
<div class="math-display">
$$BW = f_{USB} - f_{LSB} = (f_c + f_m) - (f_c - f_m) = 2 f_m$$
</div>

<h4>3. Power Derivation and Transmission Efficiency</h4>
<p>Total average power $P_t$ delivered to an antenna resistance $R$ is the sum of powers in each spectral component:</p>
<div class="math-display">
$$P_c = \\frac{V_c^2 / 2}{R} = \\frac{V_c^2}{2 R}$$
</div>
<div class="math-display">
$$P_{USB} = P_{LSB} = \\frac{(m_a V_c / 2)^2 / 2}{R} = \\frac{m_a^2}{4} \\left( \\frac{V_c^2}{2 R} \\right) = \\frac{m_a^2}{4} P_c$$
</div>
<div class="math-display">
$$P_{SB} = P_{USB} + P_{LSB} = \\frac{m_a^2}{2} P_c$$
</div>
<div class="math-display">
$$P_t = P_c + P_{SB} = P_c \\left( 1 + \\frac{m_a^2}{2} \\right)$$
</div>
<p>The <strong>Transmission Efficiency $\\eta$</strong> is the ratio of useful information power (sideband power) to total transmitted power:</p>
<div class="math-display">
$$\\eta = \\frac{P_{SB}}{P_t} = \\frac{\\frac{m_a^2}{2} P_c}{P_c (1 + \\frac{m_a^2}{2})} = \\frac{m_a^2}{2 + m_a^2}$$
</div>
<p>At maximum 100% modulation ($m_a = 1$):</p>
<div class="math-display">
$$\\eta_{max} = \\frac{1^2}{2 + 1^2} = \\frac{1}{3} \\approx 33.33\\%$$
</div>
<p>At least $66.7\\%$ of total broadcast power is permanently consumed by the unmodulated carrier, which transmits zero actual message information but enables low-cost diode detection at receivers.</p>"""
        },
        {
            "id": "u6-sec3",
            "title": "AM Demodulation (Diode Envelope Detector) & Frequency Modulation (FM)",
            "content": """<h4>1. Diode Envelope Detector and Distortion Limits</h4>
<p>An envelope detector comprises a silicon diode in series with a parallel $RC$ filter load. On positive carrier peaks, the diode conducts and charges capacitor $C$ to peak envelope voltage. When carrier voltage drops, the diode becomes reverse-biased, and $C$ discharges through $R$.</p>
<p>To follow the audio modulation envelope faithfully without carrier ripple:
<ol>
<li>$RC \\gg 1/f_c$ (Capacitor discharges slowly between carrier RF cycles, filtering RF ripple).</li>
<li>$RC \\le \\frac{1}{\\omega_m} \\frac{\\sqrt{1 - m_a^2}}{m_a}$ (To prevent <strong>Diagonal Peak Clipping</strong>). If $RC$ is too large, the capacitor voltage cannot decay as fast as the modulation envelope, clipping the audio waveform.</li>
</ol>
</p>

<h4>2. Frequency Modulation (FM): Theory and Carson's Bandwidth Rule</h4>
<p>In Frequency Modulation, the instantaneous frequency $f_i(t)$ of the carrier varies linearly with message voltage $v_m(t)$ while amplitude $V_c$ remains constant:</p>
<div class="math-display">
$$f_i(t) = f_c + k_f v_m(t) = f_c + \\Delta f \\cos(\\omega_m t)$$
</div>
<p>where $\\Delta f = k_f V_m$ is the <strong>Peak Frequency Deviation</strong>.</p>
<p>The <strong>FM Modulation Index $\\beta$</strong> is:</p>
<div class="math-display">
$$\\beta = \\frac{\\Delta f}{f_m}$$
</div>
<p>In time domain, the FM wave is expressed using Bessel functions of the first kind $J_n(\\beta)$:</p>
<div class="math-display">
$$v_{FM}(t) = V_c \\sum_{n=-\\infty}^{\\infty} J_n(\\beta) \\cos((\\omega_c + n \\omega_m) t)$$
</div>
<p>Theoretically, FM contains infinite sideband pairs. However, sidebands with $|n| > (\\beta + 1)$ have negligible amplitude (< 1%). The total occupied bandwidth is given by <strong>Carson's Bandwidth Rule</strong>:</p>
<div class="math-display">
$$BW_{FM} \\approx 2 (\\Delta f + f_m) = 2 f_m (1 + \\beta)$$
</div>
<p>For standard commercial FM broadcast ($\Delta f = 75\\,\\text{kHz}$, $f_{m,max} = 15\\,\\text{kHz}$):</p>
<div class="math-display">
$$\\beta = \\frac{75}{15} = 5 \\implies BW_{FM} = 2 (75 + 15) = 180\\,\\text{kHz}$$
</div>
<p>Adding a $20\\,\\text{kHz}$ guard band establishes the standard $200\\,\\text{kHz}$ channel allocation per FM broadcast station.</p>"""
        },
        {
            "id": "u6-sec4",
            "title": "Superheterodyne Radio Receiver Architecture & Image Frequency",
            "content": """<h4>1. Architecture of the Superheterodyne Receiver</h4>
<p>Direct tuned radio frequency (TRF) receivers suffer from two fatal flaws: bandwidth varies across the tuning dial ($BW = f_0 / Q$), and multiple cascading tuned circuits cannot track simultaneously without instability. Edwin Armstrong solved this by inventing the <strong>Superheterodyne Receiver</strong>, which downconverts all incoming RF carriers to a fixed <strong>Intermediate Frequency (IF)</strong>.</p>
<p>The functional block stages are:
<ol>
<li><strong>RF Amplifier:</strong> Provides low-noise amplification, improves receiver sensitivity, and provides pre-selection to reject image frequencies.</li>
<li><strong>Local Oscillator (LO):</strong> Generates an unmodulated RF sine wave at frequency $f_{LO}$. Standard designs use <em>high-side (supradyne) injection</em>: $f_{LO} = f_s + f_{IF}$.</li>
<li><strong>Mixer (Frequency Converter):</strong> Multiplies the incoming signal $f_s$ and local oscillator $f_{LO}$, producing sum and difference frequencies: $f_{LO} \\pm f_s$.</li>
<li><strong>IF Amplifier:</strong> Highly selective, high-gain tuned amplifier permanently aligned to the fixed Intermediate Frequency ($f_{IF} = 455\\,\\text{kHz}$ for AM; $f_{IF} = 10.7\\,\\text{MHz}$ for FM). All adjacent-channel selectivity and main voltage gain are provided here.</li>
<li><strong>Demodulator / Detector:</strong> Diode envelope detector (AM) or ratio detector / PLL (FM) recovering the baseband audio.</li>
<li><strong>Audio Power Amplifier:</strong> Drives low-impedance speakers.</li>
<li><strong>Automatic Gain Control (AGC):</strong> Feeds rectified DC voltage back to the RF and IF stages, maintaining constant audio output volume regardless of incoming antenna signal strength variations.</li>
</ol>
</p>

<h4>2. Image Frequency ($f_{img}$) and Image Rejection Ratio (IRR)</h4>
<p>Because the mixer responds to the absolute difference $|f_{LO} - f_{signal}| = f_{IF}$, an unwanted signal at the <strong>Image Frequency $f_{img}$</strong> will also mix with $f_{LO}$ to produce the exact same IF:</p>
<div class="math-display">
$$f_{img} - f_{LO} = f_{IF} \\implies f_{img} = f_{LO} + f_{IF} = (f_s + f_{IF}) + f_{IF} = f_s + 2 f_{IF}$$
</div>
<p>Once the image frequency enters the mixer, the IF amplifier cannot distinguish it from the desired station, causing severe simultaneous heterodyne whistle and crosstalk.</p>
<p>Image rejection must therefore be performed entirely by the RF pre-selection filter <em>before</em> the mixer. The <strong>Image Rejection Ratio (IRR)</strong> is:</p>
<div class="math-display">
$$\\text{IRR} = \\sqrt{1 + Q^2 \\rho^2}$$
</div>
<p>where $Q$ is the quality factor of the tuned RF input circuit, and $\\rho$ is the fractional frequency separation:</p>
<div class="math-display">
$$\\rho = \\frac{f_{img}}{f_s} - \\frac{f_s}{f_{img}}$$
</div>
<p>In decibels, $\\text{IRR}(\\text{dB}) = 20 \\log_{10}(\\text{IRR})$. High IF choices (e.g. 10.7 MHz) push the image frequency far away, making it easy for simple RF front-ends to eliminate image interference completely.</p>"""
        }
    ],
    "problems": [
        {
            "id": "u6-prob1",
            "title": "AM Transmitter Power, Spectrum & Efficiency Calculation",
            "statement": "An AM broadcast transmitter radiates a total power of P_t = 11.8\\,\\text{kW}$ when modulated by a single sinusoidal audio tone to a depth of 60% ($m_a = 0.6$). The unmodulated carrier frequency is 1000 kHz, and the audio tone is 5 kHz. Calculate: (a) The unmodulated carrier power P_c, (b) The power in each sideband P_{USB} and P_{LSB}, (c) The transmission efficiency \\eta, (d) The spectral frequencies present in the output, and (e) The new total power radiated if the modulation index is increased to 90% ($m_a = 0.9$).",
            "solution": """<p><strong>Step 1: Calculate Unmodulated Carrier Power $P_c$</strong></p>
<p>Using the AM total power relation:</p>
<div class="math-display">
$$P_t = P_c \\left( 1 + \\frac{m_a^2}{2} \\right)$$
</div>
<div class="math-display">
$$1 + \\frac{m_a^2}{2} = 1 + \\frac{0.6^2}{2} = 1 + \\frac{0.36}{2} = 1.18$$
</div>
<div class="math-display">
$$P_c = \\frac{P_t}{1.18} = \\frac{11.8\\,\\text{kW}}{1.18} = 10.0\\,\\text{kW}$$
</div>

<p><strong>Step 2: Calculate Power in Sidebands</strong></p>
<div class="math-display">
$$P_{total,SB} = P_t - P_c = 11.8\\,\\text{kW} - 10.0\\,\\text{kW} = 1.8\\,\\text{kW}$$
</div>
<div class="math-display">
$$P_{USB} = P_{LSB} = \\frac{P_{total,SB}}{2} = \\frac{1.8\\,\\text{kW}}{2} = 0.9\\,\\text{kW} = 900\\,\\text{W}$$
</div>

<p><strong>Step 3: Calculate Transmission Efficiency $\\eta$</strong></p>
<div class="math-display">
$$\\eta = \\frac{P_{total,SB}}{P_t} \\times 100\\% = \\frac{1.8\\,\\text{kW}}{11.8\\,\\text{kW}} \\times 100\\% \\approx 15.25\\%$$
</div>

<p><strong>Step 4: Spectral Frequencies Present</strong></p>
<div class="math-display">
$$f_c = 1000\\,\\text{kHz}$$
</div>
<div class="math-display">
$$f_{USB} = f_c + f_m = 1000\\,\\text{kHz} + 5\\,\\text{kHz} = 1005\\,\\text{kHz}$$
</div>
<div class="math-display">
$$f_{LSB} = f_c - f_m = 1000\\,\\text{kHz} - 5\\,\\text{kHz} = 995\\,\\text{kHz}$$
</div>
<div class="math-display">
$$BW = 2 f_m = 10\\,\\text{kHz}$$
</div>

<p><strong>Step 5: Total Radiated Power at $m_a = 0.9$</strong></p>
<div class="math-display">
$$P_t' = P_c \\left( 1 + \\frac{m_a^2}{2} \\right) = 10.0\\,\\text{kW} \\times \\left( 1 + \\frac{0.9^2}{2} \\right) = 10.0 \\times (1 + 0.405) = 14.05\\,\\text{kW}$$
</div>"""
        },
        {
            "id": "u6-prob2",
            "title": "FM Signal Analysis & Carson's Rule Bandwidth Calculation",
            "statement": "A commercial FM signal is given by the mathematical expression: v(t) = 12 \\cos\\left( 2\\pi \\times 10^8 t + 6 \\sin(2\\pi \\times 1.25 \\times 10^4 t) \\right)\\,\\text{V}$. Determine: (a) The unmodulated carrier frequency f_c, (b) The modulating audio frequency f_m, (c) The modulation index \\beta, (d) The peak frequency deviation \\Delta f, (e) The occupied transmission bandwidth using Carson's Rule, and (f) The total average power dissipated in a 50 \\Omega antenna load.",
            "solution": """<p><strong>Step 1: Identify Carrier and Modulating Frequencies</strong></p>
<p>Comparing with canonical FM equation $v(t) = V_c \\cos(\\omega_c t + \\beta \\sin(\\omega_m t))$:</p>
<div class="math-display">
$$\\omega_c = 2\\pi \\times 10^8\\,\\text{rad/s} \\implies f_c = 10^8\\,\\text{Hz} = 100\\,\\text{MHz}$$
</div>
<div class="math-display">
$$\\omega_m = 2\\pi \\times 1.25 \\times 10^4\\,\\text{rad/s} \\implies f_m = 1.25 \\times 10^4\\,\\text{Hz} = 12.5\\,\\text{kHz}$$
</div>

<p><strong>Step 2: Determine Modulation Index $\\beta$ and Frequency Deviation $\\Delta f$</strong></p>
<div class="math-display">
$$\\beta = 6$$
</div>
<div class="math-display">
$$\\beta = \\frac{\\Delta f}{f_m} \\implies \\Delta f = \\beta \\cdot f_m = 6 \\times 12.5\\,\\text{kHz} = 75\\,\\text{kHz}$$
</div>

<p><strong>Step 3: Calculate Bandwidth via Carson's Rule</strong></p>
<div class="math-display">
$$BW = 2 (\\Delta f + f_m) = 2 (75\\,\\text{kHz} + 12.5\\,\\text{kHz}) = 2 \\times 87.5\\,\\text{kHz} = 175\\,\\text{kHz}$$
</div>

<p><strong>Step 4: Calculate Total Transmitted Power into $50\\,\\Omega$ Load</strong></p>
<p>Since FM amplitude is strictly constant ($V_c = 12\\,\\text{V}$), total power is unaffected by modulation:</p>
<div class="math-display">
$$P = \\frac{V_c^2}{2 R_L} = \\frac{(12\\,\\text{V})^2}{2 \\times 50\\,\\Omega} = \\frac{144}{100} = 1.44\\,\\text{W}$$
</div>"""
        },
        {
            "id": "u6-prob3",
            "title": "Superheterodyne Receiver Tuning Range & Image Rejection Analysis",
            "statement": "A standard AM broadcast superheterodyne receiver tunes across the medium wave band from f_{s,min} = 535\\,\\text{kHz}$ to f_{s,max} = 1605\\,\\text{kHz}$ with an Intermediate Frequency of f_{IF} = 455\\,\\text{kHz}$. (a) Calculate the local oscillator tuning frequency range using high-side injection, (b) Find the image frequency when the receiver is tuned to 1000 kHz, (c) If the RF pre-selector input stage has a quality factor Q = 80 at 1000 kHz, calculate the Image Rejection Ratio (IRR) both as a numerical ratio and in decibels.",
            "solution": """<p><strong>Step 1: Calculate Local Oscillator Tuning Range</strong></p>
<p>With high-side injection ($f_{LO} = f_s + f_{IF}$):</p>
<div class="math-display">
$$f_{LO,min} = 535\\,\\text{kHz} + 455\\,\\text{kHz} = 990\\,\\text{kHz}$$
</div>
<div class="math-display">
$$f_{LO,max} = 1605\\,\\text{kHz} + 455\\,\\text{kHz} = 2060\\,\\text{kHz}$$
</div>
<p>Tuning ratio: $2060 / 990 \\approx 2.08:1$. If low-side injection had been used, the range would be $80\\,\\text{kHz}$ to $1150\\,\\text{kHz}$ (a $14.4:1$ ratio), requiring an impractically large variable capacitor tuning ratio of $(14.4)^2 \\approx 207:1$. High-side injection requires only $(2.08)^2 \\approx 4.33:1$ capacitance range.</p>

<p><strong>Step 2: Calculate Image Frequency for $f_s = 1000\\,\\text{kHz}$</strong></p>
<div class="math-display">
$$f_{img} = f_s + 2 f_{IF} = 1000\\,\\text{kHz} + 2(455\\,\\text{kHz}) = 1000 + 910 = 1910\\,\\text{kHz}$$
</div>

<p><strong>Step 3: Calculate Image Rejection Ratio (IRR)</strong></p>
<p>Calculate fractional separation parameter $\\rho$:</p>
<div class="math-display">
$$\\rho = \\frac{f_{img}}{f_s} - \\frac{f_s}{f_{img}} = \\frac{1910}{1000} - \\frac{1000}{1910} = 1.91 - 0.5236 = 1.3864$$
</div>
<p>With $Q = 80$:</p>
<div class="math-display">
$$Q \\rho = 80 \\times 1.3864 \\approx 110.91$$
</div>
<div class="math-display">
$$\\text{IRR} = \\sqrt{1 + (Q \\rho)^2} = \\sqrt{1 + (110.91)^2} \\approx 110.91$$
</div>
<p>In decibels:</p>
<div class="math-display">
$$\\text{IRR}(\\text{dB}) = 20 \\log_{10}(110.91) \\approx 20 \\times 2.0449 = 40.90\\,\\text{dB}$$
</div>
<p>The RF pre-selector suppresses the image frequency by nearly $41\\,\\text{dB}$ ($111$ times in voltage) prior to the mixer.</p>"""
        }
    ]
}

with open("be_u5.json", "w") as f:
    json.dump(unit5, f, indent=2)

with open("be_u6.json", "w") as f:
    json.dump(unit6, f, indent=2)

print("be_u5.json and be_u6.json generated successfully!")
