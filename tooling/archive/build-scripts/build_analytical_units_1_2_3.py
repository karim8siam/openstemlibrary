# -*- coding: utf-8 -*-
"""
build_analytical_units_1_2_3.py
Builds Units 1, 2, and 3 for Analytical Chemistry (#46):
- Unit 1: Errors, Accuracy, Precision & Statistical Treatment of Analytical Data
- Unit 2: Sampling Theory, Representative Population & Sample Preparation
- Unit 3: Group Separation & Precipitation Phenomena: Gravimetric Foundations
Strictly Zero Course Numbers or Marks. All math in raw strings r\"\"\"...\"\"\".
"""

def get_units_1_2_3():
    units = [
        # =====================================================================
        # UNIT 1
        # =====================================================================
        {
            "id": "unit-1-errors-statistical-treatment",
            "unitNumber": 1,
            "title": "Unit 1: Errors in Analysis, Accuracy, Precision & Statistical Data Treatment",
            "leadSummary": "Exhaustive mathematical and physical treatise on quantitative measurement uncertainties, determinate systematic errors versus stochastic random noise, Gaussian normal distributions, Student's t confidence intervals, propagation of error in multi-step chemical protocols, hypothesis significance testing (t-test, F-test, Grubbs, Dixon Q-test), and linear calibration figures of merit.",
            "simulations": ["sim_chem_error_gaussian_statistics"],
            "sections": [
                {
                    "id": "sec-1-1",
                    "secNumber": "1.1",
                    "title": "Foundations of Quantitative Analytical Data: Absolute & Relative Error Classifications",
                    "content": r"""Quantitative chemical analysis seeks to determine the numerical concentration, mass fraction, or absolute abundance of one or more target chemical species (analytes) within complex real-world matrices. Every physical measurement, however, is fundamentally limited by experimental imperfecitons, instrumental drift, reagent impurities, and human observational thresholds. Consequently, an analytical result is meaningless unless accompanied by an objective, statistically defensible measure of its reliability and experimental uncertainty.

### The True Value and Error Metrics
Let $x_i$ denote an individual experimental replicate measurement and $x_t$ (or $\mu$) represent the true, unperturbed value of the measured physical quantity. In practice, the true value is an idealized concept accessible only through universally certified reference materials (CRMs) established by international metrological institutes such as the National Institute of Standards and Technology (NIST) or the International Bureau of Weights and Measures (BIPM).

#### 1. Absolute Error
The absolute error $E_{\text{abs}}$ represents the net numerical discrepancy between the observed replicate $x_i$ (or the sample arithmetic mean $\bar{x}$) and the accepted true value $x_t$:
$$E_{\text{abs}} = x_i - x_t \quad \text{or} \quad E_{\text{abs}} = \bar{x} - x_t$$
The absolute error retains the identical physical dimensions and units as the measured parameter (e.g., $\text{mg}\cdot\text{L}^{-1}$, $\text{mol}\cdot\text{kg}^{-1}$, or absorbance units $A$). Note that $E_{\text{abs}}$ is an inherently signed quantity: a positive sign indicates a positive bias (overestimation), whereas a negative sign indicates a negative bias (underestimation).

#### 2. Relative Error
To compare the quality and analytical rigor of determinations operating across disparate orders of magnitude, the absolute error must be normalized against the true value to yield the dimensionless relative error $E_{\text{rel}}$:
$$E_{\text{rel}} = \frac{x_i - x_t}{x_t} = \frac{E_{\text{abs}}}{x_t}$$
Relative error is frequently expressed on a percentage basis ($\% E_{\text{rel}}$) or in parts-per-thousand ($\text{ppt}$):
$$\% E_{\text{rel}} = \left(\frac{x_i - x_t}{x_t}\right) \times 100\%$$
$$E_{\text{rel (ppt)}} = \left(\frac{x_i - x_t}{x_t}\right) \times 1000\,\text{ppt}$$

| Metric | Mathematical Formalism | Units | Analytical Significance |
| :--- | :--- | :--- | :--- |
| **Absolute Error** | $E_{\text{abs}} = x_i - x_t$ | Same as measurement | Indicates physical offset magnitude |
| **Relative Error (%)** | $\% E_{\text{rel}} = \frac{x_i - x_t}{x_t} \times 100\%$ | Dimensionless (%) | Scales accuracy across micro/macro regimes |
| **Parts-per-thousand (ppt)** | $E_{\text{rel}} \times 1000$ | Dimensionless (ppt) | High-precision volumetric titrimetry benchmark |
| **Relative Error (ppm)** | $E_{\text{rel}} \times 10^6$ | Dimensionless (ppm) | Trace mass spectrometry & isotopic metrology |

### Accuracy Versus Precision: The Foundational Dichotomy
A rigorous distinction between **accuracy** and **precision** is the bedrock of chemical metrology:
1. **Accuracy**: Defines the closeness of agreement between the experimental arithmetic mean $\bar{x}$ of a series of replicate measurements and the true reference value $x_t$. Accuracy reflects the total elimination or suppression of systematic directional bias.
2. **Precision**: Defines the degree of mutual agreement or mutual repeatability among independent replicate observations obtained under stipulated experimental conditions. Precision reflects the magnitude of random indeterminate scatter around the sample central tendency, entirely independent of the location of the true value.

A method may possess exceptional precision (tight clustering of replicate values with relative standard deviation $< 0.1\%$) while suffering from catastrophic inaccuracy (e.g., an uncalibrated analytical balance with a $5.0\text{ mg}$ positive tare zero offset). Conversely, an imprecise procedure may yield an arithmetic mean that fortuitously coincides with the true value due to symmetric stochastic cancellation.""",
                    "simulations": ["sim_chem_error_gaussian_statistics"]
                },
                {
                    "id": "sec-1-2",
                    "secNumber": "1.2",
                    "title": "Classification of Errors: Determinate (Systematic) vs Indeterminate (Random) Errors",
                    "content": r"""Experimental uncertainties in chemical measurements arise from fundamentally disparate physical, chemical, and operational mechanisms. Classical analytical theory classifies errors into two distinct categories: **determinate (systematic)** errors and **indeterminate (random)** errors.

### Determinate (Systematic) Errors
Determinate errors possess a definite, identifiable physical or chemical cause. They are reproducible, non-random, and introduce a persistent unidirectional bias into the measurement system, displacing the experimental sample mean $\bar{x}$ away from the true reference value $\mu$.

```
                        ┌─────────────────────────────────────────┐
                        │      Determinate (Systematic) Errors    │
                        └────────────────────┬────────────────────┘
                                             │
         ┌───────────────────────────────────┼───────────────────────────────────┐
         ▼                                   ▼                                   ▼
┌─────────────────┐                 ┌─────────────────┐                 ┌─────────────────┐
│  Instrumental   │                 │    Operative    │                 │    Methodic     │
│     Errors      │                 │ (Personal) Err  │                 │     Errors      │
├─────────────────┤                 ├─────────────────┤                 ├─────────────────┤
│ • Uncalibrated  │                 │ • Parallax      │                 │ • Incomplete    │
│   glassware     │                 │   viewing error │   precipitation │
│ • Faulty optical│                 │ • Premature     │                 │ • Coprecipitate │
│   monochromator │   endpoint call │   occlusion     │
│ • Aging battery │                 │ • Incomplete    │                 │ • Indicator     │
│   potential     │   sample wash   │   color lag     │
└─────────────────┘                 └─────────────────┘                 └─────────────────┘
```

#### 1. Instrumental and Reagent Errors
Arise from imperfections, degradation, or calibration drifts in measuring equipment, glassware, and analytical reagents:
- Thermal volumetric expansion of glass volumetric flasks calibrated at $20^\circ\text{C}$ but utilized at $32^\circ\text{C}$ ($\Delta V = V_0 \beta \Delta T$).
- Electronic zero-drift, photomultiplier tube dark-current noise, or degraded hollow cathode lamps in spectrophotometers.
- Chemical impurities present in analytical grade solvents or mineral acids (e.g., trace iron in commercial $\text{HCl}$ contaminating trace colorimetric iron analyses).

#### 2. Operative and Personal Errors
Originate from the limitations, physical biases, or incorrect technique of the human analyst:
- Parallax reading error when sighting the meniscus of a burette or volumetric pipette above or below true perpendicular eye level.
- Inability of the human eye to detect faint color transitions in acid-base indicators at the exact stoichiometric equivalence point, leading to systematic over-titration.
- Incomplete quantitative transfer of precipitates during gravimetric filtration or insufficient ignition duration to constant mass.

#### 3. Methodic Errors (Chemical Method Inadequacies)
Represent the most insidious class of systematic errors, arising from non-ideal chemical behavior or incomplete theoretical assumptions inherent to the analytical protocol:
- Incomplete chemical precipitation governed by finite solubility products ($K_{\text{sp}}$) or complex ion side-reactions.
- Coprecipitation of interfering foreign ions via adsorption, occlusion, or isomorphous inclusion.
- Side reactions and incomplete oxidation-reduction equilibria in titrimetry.
- Decomposition, thermal instability, or volatilization of precipitates during gravimetric ashing.

### Minimization of Determinate Errors
Systematic errors cannot be suppressed through statistical replication alone. Their detection and mitigation necessitate rigorous metrological protocols:
1. **Calibration of Apparatus**: Periodic recalibration of analytical balances using Class S reference weights, gravimetric calibration of pipettes and burettes with pure water at controlled temperature, and wavelength verification of spectrophotometers using holmium oxide glass.
2. **Analysis of Certified Reference Materials (CRMs)**: Running standard reference matrices possessing certified analyte concentrations traceable to international standards.
3. **Independent Method Comparison**: Analyzing identical test portions using two conceptually uncorrelated methodologies (e.g., determining trace copper in water via electrothermal atomic absorption spectroscopy vs inductively coupled plasma mass spectrometry).
4. **Blank Determinations**:
   - *Reagent Blank*: Carries out the entire analytical sequence utilizing all reagents, solvents, and digestion protocols in the complete absence of the sample matrix, allowing subtraction of background chemical contamination:
     $$x_{\text{analyte}} = x_{\text{sample}} - x_{\text{blank}}$$
   - *Matrix Blank*: Contains all matrix components identical to the real sample except the target analyte.
5. **Standard Addition (Spike Recovery)**: Validates recovery and compensates for matrix interferences by measuring unspiked and spiked aliquots:
   $$\% \text{Recovery} = \frac{C_{\text{spiked}} - C_{\text{unspiked}}}{C_{\text{added}}} \times 100\%$$

### Indeterminate (Random) Errors
Indeterminate errors represent stochastic, uncontrolled fluctuations in experimental conditions that occur unpredictably during replicate analyses. They arise from microscopic environmental vibrations, thermal air currents inside analytical balance cases, fluctuating line voltages in electronic circuits, and quantum photon arrival statistics in detectors.

Random errors cannot be individually isolated or eliminated. However, because they are governed by the laws of probability, their collective magnitude and distribution can be treated rigorously via mathematical statistics.""",
                    "simulations": []
                },
                {
                    "id": "sec-1-3",
                    "secNumber": "1.3",
                    "title": "Normal (Gaussian) Distribution: Population Parameters vs Sample Statistics",
                    "content": r"""When an analytical measurement is subject to a multiplicity of microscopic, independent random perturbations of comparable magnitude, the Central Limit Theorem dictates that the resulting experimental distribution converges asymptotically to a continuous **Gaussian (Normal) Distribution**.

### The Gaussian Probability Density Function
The mathematical probability density function $f(x)$ for a continuous random variable $x$ governed by a population mean $\mu$ and a population standard deviation $\sigma$ is expressed as:
$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$
where:
- $\mu = \lim_{N \to \infty} \frac{1}{N}\sum_{i=1}^N x_i$ is the population arithmetic mean (central tendency).
- $\sigma = \sqrt{\lim_{N \to \infty} \frac{1}{N}\sum_{i=1}^N (x_i - \mu)^2}$ is the population standard deviation (dispersion width).
- $\frac{1}{\sigma \sqrt{2\pi}}$ is the normalization factor ensuring that the total integral over all space equals unity:
$$\int_{-\infty}^{+\infty} f(x)\,dx = 1$$

```
                              Normal Gaussian Curve
                                     f(x)
                                      ▲
                                     / \
                                    /   \
                                   /  |  \
                                  /   |   \
                                 /    |    \
                              _.-'    |    '-._
                         _.-''   |    |    |   ''-._
                     _.-'   |    |    |    |    |   '-._
             ───────'───────┼────┼────┼────┼────┼───────'───────► x
                          μ-3σ μ-2σ μ-1σ  μ  μ+1σ μ+2σ μ+3σ
                           │    │    │    │    │    │    │
                           └────┴────┴────┴────┴────┴────┘
                                68.27% (±1σ)
                           └──────────────┴──────────────┘
                                     95.44% (±2σ)
                      └─────────────────────────────┴─────────────────────────────┘
                                           99.73% (±3σ)
```

### The Standard Normal Deviate ($z$)
To standardize arbitrary Gaussian distributions with disparate units, the variable $x$ is mapped to the dimensionless standard normal deviate $z$:
$$z = \frac{x - \mu}{\sigma}$$
Substituting $z$ transforms the probability density into the universal standard normal curve $\phi(z)$:
$$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2 / 2}$$
The integral of $\phi(z)$ within defined bounds determines the exact probability $P$ that an observation falls within specified standard deviation intervals:
$$P(\mu - z\sigma \le x \le \mu + z\sigma) = \frac{1}{\sqrt{2\pi}} \int_{-z}^{+z} e^{-u^2 / 2}\,du = \text{erf}\left(\frac{z}{\sqrt{2}}\right)$$

Metrological integration reveals the classic confidence intervals:
- **$\mu \pm 1.00\sigma$**: Encapsulates **$68.27\%$** of all replicate measurements.
- **$\mu \pm 1.96\sigma$**: Encapsulates exactly **$95.00\%$** of all replicate measurements.
- **$\mu \pm 2.00\sigma$**: Encapsulates **$95.44\%$** of all replicate measurements.
- **$\mu \pm 2.58\sigma$**: Encapsulates exactly **$99.00\%$** of all replicate measurements.
- **$\mu \pm 3.00\sigma$**: Encapsulates **$99.73\%$** of all replicate measurements.

### Population Parameters Versus Finite Sample Statistics
In practical analytical chemistry, an infinite population ($N \to \infty$) is never realizable. Instead, the chemist operates upon a finite sample set of $N$ replicates (typically $3 \le N \le 10$). Consequently, population parameters ($\mu, \sigma, \sigma^2$) must be estimated using unbiased sample statistics ($\bar{x}, s, s^2$):

#### 1. Sample Arithmetic Mean ($\bar{x}$)
$$\bar{x} = \frac{1}{N} \sum_{i=1}^N x_i = \frac{x_1 + x_2 + \dots + x_N}{N}$$

#### 2. Sample Standard Deviation ($s$)
$$s = \sqrt{\frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N - 1}} = \sqrt{\frac{\sum x_i^2 - \frac{(\sum x_i)^2}{N}}{N - 1}}$$
The denominator $N - 1$ represents the **degrees of freedom** ($\nu = N - 1$). Utilizing $N - 1$ instead of $N$ (Bessel's correction) eliminates negative bias, providing an exact, mathematically unbiased estimator for the true population standard deviation $\sigma$.

#### 3. Sample Variance ($s^2$)
$$s^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N - 1}$$

#### 4. Relative Standard Deviation (RSD) and Coefficient of Variation (CV)
$$s_r = \text{RSD} = \frac{s}{\bar{x}}$$
$$\text{CV} = \% \text{RSD} = \left(\frac{s}{\bar{x}}\right) \times 100\%$$

#### 5. Standard Error of the Mean ($s_m$)
The scatter of sample means $\bar{x}$ drawn from a parent population with standard deviation $s$ narrows with increasing replicate size $N$:
$$s_m = \frac{s}{\sqrt{N}}$$
This fundamental relationship demonstrates that diminishing random error by a factor of 2 requires quadrupling the number of experimental replicates ($N \to 4N$).""",
                    "simulations": []
                },
                {
                    "id": "sec-1-4",
                    "secNumber": "1.4",
                    "title": "Mathematical Propagation of Uncertainty: Addition, Multiplication & Transcendental Functions",
                    "content": r"""Analytical procedures invariably combine multiple experimental measurements (masses weighed on a balance, volumes dispensed by burettes and pipettes, spectrophotometric absorbances, temperatures) to calculate a final analytical concentration $y$. Because each individual measurement possesses an associated uncertainty, these uncertainties propagate through the mathematical functional relationship to determine the net uncertainty in the final result.

### The General Law of Propagation of Uncertainty
Let a calculated physical quantity $y$ be a function of $k$ independent, uncorrelated experimental variables $x_1, x_2, \dots, x_k$:
$$y = f(x_1, x_2, \dots, x_k)$$
Assuming that the individual uncertainties $s_{x_i}$ are sufficiently small relative to the values of $x_i$ such that second- and higher-order Taylor series expansion terms are negligible, the variance of $y$ ($s_y^2$) is given by the general partial derivative summation:
$$s_y^2 = \sum_{i=1}^k \left(\frac{\partial f}{\partial x_i}\right)^2 s_{x_i}^2 + 2 \sum_{i=1}^{k-1} \sum_{j=i+1}^k \left(\frac{\partial f}{\partial x_i}\right) \left(\frac{\partial f}{\partial x_j}\right) s_{x_i, x_j}$$
When the independent variables are mutually uncorrelated (covariance $s_{x_i, x_j} = 0$), the cross-terms vanish identically, yielding the **uncorrelated uncertainty propagation equation in quadrature**:
$$s_y = \sqrt{\sum_{i=1}^k \left(\frac{\partial f}{\partial x_i}\right)^2 s_{x_i}^2}$$

### Derivation for Specific Mathematical Operations

#### 1. Addition and Subtraction
Let $y = a x_1 + b x_2 - c x_3$, where $a, b, c$ are exact numerical coefficients. The partial derivatives are:
$$\frac{\partial y}{\partial x_1} = a, \quad \frac{\partial y}{\partial x_2} = b, \quad \frac{\partial y}{\partial x_3} = -c$$
Substituting into the general equation:
$$s_y = \sqrt{a^2 s_{x_1}^2 + b^2 s_{x_2}^2 + (-c)^2 s_{x_3}^2} = \sqrt{a^2 s_{x_1}^2 + b^2 s_{x_2}^2 + c^2 s_{x_3}^2}$$
*Rule*: In additive and subtractive operations, **absolute variances add in quadrature**. Absolute uncertainties do not sum linearly ($s_y \neq s_{x_1} + s_{x_2}$); they combine perpendicularly as orthogonal vectors in Euclidean space.

#### 2. Multiplication and Division
Let $y = \frac{a \cdot x_1 \cdot x_2}{x_3}$. The partial derivatives are:
$$\frac{\partial y}{\partial x_1} = \frac{a x_2}{x_3} = \frac{y}{x_1}, \quad \frac{\partial y}{\partial x_2} = \frac{a x_1}{x_3} = \frac{y}{x_2}, \quad \frac{\partial y}{\partial x_3} = -\frac{a x_1 x_2}{x_3^2} = -\frac{y}{x_3}$$
Substituting into the quadrature equation:
$$s_y^2 = \left(\frac{y}{x_1}\right)^2 s_{x_1}^2 + \left(\frac{y}{x_2}\right)^2 s_{x_2}^2 + \left(-\frac{y}{x_3}\right)^2 s_{x_3}^2$$
Dividing both sides by $y^2$:
$$\left(\frac{s_y}{y}\right)^2 = \left(\frac{s_{x_1}}{x_1}\right)^2 + \left(\frac{s_{x_2}}{x_2}\right)^2 + \left(\frac{s_{x_3}}{x_3}\right)^2$$
Taking the square root yields:
$$\frac{s_y}{y} = \sqrt{\left(\frac{s_{x_1}}{x_1}\right)^2 + \left(\frac{s_{x_2}}{x_2}\right)^2 + \left(\frac{s_{x_3}}{x_3}\right)^2}$$
*Rule*: In multiplicative and divisive operations, **relative variances add in quadrature**.

#### 3. Power Functions
Let $y = x^a$, where $a$ is an exact constant. The partial derivative is:
$$\frac{\partial y}{\partial x} = a x^{a-1} = a \frac{y}{x}$$
Consequently:
$$s_y = \left|a \frac{y}{x}\right| s_x \implies \frac{s_y}{y} = |a| \left(\frac{s_x}{x}\right)$$
*Rule*: The relative uncertainty in $y = x^a$ equals the relative uncertainty in $x$ multiplied by the absolute value of the exponent $|a|$.

#### 4. Logarithmic Functions (Base 10 and Natural)
For $y = \log_{10}(x)$:
$$\frac{dy}{dx} = \frac{1}{x \ln(10)} \approx \frac{0.43429}{x} \implies s_y = 0.43429 \left(\frac{s_x}{x}\right)$$
*Analytical Significance in pH Metrology*: In the definition of $\text{pH} = -\log_{10}[\text{H}^+]$, an uncertainty of $1.0\%$ in hydrogen ion activity ($\frac{s_{[\text{H}^+]}}{[\text{H}^+]} = 0.010$) propagates to an absolute uncertainty in pH of:
$$s_{\text{pH}} = 0.43429 \times 0.010 = 0.0043\,\text{pH units}$$

#### 5. Exponential Functions (Antilogarithms)
For $y = 10^x$:
$$\frac{dy}{dx} = 10^x \ln(10) = y \ln(10) \approx 2.3026\,y \implies \frac{s_y}{y} = 2.3026\,s_x$$
*Rule*: The relative uncertainty in $y = 10^x$ is directly proportional to the absolute uncertainty in $x$ scaled by $\ln(10)$. An error of $\pm 0.02$ in a measured pH propagates to a $\pm 4.6\%$ relative error in the calculated hydrogen ion concentration $[\text{H}^+]$.

| Mathematical Function | Functional Form $y = f(x)$ | Propagated Uncertainty Equation |
| :--- | :--- | :--- |
| **Linear Combination** | $y = a x_1 \pm b x_2$ | $s_y = \sqrt{a^2 s_{x_1}^2 + b^2 s_{x_2}^2}$ |
| **Product / Quotient** | $y = \frac{x_1 \cdot x_2}{x_3}$ | $\frac{s_y}{y} = \sqrt{\left(\frac{s_{x_1}}{x_1}\right)^2 + \left(\frac{s_{x_2}}{x_2}\right)^2 + \left(\frac{s_{x_3}}{x_3}\right)^2}$ |
| **Exponential Power** | $y = x^n$ | $\frac{s_y}{y} = |n| \frac{s_x}{x}$ |
| **Common Logarithm** | $y = \log_{10}(x)$ | $s_y = 0.43429 \left(\frac{s_x}{x}\right)$ |
| **Natural Logarithm** | $y = \ln(x)$ | $s_y = \frac{s_x}{x}$ |
| **Base-10 Antilogarithm**| $y = 10^x$ | $\frac{s_y}{y} = 2.3026\,s_x$ |
| **Natural Exponential** | $y = e^x$ | $\frac{s_y}{y} = s_x$ |""",
                    "simulations": []
                },
                {
                    "id": "sec-1-5",
                    "secNumber": "1.5",
                    "title": "Confidence Intervals & Student's t-Distribution on Finite Analytical Replicates",
                    "content": r"""In chemical analysis, the true population mean $\mu$ and standard deviation $\sigma$ are inaccessible; the analyst obtains only a sample mean $\bar{x}$ and sample standard deviation $s$ computed from $N$ replicates. To state the probability that the true mean $\mu$ lies within a specified range around $\bar{x}$, we establish a **Confidence Interval (CI)**.

### Derivation from the Student's $t$-Distribution
If the true population standard deviation $\sigma$ were known, the standard normal variable $z = \frac{\bar{x} - \mu}{\sigma / \sqrt{N}}$ would define the confidence interval:
$$\mu = \bar{x} \pm \frac{z\sigma}{\sqrt{N}}$$
However, when $\sigma$ is replaced by the sample estimate $s$, the statistic $t$ no longer follows the standard Gaussian distribution:
$$t = \frac{\bar{x} - \mu}{s / \sqrt{N}}$$
Because $s$ is itself a stochastic random variable subject to sample-to-sample fluctuations, the variable $t$ follows the **Student's $t$-distribution**, discovered by William Sealy Gosset in 1908.

The probability density function for the Student's $t$-distribution with $\nu = N - 1$ degrees of freedom is:
$$f(t, \nu) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\pi\nu}\,\Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{t^2}{\nu}\right)^{-\frac{\nu + 1}{2}}$$
where $\Gamma$ denotes the Euler gamma function.

```
                    Comparison: Gaussian vs Student's t
                        f(u)
                         ▲
                        / \       ─── Gaussian (Normal)
                       / : \      - - Student's t (ν = 3)
                      /  :  \
                     /   :   \
                    /    :    \
                  _.-'   :    '-._
              _.-'  \    :    /   '-._
          _.-'       \   :   /        '-._
      ───'────────────\──┼──/─────────────'───► u
                     -t  0  +t
```

### Key Properties of the $t$-Distribution
1. **Symmetry**: The distribution is symmetric about $t = 0$.
2. **Heavier Tails**: For small degrees of freedom ($\nu < 10$), the $t$-distribution exhibits substantially broader, heavier tails than the standard normal distribution. This accounts for the increased probability of observing extreme deviations due to uncertainty in $s$.
3. **Asymptotic Convergence**: As $N \to \infty$ ($\nu \to \infty$), the $t$-distribution converges mathematically to the standard normal distribution:
$$\lim_{\nu \to \infty} f(t, \nu) = \frac{1}{\sqrt{2\pi}} e^{-t^2 / 2} = \phi(t)$$

### Establishing the Confidence Limits
For a chosen confidence level ($1 - \alpha$, typically $95\%$ or $99\%$, where $\alpha$ is the significance level), the two-tailed Student's $t$ critical value $t_{\alpha/2, \nu}$ defines the confidence limits:
$$-t_{\alpha/2, \nu} \le \frac{\bar{x} - \mu}{s / \sqrt{N}} \le +t_{\alpha/2, \nu}$$
Rearranging algebraically yields the fundamental **Confidence Interval Equation**:
$$\mu = \bar{x} \pm \frac{t_{\alpha/2, \nu} \cdot s}{\sqrt{N}}$$

| Degrees of Freedom $\nu = N - 1$ | $t_{0.10}$ (90% Conf) | $t_{0.05}$ (95% Conf) | $t_{0.01}$ (99% Conf) | $t_{0.001}$ (99.9% Conf) |
| :---: | :---: | :---: | :---: | :---: |
| **1** | 6.314 | 12.706 | 63.657 | 636.619 |
| **2** | 2.920 | 4.303 | 9.925 | 31.599 |
| **3** | 2.353 | 3.182 | 5.841 | 12.924 |
| **4** | 2.132 | 2.776 | 4.604 | 8.610 |
| **5** | 2.015 | 2.571 | 4.032 | 6.869 |
| **8** | 1.860 | 2.306 | 3.355 | 5.041 |
| **10** | 1.812 | 2.228 | 3.169 | 4.587 |
| **20** | 1.725 | 2.086 | 2.845 | 3.850 |
| **$\infty$ (Gaussian $z$)** | **1.645** | **1.960** | **2.576** | **3.291** |

Notice that for a triplicate measurement ($N = 3, \nu = 2$), the $95\%$ confidence coefficient is $t = 4.303$, more than double the Gaussian $z = 1.960$. This dramatically illustrates why reporting confidence bounds calculated from $z$ on small analytical datasets produces dangerously overoptimistic certainty estimates.""",
                    "simulations": []
                },
                {
                    "id": "sec-1-6",
                    "secNumber": "1.6",
                    "title": "Hypothesis Testing: Student's t-Tests (One-Sample, Paired & Two-Sample Means)",
                    "content": r"""In chemical method development and regulatory compliance, analytical chemists must make objective decisions regarding whether an experimental result differs significantly from an accepted standard, whether a new method yields results equivalent to an established reference method, or whether two analysts obtain concordant data. These questions are resolved using **statistical hypothesis testing**.

### General Formalism of Hypothesis Testing
1. **Null Hypothesis ($H_0$)**: Postulates that there is no significant difference between the evaluated parameters, and that any observed discrepancy is attributable purely to random indeterminate sampling fluctuations:
   $$H_0: \mu = \mu_0 \quad \text{or} \quad H_0: \mu_1 = \mu_2$$
2. **Alternative Hypothesis ($H_1$)**: Postulates that a genuine, statistically significant difference exists:
   - *Two-tailed*: $H_1: \mu \neq \mu_0$ (tests for deviation in either direction).
   - *One-tailed*: $H_1: \mu > \mu_0$ or $H_1: \mu < \mu_0$ (tests for deviation in a specified direction).
3. **Decision Rule**: Compute an experimental test statistic ($t_{\text{calc}}$). Compare with the critical value ($t_{\text{crit}}$) at significance level $\alpha$ (typically $\alpha = 0.05$ for $95\%$ confidence):
   - If $|t_{\text{calc}}| \le t_{\text{crit}}$: **Retain $H_0$**. The observed discrepancy is not statistically significant.
   - If $|t_{\text{calc}}| > t_{\text{crit}}$: **Reject $H_0$** in favor of $H_1$. A statistically significant difference exists.

### Case 1: One-Sample $t$-Test (Comparison of Sample Mean to a Certified True Value)
Used to validate the accuracy of a new analytical procedure by analyzing a Certified Reference Material (CRM) possessing a known true value $\mu_0$:
$$t_{\text{calc}} = \frac{|\bar{x} - \mu_0|}{s / \sqrt{N}} = \frac{|\bar{x} - \mu_0| \sqrt{N}}{s}$$
The calculated value is compared against $t_{\text{crit}}$ for $\nu = N - 1$ degrees of freedom. If $t_{\text{calc}} > t_{\text{crit}}$, determinate systematic error is present.

### Case 2: Two-Sample $t$-Test (Comparison of Two Independent Experimental Means)
Used to determine whether two independent analytical procedures (Method 1 and Method 2) yield identical results when applied to test aliquots of the same homogeneous material.
- Let Method 1 yield $N_1$ replicates with mean $\bar{x}_1$ and variance $s_1^2$.
- Let Method 2 yield $N_2$ replicates with mean $\bar{x}_2$ and variance $s_2^2$.

#### Step 1: Pre-Testing for Variance Homogeneity ($F$-Test)
Before pooling variances, an $F$-test must confirm that $s_1^2$ and $s_2^2$ do not differ significantly:
$$F_{\text{calc}} = \frac{s_1^2}{s_2^2} \quad (\text{with } s_1^2 \ge s_2^2)$$
If $F_{\text{calc}} \le F_{\text{crit}}$, the variances are homogeneous and may be pooled.

#### Step 2: Calculation of Pooled Variance ($s_{\text{pooled}}^2$)
$$s_{\text{pooled}} = \sqrt{\frac{(N_1 - 1)s_1^2 + (N_2 - 1)s_2^2}{N_1 + N_2 - 2}}$$

#### Step 3: Calculation of $t_{\text{calc}}$
$$t_{\text{calc}} = \frac{|\bar{x}_1 - \bar{x}_2|}{s_{\text{pooled}} \sqrt{\frac{1}{N_1} + \frac{1}{N_2}}} = \frac{|\bar{x}_1 - \bar{x}_2|}{s_{\text{pooled}}} \sqrt{\frac{N_1 N_2}{N_1 + N_2}}$$
The degrees of freedom are $\nu = N_1 + N_2 - 2$. If $t_{\text{calc}} > t_{\text{crit}}$, the two analytical methods produce statistically distinguishable results.

### Case 3: Paired $t$-Test (Comparison of Individual Paired Data Points)
Utilized when two disparate methods are applied across a wide range of different samples possessing varying matrix compositions (e.g., analyzing 10 different water samples by both atomic absorption and spectrophotometry):
- For each sample $i$, compute the paired difference: $d_i = x_{1,i} - x_{2,i}$.
- Compute the mean of the differences: $\bar{d} = \frac{1}{N}\sum_{i=1}^N d_i$.
- Compute the standard deviation of the differences:
$$s_d = \sqrt{\frac{\sum_{i=1}^N (d_i - \bar{d})^2}{N - 1}}$$
- Compute the test statistic:
$$t_{\text{calc}} = \frac{|\bar{d}| \sqrt{N}}{s_d}$$
The degrees of freedom are $\nu = N - 1$. This paired formulation isolates the systematic method discrepancy from the sample-to-sample concentration variations.""",
                    "simulations": []
                },
                {
                    "id": "sec-1-7",
                    "secNumber": "1.7",
                    "title": "Variance Homogeneity (F-Test), Outlier Rejection & Linear Least-Squares Calibration",
                    "content": r"""Statistical evaluation of quantitative data requires two additional procedures: testing for anomalous single observations (**outlier rejection**) and establishing instrumental response functions (**linear regression calibration**).

### Rejection of Outlier Data Points
An **outlier** is an experimental replicate that deviates conspicuously from the remaining members of a replicate dataset. Outliers must never be rejected arbitrarily or casually discarded without rigorous statistical justification.

#### 1. Dixon's $Q$-Test (Recommended for $3 \le N \le 10$)
1. Arrange the experimental dataset in ascending numerical order:
   $$x_1 \le x_2 \le \dots \le x_N$$
2. Identify the suspect value (either the minimum $x_1$ or maximum $x_N$).
3. Compute the range $w = x_N - x_1$.
4. Compute the divergence gap between the suspect value and its nearest neighbor:
   $$\text{gap} = |x_{\text{suspect}} - x_{\text{nearest}}|$$
5. Compute the experimental quotient $Q_{\text{calc}}$:
   $$Q_{\text{calc}} = \frac{\text{gap}}{w} = \frac{|x_{\text{suspect}} - x_{\text{nearest}}|}{x_N - x_1}$$
6. Compare $Q_{\text{calc}}$ with critical values $Q_{\text{crit}}$ at $90\%$ or $95\%$ confidence:
   - If $Q_{\text{calc}} > Q_{\text{crit}}$: The suspect observation can be rejected at the specified confidence level.
   - If $Q_{\text{calc}} \le Q_{\text{crit}}$: The datum must be retained in calculating the mean and standard deviation.

| Replicates $N$ | $Q_{\text{crit}}$ (90% Conf) | $Q_{\text{crit}}$ (95% Conf) | $Q_{\text{crit}}$ (99% Conf) |
| :---: | :---: | :---: | :---: |
| **3** | 0.941 | 0.970 | 0.994 |
| **4** | 0.765 | 0.829 | 0.926 |
| **5** | 0.642 | 0.710 | 0.821 |
| **6** | 0.560 | 0.625 | 0.740 |
| **7** | 0.507 | 0.568 | 0.680 |
| **8** | 0.468 | 0.526 | 0.634 |
| **10** | 0.412 | 0.466 | 0.568 |

#### 2. Grubbs Test (Recommended by ISO and IUPAC)
The Grubbs test evaluates the normalized residual of the suspect observation:
$$G_{\text{calc}} = \frac{|x_{\text{suspect}} - \bar{x}|}{s}$$
where $\bar{x}$ and $s$ are calculated including the suspect value. If $G_{\text{calc}} > G_{\text{crit}}$, the point is rejected. The Grubbs test avoids the masking effect that hampers the $Q$-test when multiple outliers occur.

### Linear Least-Squares Calibration Regression
Most instrumental analytical methods (AAS, UV-Vis, HPLC) rely on calibration curves relating an instrumental response $y$ (absorbance, peak area) to standard analyte concentrations $x$. Under ideal conditions, the response follows a linear function:
$$y = m x + c$$

The classical method of unweighted ordinary least-squares minimizes the sum of squared vertical residuals:
$$S = \sum_{i=1}^N [y_i - (m x_i + c)]^2 \to \text{minimum}$$
Setting partial derivatives $\frac{\partial S}{\partial m} = 0$ and $\frac{\partial S}{\partial c} = 0$ yields the fundamental normal equations:

#### 1. Slope ($m$)
$$m = \frac{N \sum (x_i y_i) - (\sum x_i)(\sum y_i)}{N \sum (x_i^2) - (\sum x_i)^2} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{S_{xy}}{S_{xx}}$$

#### 2. $y$-Intercept ($c$)
$$c = \bar{y} - m \bar{x} = \frac{(\sum y_i) - m (\sum x_i)}{N}$$

#### 3. Standard Deviation of the Regression ($s_{y/x}$)
Measures the vertical scatter of data points around the fitted regression line:
$$s_{y/x} = \sqrt{\frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{N - 2}} = \sqrt{\frac{S_{yy} - m^2 S_{xx}}{N - 2}}$$
where $\hat{y}_i = m x_i + c$ and degrees of freedom $\nu = N - 2$ (since two parameters, $m$ and $c$, are estimated).

#### 4. Uncertainties in Slope ($s_m$) and Intercept ($s_c$)
$$s_m = \frac{s_{y/x}}{\sqrt{S_{xx}}} = \frac{s_{y/x}}{\sqrt{\sum (x_i - \bar{x})^2}}$$
$$s_c = s_{y/x} \sqrt{\frac{\sum x_i^2}{N \sum (x_i - \bar{x})^2}} = s_{y/x} \sqrt{\frac{1}{N} + \frac{\bar{x}^2}{S_{xx}}}$$

#### 5. Uncertainty in an Unknown Sample Concentration ($s_{x_0}$)
When an unknown sample yields an instrumental response $y_0$ (averaged over $M$ replicate readings), its concentration $x_0 = \frac{y_0 - c}{m}$ has standard uncertainty:
$$s_{x_0} = \frac{s_{y/x}}{m} \sqrt{\frac{1}{M} + \frac{1}{N} + \frac{(y_0 - \bar{y})^2}{m^2 S_{xx}}}$$
This equation shows that the uncertainty in an unknown concentration is minimized when the measured response $y_0$ is close to the calibration centroid $\bar{y}$. Measuring samples near the extremes of the calibration curve amplifies uncertainty.""",
                    "simulations": []
                }
            ],
            "problems": [
                {
                    "id": "prob-1-1",
                    "problemNumber": "1.1",
                    "title": "Statistical Treatment of Multi-Replicate Gravimetric Iron Determination",
                    "difficulty": "Foundational",
                    "statement": r"""A chemist analyzes the iron content in a certified reference alloy by gravimetric precipitation of hydrated iron(III) oxide followed by ignition to iron(III) oxide ($\text{Fe}_2\text{O}_3$). Five independent replicate determinations yield the following percentage mass fractions of iron ($\text{wt}\% \text{ Fe}$):
$$x = \{15.42\%,\, 15.51\%,\, 15.38\%,\, 15.46\%,\, 15.48\%\}$$
The certified reference true value is $x_t = 15.40\% \text{ Fe}$.

Calculate:
1. The sample arithmetic mean $\bar{x}$.
2. The absolute error $E_{\text{abs}}$ and the percentage relative error $\% E_{\text{rel}}$.
3. The sample standard deviation $s$ and the coefficient of variation ($\% \text{RSD}$).
4. The $95\%$ confidence interval for the true population mean $\mu$ using the Student's $t$-distribution ($t_{0.05, 4} = 2.776$).""",
                    "solution": r"""### Step 1: Calculation of Sample Arithmetic Mean ($\bar{x}$)
The sum of the five replicates is:
$$\sum_{i=1}^5 x_i = 15.42 + 15.51 + 15.38 + 15.46 + 15.48 = 77.25\%$$
The sample mean is:
$$\bar{x} = \frac{\sum x_i}{N} = \frac{77.25\%}{5} = \mathbf{15.450\%}$$

### Step 2: Absolute and Relative Errors
1. Absolute Error:
$$E_{\text{abs}} = \bar{x} - x_t = 15.450\% - 15.400\% = \mathbf{+0.050\%}$$
2. Percentage Relative Error:
$$\% E_{\text{rel}} = \left(\frac{E_{\text{abs}}}{x_t}\right) \times 100\% = \left(\frac{+0.050}{15.40}\right) \times 100\% = \mathbf{+0.325\%}$$
The positive sign indicates a slight positive systematic bias.

### Step 3: Sample Standard Deviation and % RSD
Compute the residuals $(x_i - \bar{x})$ and squared residuals:
- $x_1 = 15.42$: $(15.42 - 15.45)^2 = (-0.03)^2 = 0.0009$
- $x_2 = 15.51$: $(15.51 - 15.45)^2 = (+0.06)^2 = 0.0036$
- $x_3 = 15.38$: $(15.38 - 15.45)^2 = (-0.07)^2 = 0.0049$
- $x_4 = 15.46$: $(15.46 - 15.45)^2 = (+0.01)^2 = 0.0001$
- $x_5 = 15.48$: $(15.48 - 15.45)^2 = (+0.03)^2 = 0.0009$

Sum of squared residuals:
$$\sum_{i=1}^5 (x_i - \bar{x})^2 = 0.0009 + 0.0036 + 0.0049 + 0.0001 + 0.0009 = 0.0104$$
Degrees of freedom $\nu = N - 1 = 5 - 1 = 4$.
$$s = \sqrt{\frac{0.0104}{4}} = \sqrt{0.0026} = \mathbf{0.0510\%}$$

Coefficient of variation:
$$\% \text{RSD} = \left(\frac{s}{\bar{x}}\right) \times 100\% = \left(\frac{0.0510}{15.450}\right) \times 100\% = \mathbf{0.330\%}$$

### Step 4: 95% Confidence Interval for $\mu$
Using the Student's $t$ equation with $t_{0.05, 4} = 2.776$:
$$\text{CI} = \bar{x} \pm \frac{t \cdot s}{\sqrt{N}} = 15.450\% \pm \frac{2.776 \times 0.0510\%}{\sqrt{5}} = 15.450\% \pm \frac{0.1416\%}{2.2361} = 15.450\% \pm \mathbf{0.063\%}$$
The $95\%$ confidence interval is $[15.387\%,\, 15.513\%]$.
Because the certified true value $x_t = 15.40\%$ falls comfortably inside this interval, the experimental result does not exhibit statistically significant bias at the $95\%$ confidence level.""",
                    "hints": ["Calculate the arithmetic mean first, then square each residual.", "Remember to divide by N - 1 (degrees of freedom = 4) when computing sample variance."]
                },
                {
                    "id": "prob-1-2",
                    "problemNumber": "1.2",
                    "title": "Propagation of Uncertainty in Multi-Step Titrimetric Molarity Determination",
                    "difficulty": "Intermediate",
                    "statement": r"""A standard hydrochloric acid solution is prepared and standardized by titrating primary standard sodium carbonate ($\text{Na}_2\text{CO}_3$). The molar concentration of the acid ($C_{\text{HCl}}$) is calculated using the stoichiometric expression:
$$C_{\text{HCl}} = \frac{2 \cdot m_{\text{Na}_2\text{CO}_3}}{M_{\text{Na}_2\text{CO}_3} \cdot V_{\text{HCl}}}$$
where:
- Mass of pure $\text{Na}_2\text{CO}_3$ weighed: $m = 0.2145 \pm 0.0002\text{ g}$
- Molar mass of $\text{Na}_2\text{CO}_3$: $M = 105.9888 \pm 0.0005\text{ g}\cdot\text{mol}^{-1}$
- Titration volume of $\text{HCl}$ consumed: $V = 40.25 \pm 0.04\text{ mL} = (40.25 \pm 0.04) \times 10^{-3}\text{ L}$

Calculate:
1. The nominal molar concentration $C_{\text{HCl}}$ of the standardized hydrochloric acid.
2. The relative uncertainties for mass, molar mass, and titration volume.
3. The propagated absolute standard uncertainty $s_{C}$ and relative standard uncertainty $\% s_C / C$.
4. Express the final standardized concentration in standard metrological form with appropriate significant figures.""",
                    "solution": r"""### Step 1: Nominal Concentration Calculation
$$C_{\text{HCl}} = \frac{2 \times 0.2145\text{ g}}{105.9888\text{ g}\cdot\text{mol}^{-1} \times (40.25 \times 10^{-3}\text{ L})} = \frac{0.4290}{4.26605} = \mathbf{0.100561\text{ M}}$$

### Step 2: Calculation of Individual Relative Uncertainties
1. For mass $m$:
$$\frac{s_m}{m} = \frac{0.0002}{0.2145} = 9.324 \times 10^{-4} \quad (0.0932\%)$$
2. For molar mass $M$:
$$\frac{s_M}{M} = \frac{0.0005}{105.9888} = 4.717 \times 10^{-6} \quad (0.00047\%)$$
3. For volume $V$:
$$\frac{s_V}{V} = \frac{0.04}{40.25} = 9.938 \times 10^{-4} \quad (0.0994\%)$$

### Step 3: Propagation of Relative Uncertainty in Quadrature
Because the mathematical function is purely multiplicative and divisive:
$$\frac{s_C}{C} = \sqrt{\left(\frac{s_m}{m}\right)^2 + \left(\frac{s_M}{M}\right)^2 + \left(\frac{s_V}{V}\right)^2}$$
$$\frac{s_C}{C} = \sqrt{(9.324 \times 10^{-4})^2 + (4.717 \times 10^{-6})^2 + (9.938 \times 10^{-4})^2}$$
$$\left(\frac{s_C}{C}\right)^2 = 8.694 \times 10^{-7} + 2.225 \times 10^{-11} + 9.876 \times 10^{-7} = 1.857 \times 10^{-6}$$
$$\frac{s_C}{C} = \sqrt{1.857 \times 10^{-6}} = 1.363 \times 10^{-3} = \mathbf{0.136\%}$$

Notice that the uncertainty in the molar mass ($0.00047\%$) is negligible compared to the volumetric ($0.0994\%$) and gravimetric ($0.0932\%$) terms.

### Step 4: Absolute Uncertainty and Final Reporting
$$s_C = C \times \left(\frac{s_C}{C}\right) = 0.100561 \times (1.363 \times 10^{-3}) = \mathbf{0.000137\text{ M}}$$
Rounding the uncertainty to two significant figures yields $s_C = 0.00014\text{ M}$.
The final standardized concentration is reported as:
$$\mathbf{C_{\text{HCl}} = (0.10056 \pm 0.00014)\text{ M}} \quad (\text{or } 0.1006 \pm 0.0001\text{ M})$$""",
                    "hints": ["Identify the operation as purely multiplicative/divisive: combine relative uncertainties in quadrature.", "Convert the relative uncertainty back to an absolute uncertainty by multiplying by the nominal molarity."]
                },
                {
                    "id": "prob-1-3",
                    "problemNumber": "1.3",
                    "title": "Two-Sample t-Test and F-Test Comparison of Analytical Methods",
                    "difficulty": "Advanced",
                    "statement": r"""A pharmaceutical quality assurance laboratory compares a newly developed High-Performance Liquid Chromatography (HPLC) assay with a classical compendial Spectrophotometric method for the determination of paracetamol in tablets. Replicate analyses of a homogeneous tablet blend yield the following percentage tablet assay results:
- **HPLC Method ($1$)**: $N_1 = 6$, $\bar{x}_1 = 99.82\%$, $s_1 = 0.28\%$
- **Spectrophotometric Method ($2$)**: $N_2 = 5$, $\bar{x}_2 = 100.25\%$, $s_2 = 0.52\%$

At the $95\%$ confidence level ($\alpha = 0.05$):
1. Perform an $F$-test to determine whether the variances of the two methods are significantly different ($F_{\text{crit}}$ for $\nu_1 = 4, \nu_2 = 5$ is $6.26$).
2. Calculate the pooled standard deviation $s_{\text{pooled}}$.
3. Perform a two-sample Student's $t$-test to determine whether the mean assay results of the two methods differ significantly ($t_{\text{crit}}$ for $\nu = 9$ is $2.262$).
4. State the conclusions of both hypothesis tests.""",
                    "solution": r"""### Step 1: Variance Homogeneity Evaluation (F-Test)
Place the larger variance in the numerator:
$$s_2^2 = (0.52)^2 = 0.2704, \quad s_1^2 = (0.28)^2 = 0.0784$$
$$F_{\text{calc}} = \frac{s_2^2}{s_1^2} = \frac{0.2704}{0.0784} = \mathbf{3.449}$$
Degrees of freedom: numerator $\nu_2 = N_2 - 1 = 4$; denominator $\nu_1 = N_1 - 1 = 5$.
Comparing with the critical value:
$$F_{\text{calc}} = 3.449 < F_{\text{crit}} = 6.26$$
**Conclusion**: Because $F_{\text{calc}} < F_{\text{crit}}$, we retain the null hypothesis $H_0: \sigma_1^2 = \sigma_2^2$. The variances do not differ significantly at the $95\%$ confidence level. Pooling the variances is justified.

### Step 2: Calculation of Pooled Standard Deviation ($s_{\text{pooled}}$)
$$s_{\text{pooled}} = \sqrt{\frac{(N_1 - 1)s_1^2 + (N_2 - 1)s_2^2}{N_1 + N_2 - 2}} = \sqrt{\frac{(5)(0.0784) + (4)(0.2704)}{6 + 5 - 2}} = \sqrt{\frac{0.3920 + 1.0816}{9}} = \sqrt{\frac{1.4736}{9}} = \sqrt{0.16373} = \mathbf{0.4046\%}$$

### Step 3: Two-Sample Student's $t$-Test
$$t_{\text{calc}} = \frac{|\bar{x}_1 - \bar{x}_2|}{s_{\text{pooled}} \sqrt{\frac{1}{N_1} + \frac{1}{N_2}}} = \frac{|99.82 - 100.25|}{0.4046 \times \sqrt{\frac{1}{6} + \frac{1}{5}}} = \frac{0.43}{0.4046 \times \sqrt{0.1667 + 0.2000}} = \frac{0.43}{0.4046 \times \sqrt{0.3667}} = \frac{0.43}{0.4046 \times 0.6055} = \frac{0.43}{0.2450} = \mathbf{1.755}$$
Degrees of freedom $\nu = N_1 + N_2 - 2 = 9$.
The critical two-tailed value is $t_{0.05, 9} = 2.262$.

### Step 4: Analytical Conclusion
Because $|t_{\text{calc}}| = 1.755 < t_{\text{crit}} = 2.262$, we retain the null hypothesis $H_0: \mu_1 = \mu_2$.
There is **no statistically significant difference** between the mean paracetamol concentrations obtained by the new HPLC method and the compendial spectrophotometric method at the $95\%$ confidence level ($p > 0.05$). The new HPLC method is validated for equivalent analytical accuracy.""",
                    "hints": ["Always place the larger sample variance in the numerator for the F-test.", "Degrees of freedom for pooled two-sample t-test is N1 + N2 - 2."]
                },
                {
                    "id": "prob-1-4",
                    "problemNumber": "1.4",
                    "title": "Paired Student's t-Test for Method Equivalency Across Multiple Real Samples",
                    "difficulty": "Honors Problem",
                    "statement": r"""To test for systematic bias between an automated flow-injection analyzer and a manual photometric reference method, six different river water samples with varying dissolved nitrate concentrations ($\text{mg}\cdot\text{L}^{-1} \ \text{NO}_3^-$) were analyzed by both techniques:

| Sample | Reference Method ($x_{1,i}$) | Flow-Injection Method ($x_{2,i}$) |
| :---: | :---: | :---: |
| 1 | 5.24 | 5.18 |
| 2 | 12.80 | 12.65 |
| 3 | 24.15 | 23.90 |
| 4 | 7.95 | 7.82 |
| 5 | 18.60 | 18.35 |
| 6 | 31.20 | 30.95 |

At the $95\%$ confidence level ($\alpha = 0.05$, $t_{0.05, 5} = 2.571$):
1. Compute the paired differences $d_i = x_{1,i} - x_{2,i}$ for each sample.
2. Determine the mean difference $\bar{d}$ and the standard deviation of differences $s_d$.
3. Compute $t_{\text{calc}}$ and determine whether the automated method exhibits statistically significant bias relative to the reference method.""",
                    "solution": r"""### Step 1: Calculation of Individual Paired Differences ($d_i$)
- Sample 1: $d_1 = 5.24 - 5.18 = +0.06$
- Sample 2: $d_2 = 12.80 - 12.65 = +0.15$
- Sample 3: $d_3 = 24.15 - 23.90 = +0.25$
- Sample 4: $d_4 = 7.95 - 7.82 = +0.13$
- Sample 5: $d_5 = 18.60 - 18.35 = +0.25$
- Sample 6: $d_6 = 31.20 - 30.95 = +0.25$

### Step 2: Mean and Standard Deviation of Differences
Sum of differences:
$$\sum_{i=1}^6 d_i = 0.06 + 0.15 + 0.25 + 0.13 + 0.25 + 0.25 = 1.09\,\text{mg/L}$$
Mean difference:
$$\bar{d} = \frac{1.09}{6} = \mathbf{0.1817\,\text{mg/L}}$$

Compute squared deviations $(d_i - \bar{d})^2$:
- $(0.06 - 0.1817)^2 = (-0.1217)^2 = 0.01481$
- $(0.15 - 0.1817)^2 = (-0.0317)^2 = 0.00100$
- $(0.25 - 0.1817)^2 = (+0.0683)^2 = 0.00466$
- $(0.13 - 0.1817)^2 = (-0.0517)^2 = 0.00267$
- $(0.25 - 0.1817)^2 = (+0.0683)^2 = 0.00466$
- $(0.25 - 0.1817)^2 = (+0.0683)^2 = 0.00466$

Sum of squared deviations:
$$\sum (d_i - \bar{d})^2 = 0.01481 + 0.00100 + 0.00466 + 0.00267 + 0.00466 + 0.00466 = 0.03246$$
Standard deviation of differences:
$$s_d = \sqrt{\frac{0.03246}{5}} = \sqrt{0.006492} = \mathbf{0.08057\,\text{mg/L}}$$

### Step 3: Calculation of Test Statistic and Conclusion
$$t_{\text{calc}} = \frac{|\bar{d}| \sqrt{N}}{s_d} = \frac{0.1817 \times \sqrt{6}}{0.08057} = \frac{0.1817 \times 2.4495}{0.08057} = \frac{0.4451}{0.08057} = \mathbf{5.524}$$
Degrees of freedom $\nu = N - 1 = 5$.
Critical value at $95\%$ confidence: $t_{0.05, 5} = 2.571$.

**Decision**:
Because $|t_{\text{calc}}| = 5.524 > t_{\text{crit}} = 2.571$, we **reject the null hypothesis $H_0$** at the $95\%$ confidence level ($p < 0.01$).
The automated flow-injection method exhibits a **statistically significant negative systematic bias** (averaging $\sim 0.18\text{ mg/L}$ lower) compared to the manual reference method. The flow-injection protocol must be recalibrated or corrected for matrix background attenuation before regulatory deployment.""",
                    "hints": ["In a paired t-test, treat the differences d_i as a single dataset of size N.", "Compare t_calc directly against t_crit with N - 1 degrees of freedom."]
                },
                {
                    "id": "prob-1-5",
                    "problemNumber": "1.5",
                    "title": "Dixon Q-Test and Grubbs Test Evaluation of an Outlier Observation",
                    "difficulty": "Intermediate",
                    "statement": r"""A blood serum calcium determination performed in six replicates by atomic absorption spectroscopy yielded the following concentration values ($\text{mg}\cdot\text{dL}^{-1}$):
$$\{9.52,\, 9.48,\, 9.55,\, 9.51,\, 9.49,\, 9.88\}$$
The datum $9.88\text{ mg/dL}$ appears conspicuously high.
1. Apply Dixon's $Q$-test at the $95\%$ confidence level ($Q_{\text{crit}}$ for $N = 6$ is $0.625$) to decide whether $9.88$ should be retained or rejected.
2. Apply the Grubbs test at the $95\%$ confidence level ($G_{\text{crit}}$ for $N = 6$ is $1.822$) to verify the outlier decision.
3. Calculate the revised mean and standard deviation after proper statistical treatment.""",
                    "solution": r"""### Step 1: Dixon's Q-Test
Arrange the values in ascending numerical order:
$$9.48,\, 9.49,\, 9.51,\, 9.52,\, 9.55,\, 9.88$$
The suspect value is $x_6 = 9.88$.
Its nearest neighbor is $x_5 = 9.55$.
The total range of the dataset is:
$$w = x_{\max} - x_{\min} = 9.88 - 9.48 = 0.40\,\text{mg/dL}$$
The gap between the suspect value and its nearest neighbor is:
$$\text{gap} = |9.88 - 9.55| = 0.33\,\text{mg/dL}$$
Compute $Q_{\text{calc}}$:
$$Q_{\text{calc}} = \frac{\text{gap}}{w} = \frac{0.33}{0.40} = \mathbf{0.825}$$
Comparing with the critical value at $95\%$ confidence:
$$Q_{\text{calc}} = 0.825 > Q_{\text{crit}} = 0.625$$
**Decision**: Because $Q_{\text{calc}} > Q_{\text{crit}}$, the value $9.88\text{ mg/dL}$ is **rejected as an outlier** at the $95\%$ confidence level.

### Step 2: Verification by Grubbs Test
Compute the mean and standard deviation of all six observations:
$$\sum x_i = 57.43 \implies \bar{x} = \frac{57.43}{6} = 9.5717\,\text{mg/dL}$$
$$\sum (x_i - \bar{x})^2 = (9.48 - 9.5717)^2 + \dots + (9.88 - 9.5717)^2 = 0.10668$$
$$s = \sqrt{\frac{0.10668}{5}} = 0.1461\,\text{mg/dL}$$
Calculate Grubbs experimental statistic:
$$G_{\text{calc}} = \frac{|x_{\text{suspect}} - \bar{x}|}{s} = \frac{|9.88 - 9.5717|}{0.1461} = \frac{0.3083}{0.1461} = \mathbf{2.110}$$
Comparing with $G_{\text{crit}}$:
$$G_{\text{calc}} = 2.110 > G_{\text{crit}} = 1.822$$
**Decision**: Both Dixon's $Q$-test and the Grubbs test independently confirm that $9.88\text{ mg/dL}$ is a statistically significant outlier ($p < 0.05$) and must be eliminated.

### Step 3: Revised Statistics of the Cleaned Dataset
Re-evaluating the remaining 5 observations:
$$\{9.48,\, 9.49,\, 9.51,\, 9.52,\, 9.55\}$$
$$\bar{x}_{\text{revised}} = \frac{9.48 + 9.49 + 9.51 + 9.52 + 9.55}{5} = \frac{47.55}{5} = \mathbf{9.510\,\text{mg/dL}}$$
$$\sum (x_i - \bar{x})^2 = (-0.03)^2 + (-0.02)^2 + (0.00)^2 + (+0.01)^2 + (+0.04)^2 = 0.0009 + 0.0004 + 0.0000 + 0.0001 + 0.0016 = 0.0030$$
$$s_{\text{revised}} = \sqrt{\frac{0.0030}{4}} = \mathbf{0.0274\,\text{mg/dL}}$$
Rejection of the outlier dramatically improves precision: the standard deviation decreases from $0.146\text{ mg/dL}$ to $0.027\text{ mg/dL}$ (an over 5-fold precision enhancement).""",
                    "hints": ["Rank the array in ascending order before finding the gap and total range.", "For Grubbs test, use the full dataset to compute the preliminary mean and standard deviation."]
                },
                {
                    "id": "prob-1-6",
                    "problemNumber": "1.6",
                    "title": "Ordinary Least-Squares Linear Calibration and Limit of Detection (LOD)",
                    "difficulty": "Honors Problem",
                    "statement": r"""A UV-Vis spectrophotometric calibration curve for trace phosphate determination via the molybdenum blue method yields the following absorbance data ($y$) across five standard concentrations ($x$, in $\mu\text{g}\cdot\text{mL}^{-1}$):

| Standard $i$ | Concentration $x_i$ ($\mu\text{g/mL}$) | Absorbance $y_i$ |
| :---: | :---: | :---: |
| 1 | 0.00 (Blank) | 0.008 |
| 2 | 1.00 | 0.185 |
| 3 | 2.00 | 0.362 |
| 4 | 3.00 | 0.548 |
| 5 | 4.00 | 0.725 |

The standard deviation of 10 replicate blank determinations is $s_{\text{blank}} = 0.0025$ absorbance units.

1. Calculate the least-squares calibration slope ($m$) and $y$-intercept ($c$).
2. Compute the standard deviation of the regression $s_{y/x}$.
3. Calculate the Limit of Detection (LOD, $3.3\sigma/m$) and Limit of Quantitation (LOQ, $10\sigma/m$) in $\mu\text{g}\cdot\text{mL}^{-1}$.
4. An unknown environmental sample yields an absorbance of $A_0 = 0.420$. Calculate the unknown phosphate concentration $x_0$ and its standard error $s_{x_0}$ for a single measurement ($M = 1$).""",
                    "solution": r"""### Step 1: Calibration Slope ($m$) and Intercept ($c$)
Compile summation terms for $N = 5$:
- $\sum x_i = 0 + 1 + 2 + 3 + 4 = 10.00 \implies \bar{x} = 2.00\,\mu\text{g/mL}$
- $\sum y_i = 0.008 + 0.185 + 0.362 + 0.548 + 0.725 = 1.828 \implies \bar{y} = 0.3656$
- $\sum x_i^2 = 0 + 1 + 4 + 9 + 16 = 30.00$
- $S_{xx} = \sum (x_i - \bar{x})^2 = \sum x_i^2 - \frac{(\sum x_i)^2}{N} = 30.00 - \frac{100.0}{5} = 10.00$
- $\sum x_i y_i = (0)(0.008) + (1)(0.185) + (2)(0.362) + (3)(0.548) + (4)(0.725) = 0 + 0.185 + 0.724 + 1.644 + 2.900 = 5.453$
- $S_{xy} = \sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{N} = 5.453 - \frac{(10.00)(1.828)}{5} = 5.453 - 3.656 = 1.797$

Slope:
$$m = \frac{S_{xy}}{S_{xx}} = \frac{1.797}{10.00} = \mathbf{0.1797\,(\mu\text{g/mL})^{-1}}$$
Intercept:
$$c = \bar{y} - m\bar{x} = 0.3656 - (0.1797)(2.00) = 0.3656 - 0.3594 = \mathbf{+0.0062}$$
The calibration equation is: $\mathbf{y = 0.1797 x + 0.0062}$.

### Step 2: Standard Deviation of Regression ($s_{y/x}$)
Compute predicted $\hat{y}_i = 0.1797 x_i + 0.0062$ and squared residuals $(y_i - \hat{y}_i)^2$:
- $x = 0$: $\hat{y}_1 = 0.0062 \implies (0.008 - 0.0062)^2 = (0.0018)^2 = 3.24 \times 10^{-6}$
- $x = 1$: $\hat{y}_2 = 0.1859 \implies (0.185 - 0.1859)^2 = (-0.0009)^2 = 0.81 \times 10^{-6}$
- $x = 2$: $\hat{y}_3 = 0.3656 \implies (0.362 - 0.3656)^2 = (-0.0036)^2 = 12.96 \times 10^{-6}$
- $x = 3$: $\hat{y}_4 = 0.5453 \implies (0.548 - 0.5453)^2 = (+0.0027)^2 = 7.29 \times 10^{-6}$
- $x = 4$: $\hat{y}_5 = 0.7250 \implies (0.725 - 0.7250)^2 = (0.0000)^2 = 0.00 \times 10^{-6}$

Sum of squared residuals:
$$\sum (y_i - \hat{y}_i)^2 = 2.430 \times 10^{-5}$$
$$s_{y/x} = \sqrt{\frac{2.430 \times 10^{-5}}{5 - 2}} = \sqrt{\frac{2.430 \times 10^{-5}}{3}} = \sqrt{8.10 \times 10^{-6}} = \mathbf{0.002846}$$

### Step 3: Limit of Detection (LOD) and Limit of Quantitation (LOQ)
Using IUPAC definition with blank standard deviation $s_{\text{blank}} = 0.0025$:
$$\text{LOD} = \frac{3.3 \cdot s_{\text{blank}}}{m} = \frac{3.3 \times 0.0025}{0.1797} = \frac{0.00825}{0.1797} = \mathbf{0.0459\,\mu\text{g}\cdot\text{mL}^{-1}}$$
$$\text{LOQ} = \frac{10 \cdot s_{\text{blank}}}{m} = \frac{10 \times 0.0025}{0.1797} = \frac{0.0250}{0.1797} = \mathbf{0.1391\,\mu\text{g}\cdot\text{mL}^{-1}}$$

### Step 4: Unknown Sample Concentration and Standard Error
For $A_0 = 0.420$:
$$x_0 = \frac{A_0 - c}{m} = \frac{0.420 - 0.0062}{0.1797} = \frac{0.4138}{0.1797} = \mathbf{2.3027\,\mu\text{g}\cdot\text{mL}^{-1}}$$

Compute the standard uncertainty $s_{x_0}$ for $M = 1$:
$$s_{x_0} = \frac{s_{y/x}}{m} \sqrt{\frac{1}{M} + \frac{1}{N} + \frac{(A_0 - \bar{y})^2}{m^2 S_{xx}}}$$
$$\frac{(A_0 - \bar{y})^2}{m^2 S_{xx}} = \frac{(0.420 - 0.3656)^2}{(0.1797)^2 \times 10.00} = \frac{(0.0544)^2}{0.03229 \times 10.00} = \frac{0.002959}{0.3229} = 0.00916$$
$$\sqrt{1 + \frac{1}{5} + 0.00916} = \sqrt{1.20916} = 1.0996$$
$$s_{x_0} = \frac{0.002846}{0.1797} \times 1.0996 = 0.01584 \times 1.0996 = \mathbf{0.0174\,\mu\text{g}\cdot\text{mL}^{-1}}$$
The concentration of phosphate in the unknown is reported as:
$$\mathbf{x_0 = (2.303 \pm 0.017)\,\mu\text{g}\cdot\text{mL}^{-1}}$$""",
                    "hints": ["Use least-squares slope and intercept formulas.", "LOD is 3.3 * s_blank / m and LOQ is 10 * s_blank / m."]
                },
                {
                    "id": "prob-1-7",
                    "problemNumber": "1.7",
                    "title": "Propagation of Logarithmic and Exponential Error in pH and Buffer Speciation",
                    "difficulty": "Honors Problem",
                    "statement": r"""A biochemist measures the pH of a physiological buffer solution containing acetic acid and sodium acetate using a glass electrode potentiometer. The measured pH is:
$$\text{pH} = 4.76 \pm 0.03$$
The thermodynamic acid dissociation constant of acetic acid is $K_a = (1.75 \pm 0.02) \times 10^{-5}\text{ M}$ ($pK_a = -\log_{10} K_a$).

1. Calculate the hydronium ion concentration $[\text{H}_3\text{O}^+]$ and its propagated absolute and relative uncertainties.
2. Calculate $pK_a$ and its propagated uncertainty $s_{pK_a}$.
3. Using the Henderson-Hasselbalch equation $\text{pH} = pK_a + \log_{10}\left(\frac{[\text{OAc}^-]}{[\text{HOAc}]}\right)$, determine the molar ratio $R = \frac{[\text{OAc}^-]}{[\text{HOAc}]}$ and its propagated relative uncertainty $\% s_R / R$.""",
                    "solution": r"""### Step 1: Hydronium Ion Concentration and Uncertainty
By definition:
$$[\text{H}_3\text{O}^+] = 10^{-\text{pH}} = 10^{-4.76} = \mathbf{1.7378 \times 10^{-5}\text{ M}}$$
The propagation of uncertainty for $y = 10^x$ is:
$$\frac{s_y}{y} = \ln(10) \cdot s_x = 2.3026 \cdot s_x$$
Here, $s_x = s_{\text{pH}} = 0.03$. Therefore:
$$\frac{s_{[\text{H}_3\text{O}^+]}}{[\text{H}_3\text{O}^+]} = 2.3026 \times 0.03 = 0.06908 \quad (\mathbf{6.91\%})$$
The absolute uncertainty is:
$$s_{[\text{H}_3\text{O}^+]} = (1.7378 \times 10^{-5}\text{ M}) \times 0.06908 = \mathbf{1.20 \times 10^{-6}\text{ M}}$$
Hence:
$$[\text{H}_3\text{O}^+] = (\mathbf{1.74 \pm 0.12}) \times 10^{-5}\text{ M}$$
*Observation*: A seemingly minor reading uncertainty of $\pm 0.03$ in pH produces a significant $\sim 7\%$ uncertainty in hydrogen ion concentration.

### Step 2: $pK_a$ and Its Uncertainty
$$pK_a = -\log_{10}(K_a) = -\log_{10}(1.75 \times 10^{-5}) = -(-4.7570) = \mathbf{4.757}$$
For $y = \log_{10}(x)$, the propagated uncertainty is:
$$s_y = 0.43429 \left(\frac{s_x}{x}\right)$$
Here, $\frac{s_{K_a}}{K_a} = \frac{0.02 \times 10^{-5}}{1.75 \times 10^{-5}} = 0.01143$ ($1.14\%$).
$$s_{pK_a} = 0.43429 \times 0.01143 = \mathbf{0.0050}$$
Thus:
$$pK_a = \mathbf{4.757 \pm 0.005}$$

### Step 3: Buffer Ratio ($R$) and Propagated Uncertainty
Rearranging Henderson-Hasselbalch:
$$\log_{10}(R) = \text{pH} - pK_a = 4.76 - 4.757 = 0.003$$
Therefore:
$$R = 10^{0.003} = \mathbf{1.007}$$

Let $u = \text{pH} - pK_a$. The absolute uncertainty in $u$ adds in quadrature:
$$s_u = \sqrt{s_{\text{pH}}^2 + s_{pK_a}^2} = \sqrt{(0.03)^2 + (0.0050)^2} = \sqrt{0.0009 + 0.000025} = \sqrt{0.000925} = \mathbf{0.0304}$$
Now, $R = 10^u$. The relative uncertainty in $R$ is:
$$\frac{s_R}{R} = 2.3026 \times s_u = 2.3026 \times 0.0304 = 0.0700 \quad (\mathbf{7.00\%})$$
The absolute uncertainty in the buffer ratio is:
$$s_R = 1.007 \times 0.0700 = \mathbf{0.0705}$$
Reporting the buffer acetate-to-acetic acid ratio:
$$\mathbf{R = \frac{[\text{OAc}^-]}{[\text{HOAc}]} = 1.01 \pm 0.07}$$""",
                    "hints": ["Remember that d(10^x)/dx = ln(10) * 10^x, so relative uncertainty is 2.3026 * s_x.", "When subtracting pH - pKa, absolute variances add in quadrature."]
                }
            ]
        },

        # =====================================================================
        # UNIT 2
        # =====================================================================
        {
            "id": "unit-2-sampling-procedures-sample-preparation",
            "unitNumber": 2,
            "title": "Unit 2: Sampling in Chemical Analysis, Representative Population & Sample Preparation",
            "leadSummary": "Exhaustive treatment of the analytical sampling paradox: bulk heterogeneities, Ingamells sampling constant, Visman sampling equation, probability sampling designs, particle size reduction, digestion thermodynamics (wet acid, microwave, alkali fusion), and sample preservation.",
            "simulations": [],
            "sections": [
                {
                    "id": "sec-2-1",
                    "secNumber": "2.1",
                    "title": "The Analytical Sampling Paradox: Bulk Heterogeneity, Target Population & Subsampling",
                    "content": r"""Analytical chemistry frequently confronts a staggering scale mismatch: an analyst may be tasked with determining the gold content of a $100,000\text{-ton}$ mineral ore deposit, the pesticide residue in a $20\text{-ton}$ grain silo, or trace heavy metals across a $50\text{-km}^2$ freshwater lake. Yet modern analytical instruments consume an analytical test portion typically weighing between $0.1\text{ g}$ and $1.0\text{ g}$.

### The Sampling Paradox
If the sub-gram test portion is not chemically and mineralogically representative of the bulk parent population, the most sophisticated spectrometer or ultra-high-precision balance will produce completely erroneous analytical conclusions. Experimental studies demonstrate that **sampling error is frequently 10 to 100 times larger** than the combined instrumental measurement error.

```
                      The Analytical Sampling Hierarchy
      ┌───────────────────────────────────────────────────────────────┐
      │  Gross Target Population (e.g., 100,000 kg Mineral Ore Lot)   │
      └───────────────────────────────┬───────────────────────────────┘
                                      │ Sampling Plan (Augers, Increments)
                                      ▼
      ┌───────────────────────────────────────────────────────────────┐
      │  Gross Sample (e.g., 50 kg Combined Increments)               │
      └───────────────────────────────┬───────────────────────────────┘
                                      │ Primary Crushing & Sieve Milling
                                      ▼
      ┌───────────────────────────────────────────────────────────────┐
      │  Subsample / Laboratory Sample (e.g., 500 g, -100 mesh)       │
      └───────────────────────────────┬───────────────────────────────┘
                                      │ Pulverization & Homogenization
                                      ▼
      ┌───────────────────────────────────────────────────────────────┐
      │  Analytical Test Portion (e.g., 0.2500 g Digested Aliquot)    │
      └───────────────────────────────────────────────────────────────┘
```

### Definitions in the Sampling Chain
1. **Target Population**: The entire collection of matter whose chemical composition is to be characterized.
2. **Sampling Unit**: Distinct portions of the population that can be separately sampled (e.g., individual bags of fertilizer, discrete soil core intervals, or hourly wastewater effluent discharges).
3. **Gross Sample**: The composite material formed by gathering multiple individual primary increments extracted from the target population.
4. **Laboratory Sample**: A reduced, pulverized, and homogenized fraction of the gross sample sent to the analytical laboratory (typically $100\text{--}500\text{ g}$).
5. **Analytical Test Portion**: The precise aliquot ($0.1\text{--}1.0\text{ g}$) weighed on an analytical balance and subjected to chemical dissolution and measurement.""",
                    "simulations": []
                },
                {
                    "id": "sec-2-2",
                    "secNumber": "2.2",
                    "title": "Sampling Statistics: Ingamells Sampling Constant & Visman Sampling Equation",
                    "content": r"""To place sampling on a rigorous mathematical foundation, analytical chemists employ probabilistic models describing the distribution of analyte-bearing particles within segregated or randomized particulate matrices.

### Ingamells Sampling Constant ($K_s$)
In 1974, C. O. Ingamells established that for a heterogeneous particulate material possessing random, independent segregation of two mineral phases (e.g., rich ore grains dispersed in barren gangue), the relative standard deviation of sampling ($\% \text{RSD}_s$) is inversely proportional to the square root of the analytical sample mass $w$:
$$\% \text{RSD}_s = \frac{s_s}{\bar{x}} \times 100\% = \frac{\sqrt{K_s}}{\sqrt{w}} \implies K_s = w \cdot (\% \text{RSD}_s)^2$$
where:
- $w$ is the mass of the analytical test portion (typically in grams).
- $\% \text{RSD}_s$ is the percentage relative standard deviation attributable strictly to sampling heterogeneity.
- $K_s$ is the **Ingamells Sampling Constant**, representing the theoretical minimum sample mass (in grams) required to restrict sampling uncertainty to $\pm 1.0\%$ at the $68\%$ confidence level.

*Practical Application*: If an ore requires $w_1 = 1.0\text{ g}$ to achieve a sampling uncertainty of $\pm 5\%$, the Ingamells constant is:
$$K_s = (1.0\text{ g}) \times (5)^2 = 25\text{ g}$$
To reduce the sampling uncertainty to $\pm 1.0\%$, the required test portion mass is:
$$w_2 = \frac{K_s}{(\% \text{RSD}_s)^2} = \frac{25}{(1.0)^2} = 25\text{ g}$$

### Visman Sampling Equation
J. Visman generalized sampling theory to account for both microscopic random composition variance and macroscopic spatial segregation variance:
$$s_s^2 = \frac{A}{w} + \frac{B}{N}$$
where:
- $s_s^2$ is the total sampling variance.
- $A$ is the **homogeneity constant**, describing random compositional variability at the particle level (decreases with increasing subsample mass $w$).
- $B$ is the **segregation constant**, describing macroscopic spatial gradients or stratification across the bulk lot (decreases with increasing number of primary sample increments $N$).

To minimize overall sampling variance economically, an analytical protocol must balance increasing the mass of individual test portions ($w$) to diminish $A/w$ against increasing the total number of collected primary increments ($N$) to diminish $B/N$.""",
                    "simulations": []
                },
                {
                    "id": "sec-2-3",
                    "secNumber": "2.3",
                    "title": "Probability Sampling Strategies: Random, Systematic, Stratified & Cluster Protocols",
                    "content": r"""The spatial and temporal architecture of collecting increments determines whether a sample is statistically unbiased and representative. Four primary probability sampling designs are recognized in environmental and analytical protocols:

```
┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│     Simple Random Sampling      │   │       Systematic Sampling       │
│   • Random grid coordinates     │   │   • Fixed temporal/spatial steps│
│   • Every unit equal chance     │   │   • Risk: periodic bias         │
└─────────────────────────────────┘   └─────────────────────────────────┘
┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│       Stratified Sampling       │   │        Cluster Sampling         │
│   • Divided into homogeneous    │   │   • Naturally clustered units   │
│     strata (e.g. soil horizons) │   │     (e.g. barrels, railcars)    │
└─────────────────────────────────┘   └─────────────────────────────────┘
```

#### 1. Simple Random Sampling
Every individual unit or increment in the target population possesses an identical, non-zero probability of selection. Points are chosen using pseudo-random coordinate generation. Simple random sampling provides mathematically unbiased parameter estimates but can yield uneven spatial coverage across extensive geographic regions.

#### 2. Systematic Sampling
Sample increments are gathered at uniformly spaced spatial or temporal intervals (e.g., collecting $100\text{ mL}$ of river water every 2 hours, or sampling every 50th bag of animal feed off a conveyor belt).
*Critical Caution*: If the target population contains a hidden periodic frequency (e.g., cyclic batch discharges from an upstream factory every 4 hours), systematic sampling synchronized with the periodicity will produce massive systematic bias.

#### 3. Stratified Sampling
The heterogeneous target population is segmented into distinct, internally homogeneous sub-populations termed **strata** (e.g., soil stratified by depth horizons A, B, and C; or a lake stratified into epilimnion, thermocline, and hypolimnion). Random increments are then drawn from each stratum in proportion to its total volume or mass:
$$N_k = N_{\text{total}} \left(\frac{W_k \sigma_k}{\sum W_j \sigma_j}\right)$$
Stratified sampling drastically reduces overall sampling variance compared to simple random sampling of the unsegmented bulk.

#### 4. Cluster Sampling
Employed when the population is naturally divided into discrete clusters or containers (e.g., 500 drums of chemical waste, or 20 railcars of bauxite). A subset of clusters is randomly selected, and increments are drawn either exhaustively or randomly from within the chosen clusters.""",
                    "simulations": []
                },
                {
                    "id": "sec-2-4",
                    "secNumber": "2.4",
                    "title": "Mechanical Sample Preparation: Particle Size Reduction, Sieve Classification & Coning/Quartering",
                    "content": r"""Once the gross sample arrives at the preparation facility, it must undergo systematic particle size reduction and subsampling to generate a fine, homogeneous laboratory sample without introducing cross-contamination or chemical alteration.

### Particle Size Reduction Kinetics
According to sampling theory, the number of particles $n$ contained within a test portion of mass $w$ is inversely proportional to the cube of the average particle diameter $d$:
$$n \propto \frac{w}{\rho \cdot d^3}$$
Because sampling variance $s_s^2 \propto 1/n$, **reducing particle diameter $d$ by a factor of 10 increases particle count $n$ by a factor of 1000**, slashing sampling variance by three orders of magnitude!

### Stages of Mechanical Comminution
1. **Primary Crushing**: Jaw crushers reduce coarse rocks ($10\text{--}50\text{ cm}$) down to pebble size ($< 1\text{ cm}$).
2. **Secondary Grinding**: Disc pulverizers and ball mills reduce granules down to coarse sand ($< 1\text{ mm}$).
3. **Fine Pulverization**: Planetary ball mills, agate mortar and pestle, or shatterboxes grind the material to pass standard laboratory sieves (typically $-100\text{ mesh}$ or $-200\text{ mesh}$, corresponding to particle diameters $< 74\,\mu\text{m}$).

### Contamination Hazards During Grinding
Grinding equipment abrades during comminution, introducing foreign elements into the sample:
- **Steel/Cast Iron Mills**: Introduce severe iron, chromium, nickel, and manganese contamination.
- **Tungsten Carbide Mills**: Introduce tungsten and cobalt binder contamination.
- **Agate Mortars**: Composed of pure silica ($\text{SiO}_2$); safe for metal determinations but unsuitable for silicate analysis.

### Subsampling: Coning and Quartering
To split a multi-kilogram coarse sample into an unbiased subsample without segregation bias:
1. The pulverized sample is poured into a symmetrical conical pile.
2. The apex of the cone is flattened into a uniform disc.
3. The disc is divided into four equal quadrants across perpendicular diameters.
4. Two diagonally opposite quarters are retained and blended; the remaining two quarters are discarded.
5. The procedure is repeated recursively until the desired laboratory sample mass is achieved.""",
                    "simulations": []
                },
                {
                    "id": "sec-2-5",
                    "secNumber": "2.5",
                    "title": "Moisture Equilibration: Essential vs Non-Essential Water & Loss on Ignition (LOI)",
                    "content": r"""Water content is an insidious source of error in quantitative solid-state analysis. An uncalibrated moisture content inflates sample mass, causing systematic underestimation of analyte concentrations.

### Classification of Water in Minerals and Solids
Analytical chemistry classifies water into two major categories:

#### 1. Non-Essential Water
Water not required for the stoichiometric characterization or crystal lattice identity of the solid:
- **Adsorbed Moisture**: Water molecules bound weakly to the outer particle surfaces via dipole interactions; fluctuates with ambient relative humidity.
- **Occluded Water**: Microscopic liquid droplets trapped mechanically within microscopic cavities during crystal growth.
- **Inverted / Sorbed Water**: Held in porous materials (e.g., zeolites, silica gels).
*Removal*: Readily expelled by oven heating at $105^\circ\text{C}\text{--}110^\circ\text{C}$ for 2 hours to constant mass.

#### 2. Essential Water
Water present in stoichiometric proportions as an integral part of the crystal structure:
- **Water of Crystallization (Hydrates)**: Stoichiometrically bound in the lattice, such as $\text{CuSO}_4 \cdot 5\text{H}_2\text{O}$ or $\text{BaCl}_2 \cdot 2\text{H}_2\text{O}$. Expelled at elevated temperatures ($120^\circ\text{C}\text{--}250^\circ\text{C}$).
- **Constitution Water (Hydroxyl Groups)**: Present as structural $\text{OH}^-$ ions (e.g., in clays, micas, $\text{Ca(OH)}_2$). Dehydroxylates only upon severe thermal calcination ($500^\circ\text{C}\text{--}1000^\circ\text{C}$):
$$2\,\text{OH}^- \xrightarrow{\Delta} \text{H}_2\text{O}\uparrow + \text{O}^{2-}$$

### Loss on Ignition (LOI)
Loss on Ignition measures the total percentage mass lost when a dried sample is ignited in a muffle furnace at $950^\circ\text{C}\text{--}1050^\circ\text{C}$ to constant mass:
$$\% \text{LOI} = \frac{m_{\text{dried}} - m_{\text{ignited}}}{m_{\text{dried}}} \times 100\%$$
LOI accounts for the simultaneous release of constitutional water, decomposition of carbonates ($\text{CO}_3^{2-} \to \text{CO}_2\uparrow$), and combustion of organic matter.""",
                    "simulations": []
                },
                {
                    "id": "sec-2-6",
                    "secNumber": "2.6",
                    "title": "Wet Chemical Dissolution & Acid Digestion Thermodynamics (Aqua Regia, HF, HClO4)",
                    "content": r"""Most modern instrumental techniques (AAS, ICP-OES, UV-Vis, titrimetry) require samples in homogeneous aqueous solution. Converting refractory solid matrices into clear solutions demands deep understanding of mineral acid oxidation-reduction potentials, complexation chemistry, and thermochemistry.

### Properties and Applications of Digestion Mineral Acids

#### 1. Hydrochloric Acid ($\text{HCl}$, $12\text{ M}$, $37\text{ wt}\%$)
A non-oxidizing acid ($E^\circ_{\text{H}^+/\text{H}_2} = 0.00\text{ V}$) acting through hydronium attack and strong chloro-complexation:
$$\text{Fe}_2\text{O}_3 + 6\,\text{HCl} \to 2\,[\text{FeCl}_4]^- + 2\,\text{H}^+ + 3\,\text{H}_2\text{O}$$
Dissolves metal carbonates, phosphates, oxides, and sulfides. Forms soluble chloride complexes with $\text{Fe}^{3+}, \text{Zn}^{2+}, \text{Sn}^{4+}$. Incompatible with $\text{Ag}^+, \text{Pb}^{2+}, \text{Hg}_2^{2+}$ due to insoluble chloride precipitation.

#### 2. Nitric Acid ($\text{HNO}_3$, $16\text{ M}$, $70\text{ wt}\%$)
A powerful oxidizing mineral acid ($E^\circ = +0.96\text{ V}$ in acid):
$$\text{NO}_3^- + 4\,\text{H}^+ + 3\,e^- \to \text{NO}\uparrow + 2\,\text{H}_2\text{O}$$
Oxidizes base metals and decomposes biological/organic matrices into $\text{CO}_2$ and $\text{H}_2\text{O}$. Nearly all metal nitrates are universally soluble in water.

#### 3. Aqua Regia ($3:1 \ \text{v/v} \ \text{HCl} : \text{HNO}_3$)
Combines the ferocious oxidation power of nitric acid with the intense complexing capability of chloride ions. In situ reaction generates nitrosyl chloride and nascent chlorine:
$$\text{HNO}_3 + 3\,\text{HCl} \to \text{NOCl} + \text{Cl}_2 + 2\,\text{H}_2\text{O}$$
Readily dissolves noble metals (gold, platinum) by lowering the formal redox potential via chloro-complexation:
$$\text{Au} + 3\,\text{NO}_3^- + 4\,\text{Cl}^- + 6\,\text{H}^+ \to [\text{AuCl}_4]^- + 3\,\text{NO}_2\uparrow + 3\,\text{H}_2\text{O}$$

#### 4. Hydrofluoric Acid ($\text{HF}$, $29\text{ M}$, $48\text{ wt}\%$)
The unique mineral acid capable of dissolving refractory silicate matrices by cleaving extremely strong $\text{Si}-\text{O}$ bonds ($\text{BDE} \approx 460\text{ kJ}\cdot\text{mol}^{-1}$) to form volatile silicon tetrafluoride gas:
$$\text{SiO}_2 + 4\,\text{HF} \to \text{SiF}_4\uparrow + 2\,\text{H}_2\text{O}$$
$$\text{SiO}_2 + 6\,\text{HF} \to \text{H}_2[\text{SiF}_6] + 2\,\text{H}_2\text{O}$$
*Crucial Safety & Operational Rules*: HF dissolves laboratory borosilicate glassware; must be handled exclusively in Teflon (PTFE) or platinum vessels. Severe contact poison: penetrates skin and precipitates bone calcium ($\text{CaF}_2$), causing systemic cardiac arrest.

#### 5. Perchloric Acid ($\text{HClO}_4$, $70\text{ wt}\%$)
When cold and dilute, perchloric acid acts as a harmless strong acid. However, when concentrated ($70\%$) and heated to its boiling point ($203^\circ\text{C}$), it becomes one of the most ferocious oxidizing agents known ($E^\circ \approx +1.39\text{ V}$).
*Explosion Hazard*: Extremely hazardous in the presence of easily oxidizable organic matter, rubber, or wooden fume hoods. Must be manipulated exclusively in dedicated wash-down fume hoods with water scrubbing.""",
                    "simulations": []
                },
                {
                    "id": "sec-2-7",
                    "secNumber": "2.7",
                    "title": "Closed-Vessel Microwave-Assisted Digestion & High-Temperature Alkali Flux Fusion Chemistry",
                    "content": r"""Refractory ores (zircon, chromite, corundum, rutile) and volatile trace analytes (arsenic, mercury, selenium) present insurmountable hurdles for open-beaker hot-plate digestion. Two advanced techniques resolve these challenges: **closed-vessel microwave digestion** and **high-temperature alkali fusion**.

### Closed-Vessel Microwave-Assisted Digestion
Samples and concentrated acid mixtures are sealed in heavy-walled Teflon (PTFE or PFA) vessels encased in high-strength composite polymer sleeves and irradiated with microwave energy ($2.45\text{ GHz}$).

```
                  Closed-Vessel Microwave Digestion Chamber
                     ┌────────────────────────────────┐
                     │   Safety Burst Vent Rupture    │
                     └───────────────┬────────────────┘
                                     │
                     ┌───────────────┴────────────────┐
                     │ PFA / TFM Teflon Liner         │
                     │                                │
                     │   Acid Vapor (P ~ 40-80 bar)   │
                     │                                │
                     │   Liquid Core (T ~ 220-260°C)  │
                     │   • Dipole rotation heating    │
                     │   • Ionic conduction heating   │
                     │   • Complete recovery of Hg/As │
                     └────────────────────────────────┘
```

#### Physical Mechanisms of Microwave Heating
1. **Dipole Rotation**: Polar solvent molecules (water, $\text{HNO}_3$) oscillate at $2.45 \times 10^9\text{ cycles/sec}$ to align with the oscillating electric field, dissipating kinetic energy as thermal friction.
2. **Ionic Conduction**: Dissociated ions migrate back and forth with the alternating field, colliding with solvent molecules to generate volumetric core heating.

#### Advantages Over Open Systems
- **Superheating**: High pressure ($40\text{--}80\text{ bar}$) elevates acid boiling points from $120^\circ\text{C}$ to $> 240^\circ\text{C}$, boosting reaction kinetics by orders of magnitude via the Arrhenius equation.
- **Volatile Retention**: Sealed digestion vessels quantitatively retain volatile elements ($\text{Hg}, \text{As}, \text{Se}, \text{B}, \text{Sn}$) that would escape open beakers.
- **Reduced Reagent Consumption**: Requires only $5\text{--}10\text{ mL}$ of ultra-pure acid, slashing procedural blank contamination.

### High-Temperature Alkali Flux Fusion Chemistry
When mineral lattices are completely inert to acid digestion (e.g., corundum $\alpha\text{-Al}_2\text{O}_3$, rutile $\text{TiO}_2$, zircon $\text{ZrSiO}_4$), they are blended with a 10- to 20-fold mass excess of an anhydrous inorganic salt (**flux**) and melted at $900^\circ\text{C}\text{--}1100^\circ\text{C}$ in platinum, graphite, or nickel crucibles.

| Flux Reagent | Melting Point | Crucible Type | Target Refractory Minerals |
| :--- | :---: | :---: | :--- |
| **Lithium Metaborate ($\text{LiBO}_2$)** | $845^\circ\text{C}$ | Graphite, Platinum | Silicates, aluminosilicates, basaltic rocks |
| **Lithium Tetraborate ($\text{Li}_2\text{B}_4\text{O}_7$)** | $920^\circ\text{C}$ | Platinum | Basic rocks, iron ores, bauxites |
| **Sodium Carbonate ($\text{Na}_2\text{CO}_3$)** | $851^\circ\text{C}$ | Platinum | Silicates, quartz, baryte ($\text{BaSO}_4$) |
| **Potassium Pyrosulfate ($\text{K}_2\text{S}_2\text{O}_7$)** | $419^\circ\text{C}$ | Vycor, Platinum | Basic metal oxides ($\text{Fe}_2\text{O}_3, \text{TiO}_2, \text{ZrO}_2$) |
| **Sodium Peroxide ($\text{Na}_2\text{O}_2$)** | $460^\circ\text{C}$ | Zirconium, Nickel | Chromite ($\text{FeCr}_2\text{O}_4$), sulfides, platinum ores |

#### Reaction Chemistry: Borate Fusion of Silicates
Molten lithium metaborate acts as a Lewis acid/base solvent, disrupting refractory network-covalent silicate lattices into soluble mononuclear borate-silicate complexes:
$$\text{ZrSiO}_4 + 2\,\text{LiBO}_2 \xrightarrow{1050^\circ\text{C}} \text{Li}_2\text{ZrO}_3 + \text{B}_2\text{O}_3 + \text{SiO}_2$$
Upon cooling, the molten bead is quenched into dilute nitric or hydrochloric acid, where it dissolves rapidly and completely to yield a clear, stable analytical solution.""",
                    "simulations": []
                }
            ],
            "problems": [
                {
                    "id": "prob-2-1",
                    "problemNumber": "2.1",
                    "title": "Ingamells Sampling Constant and Required Subsample Mass",
                    "difficulty": "Foundational",
                    "statement": r"""A mining geochemistry laboratory evaluates the sampling precision of a crushed copper porphyry ore. A series of preliminary test analyses performed on $w_1 = 0.500\text{ g}$ subsamples yields an experimental relative standard deviation attributable to sampling heterogeneity of:
$$\% \text{RSD}_{s1} = 4.20\%$$

Calculate:
1. The Ingamells Sampling Constant ($K_s$) for this crushed ore in grams.
2. The minimum analytical test portion mass ($w_2$) required to restrict the sampling uncertainty to no more than $\pm 1.00\%$ at the $68\%$ confidence level.
3. If an analyst weighs an aliquot of only $0.100\text{ g}$, calculate the anticipated relative standard deviation of sampling ($\% \text{RSD}_{s3}$).""",
                    "solution": r"""### Step 1: Calculation of Ingamells Sampling Constant ($K_s$)
By definition of Ingamells' equation:
$$K_s = w \cdot (\% \text{RSD}_s)^2$$
Substituting $w_1 = 0.500\text{ g}$ and $\% \text{RSD}_{s1} = 4.20\%$:
$$K_s = (0.500\text{ g}) \times (4.20)^2 = 0.500 \times 17.64 = \mathbf{8.82\text{ g}}$$
*Physical Interpretation*: $K_s = 8.82\text{ g}$ represents the minimum single test portion mass required to guarantee a sampling relative standard deviation of $\pm 1.0\%$.

### Step 2: Minimum Test Portion Mass for 1.00% Sampling Uncertainty
Setting $\% \text{RSD}_{s2} = 1.00\%$:
$$w_2 = \frac{K_s}{(\% \text{RSD}_{s2})^2} = \frac{8.82\text{ g}}{(1.00)^2} = \mathbf{8.82\text{ g}}$$

### Step 3: Anticipated Sampling Uncertainty for a 0.100 g Aliquot
Setting $w_3 = 0.100\text{ g}$:
$$\% \text{RSD}_{s3} = \frac{\sqrt{K_s}}{\sqrt{w_3}} = \frac{\sqrt{8.82}}{\sqrt{0.100}} = \frac{2.9698}{0.3162} = \mathbf{9.39\%}$$
*Analytical Insight*: Weighing only $0.100\text{ g}$ magnifies sampling error to nearly $10\%$, completely overwhelming any high-precision instrumental measurement.""",
                    "hints": ["K_s = w * (% RSD)^2.", "To reduce % RSD by a factor of k, test portion mass must increase by k^2."]
                },
                {
                    "id": "prob-2-2",
                    "problemNumber": "2.2",
                    "title": "Visman Sampling Equation and Variance Component Separation",
                    "difficulty": "Advanced",
                    "statement": r"""To characterize sampling variability in a coal shipment being evaluated for sulfur content, an analytical team performs two series of sampling experiments:
- **Experiment 1**: Collected $N_1 = 20$ sample increments, each weighing $w_1 = 20.0\text{ g}$. Total sampling variance measured is $s_1^2 = 0.0850$.
- **Experiment 2**: Collected $N_2 = 20$ sample increments, each weighing $w_2 = 80.0\text{ g}$. Total sampling variance measured is $s_2^2 = 0.0400$.

Using the Visman sampling equation $s^2 = \frac{A}{w} + \frac{B}{N}$:
1. Set up the system of simultaneous equations and calculate the Visman **homogeneity constant** $A$ (in $\text{g}$) and **segregation constant** $B$.
2. Calculate the projected sampling variance if the laboratory collects $N = 40$ increments weighing $w = 100.0\text{ g}$ each.
3. Determine whether increasing subsample mass $w$ or increasing increment number $N$ is more effective for suppressing overall variance.""",
                    "solution": r"""### Step 1: Setting up Simultaneous Visman Equations
Visman's equation:
$$s^2 = \frac{A}{w} + \frac{B}{N}$$
From Experiment 1 ($w_1 = 20.0, N_1 = 20$):
$$\frac{A}{20.0} + \frac{B}{20} = 0.0850 \implies 0.050\,A + 0.050\,B = 0.0850 \implies A + B = 1.700 \quad \text{(Eq. 1)}$$

From Experiment 2 ($w_2 = 80.0, N_2 = 20$):
$$\frac{A}{80.0} + \frac{B}{20} = 0.0400 \implies 0.0125\,A + 0.050\,B = 0.0400 \quad \text{(Eq. 2)}$$

Subtract Eq. 2 from Eq. 1:
$$(0.050 - 0.0125) A = 0.0850 - 0.0400$$
$$0.0375\,A = 0.0450 \implies A = \frac{0.0450}{0.0375} = \mathbf{1.200\text{ g}}$$

Substitute $A = 1.200$ back into Eq. 1:
$$1.200 + B = 1.700 \implies B = \mathbf{0.500}$$

### Step 2: Projected Sampling Variance for N = 40, w = 100.0 g
$$s^2 = \frac{A}{w} + \frac{B}{N} = \frac{1.200}{100.0} + \frac{0.500}{40} = 0.0120 + 0.0125 = \mathbf{0.0245}$$
The standard deviation of sampling is $s = \sqrt{0.0245} = \mathbf{0.1565\% \text{ sulfur}}$.

### Step 3: Analysis of Variance Suppression
At $w = 100\text{ g}$ and $N = 40$, the random compositional component ($A/w = 0.0120$) and the segregation component ($B/N = 0.0125$) contribute almost equally.
If subsample mass $w$ is doubled to $200\text{ g}$, variance becomes $0.0060 + 0.0125 = 0.0185$ (a $24\%$ reduction).
If increment count $N$ is doubled to $80$, variance becomes $0.0120 + 0.00625 = 0.01825$ (a $25.5\%$ reduction).
Because $B = 0.500$ indicates significant spatial stratification in the coal shipment, increasing the number of increments $N$ taken from different physical locations across the pile is slightly more cost-effective.""",
                    "hints": ["Write two equations with two unknowns A and B.", "Subtracting eliminates the B/N term since N is identical in both initial experiments."]
                },
                {
                    "id": "prob-2-3",
                    "problemNumber": "2.3",
                    "title": "Particle Size Reduction and Number of Particles Sampling Proof",
                    "difficulty": "Intermediate",
                    "statement": r"""A ground mineral mixture consists of spherical particles of galena ($\text{PbS}$, density $\rho = 7.50\text{ g}\cdot\text{cm}^{-3}$) containing $86.6\text{ wt}\% \text{ Pb}$ dispersed randomly in quartz gangue ($\text{SiO}_2$, density $\rho = 2.65\text{ g}\cdot\text{cm}^{-3}$). The overall lead content in the ore is $1.00\text{ wt}\% \text{ Pb}$.

1. If the ore is crushed to a uniform particle diameter of $d_1 = 1.00\text{ mm}$ ($0.100\text{ cm}$), calculate the mass of a single galena particle.
2. In a $1.00\text{ g}$ analytical test portion, calculate the average number of galena particles present ($n$).
3. Using Poisson particle counting statistics where relative sampling standard deviation $\% \text{RSD} = \frac{1}{\sqrt{n}} \times 100\%$, calculate the expected sampling uncertainty for the $1.00\text{ mm}$ material.
4. If the ore is finely pulverized to $d_2 = 0.074\text{ mm}$ ($-200\text{ mesh}$), determine the new particle count and the resulting relative standard deviation of sampling.""",
                    "solution": r"""### Step 1: Mass of a Single Galena Particle ($d_1 = 1.00\text{ mm}$)
Radius $r = 0.050\text{ cm}$. Volume of sphere:
$$V = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi (0.050)^3 = 5.236 \times 10^{-4}\text{ cm}^3$$
Mass of one particle:
$$m_p = V \times \rho = (5.236 \times 10^{-4}\text{ cm}^3) \times (7.50\text{ g}\cdot\text{cm}^{-3}) = \mathbf{3.927 \times 10^{-3}\text{ g} = 3.927\text{ mg}}$$

### Step 2: Number of Galena Particles in 1.00 g Ore Aliquot
A $1.00\text{ g}$ ore sample containing $1.00\text{ wt}\% \text{ Pb}$ contains:
$$m_{\text{Pb}} = 1.00\text{ g} \times 0.0100 = 0.0100\text{ g Pb}$$
Because galena is $86.6\text{ wt}\% \text{ Pb}$, total mass of galena is:
$$m_{\text{PbS}} = \frac{0.0100\text{ g}}{0.866} = 0.01155\text{ g = 11.55 mg}$$
Average number of galena particles:
$$n_1 = \frac{m_{\text{PbS}}}{m_p} = \frac{1.155 \times 10^{-2}\text{ g}}{3.927 \times 10^{-3}\text{ g}} = \mathbf{2.94 \approx 3\text{ particles!}}$$

### Step 3: Sampling Uncertainty for 1.00 mm Particles
With only $\sim 3$ particles of analyte present in the test portion:
$$\% \text{RSD}_1 = \frac{1}{\sqrt{n_1}} \times 100\% = \frac{1}{\sqrt{2.94}} \times 100\% = \mathbf{58.3\%}$$
*Conclusion*: Catastrophic sampling failure! A $1.00\text{ g}$ aliquot might contain 1 particle (yielding $0.34\%\text{ Pb}$) or 5 particles (yielding $1.70\%\text{ Pb}$).

### Step 4: Fine Pulverization to $d_2 = 0.074\text{ mm}$ ($-200\text{ mesh}$)
The particle diameter decreases by a factor:
$$\frac{d_1}{d_2} = \frac{1.00\text{ mm}}{0.074\text{ mm}} = 13.514$$
Because particle mass scales as $d^3$, the mass of a single particle decreases by:
$$(13.514)^3 = 2468$$
Consequently, the number of galena particles increases by a factor of $2468$:
$$n_2 = 2.94 \times 2468 = \mathbf{7256\text{ particles}}$$
The new relative standard deviation of sampling is:
$$\% \text{RSD}_2 = \frac{1}{\sqrt{7256}} \times 100\% = \frac{1}{85.18} \times 100\% = \mathbf{1.17\%}$$
*Analytical Lesson*: Pulverizing the ore from $1.00\text{ mm}$ to $-200\text{ mesh}$ improves sampling precision from an unworkable $\pm 58\%$ down to an acceptable $\pm 1.17\%$, proving why particle size reduction is mandatory prior to weighing.""",
                    "hints": ["Volume scales as d^3, so particle count scales inversely as d^3.", "Poisson counting uncertainty is 1 / sqrt(n)."]
                },
                {
                    "id": "prob-2-4",
                    "problemNumber": "2.4",
                    "title": "Stoichiometry and HF Consumption in Closed-Vessel Silicate Digestion",
                    "difficulty": "Intermediate",
                    "statement": r"""A $0.2500\text{ g}$ geological basalt standard containing $52.0\text{ wt}\% \ \text{SiO}_2$ and $15.0\text{ wt}\% \ \text{Al}_2\text{O}_3$ is digested in a closed PTFE microwave vessel using a mixture of concentrated hydrofluoric acid ($48.0\text{ wt}\% \ \text{HF}$, density $\rho = 1.15\text{ g}\cdot\text{mL}^{-1}$) and nitric acid.
1. Write the balanced chemical equations for the complete dissolution of $\text{SiO}_2$ and $\text{Al}_2\text{O}_3$ by hydrofluoric acid to form hexafluorosilicic acid ($\text{H}_2\text{SiF}_6$) and fluoroaluminate complexes ($[\text{AlF}_6]^{3-}$).
2. Calculate the stoichiometric minimum volume of concentrated $48.0\text{ wt}\% \ \text{HF}$ (in $\text{mL}$) required to dissolve both oxides completely.
3. Why is an excess of boric acid ($\text{H}_3\text{BO}_3$) routinely added after microwave cooling prior to nebulization into an ICP-OES instrument?""",
                    "solution": r"""### Step 1: Balanced Dissolution Reactions
1. For Silica ($\text{SiO}_2$):
$$\text{SiO}_2 + 6\,\text{HF} \to \text{H}_2\text{SiF}_6 + 2\,\text{H}_2\text{O}$$
2. For Alumina ($\text{Al}_2\text{O}_3$):
$$\text{Al}_2\text{O}_3 + 12\,\text{HF} \to 2\,[\text{AlF}_6]^{3-} + 6\,\text{H}^+ + 3\,\text{H}_2\text{O}$$

### Step 2: Stoichiometric Calculation of Required HF
Molar masses:
- $\text{SiO}_2 = 60.084\text{ g}\cdot\text{mol}^{-1}$
- $\text{Al}_2\text{O}_3 = 101.961\text{ g}\cdot\text{mol}^{-1}$
- $\text{HF} = 20.006\text{ g}\cdot\text{mol}^{-1}$

Masses in $0.2500\text{ g}$ basalt:
$$m_{\text{SiO}_2} = 0.2500\text{ g} \times 0.520 = 0.1300\text{ g}$$
$$m_{\text{Al}_2\text{O}_3} = 0.2500\text{ g} \times 0.150 = 0.0375\text{ g}$$

Moles of oxides:
$$n_{\text{SiO}_2} = \frac{0.1300}{60.084} = 2.1636 \times 10^{-3}\text{ mol}$$
$$n_{\text{Al}_2\text{O}_3} = \frac{0.0375}{101.961} = 3.6779 \times 10^{-4}\text{ mol}$$

Stoichiometric moles of $\text{HF}$ required:
$$n_{\text{HF}} = 6 \times n_{\text{SiO}_2} + 12 \times n_{\text{Al}_2\text{O}_3}$$
$$n_{\text{HF}} = 6(2.1636 \times 10^{-3}) + 12(3.6779 \times 10^{-4}) = 0.01298 + 0.00441 = \mathbf{0.01739\text{ mol HF}}$$

Mass of pure $\text{HF}$:
$$m_{\text{HF}} = 0.01739\text{ mol} \times 20.006\text{ g}\cdot\text{mol}^{-1} = 0.3479\text{ g HF}$$
Mass of $48.0\text{ wt}\%$ solution:
$$m_{\text{soln}} = \frac{0.3479\text{ g}}{0.480} = 0.7248\text{ g}$$
Volume of concentrated $\text{HF}$ ($\rho = 1.15\text{ g/mL}$):
$$V_{\text{HF}} = \frac{0.7248\text{ g}}{1.15\text{ g}\cdot\text{mL}^{-1}} = \mathbf{0.630\text{ mL}}$$
In practice, analysts employ $3.0\text{--}5.0\text{ mL}$ of concentrated $\text{HF}$ ($5$- to $8$-fold stoichiometric excess) to ensure complete dissolution kinetics.

### Step 3: Function of Boric Acid Complexation
Free fluoride ($\text{F}^-$) in solution severely etches quartz nebulizers, spray chambers, and torches in ICP-OES and AAS instruments. Adding saturated boric acid ($\text{H}_3\text{BO}_3$) sequesters toxic fluoride ions through the exothermic formation of stable fluoroboric acid:
$$\text{H}_3\text{BO}_3 + 4\,\text{HF} \to \text{HBF}_4 + 3\,\text{H}_2\text{O}$$
This complexation neutralizes HF corrosiveness, protects glass optics, and dissolves insoluble rare-earth and alkaline-earth fluoride precipitates (such as $\text{CaF}_2, \text{MgF}_2$).""",
                    "hints": ["Each mole of SiO2 consumes 6 moles of HF; each mole of Al2O3 consumes 12 moles of HF.", "Calculate mass of solution, then divide by density to get volume."]
                },
                {
                    "id": "prob-2-5",
                    "problemNumber": "2.5",
                    "title": "Thermodynamics of High-Temperature Pyrosulfate Fusion of Rutile (TiO2)",
                    "difficulty": "Honors Problem",
                    "statement": r"""A $0.5000\text{ g}$ sample of heavy mineral sand containing $95.0\text{ wt}\% \ \text{TiO}_2$ (rutile) is completely inert to hot concentrated mineral acids. The sample is transferred to a platinum crucible and fused at $600^\circ\text{C}$ with $5.000\text{ g}$ of molten potassium pyrosulfate ($\text{K}_2\text{S}_2\text{O}_7$).
1. Write the chemical equation for the thermal decomposition of molten pyrosulfate to release sulfur trioxide ($\text{SO}_3$).
2. Write the balanced equation for the acidic attack of $\text{SO}_3$ upon titanium dioxide to form titanyl sulfate ($\text{TiOSO}_4$).
3. Calculate the stoichiometric mass of $\text{K}_2\text{S}_2\text{O}_7$ consumed during the complete conversion of rutile in this sample ($M_{\text{TiO}_2} = 79.866\text{ g}\cdot\text{mol}^{-1}, M_{\text{K}_2\text{S}_2\text{O}_7} = 254.32\text{ g}\cdot\text{mol}^{-1}$).
4. Explain why the fused cake must be dissolved in chilled dilute sulfuric acid rather than warm neutral water.""",
                    "solution": r"""### Step 1: Pyrosulfate Thermal Dissociation
At temperatures exceeding $400^\circ\text{C}$, potassium pyrosulfate undergoes reversible thermal dissociation to liberate gaseous, highly reactive Lewis-acidic sulfur trioxide:
$$\text{K}_2\text{S}_2\text{O}_7 \xrightarrow{\Delta} \text{K}_2\text{SO}_4 + \text{SO}_3$$

### Step 2: Dissolution of Rutile by In Situ Sulfur Trioxide
Sulfur trioxide attacks the basic titanium dioxide lattice:
$$\text{TiO}_2 + \text{SO}_3 \to \text{TiOSO}_4$$
Overall net fusion reaction:
$$\text{TiO}_2 + \text{K}_2\text{S}_2\text{O}_7 \to \text{TiOSO}_4 + \text{K}_2\text{SO}_4$$
(or forming potassium titanyl double sulfate: $\text{K}_2[\text{TiO}(\text{SO}_4)_2]$).

### Step 3: Stoichiometric Calculation
Mass of pure $\text{TiO}_2$ in sample:
$$m_{\text{TiO}_2} = 0.5000\text{ g} \times 0.950 = 0.4750\text{ g}$$
Moles of $\text{TiO}_2$:
$$n_{\text{TiO}_2} = \frac{0.4750\text{ g}}{79.866\text{ g}\cdot\text{mol}^{-1}} = 5.9475 \times 10^{-3}\text{ mol}$$

Because the stoichiometry is $1:1$:
$$n_{\text{K}_2\text{S}_2\text{O}_7} = 5.9475 \times 10^{-3}\text{ mol}$$
Stoichiometric mass consumed:
$$m_{\text{consumed}} = 5.9475 \times 10^{-3}\text{ mol} \times 254.32\text{ g}\cdot\text{mol}^{-1} = \mathbf{1.5126\text{ g}}$$
The $5.000\text{ g}$ flux added represents a $3.3$-fold stoichiometric excess, ensuring a fluid melt that drives the equilibrium to completion.

### Step 4: Dissolution Protocol and Hydrolysis Prevention
Titanyl sulfate ($\text{TiOSO}_4$) is prone to rapid, irreversible hydrolytic polymerization in neutral or warm aqueous media, precipitating insoluble hydrated titanium dioxide (metatitanic acid):
$$\text{TiOSO}_4 + 2\,\text{H}_2\text{O} \xrightarrow{\Delta} \text{TiO}_2 \cdot \text{H}_2\text{O}\downarrow + \text{H}_2\text{SO}_4$$
To prevent premature precipitation, the cooled fusion cake must be leached in chilled, dilute sulfuric acid ($1\text{--}2\text{ M }\text{H}_2\text{SO}_4$). The high hydronium ion concentration shifts the hydrolysis equilibrium back to the soluble monomeric titanyl dication $[\text{TiO}]^{2+}(\text{aq})$.""",
                    "hints": ["Pyrosulfate splits into sulfate and sulfur trioxide at high temperature.", "Titanyl ions hydrolyze and precipitate unless kept in acidic solution."]
                },
                {
                    "id": "prob-2-6",
                    "problemNumber": "2.6",
                    "title": "Moisture Correction and Loss on Ignition Calculations",
                    "difficulty": "Foundational",
                    "statement": r"""A limestone core sample is analyzed for total calcium content. The as-received powdered sample is weighed into a porcelain crucible:
- Mass of empty crucible: $24.1520\text{ g}$
- Mass of crucible + sample: $26.6520\text{ g}$
- Mass of crucible + sample after drying at $105^\circ\text{C}$ to constant mass: $26.5895\text{ g}$
- Mass of crucible + sample after muffle furnace ignition at $1000^\circ\text{C}$ to constant mass: $25.5015\text{ g}$

Calculate:
1. The percentage of non-essential moisture ($\% \text{H}_2\text{O}_{\text{adsorbed}}$) in the as-received sample.
2. The Loss on Ignition ($\% \text{LOI}$) calculated on both the as-received and dry basis.
3. If the analytical test portion of the dried sample was analyzed and found to contain $38.50\text{ wt}\% \ \text{Ca}$, calculate the calcium percentage on the original as-received wet basis.""",
                    "solution": r"""### Step 1: Percentage of Non-Essential Moisture
Initial mass of wet sample:
$$m_{\text{wet}} = 26.6520 - 24.1520 = 2.5000\text{ g}$$
Mass of dried sample ($105^\circ\text{C}$):
$$m_{\text{dry}} = 26.5895 - 24.1520 = 2.4375\text{ g}$$
Moisture lost:
$$\Delta m_{\text{moisture}} = 2.5000 - 2.4375 = 0.0625\text{ g}$$
Percentage moisture:
$$\% \text{H}_2\text{O} = \left(\frac{0.0625\text{ g}}{2.5000\text{ g}}\right) \times 100\% = \mathbf{2.500\%}$$

### Step 2: Loss on Ignition (LOI)
Mass of residue after $1000^\circ\text{C}$ calcination:
$$m_{\text{ignited}} = 25.5015 - 24.1520 = 1.3495\text{ g}$$
Loss during ignition (from dried state):
$$\Delta m_{\text{LOI}} = m_{\text{dry}} - m_{\text{ignited}} = 2.4375 - 1.3495 = 1.0880\text{ g}$$
1. $\% \text{LOI}$ on **Dry Basis**:
$$\% \text{LOI}_{\text{dry}} = \left(\frac{1.0880\text{ g}}{2.4375\text{ g}}\right) \times 100\% = \mathbf{44.636\%}$$
2. $\% \text{LOI}$ on **As-Received Basis** (loss of both moisture and ignition volatiles):
$$\Delta m_{\text{total}} = 2.5000 - 1.3495 = 1.1505\text{ g}$$
$$\% \text{LOI}_{\text{wet}} = \left(\frac{1.1505\text{ g}}{2.5000\text{ g}}\right) \times 100\% = \mathbf{46.020\%}$$

### Step 3: Conversion of Analyte Content to Wet Basis
Because the moisture ($2.50\%$) diluted the sample:
$$\% \text{Ca}_{\text{wet}} = \% \text{Ca}_{\text{dry}} \times \left(1 - \frac{\% \text{Moisture}}{100}\right) = 38.50\% \times (1 - 0.0250) = 38.50\% \times 0.9750 = \mathbf{37.538\% \text{ Ca}}$$""",
                    "hints": ["Calculate moisture loss as (wet - dry) / wet * 100%.", "Converting from dry to wet basis involves multiplying by (1 - moisture fraction)."]
                },
                {
                    "id": "prob-2-7",
                    "problemNumber": "2.7",
                    "title": "Optimization of Closed-Vessel Microwave Digestion Acid Ratios",
                    "difficulty": "Honors Problem",
                    "statement": r"""An analytical laboratory digests $0.5000\text{ g}$ of dried bovine liver tissue to determine trace selenium and mercury by hydride-generation AAS. The closed-vessel microwave digestion uses a mixture of $65\text{ wt}\% \ \text{HNO}_3$ and $30\text{ wt}\% \ \text{H}_2\text{O}_2$.
1. Explain the role of hydrogen peroxide in closed-vessel digestion of lipid-rich biological matrices.
2. If the bovine liver contains approximately $50\text{ wt}\%$ carbon, calculate the stoichiometric volume of $65\text{ wt}\% \ \text{HNO}_3$ ($\rho = 1.40\text{ g}\cdot\text{mL}^{-1}$) required to completely oxidize the carbon to carbon dioxide according to:
$$\text{C} + 4\,\text{HNO}_3 \to \text{CO}_2 + 4\,\text{NO}_2 + 2\,\text{H}_2\text{O}$$
3. Calculate the ideal gas pressure generated inside a $75\text{-mL}$ vessel at $200^\circ\text{C}$ by the evolved gases ($\text{CO}_2$ and $\text{NO}_2$).""",
                    "solution": r"""### Step 1: Role of Hydrogen Peroxide
Concentrated nitric acid alone is often kinetically sluggish in breaking down long-chain aliphatic fatty acids and lipids below $180^\circ\text{C}$. The addition of $\text{H}_2\text{O}_2$ initiates Fenton-type and peroxynitric oxidation cascades, generating extremely reactive hydroxyl radicals ($\cdot\text{OH}$) that rapidly cleave lipid carbon-carbon bonds, accelerating digestion and preventing residual organic carbon interference during hydride generation.

### Step 2: Stoichiometric Acid Calculation
Mass of carbon in $0.5000\text{ g}$ liver:
$$m_{\text{C}} = 0.5000\text{ g} \times 0.50 = 0.2500\text{ g}$$
Moles of carbon:
$$n_{\text{C}} = \frac{0.2500\text{ g}}{12.011\text{ g}\cdot\text{mol}^{-1}} = 0.020814\text{ mol}$$
Stoichiometric moles of $\text{HNO}_3$:
$$n_{\text{HNO}_3} = 4 \times n_{\text{C}} = 4 \times 0.020814 = 0.083256\text{ mol}$$
Mass of pure $\text{HNO}_3$:
$$m_{\text{pure}} = 0.083256\text{ mol} \times 63.013\text{ g}\cdot\text{mol}^{-1} = 5.2462\text{ g}$$
Mass of $65\text{ wt}\%$ solution:
$$m_{\text{soln}} = \frac{5.2462\text{ g}}{0.65} = 8.071\text{ g}$$
Volume of nitric acid ($\rho = 1.40\text{ g/mL}$):
$$V = \frac{8.071\text{ g}}{1.40\text{ g}\cdot\text{mL}^{-1}} = \mathbf{5.765\text{ mL}}$$
Analysts typically utilize $6.0\text{--}8.0\text{ mL}$ of $\text{HNO}_3$ plus $1.0\text{--}2.0\text{ mL}$ of $\text{H}_2\text{O}_2$.

### Step 3: Gas Pressure Calculation in Sealed Vessel
Total moles of gas produced from $0.020814\text{ mol}$ of carbon:
$$n_{\text{gas}} = n_{\text{CO}_2} + n_{\text{NO}_2} = n_{\text{C}} + 4\,n_{\text{C}} = 5 \times 0.020814 = \mathbf{0.10407\text{ mol gas}}$$
Volume of vessel headspace: $V = 75\text{ mL} = 0.075\text{ L}$.
Temperature: $T = 200^\circ\text{C} = 473.15\text{ K}$.
Using the ideal gas equation:
$$P = \frac{n R T}{V} = \frac{0.10407\text{ mol} \times 0.082057\text{ L}\cdot\text{atm}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} \times 473.15\text{ K}}{0.075\text{ L}} = \frac{4.0404}{0.075} = \mathbf{53.87\text{ atm}}$$
Converting to bar:
$$P = 53.87 \times 1.01325 = \mathbf{54.6\text{ bar}}$$
*Safety Implication*: The reaction generates over $50\text{ bar}$ of internal pressure! This proves why microwave digestion must use reinforced vessels with calibrated pressure-relief rupture discs.""",
                    "hints": ["4 moles of HNO3 are consumed per mole of carbon.", "Total gas moles = moles CO2 + moles NO2 = 5 * moles C."]
                }
            ]
        },

        # =====================================================================
        # UNIT 3
        # =====================================================================
        {
            "id": "unit-3-group-separation-precipitation-phenomena",
            "unitNumber": 3,
            "title": "Unit 3: Group Separation & Precipitation Phenomena: Gravimetric Foundations",
            "leadSummary": "Comprehensive physical and analytical chemistry of solubility equilibria, extended Debye-Hückel ionic strength corrections, von Weimarn ratio of relative supersaturation, nucleation and crystal growth kinetics, coprecipitation and occlusion mechanisms, homogeneous precipitation, and the classical qualitative cation group separation scheme.",
            "simulations": ["sim_chem_precipitation_titration_solubility"],
            "sections": [
                {
                    "id": "sec-3-1",
                    "secNumber": "3.1",
                    "title": "Solubility Product Equilibria: Thermodynamic K°_sp vs Concentration K_sp",
                    "content": r"""Precipitation gravimetry and classical qualitative separation rely upon controlling the dynamic equilibrium between a sparingly soluble ionic solid $M_m X_n(s)$ and its constituent solvated ions in aqueous solution:
$$M_m X_n(s) \rightleftharpoons m\,M^{z+}(aq) + n\,X^{z-}(aq)$$

### The Thermodynamic Solubility Product ($K^\circ_{\text{sp}}$)
At thermodynamic equilibrium, the chemical potential of the solid phase equals the sum of the chemical potentials of its dissolved ions. The true thermodynamic solubility product $K^\circ_{\text{sp}}$ is formulated in terms of **chemical activities** $a_i$:
$$K^\circ_{\text{sp}} = a_{M^{z+}}^m \cdot a_{X^{z-}}^n$$
Because the activity of an ion is related to its molar concentration $[M^{z+}]$ via the single-ion activity coefficient $\gamma_i$ ($a_i = \gamma_i [C_i]$):
$$K^\circ_{\text{sp}} = (\gamma_M [M^{z+}])^m \cdot (\gamma_X [X^{z-}])^n = (\gamma_M^m \gamma_X^n) \cdot [M^{z+}]^m [X^{z-}]^n$$

### The Concentration Solubility Product ($K_{\text{sp}}$)
The operational concentration solubility product $K_{\text{sp}}$ is defined purely in terms of analytical molar concentrations:
$$K_{\text{sp}} = [M^{z+}]^m [X^{z-}]^n = \frac{K^\circ_{\text{sp}}}{\gamma_M^m \gamma_X^n} = \frac{K^\circ_{\text{sp}}}{\gamma_\pm^{m+n}}$$
where $\gamma_\pm$ is the mean ionic activity coefficient:
$$\gamma_\pm = (\gamma_M^m \gamma_X^n)^{\frac{1}{m+n}}$$

In infinitely dilute solution (ionic strength $\mu \to 0$), inter-ionic electrostatic interactions vanish, $\gamma_\pm \to 1.0$, and $K_{\text{sp}} \to K^\circ_{\text{sp}}$. In finite electrolyte solutions, however, $\gamma_\pm < 1.0$, causing the apparent concentration solubility product $K_{\text{sp}}$ to increase—a phenomenon termed the **diverse ion (salt) effect** or **inert electrolyte effect**.""",
                    "simulations": ["sim_chem_precipitation_titration_solubility"]
                },
                {
                    "id": "sec-3-2",
                    "secNumber": "3.2",
                    "title": "Ionic Strength & Extended Debye-Hückel Activity Coefficient Corrections",
                    "content": r"""To calculate quantitative solubility in real analytical solutions containing dissolved salts, the activity coefficients must be evaluated as a function of the solution's total electrical environment, quantified by the **ionic strength** ($\mu$ or $I$).

### Definition of Ionic Strength
Introduced by G. N. Lewis in 1921, the ionic strength measures the intensity of the electric field generated by all dissolved ions:
$$\mu = \frac{1}{2} \sum_{i=1}^k c_i z_i^2$$
where $c_i$ is the molar concentration of ion $i$ and $z_i$ is its integer ionic charge. Because the charge $z_i$ is squared, multivalent ions ($\text{Ca}^{2+}, \text{Al}^{3+}, \text{SO}_4^{2-}$) exert an effect out of proportion to their concentration.

### The Debye-Hückel Theory of Electrolyte Solutions
P. Debye and E. Hückel (1923) demonstrated that thermal kinetic motion and Coulombic electrostatic forces organize a central ion with an oppositely charged **ionic atmosphere**.

#### 1. Debye-Hückel Limiting Law (DHLL, valid for $\mu < 0.01\text{ M}$)
$$\log_{10} \gamma_i = -A\,z_i^2 \sqrt{\mu}$$
For aqueous solutions at $25^\circ\text{C}$, the solvent dielectric constant and temperature yield $A \approx 0.509\text{ L}^{1/2}\cdot\text{mol}^{-1/2}$:
$$\log_{10} \gamma_i = -0.509\,z_i^2 \sqrt{\mu}$$

#### 2. Extended Debye-Hückel Equation (valid for $\mu \le 0.10\text{ M}$)
Accounts for the finite effective physical diameter of the hydrated ion ($\alpha_i$, in angstroms or picometers):
$$\log_{10} \gamma_i = -\frac{0.509\,z_i^2 \sqrt{\mu}}{1 + B \alpha_i \sqrt{\mu}}$$
where in water at $25^\circ\text{C}$, $B \approx 0.328\text{ \AA}^{-1}\text{L}^{1/2}\cdot\text{mol}^{-1/2}$. When $\alpha_i$ is expressed in Angstroms:
$$\log_{10} \gamma_i = -\frac{0.509\,z_i^2 \sqrt{\mu}}{1 + 0.328\,\alpha_i \sqrt{\mu}}$$

```
                      Ionic Atmosphere Stabilization
                       ─  +  ─   +   ─   +
                         +  ┌────────┐  +
                       ─    │  Cation│    ─    Screening reduces chemical
                         +  │   M²⁺  │  +      activity (γ < 1), pulling
                       ─    └────────┘    ─    more solid into solution!
                         +  ─   +   ─   +
```

### The Diverse Ion Effect on Solubility
Consider the solubility of barium sulfate ($\text{BaSO}_4$, $K^\circ_{\text{sp}} = 1.1 \times 10^{-10}$) in pure water versus in $0.050\text{ M }\text{KNO}_3$.
- In pure water: $\mu \approx 10^{-5}\text{ M} \implies \gamma_\pm \approx 1.0 \implies s = \sqrt{K^\circ_{\text{sp}}} = 1.05 \times 10^{-5}\text{ M}$.
- In $0.050\text{ M }\text{KNO}_3$: $\mu = 0.050\text{ M}$. For divalent ions ($z = 2$, $\alpha \approx 4.5\text{ \AA}$):
$$\log_{10} \gamma_\pm = -\frac{0.509 (4) \sqrt{0.050}}{1 + 0.328 (4.5) \sqrt{0.050}} = -\frac{0.4553}{1.330} = -0.3423 \implies \gamma_\pm = 0.455$$
The concentration solubility becomes:
$$s = \frac{\sqrt{K^\circ_{\text{sp}}}}{\gamma_\pm} = \frac{1.05 \times 10^{-5}}{0.455} = \mathbf{2.31 \times 10^{-5}\text{ M}}$$
The presence of $0.05\text{ M}$ inert electrolyte **more than doubles the solubility** of barium sulfate! The ionic atmosphere screens electrostatic attraction between $\text{Ba}^{2+}$ and $\text{SO}_4^{2-}$, stabilizing them in solution.""",
                    "simulations": []
                },
                {
                    "id": "sec-3-3",
                    "secNumber": "3.3",
                    "title": "von Weimarn Ratio of Relative Supersaturation & Nucleation Kinetics",
                    "content": r"""The physical morphology, purity, and filterability of a precipitate are governed by the competition between two physical processes: **nucleation** and **crystal growth**.

### von Weimarn's Ratio of Relative Supersaturation (RSS)
In the 1920s, P. P. von Weimarn established that the initial rate of precipitation is directly proportional to the **relative supersaturation (RSS)**:
$$\text{RSS} = \frac{Q - S}{S}$$
where:
- $Q$ is the instantaneous molar concentration of the mixed reagents before precipitation commences.
- $S$ is the thermodynamic equilibrium solubility of the precipitate in the reaction medium.
- $(Q - S)$ represents the absolute supersaturation driving force.

```
                  Nucleation vs Crystal Growth Regimes
         Rate
          ▲
          │                          / Nucleation Rate
          │                         /  (Exponential)
          │                        /
          │                       /
          │                      /
          │       /─────────────/
          │      /             /
          │     /             /
          │    /  Crystal Growth Rate (Linear)
          │   /
          └──/───────────────────────────────────────►
             0             Low RSS              High RSS
                         (Crystalline)         (Colloidal)
```

### Physical Manifestations of the RSS Regimes

#### 1. High Relative Supersaturation ($\text{RSS} > 50\text{--}100$)
- Nucleation rate completely overwhelms particle growth: millions of sub-microscopic nuclei form simultaneously.
- Result: **Colloidal Dispersions** (particle diameters $1\text{--}100\text{ nm}$).
- Particles remain suspended due to Brownian motion, pass through standard filter paper, scatter light (Tyndall effect), and cannot be washed or collected directly.

#### 2. Low Relative Supersaturation ($\text{RSS} < 10$)
- Nuclei form slowly and sparsely; crystal growth dominates as solute ions deposit onto existing crystal faces.
- Result: **Coarse Crystalline Precipitates** (particle diameters $> 0.1\text{ mm}$).
- Dense, rapidly settling, easily filterable crystals that trap minimal mother liquor.

### Practical Experimental Techniques to Minimize RSS
To produce crystalline, highly pure precipitates, the analyst manipulates reaction conditions to keep $Q$ as low as possible and $S$ as high as possible:
1. **High Dilution**: Mix reagents at low initial concentrations to minimize $Q$.
2. **Slow Addition with Vigorous Stirring**: Add precipitating reagent dropwise while stirring rapidly to avoid localized pockets of high $Q$.
3. **Elevated Temperature**: Precipitate from hot solutions, exploiting the endothermic increase in solubility ($S$) according to the van 't Hoff equation.
4. **pH Control**: Perform precipitation at a controlled pH where equilibrium solubility $S$ is moderately elevated, then slowly adjust pH to complete quantitative recovery.""",
                    "simulations": []
                },
                {
                    "id": "sec-3-4",
                    "secNumber": "3.4",
                    "title": "Crystal Growth vs Colloidal Dispersion, Coagulation & Peptization",
                    "content": r"""When precipitates form as colloidal dispersions (such as silver chloride $\text{AgCl}$ or hydrated iron(III) oxide $\text{Fe}_2\text{O}_3 \cdot x\text{H}_2\text{O}$), they must undergo controlled agglomeration into filterable macroscopic masses (**coagulation**) without redispersing (**peptization**).

### Structure of the Colloidal Electrical Double Layer
Colloidal particles in contact with solution adsorb a surplus of their own constituent lattice ions, acquiring an electrostatic surface charge.

```
                      Colloidal Electrical Double Layer
                     ┌──────────────────────────────────┐
                     │   Bulk Solution (Zero Potential) │
                     ├──────────────────────────────────┤
                     │   Counter-Ion Outer Layer        │
                     │   (Diffusive diffuse layer, NO₃⁻)│
                     ├──────────────────────────────────┤
                     │   Primary Adsorption Inner Layer │
                     │   (Ag⁺ strongly coordinated)     │
                     ├──────────────────────────────────┤
                     │   Solid Colloidal Core           │
                     │   [AgCl] Solid Lattice Particle  │
                     └──────────────────────────────────┘
```

Consider precipitating $\text{AgCl}$ with a slight excess of $\text{AgNO}_3$:
1. **Primary Adsorbed Layer**: The $\text{AgCl}$ lattice surface preferentially adsorbs lattice cations ($\text{Ag}^+$) according to Paneth-Fajans-Hahn adsorption rules, creating a net positive surface potential.
2. **Counter-Ion Layer**: An equivalent quantity of solution counter-ions ($\text{NO}_3^-$) is held by Coulombic attraction in a surrounding diffuse layer.

### Coagulation (Flocculation)
Colloidal stability is governed by the Derjaguin-Landau-Verwey-Overbeek (DLVO) balance between attractive van der Waals dispersion forces and repulsive electrostatic double-layer forces.
- When double layers are thick, particles approaching within Brownian distances experience electrostatic repulsion and rebound, remaining colloidal.
- **Double-Layer Compression**: Adding a high concentration of inert electrolyte (e.g., $0.1\text{ M }\text{HNO}_3$) compresses the diffuse counter-ion layer closer to the particle surface. This shields the surface charge, lowering the **zeta potential** ($\zeta$).
- Once the repulsive barrier falls below thermal kinetic energy ($k_B T$), van der Waals forces dominate, causing particles to coalesce into heavy, flocculated curds that settle rapidly.

### Peptization (The Gravimetric Hazard)
**Peptization** is the process by which a coagulated precipitate reverts back into a colloidal dispersion.
*The Danger in Washing*: If coagulated $\text{AgCl}$ is washed with pure distilled water, the electrolyte ions ($\text{HNO}_3$) maintaining double-layer compression are rinsed away. The double layers expand, electrostatic repulsion is restored, and the precipitate peptizes into a milky colloidal suspension that passes through filter pores!
*Universal Gravimetric Rule*: Precipitates must **never be washed with pure water**. They must always be washed with a dilute solution of a volatile electrolyte (e.g., dilute $\text{HNO}_3$ for $\text{AgCl}$; dilute $\text{NH}_4\text{NO}_3$ for hydrous oxides) that maintains double-layer compression and volatilizes completely during subsequent drying or ignition.""",
                    "simulations": []
                },
                {
                    "id": "sec-3-5",
                    "secNumber": "3.5",
                    "title": "Coprecipitation Contamination Mechanisms: Surface Adsorption, Inclusion & Occlusion",
                    "content": r"""**Coprecipitation** is the phenomenon whereby chemical compounds that are normally completely soluble under experimental conditions precipitate simultaneously along with the target precipitate. Coprecipitation contaminates the precipitate and represents a primary source of systematic error in gravimetric analysis.

### The Four Coprecipitation Mechanisms

```
                        Coprecipitation Mechanisms
       ┌───────────────────────────────┬───────────────────────────────┐
       ▼                               ▼                               ▼
┌─────────────────┐             ┌─────────────────┐             ┌─────────────────┐
│Surface Adsorpt. │             │Mixed-Crystal    │             │   Occlusion     │
│                 │             │  Inclusion      │             │ & Mechanical    │
├─────────────────┤             ├─────────────────┤             ├─────────────────┤
│Foreign ions     │             │Foreign ion      │             │Mother liquor    │
│adsorb onto      │             │isomorphously    │             │droplets trapped │
│external crystal │             │substitutes in   │             │inside growing   │
│faces.           │             │crystal lattice. │             │crystal defects. │
└─────────────────┘             └─────────────────┘             └─────────────────┘
```

#### 1. Surface Adsorption
Foreign ions in the solution adhere to the exterior surfaces of the precipitate particles via electrostatic coordination.
- *Paneth-Fajans-Hahn Rule*: The ion most strongly adsorbed is that which forms the least soluble compound with one of the lattice ions.
- *Example*: In precipitating $\text{BaSO}_4$ in the presence of $\text{Ca}^{2+}$, $\text{Ca}^{2+}$ adsorbs onto the sulfate-rich surface.
- *Mitigation*: Maximize crystal size to minimize specific surface area ($A/V \propto 1/r$), perform thorough washing with volatile electrolyte, or dissolve and **reprecipitate**.

#### 2. Mixed-Crystal Inclusion (Isomorphous Substitution)
A foreign contaminant ion replaces a normal lattice ion within the crystal interior because both ions possess identical charges and comparable ionic radii (typically within $15\%$, obeying Goldschmidt's crystal chemical rules).
- *Example*: Lead substituting for barium in barium sulfate ($\text{PbSO}_4$ in $\text{BaSO}_4$); or $\text{Mn}^{2+}$ substituting for $\text{Mg}^{2+}$ in magnesium ammonium phosphate ($\text{MgNH}_4\text{PO}_4$).
- *Severity*: Inclusion cannot be eliminated by washing or thermal digestion. The only remediation is chemical separation or masking of the interfering ion prior to precipitation.

#### 3. Occlusion
Occurs during rapid crystal growth when pockets of liquid containing dissolved foreign salts become mechanically enveloped and trapped within internal crystal defects, voids, or cleavage planes.
- *Mitigation*: Minimized by slow crystal growth and thermal **Ostwald ripening (digestion)**.

#### 4. Mechanical Entrapment
Occurs when multiple adjacent crystals grow together, trapping pockets of mother liquor in the interstices between crystals.

### Digestion (Ostwald Ripening)
**Digestion** involves allowing the freshly formed precipitate to stand in contact with the hot mother liquor for 1 to 2 hours.
- *Mechanism*: According to the Ostwald-Freundlich equation:
$$S(r) = S_0 \exp\left(\frac{2\gamma V_m}{R T r}\right)$$
Sub-microscopic particles with small radius $r$ possess significantly higher equilibrium solubility than macroscopic crystals with large radius. Consequently, tiny particles dissolve, and their solute recrystallizes onto the surfaces of larger crystals.
- *Benefits*: Eliminates colloidal fines, heals lattice defects, expels occluded impurities, and consolidates the precipitate into coarse, dense, filterable crystals.""",
                    "simulations": []
                },
                {
                    "id": "sec-3-6",
                    "secNumber": "3.6",
                    "title": "Homogeneous Precipitation Protocols: Slow In Situ Reagent Generation",
                    "content": r"""The ultimate method for eliminating localized high supersaturation ($Q$) and achieving near-zero relative supersaturation is **Precipitation from Homogeneous Solution (PFHS)**.

### Principles of Homogeneous Precipitation
In classical precipitation, adding a reagent dropwise from a pipette causes transient, localized pockets of extreme reagent concentration at the liquid interface ($Q \gg S$), driving rapid uncontrolled nucleation and coprecipitation.
In homogeneous precipitation, the precipitating reagent is not added directly. Instead, a chemical precursor is dissolved homogeneously throughout the solution. Subsequent gentle heating initiates a slow, uniform chemical reaction that generates the precipitating agent in situ at an infinitesimal rate simultaneously throughout the entire liquid volume.

### Major Homogeneous Precipitation Systems

#### 1. Homogeneous Hydroxide Generation: Urea Hydrolysis
Urea ($\text{CO(NH}_2)_2$) is a neutral, non-reactive molecule at room temperature. When heated to $90^\circ\text{C}\text{--}100^\circ\text{C}$, it hydrolyzes slowly and smoothly, releasing ammonia and elevating solution pH uniformly:
$$\text{CO(NH}_2)_2 + \text{H}_2\text{O} \xrightarrow{95^\circ\text{C}} 2\,\text{NH}_3 + \text{CO}_2\uparrow$$
$$\text{NH}_3 + \text{H}_2\text{O} \rightleftharpoons \text{NH}_4^+ + \text{OH}^-$$
- *Application*: Quantitative precipitation of aluminum, iron(III), and chromium(III) hydrous oxides:
$$\text{Al}^{3+} + 3\,\text{OH}^- \xrightarrow{\text{urea}} \text{Al(OH)}_3(s)$$
- *Result*: Rather than the gelatinous, unfilterable slime produced by adding aqueous ammonia, urea hydrolysis produces dense, crystalline, granular precipitates that filter in seconds and exhibit negligible coprecipitation of divalent ions ($\text{Mg}^{2+}, \text{Ca}^{2+}$).

#### 2. Homogeneous Sulfate Generation: Sulfamic Acid & Dimethyl Sulfate
Hydrolysis of sulfamic acid ($\text{NH}_2\text{SO}_3\text{H}$) or dimethyl sulfate:
$$\text{NH}_2\text{SO}_3\text{H} + \text{H}_2\text{O} \xrightarrow{\Delta} \text{NH}_4^+ + \text{H}^+ + \text{SO}_4^{2-}$$
Produces large, coarse, diamond-shaped barium sulfate crystals with near-zero occlusion of nitrate or alkali metals.

#### 3. Homogeneous Sulfide Generation: Thioacetamide
Thioacetamide ($\text{CH}_3\text{CSNH}_2$) hydrolyzes in warm acidic or basic solution to release hydrogen sulfide:
$$\text{CH}_3\text{CSNH}_2 + 2\,\text{H}_2\text{O} \xrightarrow{\text{acid, }\Delta} \text{CH}_3\text{COOH} + \text{NH}_4^+ + \text{H}_2\text{S}$$
Generates dense, easily filterable metal sulfides ($\text{CuS}, \text{PbS}, \text{CdS}$) without the noxious odors and erratic precipitation associated with bubbling $\text{H}_2\text{S}$ gas.

| Precipitating Agent | Homogeneous Precursor | Reaction Mechanism | Target Analyte |
| :--- | :--- | :--- | :--- |
| **Hydroxide ($\text{OH}^-$)** | Urea ($\text{CO(NH}_2)_2$) | Thermal hydrolysis at $95^\circ\text{C}$ | $\text{Al}^{3+}, \text{Fe}^{3+}, \text{Ga}^{3+}, \text{Th}^{4+}$ |
| **Sulfate ($\text{SO}_4^{2-}$)** | Sulfamic acid / Dimethyl sulfate | Hydrolytic ester cleavage | $\text{Ba}^{2+}, \text{Sr}^{2+}, \text{Pb}^{2+}$ |
| **Sulfide ($\text{S}^{2-}$)** | Thioacetamide ($\text{CH}_3\text{CSNH}_2$) | Thermal hydrolysis in acid/base | $\text{Cu}^{2+}, \text{Cd}^{2+}, \text{Pb}^{2+}, \text{Zn}^{2+}$ |
| **Oxalate ($\text{C}_2\text{O}_4^{2-}$)** | Dimethyl oxalate / Diethyl oxalate | Base-catalyzed ester hydrolysis | $\text{Ca}^{2+}, \text{Mg}^{2+}, \text{Th}^{4+}$ |
| **Phosphate ($\text{PO}_4^{3-}$)** | Triethyl phosphate | Acid-catalyzed ester cleavage | $\text{Zr}^{4+}, \text{Hf}^{4+}, \text{Mg}^{2+}$ |""",
                    "simulations": []
                },
                {
                    "id": "sec-3-7",
                    "secNumber": "3.7",
                    "title": "Classical Qualitative Cation Group Separation Scheme (Groups I–V)",
                    "content": r"""The classical qualitative inorganic analysis scheme, developed by Heinrich Rose and Carl Remigius Fresenius, is a masterpiece of applied equilibrium chemistry. A complex mixture of up to 25 common metallic cations is systematically resolved into five distinct groups through selective precipitation controlled by precipitation reagents and pH buffering.

```
                  Classical Cation Group Separation Scheme
                    Mixture of Cations (Groups I - V)
                                   │ + 6 M HCl
                    ┌──────────────┴──────────────┐
                    ▼ Precipitate                 ▼ Filtrate
             ┌──────────────┐              (Groups II - V)
             │   Group I    │                     │ + H₂S / Thioacetamide at pH 0.5
             │ Insoluble    │              ┌──────┴──────┐
             │ Chlorides    │              ▼ Precipitate ▼ Filtrate
             │ AgCl, PbCl₂, │       ┌──────────────┐  (Groups III - V)
             │ Hg₂Cl₂       │       │   Group II   │         │ + NH₄Cl, NH₃, H₂S (pH 9)
             └──────────────┘       │ Acid Sulfides│  ┌──────┴──────┐
                                    │ CuS, CdS,    │  ▼ Precip.     ▼ Filtrate
                                    │ Bi₂S₃, HgS,  │ ┌──────────┐ (Groups IV - V)
                                    │ SnS, Sb₂S₃   │ │Group III │        │ + (NH₄)₂CO₃ (pH 9)
                                    └──────────────┘ │Al(OH)₃,  │ ┌──────┴──────┐
                                                     │Fe(OH)₃,  │ ▼ Precip.     ▼ Soluble
                                                     │Cr(OH)₃,  │┌───────────┐┌───────────┐
                                                     │ZnS, NiS, ││ Group IV  ││  Group V  │
                                                     │CoS, MnS  ││BaCO₃,CaCO₃││Na⁺, K⁺,   │
                                                     └──────────┘│SrCO₃      ││Mg²⁺, NH₄⁺ │
                                                                 └───────────┘└───────────┘
```

### Chemistry of the Five Analytical Groups

#### Group I: The Insoluble Chloride Group ($\text{Ag}^+, \text{Pb}^{2+}, \text{Hg}_2^{2+}$)
- **Reagent**: Dilute $\text{HCl}$ ($2\text{--}6\text{ M}$) in cold solution.
- **Precipitates**: $\text{AgCl}$ (white), $\text{PbCl}_2$ (white), $\text{Hg}_2\text{Cl}_2$ (white).
- **Separation Chemistry**:
  - Lead chloride ($\text{PbCl}_2$) possesses a relatively high $K_{\text{sp}} = 1.7 \times 10^{-5}$; it dissolves completely in boiling water ($33.4\text{ g/L}$ at $100^\circ\text{C}$ vs $9.9\text{ g/L}$ at $20^\circ\text{C}$), separating from $\text{AgCl}$ and $\text{Hg}_2\text{Cl}_2$. Confirmed by yellow $\text{PbCrO}_4$ precipitation.
  - Adding aqueous $\text{NH}_3$ dissolves $\text{AgCl}$ via diamminesilver(I) complex formation:
    $$\text{AgCl}(s) + 2\,\text{NH}_3 \to [\text{Ag(NH}_3)_2]^+ + \text{Cl}^-$$
  - $\text{Hg}_2\text{Cl}_2$ undergoes disproportionation with ammonia, turning pitch black due to finely divided elemental mercury:
    $$\text{Hg}_2\text{Cl}_2 + 2\,\text{NH}_3 \to \text{Hg}(0)\downarrow \text{ (black)} + \text{Hg(NH}_2)\text{Cl}\downarrow \text{ (white)} + \text{NH}_4^+ + \text{Cl}^-$$

#### Group II: The Acid Sulfide Group ($\text{Hg}^{2+}, \text{Bi}^{3+}, \text{Cu}^{2+}, \text{Cd}^{2+}, \text{As}^{3+/5+}, \text{Sb}^{3+/5+}, \text{Sn}^{2+/4+}$)
- **Reagent**: Hydrogen sulfide ($\text{H}_2\text{S}$ or thioacetamide) in $0.3\text{ M }\text{HCl}$ ($\text{pH } \approx 0.5$).
- **Equilibrium Control**: In $0.3\text{ M }\text{H}^+$, the polyprotic ionization of $\text{H}_2\text{S}$ ($K_{a1} K_{a2} = 1.1 \times 10^{-21}$) is repressed by the common-ion effect:
$$[\text{S}^{2-}] = \frac{K_{a1} K_{a2} [\text{H}_2\text{S}]}{[\text{H}^+]^2} \approx \frac{(1.1 \times 10^{-21})(0.10)}{(0.3)^2} \approx 1.2 \times 10^{-21}\text{ M}$$
This tiny sulfide concentration is sufficient to exceed the $K_{\text{sp}}$ of Group II sulfides ($\text{CuS } 6 \times 10^{-36}, \text{HgS } 10^{-52}, \text{Bi}_2\text{S}_3 10^{-72}$) but remains too low to precipitate the more soluble Group III sulfides ($\text{ZnS } 10^{-24}, \text{FeS } 6 \times 10^{-18}, \text{MnS } 3 \times 10^{-13}$).

#### Group III: The Basic Sulfide and Hydroxide Group ($\text{Fe}^{3+/2+}, \text{Al}^{3+}, \text{Cr}^{3+}, \text{Ni}^{2+}, \text{Co}^{2+}, \text{Zn}^{2+}, \text{Mn}^{2+}$)
- **Reagent**: $\text{H}_2\text{S}$ in ammoniacal buffer ($\text{NH}_4\text{Cl} + \text{NH}_3$, $\text{pH } \approx 9.0$).
- **Precipitates**: Hydroxides of $\text{Al(OH)}_3$ (white gelatinous), $\text{Fe(OH)}_3$ (reddish-brown), $\text{Cr(OH)}_3$ (greenish-gray); and sulfides of $\text{ZnS}$ (white), $\text{NiS}$ (black), $\text{CoS}$ (black), $\text{MnS}$ (flesh-colored).

#### Group IV: The Insoluble Carbonate Group ($\text{Ba}^{2+}, \text{Sr}^{2+}, \text{Ca}^{2+}$)
- **Reagent**: Ammonium carbonate ($(\text{NH}_4)_2\text{CO}_3$) in neutral/mildly alkaline ammoniacal buffer ($\text{pH } \approx 9.2$).
- **Precipitates**: $\text{BaCO}_3, \text{SrCO}_3, \text{CaCO}_3$ (all white).
- Magnesium does not precipitate because the $\text{NH}_4\text{Cl}$ buffer keeps $[\text{CO}_3^{2-}]$ low enough to prevent exceeding $K_{\text{sp}}(\text{MgCO}_3)$.

#### Group V: The Soluble Alkali and Magnesium Group ($\text{Mg}^{2+}, \text{Na}^+, \text{K}^+, \text{NH}_4^+$)
- Cations whose chlorides, sulfides, and carbonates are universally soluble. Tested individually via specific spot tests (e.g., magnesium as magnesium ammonium phosphate $\text{MgNH}_4\text{PO}_4$; potassium as yellow potassium cobaltinitrite $\text{K}_3[\text{Co(NO}_2)_6]$; sodium by intense yellow flame emission at $589\text{ nm}$).""",
                    "simulations": []
                }
            ],
            "problems": [
                {
                    "id": "prob-3-1",
                    "problemNumber": "3.1",
                    "title": "Thermodynamic vs Concentration Solubility and Ionic Strength Effects",
                    "difficulty": "Foundational",
                    "statement": r"""The thermodynamic solubility product of silver sulfate ($\text{Ag}_2\text{SO}_4$) at $25^\circ\text{C}$ is:
$$K^\circ_{\text{sp}} = 1.20 \times 10^{-5}$$
1. Calculate the molar solubility $s_0$ of silver sulfate in pure water, assuming activity coefficients $\gamma_i \approx 1.0$.
2. Calculate the ionic strength $\mu$ of an aqueous solution containing $0.020\text{ M }\text{KNO}_3$ and $0.010\text{ M }\text{Mg(NO}_3)_2$.
3. Using the Debye-Hückel limiting law ($\log_{10} \gamma_i = -0.509\,z_i^2 \sqrt{\mu}$), calculate the activity coefficients $\gamma_{\text{Ag}^+}$ and $\gamma_{\text{SO}_4^{2-}}$ in this electrolyte matrix.
4. Calculate the molar solubility $s$ of $\text{Ag}_2\text{SO}_4$ in this electrolyte solution and determine the percentage increase in solubility attributable to the diverse ion effect.""",
                    "solution": r"""### Step 1: Solubility in Pure Water ($\gamma \approx 1$)
$$\text{Ag}_2\text{SO}_4(s) \rightleftharpoons 2\,\text{Ag}^+ + \text{SO}_4^{2-}$$
Let molar solubility be $s_0$. Then $[\text{Ag}^+] = 2 s_0$ and $[\text{SO}_4^{2-}] = s_0$.
$$K^\circ_{\text{sp}} = [\text{Ag}^+]^2 [\text{SO}_4^{2-}] = (2 s_0)^2 (s_0) = 4 s_0^3$$
$$s_0 = \left(\frac{1.20 \times 10^{-5}}{4}\right)^{1/3} = (3.00 \times 10^{-6})^{1/3} = \mathbf{0.01442\text{ M}}$$

### Step 2: Ionic Strength of the Electrolyte Solution
The solution contains:
- $0.020\text{ M }\text{KNO}_3 \implies 0.020\text{ M }\text{K}^+ + 0.020\text{ M }\text{NO}_3^-$
- $0.010\text{ M }\text{Mg(NO}_3)_2 \implies 0.010\text{ M }\text{Mg}^{2+} + 0.020\text{ M }\text{NO}_3^-$

Total ion concentrations:
- $[\text{K}^+] = 0.020\text{ M}$, $z = 1$
- $[\text{Mg}^{2+}] = 0.010\text{ M}$, $z = 2$
- $[\text{NO}_3^-] = 0.020 + 0.020 = 0.040\text{ M}$, $z = 1$

Calculate ionic strength $\mu$:
$$\mu = \frac{1}{2} \left( [K^+](1)^2 + [\text{Mg}^{2+}](2)^2 + [\text{NO}_3^-](1)^2 \right)$$
$$\mu = \frac{1}{2} \left( 0.020(1) + 0.010(4) + 0.040(1) \right) = \frac{1}{2} (0.020 + 0.040 + 0.040) = \frac{1}{2} (0.100) = \mathbf{0.050\text{ M}}$$

### Step 3: Activity Coefficients via Debye-Hückel Limiting Law
$\sqrt{\mu} = \sqrt{0.050} = 0.2236$.
1. For $\text{Ag}^+$ ($z = 1$):
$$\log_{10} \gamma_{\text{Ag}^+} = -0.509 (1)^2 (0.2236) = -0.1138 \implies \gamma_{\text{Ag}^+} = 10^{-0.1138} = \mathbf{0.7695}$$
2. For $\text{SO}_4^{2-}$ ($z = 2$):
$$\log_{10} \gamma_{\text{SO}_4^{2-}} = -0.509 (2)^2 (0.2236) = -0.509 (4) (0.2236) = -0.4553 \implies \gamma_{\text{SO}_4^{2-}} = 10^{-0.4553} = \mathbf{0.3505}$$

### Step 4: Solubility in Electrolyte Solution
The thermodynamic expression is:
$$K^\circ_{\text{sp}} = (\gamma_{\text{Ag}^+}^2 [\text{Ag}^+]^2) (\gamma_{\text{SO}_4^{2-}} [\text{SO}_4^{2-}]) = \gamma_{\text{Ag}^+}^2 \gamma_{\text{SO}_4^{2-}} (4 s^3)$$
$$4 s^3 = \frac{K^\circ_{\text{sp}}}{\gamma_{\text{Ag}^+}^2 \gamma_{\text{SO}_4^{2-}}} = \frac{1.20 \times 10^{-5}}{(0.7695)^2 (0.3505)} = \frac{1.20 \times 10^{-5}}{(0.5921)(0.3505)} = \frac{1.20 \times 10^{-5}}{0.2075} = 5.783 \times 10^{-5}$$
$$s^3 = \frac{5.783 \times 10^{-5}}{4} = 1.4458 \times 10^{-5}$$
$$s = (1.4458 \times 10^{-5})^{1/3} = \mathbf{0.02436\text{ M}}$$

Percentage increase in solubility:
$$\% \text{Increase} = \left(\frac{s - s_0}{s_0}\right) \times 100\% = \left(\frac{0.02436 - 0.01442}{0.01442}\right) \times 100\% = \mathbf{+68.9\%}$$
The diverse ion effect increases the solubility of silver sulfate by nearly $70\%$!""",
                    "hints": ["Calculate the total ionic strength from all ions before evaluating activity coefficients.", "Remember that K_sp = 4 * s^3 for a 2:1 electrolyte."]
                },
                {
                    "id": "prob-3-2",
                    "problemNumber": "3.2",
                    "title": "Selective Sulfide Precipitation in Group II vs Group III Separation",
                    "difficulty": "Advanced",
                    "statement": r"""An analytical solution contains $0.050\text{ M }\text{Cu}^{2+}$ and $0.050\text{ M }\text{Zn}^{2+}$. To perform a quantitative Group II separation, the solution is saturated with $\text{H}_2\text{S}$ ($[\text{H}_2\text{S}] \approx 0.10\text{ M}$) in hydrochloric acid.
Given thermodynamic parameters at $25^\circ\text{C}$:
- $\text{H}_2\text{S}$: $K_{a1} = 1.0 \times 10^{-7}, K_{a2} = 1.2 \times 10^{-14} \implies K_{a1} K_{a2} = 1.2 \times 10^{-21}$
- $\text{CuS}$: $K_{\text{sp}} = 6.3 \times 10^{-36}$
- $\text{ZnS}$: $K_{\text{sp}} = 1.6 \times 10^{-24}$

1. Calculate the maximum sulfide ion concentration $[\text{S}^{2-}]$ that can be tolerated in solution without precipitating zinc sulfide ($\text{ZnS}$).
2. Calculate the minimum hydronium ion concentration $[\text{H}^+]$ (and maximum pH) required to maintain $[\text{S}^{2-}]$ below this threshold.
3. At this $[\text{H}^+]$, calculate the residual concentration of copper ion $[\text{Cu}^{2+}]$ remaining unprecipitated at equilibrium, and verify that copper removal exceeds $99.99\%$.
4. What happens if the pH rises to $9.0$?""",
                    "solution": r"""### Step 1: Maximum Sulfide Concentration to Avoid ZnS Precipitation
Zinc sulfide precipitates when the ionic product exceeds $K_{\text{sp}}(\text{ZnS})$:
$$Q = [\text{Zn}^{2+}][\text{S}^{2-}] \ge K_{\text{sp}}(\text{ZnS}) = 1.6 \times 10^{-24}$$
Given $[\text{Zn}^{2+}] = 0.050\text{ M}$:
$$[\text{S}^{2-}]_{\max} = \frac{K_{\text{sp}}(\text{ZnS})}{[\text{Zn}^{2+}]} = \frac{1.6 \times 10^{-24}}{0.050} = \mathbf{3.20 \times 10^{-23}\text{ M}}$$

### Step 2: Minimum $[\text{H}^+]$ to Regulate Sulfide Ion Activity
The polyprotic equilibrium for saturated $\text{H}_2\text{S}$ ($0.10\text{ M}$) is:
$$[\text{S}^{2-}] = \frac{K_{a1} K_{a2} [\text{H}_2\text{S}]}{[\text{H}^+]^2} = \frac{(1.2 \times 10^{-21})(0.10)}{[\text{H}^+]^2} = \frac{1.20 \times 10^{-22}}{[\text{H}^+]^2}$$
To ensure $[\text{S}^{2-}] \le 3.20 \times 10^{-23}\text{ M}$:
$$\frac{1.20 \times 10^{-22}}{[\text{H}^+]^2} \le 3.20 \times 10^{-23}$$
$$[\text{H}^+]^2 \ge \frac{1.20 \times 10^{-22}}{3.20 \times 10^{-23}} = 3.75$$
$$[\text{H}^+] \ge \sqrt{3.75} = \mathbf{1.936\text{ M}} \implies \text{pH} \le -0.287$$
*Analytical Benchmark*: In standard qualitative schemes, analysts utilize $[\text{H}^+] \approx 0.30\text{ M}$ ($\text{pH} \approx 0.5$).
At $[\text{H}^+] = 0.30\text{ M}$:
$$[\text{S}^{2-}] = \frac{1.20 \times 10^{-22}}{(0.30)^2} = \frac{1.20 \times 10^{-22}}{0.090} = 1.33 \times 10^{-21}\text{ M}$$
Notice that $Q_{\text{ZnS}} = (0.050)(1.33 \times 10^{-21}) = 6.67 \times 10^{-23} > 1.6 \times 10^{-24}$, meaning that at $0.3\text{ M }\text{H}^+$, $\text{ZnS}$ would begin to precipitate unless $[\text{H}^+]$ is held at $\sim 0.6\text{--}1.0\text{ M}$ or zinc concentration is lower.

### Step 3: Residual Copper Concentration at $[\text{H}^+] = 0.50\text{ M}$
At $[\text{H}^+] = 0.50\text{ M}$:
$$[\text{S}^{2-}] = \frac{1.20 \times 10^{-22}}{(0.50)^2} = 4.80 \times 10^{-22}\text{ M}$$
The residual copper concentration is:
$$[\text{Cu}^{2+}] = \frac{K_{\text{sp}}(\text{CuS})}{[\text{S}^{2-}]} = \frac{6.3 \times 10^{-36}}{4.80 \times 10^{-22}} = \mathbf{1.31 \times 10^{-14}\text{ M}}$$
Fraction of copper remaining:
$$\text{Fraction remaining} = \frac{1.31 \times 10^{-14}\text{ M}}{0.050\text{ M}} = 2.6 \times 10^{-13} \implies \mathbf{99.99999999997\% \text{ precipitated!}}$$
Copper removal is completely quantitative while zinc remains entirely in solution.

### Step 4: Outcome at pH 9.0
At $\text{pH } 9.0$ ($[\text{H}^+] = 1.0 \times 10^{-9}\text{ M}$):
$$[\text{S}^{2-}] = \frac{1.20 \times 10^{-22}}{(1.0 \times 10^{-9})^2} = 1.20 \times 10^{-4}\text{ M}$$
The ionic product for $\text{ZnS}$ becomes:
$$Q = (0.050)(1.20 \times 10^{-4}) = 6.0 \times 10^{-6} \gg K_{\text{sp}} (1.6 \times 10^{-24})$$
$\text{ZnS}$ precipitates instantaneously and completely alongside $\text{CuS}$, destroying the separation. This confirms why Group II separation requires strictly controlled acidic conditions ($0.3\text{--}0.5\text{ M }\text{HCl}$).""",
                    "hints": ["Use the overall diprotic acid equation [S2-] = Ka1 * Ka2 * [H2S] / [H+]^2.", "Equate the ion product [Zn2+][S2-] to Ksp(ZnS) to find the critical boundary."]
                },
                {
                    "id": "prob-3-3",
                    "problemNumber": "3.3",
                    "title": "Coprecipitation via Surface Adsorption: Paneth-Fajans-Hahn Rules",
                    "difficulty": "Intermediate",
                    "statement": r"""A $50.0\text{ mL}$ aliquot of $0.0200\text{ M }\text{AgNO}_3$ is titrated with $0.0200\text{ M }\text{NaCl}$ to precipitate silver chloride:
$$\text{Ag}^+ + \text{Cl}^- \rightleftharpoons \text{AgCl}(s) \quad (K_{\text{sp}} = 1.82 \times 10^{-10})$$
1. When $40.0\text{ mL}$ of $\text{NaCl}$ has been added (pre-equivalence point), state which ion forms the primary adsorption layer on the $\text{AgCl}$ colloidal particle surface, and identify the counter-ion layer.
2. When $60.0\text{ mL}$ of $\text{NaCl}$ has been added (post-equivalence point), identify the primary adsorbed ion and the counter-ion layer.
3. According to the Paneth-Fajans-Hahn rules, if both $\text{NO}_3^-$ and $\text{ClO}_4^-$ are present in equal concentration in the mother liquor at the pre-equivalence point, which anion will be more strongly coprecipitated onto the colloidal surface?""",
                    "solution": r"""### Step 1: Pre-Equivalence Point (40.0 mL NaCl Added)
Initial moles of $\text{Ag}^+$:
$$n_{\text{Ag}^+} = 50.0\text{ mL} \times 0.0200\text{ M} = 1.00\text{ mmol}$$
Moles of $\text{Cl}^-$ added:
$$n_{\text{Cl}^-} = 40.0\text{ mL} \times 0.0200\text{ M} = 0.80\text{ mmol}$$
Excess $\text{Ag}^+$ in solution:
$$n_{\text{Ag}^+, \text{excess}} = 1.00 - 0.80 = 0.20\text{ mmol}$$
- **Primary Adsorption Layer**: Because silver ions are present in excess and are constituent lattice cations, $\mathbf{\text{Ag}^+}$ ions are strongly chemisorbed onto the surface lattice defects of $\text{AgCl}$, giving the colloidal particles a **net positive electrical surface charge**:
  $$[\text{AgCl}] \cdot \text{Ag}^+$$
- **Counter-Ion Diffuse Layer**: An equivalent quantity of solution anions, predominantly nitrate ($\mathbf{\text{NO}_3^-}$), is held by Coulombic attraction in the surrounding diffuse electric layer:
  $$\{[\text{AgCl}] \cdot \text{Ag}^+\} \ : \ \text{NO}_3^-$$

### Step 2: Post-Equivalence Point (60.0 mL NaCl Added)
Moles of $\text{Cl}^-$ added:
$$n_{\text{Cl}^-} = 60.0\text{ mL} \times 0.0200\text{ M} = 1.20\text{ mmol}$$
Excess $\text{Cl}^-$ in solution:
$$n_{\text{Cl}^-, \text{excess}} = 1.20 - 1.00 = 0.20\text{ mmol}$$
- **Primary Adsorption Layer**: Chloride lattice anions ($\mathbf{\text{Cl}^-}$) now saturate the surface, imparting a **net negative electrical surface charge**:
  $$[\text{AgCl}] \cdot \text{Cl}^-$$
- **Counter-Ion Diffuse Layer**: Sodium cations ($\mathbf{\text{Na}^+}$) form the diffuse counter-ion layer:
  $$\{[\text{AgCl}] \cdot \text{Cl}^-\} \ : \ \text{Na}^+$$

### Step 3: Application of Paneth-Fajans-Hahn Adsorption Rules
The Paneth-Fajans-Hahn rules state:
*"Other factors being equal, that counter-ion is most strongly adsorbed which forms the compound with the lowest solubility with one of the constituent lattice ions of the precipitate."*
Here, the lattice cation is $\text{Ag}^+$.
Comparing silver nitrate ($\text{AgNO}_3$) vs silver perchlorate ($\text{AgClO}_4$):
- Both salts are highly soluble, but silver nitrate has a lower solubility and greater covalent lattice coordination propensity with silver than the bulky, weakly coordinating perchlorate ion.
- Therefore, **$\text{NO}_3^-$ will be more strongly coprecipitated** than $\text{ClO}_4^-$.
*Practical Consequence*: Precipitations of silver are preferred in perchlorate or fluoroborate media rather than nitrate or sulfate media to minimize coprecipitative contamination.""",
                    "hints": ["The lattice ion in stoichiometric excess always forms the primary adsorbed layer.", "The Paneth-Fajans-Hahn rule links adsorption affinity to the solubility of the compound formed with the lattice ion."]
                },
                {
                    "id": "prob-3-4",
                    "problemNumber": "3.4",
                    "title": "Homogeneous Precipitation of Aluminum Hydroxide via Urea Hydrolysis Kinetics",
                    "difficulty": "Honors Problem",
                    "statement": r"""A $100.0\text{ mL}$ analytical solution containing $0.0200\text{ M }\text{Al}^{3+}$ and $0.0500\text{ M }\text{Mg}^{2+}$ in $0.100\text{ M }\text{HCl}$ is treated with $5.00\text{ g}$ of urea ($\text{CO(NH}_2)_2$, $M = 60.06\text{ g}\cdot\text{mol}^{-1}$) and heated at $95^\circ\text{C}$ to precipitate aluminum hydroxide homogeneously.
Given solubility products:
- $\text{Al(OH)}_3$: $K_{\text{sp}} = 1.9 \times 10^{-33}$
- $\text{Mg(OH)}_2$: $K_{\text{sp}} = 5.6 \times 10^{-12}$

1. Write the rate law for urea hydrolysis and explain why heating to $> 90^\circ\text{C}$ is required.
2. Calculate the exact pH at which aluminum hydroxide begins to precipitate from this solution.
3. Calculate the pH at which aluminum precipitation is quantitative ($[\text{Al}^{3+}] \le 1.0 \times 10^{-6}\text{ M}$).
4. Calculate the pH at which magnesium hydroxide ($\text{Mg(OH)}_2$) would begin to coprecipitate, and define the optimum final pH window for clean separation.""",
                    "solution": r"""### Step 1: Kinetics of Urea Hydrolysis
Urea hydrolyzes via a pseudo-first-order mechanism at constant water activity:
$$\text{CO(NH}_2)_2 + \text{H}_2\text{O} \to 2\,\text{NH}_3 + \text{CO}_2\uparrow$$
$$\text{Rate} = k [\text{CO(NH}_2)_2]$$
The activation energy for urea hydrolysis is very high ($E_a \approx 135\text{ kJ}\cdot\text{mol}^{-1}$). At room temperature ($25^\circ\text{C}$), $k \approx 3 \times 10^{-9}\text{ s}^{-1}$ (negligible reaction). Elevating temperature to $95^\circ\text{C}$ increases $k$ by a factor of $> 10^5$, allowing smooth, controllable ammonia generation over a $60\text{--}90\text{ minute}$ analytical timeframe.

### Step 2: pH for Onset of $\text{Al(OH)}_3$ Precipitation
Precipitation begins when $Q = [\text{Al}^{3+}][\text{OH}^-]^3 = K_{\text{sp}}(\text{Al(OH)}_3) = 1.9 \times 10^{-33}$.
Given $[\text{Al}^{3+}] = 0.0200\text{ M}$:
$$[\text{OH}^-]^3 = \frac{1.9 \times 10^{-33}}{0.0200} = 9.50 \times 10^{-32}$$
$$[\text{OH}^-] = (9.50 \times 10^{-32})^{1/3} = 4.563 \times 10^{-11}\text{ M}$$
$$p\text{OH} = -\log_{10}(4.563 \times 10^{-11}) = 10.34 \implies \mathbf{\text{pH} = 14.00 - 10.34 = 3.66}$$
$\text{Al(OH)}_3$ begins precipitating at an acidic pH of **$3.66$**.

### Step 3: pH for Quantitative Removal of $\text{Al}^{3+}$ ($[\text{Al}^{3+}] \le 1.0 \times 10^{-6}\text{ M}$)
$$[\text{OH}^-]^3 = \frac{1.9 \times 10^{-33}}{1.0 \times 10^{-6}} = 1.90 \times 10^{-27}$$
$$[\text{OH}^-] = (1.90 \times 10^{-27})^{1/3} = 1.239 \times 10^{-9}\text{ M}$$
$$p\text{OH} = -\log_{10}(1.239 \times 10^{-9}) = 8.91 \implies \mathbf{\text{pH} = 14.00 - 8.91 = 5.09}$$
Aluminum removal is quantitative at $\mathbf{\text{pH } \ge 5.09}$.

### Step 4: pH Threshold for Onset of $\text{Mg(OH)}_2$ Precipitation
Precipitation of $\text{Mg(OH)}_2$ occurs when:
$$[\text{Mg}^{2+}][\text{OH}^-]^2 = K_{\text{sp}}(\text{Mg(OH)}_2) = 5.6 \times 10^{-12}$$
Given $[\text{Mg}^{2+}] = 0.0500\text{ M}$:
$$[\text{OH}^-]^2 = \frac{5.6 \times 10^{-12}}{0.0500} = 1.12 \times 10^{-10}$$
$$[\text{OH}^-] = \sqrt{1.12 \times 10^{-10}} = 1.058 \times 10^{-5}\text{ M}$$
$$p\text{OH} = -\log_{10}(1.058 \times 10^{-5}) = 4.98 \implies \mathbf{\text{pH} = 14.00 - 4.98 = 9.02}$$
Magnesium does not precipitate until $\mathbf{\text{pH } 9.02}$!

### Optimum Separation Window
The ideal operational pH window is:
$$\mathbf{6.5 \le \text{pH} \le 7.5}$$
In this window:
- Aluminum is $> 99.999\%$ precipitated as a dense, easily filterable basic hydroxide.
- Magnesium remains $100\%$ soluble ($Q_{\text{Mg(OH)}_2} \approx 10^{-15} \ll K_{\text{sp}} = 5.6 \times 10^{-12}$).
- Because urea hydrolysis buffers naturally around $\text{pH } 7.0\text{--}7.5$ as carbon dioxide boils off, the homogeneous method automatically stops in the perfect separation zone!""",
                    "hints": ["Calculate [OH-] from Ksp = [M][OH-]^n.", "Find the pH range between quantitative Al precipitation and initial Mg precipitation."]
                },
                {
                    "id": "prob-3-5",
                    "problemNumber": "3.5",
                    "title": "Ostwald Ripening and Equilibrium Particle Solubility Kinetics",
                    "difficulty": "Honors Problem",
                    "statement": r"""The equilibrium solubility of barium sulfate ($\text{BaSO}_4$) crystals possessing macroscopic planar surfaces ($r \to \infty$) is $S_0 = 1.05 \times 10^{-5}\text{ M}$ at $25^\circ\text{C}$.
Given:
- Interfacial solid-liquid surface tension: $\gamma = 0.125\text{ J}\cdot\text{m}^{-2}$ ($125\text{ mJ/m}^2$)
- Molar volume of solid $\text{BaSO}_4$: $V_m = 5.21 \times 10^{-5}\text{ m}^3\cdot\text{mol}^{-1}$
- Temperature: $T = 298.15\text{ K}$, $R = 8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$

Using the Ostwald-Freundlich equation:
$$S(r) = S_0 \exp\left(\frac{2\gamma V_m}{R T r}\right)$$
1. Calculate the equilibrium solubility $S(r)$ of colloidal $\text{BaSO}_4$ nanoparticles with radius $r_1 = 5.0\text{ nm}$ ($5.0 \times 10^{-9}\text{ m}$).
2. Calculate the solubility ratio $S(r) / S_0$ for particles of radius $r_2 = 50.0\text{ nm}$ and $r_3 = 1.0\,\mu\text{m}$.
3. Explain how this thermodynamic gradient drives Ostwald ripening during precipitate digestion.""",
                    "solution": r"""### Step 1: Calculation for $r_1 = 5.0\text{ nm}$ ($5.0 \times 10^{-9}\text{ m}$)
First compute the exponent factor:
$$\frac{2\gamma V_m}{R T} = \frac{2 \times (0.125\text{ J}\cdot\text{m}^{-2}) \times (5.21 \times 10^{-5}\text{ m}^3\cdot\text{mol}^{-1})}{(8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (298.15\text{ K})} = \frac{1.3025 \times 10^{-5}}{2478.8} = 5.2546 \times 10^{-9}\text{ m} = \mathbf{5.255\text{ nm}}$$

Now calculate the exponent for $r_1 = 5.0 \times 10^{-9}\text{ m}$:
$$\frac{2\gamma V_m}{R T r_1} = \frac{5.2546 \times 10^{-9}\text{ m}}{5.0 \times 10^{-9}\text{ m}} = 1.0509$$
Compute the solubility:
$$S(5\text{ nm}) = S_0 \exp(1.0509) = (1.05 \times 10^{-5}\text{ M}) \times 2.860 = \mathbf{3.00 \times 10^{-5}\text{ M}}$$
Colloidal particles of $5\text{ nm}$ radius are **$2.86$ times more soluble** than bulk macroscopic crystals!

### Step 2: Calculation for $r_2 = 50.0\text{ nm}$ and $r_3 = 1.0\,\mu\text{m}$
1. For $r_2 = 50.0\text{ nm}$:
$$\frac{2\gamma V_m}{R T r_2} = \frac{5.255\text{ nm}}{50.0\text{ nm}} = 0.1051 \implies \frac{S(50\text{ nm})}{S_0} = \exp(0.1051) = \mathbf{1.111}$$
The solubility is elevated by $11.1\%$ ($S = 1.17 \times 10^{-5}\text{ M}$).

2. For $r_3 = 1.0\,\mu\text{m} = 1000\text{ nm}$:
$$\frac{2\gamma V_m}{R T r_3} = \frac{5.255\text{ nm}}{1000\text{ nm}} = 0.005255 \implies \frac{S(1\,\mu\text{m})}{S_0} = \exp(0.005255) = \mathbf{1.0053}$$
The solubility is essentially indistinguishable from macroscopic bulk ($+0.53\%$).

### Step 3: Mechanism of Ostwald Ripening
In a freshly precipitated slurry:
- Tiny nuclei ($r \le 5\text{ nm}$) establish a local equilibrium concentration of $[\text{Ba}^{2+}] \approx 3.0 \times 10^{-5}\text{ M}$ in their immediate boundary layer.
- Large crystals ($r \ge 1\,\mu\text{m}$) establish a boundary concentration of $[\text{Ba}^{2+}] \approx 1.05 \times 10^{-5}\text{ M}$.
- This concentration gradient establishes spontaneous mass transport: solute diffuses from high concentration (near small particles) to low concentration (near large crystals).
- As solute leaves, the solution around small particles becomes undersaturated ($Q < S(r)$), causing the small particles to dissolve. Simultaneously, the solution around large crystals becomes supersaturated ($Q > S_0$), driving crystal growth.
- **Net Result**: The smallest particles dissolve completely and redeposit onto the larger crystals, transforming colloidal fines into coarse, filterable, high-purity crystals.""",
                    "hints": ["Calculate the characteristic length scale 2 * gamma * Vm / (R * T) first.", "Particles with small radii have high positive surface curvature, increasing chemical potential."]
                },
                {
                    "id": "prob-3-6",
                    "problemNumber": "3.6",
                    "title": "Gravimetric Factor and Stoichiometric Calculation for Barium and Sulfate",
                    "difficulty": "Foundational",
                    "statement": r"""A $0.6240\text{ g}$ sample of impure soluble sulfate salt is dissolved in water and acidified with $\text{HCl}$. Barium chloride ($\text{BaCl}_2$) is added slowly to precipitate barium sulfate:
$$\text{SO}_4^{2-} + \text{Ba}^{2+} \to \text{BaSO}_4(s)$$
The precipitate is digested, filtered through ashless filter paper, washed with dilute $\text{HNO}_3$, and ignited to constant mass in a porcelain crucible:
- Mass of empty crucible: $18.4230\text{ g}$
- Mass of crucible + ignited $\text{BaSO}_4$: $18.9852\text{ g}$
Atomic weights: $\text{Ba} = 137.327, \text{S} = 32.065, \text{O} = 15.9994$.

1. Calculate the gravimetric factor for:
   - Converting $\text{BaSO}_4$ to $\text{S}$.
   - Converting $\text{BaSO}_4$ to $\text{SO}_3$.
   - Converting $\text{BaSO}_4$ to $\text{SO}_4^{2-}$.
2. Calculate the mass of ignited $\text{BaSO}_4$ recovered.
3. Calculate the percentage of sulfur ($\% \text{S}$) and percentage of sulfate ($\% \text{SO}_4^{2-}$) in the original sample.""",
                    "solution": r"""### Step 1: Calculation of Gravimetric Factors
Molar mass of $\text{BaSO}_4$:
$$M_{\text{BaSO}_4} = 137.327 + 32.065 + 4(15.9994) = 137.327 + 32.065 + 63.9976 = \mathbf{233.390\text{ g}\cdot\text{mol}^{-1}}$$

1. Gravimetric factor for $\text{S}$:
$$\text{GF}_{\text{S}} = \frac{M_{\text{S}}}{M_{\text{BaSO}_4}} = \frac{32.065}{233.390} = \mathbf{0.137388}$$
2. Gravimetric factor for $\text{SO}_3$ ($M = 80.0632$):
$$\text{GF}_{\text{SO}_3} = \frac{M_{\text{SO}_3}}{M_{\text{BaSO}_4}} = \frac{80.0632}{233.390} = \mathbf{0.343045}$$
3. Gravimetric factor for $\text{SO}_4^{2-}$ ($M = 96.0626$):
$$\text{GF}_{\text{SO}_4^{2-}} = \frac{M_{\text{SO}_4^{2-}}}{M_{\text{BaSO}_4}} = \frac{96.0626}{233.390} = \mathbf{0.411597}$$

### Step 2: Mass of Ignited $\text{BaSO}_4$
$$m_{\text{BaSO}_4} = 18.9852\text{ g} - 18.4230\text{ g} = \mathbf{0.5622\text{ g}}$$

### Step 3: Percentage of Sulfur and Sulfate
1. Percentage of Sulfur:
$$\% \text{S} = \left(\frac{m_{\text{BaSO}_4} \times \text{GF}_{\text{S}}}{m_{\text{sample}}}\right) \times 100\% = \left(\frac{0.5622\text{ g} \times 0.137388}{0.6240\text{ g}}\right) \times 100\% = \left(\frac{0.077239\text{ g}}{0.6240\text{ g}}\right) \times 100\% = \mathbf{12.378\% \text{ S}}$$

2. Percentage of Sulfate ($\text{SO}_4^{2-}$):
$$\% \text{SO}_4^{2-} = \left(\frac{0.5622\text{ g} \times 0.411597}{0.6240\text{ g}}\right) \times 100\% = \left(\frac{0.231400\text{ g}}{0.6240\text{ g}}\right) \times 100\% = \mathbf{37.083\% \text{ SO}_4^{2-}}$$""",
                    "hints": ["Gravimetric factor GF = (formula weight of analyte sought) / (formula weight of substance weighed).", "Multiply mass of precipitate by GF to obtain analyte mass."]
                },
                {
                    "id": "prob-3-7",
                    "problemNumber": "3.7",
                    "title": "Equilibrium pH Control in Group IV Carbonate vs Magnesium Separation",
                    "difficulty": "Honors Problem",
                    "statement": r"""In qualitative group separation, Group IV cations ($\text{Ca}^{2+}, \text{Sr}^{2+}, \text{Ba}^{2+}$, each $\sim 0.010\text{ M}$) are precipitated as carbonates using $0.10\text{ M } (\text{NH}_4)_2\text{CO}_3$ in an ammonia/ammonium chloride buffer, while $\text{Mg}^{2+}$ ($0.010\text{ M}$) must remain completely in solution.
Given:
- $\text{CaCO}_3$: $K_{\text{sp}} = 4.5 \times 10^{-9}$
- $\text{MgCO}_3$: $K_{\text{sp}} = 3.5 \times 10^{-8}$
- $\text{Mg(OH)}_2$: $K_{\text{sp}} = 5.6 \times 10^{-12}$
- Carbonic acid: $pK_{a1} = 6.35, pK_{a2} = 10.33$
- Ammonium ion: $pK_a = 9.25$

1. Calculate the maximum carbonate ion concentration $[\text{CO}_3^{2-}]$ allowable to avoid precipitating magnesium carbonate ($\text{MgCO}_3$).
2. Calculate the minimum carbonate ion concentration $[\text{CO}_3^{2-}]$ required to precipitate $99.9\%$ of $\text{Ca}^{2+}$.
3. Calculate the required buffer ratio $\frac{[\text{NH}_3]}{[\text{NH}_4^+]}$ and corresponding pH to establish this precise carbonate concentration in $0.10\text{ M}$ total carbonate solution.""",
                    "solution": r"""### Step 1: Maximum $[\text{CO}_3^{2-}]$ to Avoid $\text{MgCO}_3$ Precipitation
$$Q = [\text{Mg}^{2+}][\text{CO}_3^{2-}] < K_{\text{sp}}(\text{MgCO}_3) = 3.5 \times 10^{-8}$$
Given $[\text{Mg}^{2+}] = 0.010\text{ M}$:
$$[\text{CO}_3^{2-}]_{\max} = \frac{3.5 \times 10^{-8}}{0.010} = \mathbf{3.5 \times 10^{-6}\text{ M}}$$

### Step 2: Minimum $[\text{CO}_3^{2-}]$ for 99.9% Precipitation of $\text{Ca}^{2+}$
For $99.9\%$ precipitation of an initial $0.010\text{ M }\text{Ca}^{2+}$, the residual concentration is:
$$[\text{Ca}^{2+}]_{\text{residual}} = 0.010 \times (1 - 0.999) = 1.0 \times 10^{-5}\text{ M}$$
To achieve this:
$$[\text{CO}_3^{2-}]_{\min} = \frac{K_{\text{sp}}(\text{CaCO}_3)}{[\text{Ca}^{2+}]_{\text{residual}}} = \frac{4.5 \times 10^{-9}}{1.0 \times 10^{-5}} = \mathbf{4.5 \times 10^{-4}\text{ M}}$$

Notice an apparent thermodynamic dilemma: $[\text{CO}_3^{2-}]_{\min}$ for $99.9\%$ calcium recovery ($4.5 \times 10^{-4}\text{ M}$) exceeds $[\text{CO}_3^{2-}]_{\max}$ to prevent $\text{MgCO}_3$ ($3.5 \times 10^{-6}\text{ M}$)!
*Resolution in Practice*: Magnesium exhibits extreme kinetic reluctance to precipitate as pure $\text{MgCO}_3$ at room temperature due to high hydration energy ($\Delta H_{\text{hyd}} \approx -1920\text{ kJ/mol}$), forming instead basic carbonate complexes or remaining supersaturated. Furthermore, $[\text{CO}_3^{2-}]$ is typically buffered at $\sim 1 \times 10^{-5}\text{ M}$ to precipitate $99\%$ of calcium while preventing magnesium precipitation.

### Step 3: Buffer Calculation for $[\text{CO}_3^{2-}] = 2.0 \times 10^{-5}\text{ M}$
In $0.10\text{ M}$ total analytical carbonate $C_T = [\text{H}_2\text{CO}_3] + [\text{HCO}_3^-] + [\text{CO}_3^{2-}] \approx 0.10\text{ M}$:
The fractional abundance $\alpha_2$ of $\text{CO}_3^{2-}$ is:
$$\alpha_2 = \frac{[\text{CO}_3^{2-}]}{C_T} = \frac{2.0 \times 10^{-5}}{0.10} = 2.0 \times 10^{-4}$$
In the pH range $8\text{--}10$, $[\text{HCO}_3^-] \approx C_T$:
$$K_{a2} = \frac{[\text{H}^+][\text{CO}_3^{2-}]}{[\text{HCO}_3^-]} \approx \frac{[\text{H}^+](2.0 \times 10^{-5})}{0.10} \implies [\text{H}^+] = \frac{0.10 \times 10^{-10.33}}{2.0 \times 10^{-5}} = \frac{0.10 \times 4.677 \times 10^{-11}}{2.0 \times 10^{-5}} = 2.339 \times 10^{-7}\text{ M}$$
$$\text{pH} = -\log_{10}(2.339 \times 10^{-7}) = \mathbf{6.63}$$
Using ammonia buffer ($pK_a = 9.25$):
$$\text{pH} = pK_a + \log_{10}\left(\frac{[\text{NH}_3]}{[\text{NH}_4^+]}\right) \implies 9.25 + \log_{10}\left(\frac{[\text{NH}_3]}{[\text{NH}_4^+]}\right) = 9.20$$
In practical schemes, ammonium chloride ($\text{NH}_4\text{Cl}$) is added in substantial excess ($1\text{--}2\text{ M}$) with dilute ammonia to buffer pH tightly between $9.0$ and $9.3$, successfully separating Group IV carbonates from Group V magnesium.""",
                    "hints": ["Calculate carbonate concentration thresholds for both metals.", "Consider both thermodynamic solubility products and buffer speciation."]
                }
            ]
        }
    ]
    return units

if __name__ == '__main__':
    u = get_units_1_2_3()
    print(f"Generated Units 1-3: {len(u)} units")
    for unit in u:
        print(f"  {unit['title']}: {len(unit['sections'])} sections, {len(unit['problems'])} problems")
