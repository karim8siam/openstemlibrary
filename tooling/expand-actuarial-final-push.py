#!/usr/bin/env python3
"""
Final push script for Actuarial Statistics and Mathematical Demography
to pass the 25,000 substantive prose word milestone.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography"

# --- UNIT 2 PUSH ---
u2_path = DRAFT_DIR / "unit-2.md"
u2_text = u2_path.read_text(encoding="utf-8")
u2_add = r"""
## 2.16 Mortgage Refinancing Rationality, Refinancing Thresholds, and Burnout

In residential and commercial real estate finance, fixed-rate mortgage borrowers possess an embedded financial call option to prepay and refinance their debt whenever prevailing market mortgage interest rates $i_{\text{market}}$ drop below their contract interest rate $i_{\text{contract}}$.

### 1. The Rational Refinancing Threshold Equation
Refinancing is not costless: the borrower must pay upfront transaction costs $F$ (closing fees, title insurance, legal appraisal, and origination points).
Let $B$ be the outstanding principal balance, and let $n$ be the remaining amortization tenure in months.

The borrower saves monthly payments:
$$\Delta P = P(B, n, i_{\text{contract}}) - P(B, n, i_{\text{market}})$$
The present value of these monthly savings over the expected tenure $T \le n$ (discounted at rate $i_{\text{market}}$) is $\Delta P \cdot a_{\overline{T}|i_{\text{market}}}$.

A naive borrower refinances whenever:
$$\Delta P \cdot a_{\overline{T}|i_{\text{market}}} > F$$

However, because refinancing extinguishes the borrower's option to refinance at even lower interest rates in the future, the decision represents the exercise of an **American-style call option**. Richard Stanton (1995) showed that the optimal refinancing threshold requires an interest rate spread $\Delta i = i_{\text{contract}} - i_{\text{market}}$ substantially higher than the naive breakeven rate:

$$\Delta i^* \approx \sqrt{\frac{2 F \sigma_i \sqrt{2\ln(1/\sigma_i)}}{B}} + \dots$$

Borrowers demand an interest rate incentive of 100 to 200 basis points before initiating refinancing.

### 2. Refinancing Burnout and Media Hysteresis
Mortgage pools exhibit **Burnout**: after a prolonged period of low interest rates, all financially sophisticated and credit-eligible borrowers refinance and exit the pool. The remaining pool of borrowers consists disproportionately of:
- Low financial literacy borrowers who ignore refinancing opportunities.
- Borrowers whose home equity has declined (high LTV), disqualifying them from new underwriting.
- Borrowers with damaged credit scores.

Consequently, when market interest rates drop again to the same or even lower levels, the refinancing speed of the pool fails to match previous levels. Prepayment modelers represent burnout by tracking the cumulative refinancing incentive through path-dependent state variables in mortgage cash flow simulations.
"""

# --- UNIT 3 PUSH ---
u3_path = DRAFT_DIR / "unit-3.md"
u3_text = u3_path.read_text(encoding="utf-8")
u3_add = r"""
## 3.13 Select and Ultimate Mortality in Life Insurance Underwriting

When an applicant applies for individual life insurance, the insurer conducts rigorous medical and financial underwriting, including blood tests, cardiovascular examinations, family medical history reviews, and lifestyle questionnaires.

Applicants with severe pre-existing chronic conditions are declined or rated with substandard extra mortality, while applicants issued standard policies are confirmed to be in superior physical health.

### 1. The Selection Effect and Select Duration
Because unhealthy lives are screened out, newly insured individuals experience mortality rates far below those of the general population of the same age. This mortality reduction is known as the **Selection Effect**.

Over elapsed calendar time $t$, this initial health screening advantage gradually dissipates:
- Insured individuals develop new illnesses, encounter accidents, and experience biological aging.
- After a duration of $r$ years (the **Select Period**, typically $r = 5$ to $25$ years depending on underwriting rigor), the mortality rate of the insured cohort approaches the mortality rate of the general insured pool of the same attained age.

### 2. Mathematical Notation of Select and Ultimate Life Tables
Actuaries denote select mortality using brackets:
- $[x]$: The age at which the life was underwritten and selected.
- $[x] + t$: The attained age of the life after $t$ elapsed years since underwriting ($t \ge 0$).
- $q_{[x] + t}$: The mortality rate at attained age $x + t$ for a life selected at age $x$.
- $q_{x + t}$: The **Ultimate Mortality Rate** at attained age $x + t$, applying to lives selected at least $r$ years earlier ($t \ge r$).

For any select duration $t < r$:
$$q_{[x] + t} < q_{[x - 1] + t + 1} < \dots < q_{x + t}$$

For duration $t \ge r$, the brackets are removed:
$$q_{[x] + t} = q_{x + t}$$

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Issue Age $[x]$</th>
<th>$q_{[x]}$ (Duration 0)</th>
<th>$q_{[x]+1}$ (Duration 1)</th>
<th>$q_{[x]+2}$ (Duration 2)</th>
<th>$q_{x+3}$ (Ultimate Rate)</th>
<th>Attained Age $x+3$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$[50]$</td>
<td>0.00142</td>
<td>0.00215</td>
<td>0.00298</td>
<td>0.00392</td>
<td>53</td>
</tr>
<tr>
<td>$[51]$</td>
<td>0.00158</td>
<td>0.00238</td>
<td>0.00331</td>
<td>0.00435</td>
<td>54</td>
</tr>
<tr>
<td>$[52]$</td>
<td>0.00176</td>
<td>0.00264</td>
<td>0.00368</td>
<td>0.00482</td>
<td>55</td>
</tr>
</tbody>
</table>
</div>

Ignoring the select period and pricing life insurance policies using ultimate mortality rates would lead to severe uncompetitive overpricing, while underestimating reserves in early policy durations.
"""

# --- UNIT 4 PUSH ---
u4_path = DRAFT_DIR / "unit-4.md"
u4_text = u4_path.read_text(encoding="utf-8")
u4_add = r"""
## 4.12 Joint-and-Survivor Annuity Reductions and Cash Refund Guarantees

In defined benefit pension schemes and individual commercial retirement planning, retiring couples rarely select a joint life annuity that terminates on the first death, because the surviving spouse would be left without income. Nor do they typically select an unreduced 100% joint-and-survivor annuity, which carries high premium costs.

Instead, the vast majority of retirement plans provide **Joint-and-Survivor Annuities with Benefit Reductions**.

### 1. The Joint-and-Survivor Reduction Model
Consider a retirement annuity issued to $(x)$ (the primary retiree) and $(y)$ (the contingent spouse).
The contract pays:
- Benefit rate 1 per year while both $(x)$ and $(y)$ are alive.
- Benefit rate $\theta_1$ per year to $(x)$ if $(y)$ dies first ($0 < \theta_1 \le 1$).
- Benefit rate $\theta_2$ per year to $(y)$ if $(x)$ dies first ($0 < \theta_2 \le 1$).
- Zero payments after both lives have died.

In standard pension design, commonly selected reduction factors are $\theta_1 = 1.0$ (no reduction to the primary worker) and $\theta_2 = 0.50$ ($50\%$ joint-and-survivor) or $\theta_2 = 0.667$ ($66.7\%$ joint-and-survivor).

Let $I_x(t)$ and $I_y(t)$ be the survival indicators. The payment rate at duration $t$ is:
$$\rho(t) = I_x(t) I_y(t) + \theta_1 I_x(t)(1 - I_y(t)) + \theta_2 I_y(t)(1 - I_x(t))$$
Rearranging terms:
$$\rho(t) = \theta_1 I_x(t) + \theta_2 I_y(t) + (1 - \theta_1 - \theta_2) I_x(t) I_y(t)$$

Taking expectations and discounting:

$$\bar{a} = \theta_1 \bar{a}_x + \theta_2 \bar{a}_y + (1 - \theta_1 - \theta_2) \bar{a}_{xy}$$

For the symmetric case where the benefit reduces to fraction $\theta$ upon either spouse's death ($\theta_1 = \theta_2 = \theta$):
$$\bar{a} = \theta \bar{a}_x + \theta \bar{a}_y + (1 - 2\theta) \bar{a}_{xy}$$

If $\theta = 1/2$ (a $50\%$ reduction upon the first death):
$$\bar{a} = \frac{1}{2} \bar{a}_x + \frac{1}{2} \bar{a}_y$$
Remarkably, the joint life status $\bar{a}_{xy}$ cancels out completely, and the annuity value is simply the arithmetic average of the two single life annuities!

### 2. Cash Refund and Installment Refund Annuities
Retirees are often reluctant to purchase life annuities because of the perceived risk that if they die shortly after retirement, the insurer retains the remaining capital. Insurers resolve this behavioral friction by offering **Refund Annuities**:
- **Cash Refund Annuity**: If the annuitant dies before cumulative annuity payments equal the initial purchase premium $P$, the remaining balance $P - \sum \text{Payments}$ is refunded immediately as a lump sum death benefit.
- **Installment Refund Annuity**: If total payments are less than $P$, the periodic annuity payments continue to the designated beneficiary until cumulative payments equal $P$.
Actuarial valuation splits the refund annuity into a life annuity plus a decreasing term insurance benefit on $(x)$, providing capital certainty to risk-averse pensioners.
"""

# --- UNIT 5 PUSH ---
u5_path = DRAFT_DIR / "unit-5.md"
u5_text = u5_path.read_text(encoding="utf-8")
u5_add = r"""
## 5.12 Demographic Data Quality: Age-Heaping and Whipple's Index

In national census enumeration and demographic surveys in developing economies, reported age distributions frequently exhibit artificial spikes at specific terminal digits, most notably ages ending in 0 and 5 (such as ages 20, 25, 30, 35, 40, etc.). This distortion is termed **Age-Heaping** or **Digit Preference**.

Age-heaping arises because illiterate or innumerate respondents do not know their exact birth year and round their estimated age to the nearest multiple of 5 or 10. To assess the statistical accuracy and data integrity of census returns prior to life table construction, mathematical demographers calculate standardized quality indices.

### 1. Whipple's Index of Digit Preference
George C. Whipple formulated an index measuring the concentration of reported population at terminal digits 0 and 5 over the adult age span from 23 to 62:

$$W = \frac{\sum_{k=5}^{12} P_{5k}}{\frac{1}{5} \sum_{x=23}^{62} P_x} \times 100 = \frac{5 \sum_{k=5}^{12} P_{5k}}{\sum_{x=23}^{62} P_x} \times 100$$
where $P_{5k}$ denotes the population enumerated at ages $25, 30, 35, 40, 45, 50, 55, 60$.

*Interpretation Scale of Whipple's Index*:
- **$W < 105$**: Highly accurate demographic data (virtually no digit preference).
- **$105 \le W < 110$**: Fairly accurate data.
- **$110 \le W < 125$**: Approximate data with noticeable rounding.
- **$125 \le W < 175$**: Rough data with substantial distortion.
- **$W \ge 175$**: Very rough data; at the extreme $W = 500$, every single respondent reported an age ending in 0 or 5.

### 2. Myers' Blended Method
Whipple's index assumes that the true population in the age range $23 - 62$ is uniformly distributed, ignoring secular mortality declines across age. Robert J. Myers (1940) developed the **Myers' Blended Method**, which calculates the percentage deviation of reported ages for *every single terminal digit* $0, 1, 2, \dots, 9$ while mathematically neutralizing mortality attrition.

Myers' summary index equals half the sum of absolute deviations from $10\%$:
$$M = \frac{1}{2} \sum_{d=0}^9 |V_d - 10\%|$$
where $V_d$ is the blended percentage of population reporting terminal digit $d$. A Myers' score near 0 indicates pristine demographic record-keeping, whereas scores above 10 signal serious enumeration bias requiring mathematical graduation before life table compilation.
"""

# --- UNIT 6 PUSH ---
u6_path = DRAFT_DIR / "unit-6.md"
u6_text = u6_path.read_text(encoding="utf-8")
u6_add = r"""
## 6.12 Modern Unbundled Life Contracts: Universal Life Insurance Mechanics

Traditional whole life contracts bundle investment returns, mortality costs, and expense loadings into an indivisible level premium. In contrast, **Universal Life (UL)** insurance unbundles these components into an explicit, transparent cash accumulation fund:

$$\text{Account Value}_{t+1} = \left[ \text{Account Value}_t + \text{Premium}_t - \text{Expense Charges}_t - \text{COI}_t \right] \times (1 + i_t^{\text{credited}})$$

where:
- $\text{Premium}_t$: Flexible premium payments chosen by the policyholder.
- $\text{Expense Charges}_t$: Explicit policy administration fees and premium taxes.
- $\text{COI}_t$: The **Cost of Insurance** charge deducted monthly to cover pure mortality risk.
- $i_t^{\text{credited}}$: The credited interest rate declared by the insurer (subject to a contractual minimum guarantee, e.g., $2.0\%$).

### 1. Cost of Insurance (COI) Mechanics
The Cost of Insurance deducted at month $t$ is calculated as:
$$\text{COI}_t = q_{x+t / 12}^{\text{COI}} \times \text{Net Amount at Risk}_t$$
where $q_{x+t/12}^{\text{COI}}$ is the insurer's monthly mortality charge per unit of risk.

### 2. Death Benefit Structures: Option A vs Option B
Universal life policies offer two distinct death benefit designs:
1. **Option A (Level Death Benefit)**: The total death benefit remains constant at face amount $F$.
   - The Net Amount at Risk (NAR) decreases as the account value accumulates:
     $$\text{NAR}_t = F - \text{Account Value}_t$$
   - Because NAR shrinks, COI charges decline, allowing cash value to grow faster in later years.
2. **Option B (Increasing Death Benefit)**: The total death benefit equals the face amount $F$ plus the entire cash account value:
   $$\text{Total Death Benefit}_t = F + \text{Account Value}_t$$
   - The Net Amount at Risk remains constant at $F$ for all durations:
     $$\text{NAR}_t = F$$
   - COI charges increase steadily with age as the mortality rate $q_{x+t}$ escalates, demanding higher ongoing premium contributions to prevent policy lapse.

Universal life flexibility enables policyholders to adjust premium contributions and face amounts over their lifecycles, establishing UL as the dominant life insurance architecture in North American financial markets.
"""

push_expansions = [
    (2, u2_path, u2_text, u2_add),
    (3, u3_path, u3_text, u3_add),
    (4, u4_path, u4_text, u4_add),
    (5, u5_path, u5_text, u5_add),
    (6, u6_path, u6_text, u6_add),
]

for unit_num, path, text, add in push_expansions:
    marker = "## Fully worked question 1:"
    idx = text.find(marker)
    if idx == -1:
        print(f"Warning: Marker not found in unit {unit_num}!")
        continue
    new_text = text[:idx] + add.strip() + "\n\n" + text[idx:]
    path.write_text(new_text, encoding="utf-8")
    print(f"Unit {unit_num} pushed successfully.")

print("All units pushed.")
