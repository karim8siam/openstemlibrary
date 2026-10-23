#!/usr/bin/env python3
"""
Boost Units 2 and 3 of Industrial and Official Statistics over 25,000 total words.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"

# Unit 2 boost: C_pmk index
u2_path = DRAFT_DIR / "unit-2.md"
u2_text = u2_path.read_text(encoding="utf-8")
u2_add = r"""
## 2.12 The Unified Capability Index $C_{pmk}$ and the Six-Sigma Benchmark

While $C_{pk}$ penalizes off-centering relative to specification boundaries and $C_{pm}$ penalizes off-target departures via quadratic loss, each index has distinct blind spots. A process can have a high $C_{pk}$ while being far from nominal target $T$ if specifications are asymmetric, and $C_{pm}$ does not indicate whether the mean is closer to the upper or lower specification limit.

To synthesize both philosophies into a single comprehensive metric, W. L. Pearn, Samuel Kotz, and Norman L. Johnson (1992) formulated the **Unified Capability Index ($C_{pmk}$)**:

$$C_{pmk} = \frac{\min(USL - \mu, \; \mu - LSL)}{3 \sqrt{\sigma^2 + (\mu - T)^2}} = \frac{d - |\mu - M|}{3 \sqrt{\sigma^2 + (\mu - T)^2}}$$

where $d = (USL - LSL)/2$ is the half-tolerance bandwidth and $M = (USL + LSL)/2$ is the specification midpoint.

Notice that the numerator of $C_{pmk}$ is identical to the numerator of $C_{pk}$ (measuring distance from the mean to the nearest specification limit), while its denominator is identical to the denominator of $C_{pm}$ (incorporating total mean-square error $\tau = \sqrt{\sigma^2 + (\mu - T)^2}$).

### Relationships and Properties
1. If the process is perfectly centered on target ($\mu = M = T$):
   $$C_{pmk} = C_{pk} = C_{pm} = C_p$$
2. If the process drifts away from target ($\mu \ne T$):
   $$C_{pmk} < \min(C_{pk}, C_{pm}) < C_p$$
   $C_{pmk}$ is strictly more sensitive to process off-centering than either $C_{pk}$ or $C_{pm}$, serving as the most stringent capability benchmark in high-precision aerospace and medical manufacturing.

### The Six-Sigma Quality Benchmark ($Z_{\text{bench}}$)
In Motorola's Six Sigma methodology, process capability is expressed in terms of the **Sigma Level ($Z_{\text{bench}}$)**. By definition, a Six Sigma process has:
$$C_p = \frac{12\sigma}{6\sigma} = 2.0$$
Motorola recognized that over long-term production cycles, automated machinery inevitably experiences intermittent environmental drifts, tooling wear, and ambient temperature shifts. Empirical industrial studies established that process means typically drift by up to $\pm 1.5\sigma$ over time.

Under a worst-case $1.5\sigma$ sustained drift, the distance from the shifted mean to the nearest specification limit is:
$$Z_{\text{short-term}} = 6.0 - 1.5 = 4.5\sigma$$
The corresponding actual capability index drops to:
$$C_{pk} = \frac{4.5\sigma}{3\sigma} = 1.50$$
The defect rate under this $1.5\sigma$ shifted distribution is:
$$p = 1 - \Phi(4.5) \approx 3.3976 \times 10^{-6} \approx 3.4\text{ Parts Per Million (PPM)}$$
Thus, the world-class Six Sigma benchmark of $3.4\text{ PPM}$ explicitly incorporates a $1.5\sigma$ long-term mean drift into its statistical foundation!
"""
idx2 = u2_text.find("## Fully worked question 1:")
u2_text = u2_text[:idx2] + u2_add.strip() + "\n\n" + u2_text[idx2:]
u2_path.write_text(u2_text, encoding="utf-8")
print("Unit 2 boosted.")

# Unit 3 boost: Attribute OC curves and Type I/II risks
u3_path = DRAFT_DIR / "unit-3.md"
u3_text = u3_path.read_text(encoding="utf-8")
u3_add = r"""
## 3.12 Operating Characteristic (OC) Functions for Attribute Control Charts

Just as variables control charts have Operating Characteristic (OC) curves, the statistical performance of attribute charts ($p$-charts and $c$-charts) is characterized by their ability to discriminate between in-control and out-of-control conditions.

### OC Curve for the $p$-Chart
For a $p$-chart with constant sample size $n$ and control limits $[LCL, UCL]$, suppose the true fraction nonconforming shifts from the baseline $p_0$ to an out-of-control state $p_1$.

The probability of Type II error $\beta$ (the probability that a sample proportion $\widehat{p}$ plots within the control limits despite the shift) is given by the cumulative binomial distribution:

$$\beta(p_1) = P(LCL \le \widehat{p} \le UCL \mid p_1) = P(n \cdot LCL \le D \le n \cdot UCL \mid p_1) = \sum_{d = \lceil n \cdot LCL \rceil}^{\lfloor n \cdot UCL \rfloor} \binom{n}{d} p_1^d (1 - p_1)^{n-d}$$

The statistical power to detect the shift on any given sample is $1 - \beta(p_1)$, and the Average Run Length is:

$$ARL_1 = \frac{1}{1 - \beta(p_1)}$$

Because the Binomial distribution is discrete, the in-control Type I error rate $\alpha = 1 - \beta(p_0)$ does not exactly equal the theoretical $0.0027$ of Gaussian charts, fluctuating significantly depending on whether $n \bar{p}$ is small or large.

### OC Curve for the $c$-Chart
For a $c$-chart monitoring defect counts with limits $[LCL, UCL]$ derived from in-control mean $\bar{c}$, suppose the true defect rate shifts to $c_1$. The probability of Type II error is:

$$\beta(c_1) = P(LCL \le C \le UCL \mid c_1) = \sum_{c = \lceil LCL \rceil}^{\lfloor UCL \rfloor} \frac{e^{-c_1} c_1^c}{c!}$$

Plotting $\beta(c_1)$ against $c_1$ produces the OC curve for the defect count chart. As with the $p$-chart, small values of $\bar{c}$ produce highly asymmetric OC curves with low power against downward shifts (quality improvements), reinforcing the necessity of using exact Poisson probability limits or switching to Time-Between-Events (TBE) charts in high-yield processes.
"""
idx3 = u3_text.find("## Fully worked question 1:")
u3_text = u3_text[:idx3] + u3_add.strip() + "\n\n" + u3_text[idx3:]
u3_path.write_text(u3_text, encoding="utf-8")
print("Unit 3 boosted.")
