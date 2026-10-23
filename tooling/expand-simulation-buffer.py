#!/usr/bin/env python3
"""
Add small buffer to Book 15 to ensure it is around ~25,700 substantive prose words.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-simulation-and-monte-carlo-methods"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")

u4_buf = r"""
## 4.17 Practical Rules for Monte Carlo Sample Size Determination

When planning a production Monte Carlo study, the required sample size $n$ must be chosen rigorously to satisfy predefined relative precision bounds. 

Let the relative error tolerance be $\delta > 0$ with nominal confidence level $1 - \alpha$:
$$P\left( \frac{|\hat{\theta}_n - \theta|}{|\theta|} \le \delta \right) \ge 1 - \alpha$$
Using the asymptotic normality of the Monte Carlo estimator, this condition translates to:
$$z_{1-\alpha/2} \frac{\sigma}{\sqrt{n} |\theta|} \le \delta \implies n \ge \left( \frac{z_{1-\alpha/2}}{\delta} \right)^2 \left( \frac{\sigma}{|\theta|} \right)^2 = \left( \frac{z_{1-\alpha/2}}{\delta} \right)^2 \mathrm{CV}^2$$
where $\mathrm{CV} = \sigma / |\theta|$ is the coefficient of variation of the integrand.

In preliminary exploratory pilot runs, an initial sample of size $n_0 \approx 1,000$ draws is evaluated to obtain a consistent plug-in estimate of the coefficient of variation $\widehat{\mathrm{CV}} = s_0 / |\bar{X}_0|$. If the estimated coefficient of variation is large (as occurs in rare-event models or highly volatile derivatives where $\mathrm{CV} \ge 10$), achieving a modest relative precision of $\delta = 1\%$ ($0.01$) with $95\%$ confidence requires:
$$n \ge \left( \frac{1.96}{0.01} \right)^2 \times 10^2 \approx 3.84 \times 10^6 \text{ draws}$$
Recognizing when raw sample size expansion becomes computationally prohibitive is the exact signal to transition to the variance reduction methods of Unit 5.
"""

u5_buf = r"""
## 5.18 Diagnostic Guidelines for Variance Reduction Techniques

When deploying variance reduction techniques in complex simulation workflows, practitioners should observe four golden diagnostic principles:

1. **Verify Covariance Direction in Antithetic Sampling**: Always verify that the transformed response is monotonic with respect to each underlying uniform input. If a non-linear payoff is non-monotonic (such as a straddle or butterfly option), pairing $U$ with $1-U$ can yield positive covariance $\mathrm{Cov}(h(U), h(1-U)) > 0$, inadvertently *increasing* estimator variance above crude Monte Carlo.
2. **Monitor Condition Numbers in Multi-Control Inversion**: When deploying dozens of control variates, compute the condition number $\kappa(\mathbf{S}_{YY})$ of the empirical sample covariance matrix. If $\kappa(\mathbf{S}_{YY}) > 10^6$, multicollinearity among controls will cause the estimated weights $\hat{\mathbf{c}}$ to oscillate erratically, requiring Tikhonov ridge regularization.
3. **Check for Finite Variance in Importance Sampling**: Never trust an importance sampling estimate without examining the empirical distribution of the unnormalized weights $w_i = f(\mathbf{x}_i) / g(\mathbf{x}_i)$. If the maximum observed weight constitutes more than $10\%$ of the sum of all weights, or if a Pareto tail fit to the weights yields shape parameter $\alpha \le 2$, the importance estimator has infinite variance and will yield deceptively tight, yet invalid, confidence intervals.
4. **Evaluate Wall-Clock Efficiency**: The true metric of variance reduction is the **Efficiency Ratio**:
$$\text{Eff} = \frac{\mathrm{Var}(\hat{\theta}_{\text{crude}}) \times \text{CPU Time}_{\text{crude}}}{\mathrm{Var}(\hat{\theta}_{\text{reduced}}) \times \text{CPU Time}_{\text{reduced}}}$$
A technique that slashes variance by $50\%$ but requires four times the CPU time to compute auxiliary transformations is inefficient ($\text{Eff} = 0.5$). Only deploy variance reduction methods that yield net efficiency ratios strictly greater than $1.0$.
"""

u7_buf = r"""
## 7.17 Systematic Debugging of Markov Chain Monte Carlo Algorithms

When developing custom MCMC samplers or diagnosing convergence failures in probabilistic programming models, following a systematic troubleshooting hierarchy prevents widespread inference errors:

1. **Analytical Test Verification via Prior Simulation**: Before fitting empirical data, simulate synthetic datasets from known parameter priors $\boldsymbol{\theta}_0 \sim p(\boldsymbol{\theta})$ and $\mathbf{x} \sim p(\mathbf{x} \mid \boldsymbol{\theta}_0)$. Verify that the posterior credibility intervals cover the true parameters $\boldsymbol{\theta}_0$ at nominal theoretical frequencies across 1,000 independent simulation replications (Simulation-Based Calibration).
2. **Detection of Geometric Funnels via Divergent Transitions**: In Hamiltonian Monte Carlo, any single divergent transition signifies that the simulated trajectory has encountered a region of infinite curvature where numerical leapfrog integration breaks down. Reparameterizing the model from a centered formulation $\theta \sim \mathcal{N}(\mu, \sigma^2)$ to a non-centered formulation $\tilde{\theta} \sim \mathcal{N}(0, 1)$ with $\theta = \mu + \sigma \tilde{\theta}$ straightens the target geometry and eliminates divergences.
3. **Energy Bayesian Fraction of Missing Information (E-BFMI)**: In HMC, compute the energy metric:
$$\text{E-BFMI} = \frac{\sum_{t=1}^N (E_t - E_{t-1})^2}{\sum_{t=1}^N (E_t - \bar{E})^2}$$
A value of $\text{E-BFMI} < 0.3$ indicates that the momentum distribution cannot effectively explore the energy state space, diagnosing poor momentum mass matrix adaptation or heavy tail pathologies.
"""

def main():
    append_to_unit(4, u4_buf)
    append_to_unit(5, u5_buf)
    append_to_unit(7, u7_buf)
    print("Buffer sections added.")

if __name__ == "__main__":
    main()
