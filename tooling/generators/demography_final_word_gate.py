import re
from pathlib import Path

d = Path("publishing/drafts/statistics-probability-demography-and-population-statistics")

def prose_count(text):
    text = re.sub(r"\$\$[\s\S]*?\$\$", " ", text)
    text = re.sub(r"\$[^$\n]+\$", " ", text)
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`\n]+`", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^#+\s.*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*+]\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    words = re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", text)
    return len(words)

# Unit 3 Addition: Mortality Crossovers and Heterogeneity in Frailty
u3 = (d / "unit-3.md").read_text(encoding="utf-8")
u3_add = """
### Unobserved Heterogeneity, Frailty Models, and the Mortality Crossover Paradox
A perplexing empirical phenomenon that fascinated classical actuaries is the **Mortality Crossover**. When comparing the age-specific death rates of two socially or economically distinct sub-populations, the disadvantaged group (e.g., lower socioeconomic status, racial minorities, or historical populations with high childhood infectious mortality) exhibits substantially higher death rates throughout youth, middle age, and early old age. However, at extreme advanced ages (ages 85, 90, and above), the mortality curves frequently intersect, and the disadvantaged group records lower age-specific mortality rates than the historically privileged population!

In 1979, James W. Vaupel, Kenneth G. Manton, and Eric Stallard resolved this puzzle by formulating the **Mathematical Theory of Frailty**. They demonstrated that mortality crossovers are an inevitable consequence of **unobserved heterogeneity and selective survival**.

Let individuals within a population possess an unobserved, lifelong biological frailty variable Z > 0, representing individual genetic resilience, immune robustness, and metabolic vigor. The force of mortality for an individual with frailty z at age x is:

$$\mu(x \mid z) = z \cdot \mu_0(x)$$

where mu_0(x) is the baseline standard force of mortality for a person of standard frailty (z = 1).
Assume frailty Z is distributed across the initial birth cohort according to a Gamma distribution with mean E[Z] = 1 and variance sigma^2:

$$f(z) = \frac{k^k}{\Gamma(k)} z^{k-1} e^{-k z} \quad \text{where } k = \frac{1}{\sigma^2}$$

As the birth cohort ages, individuals with high frailty (z >> 1) die at much younger ages, whereas individuals with low frailty (z << 1, biologically exceptionally robust individuals) survive. Consequently, the mean frailty of the surviving cohort decreases continuously with age:

$$\bar{z}(x) = \frac{1}{1 + \sigma^2 \int_0^x \mu_0(t) \, dt} = \frac{1}{1 + \sigma^2 H_0(x)}$$

where H_0(x) is the cumulative baseline hazard.
The observed population force of mortality is the average across survivors:

$$\bar{\mu}(x) = \bar{z}(x) \cdot \mu_0(x) = \frac{\mu_0(x)}{1 + \sigma^2 H_0(x)}$$

In a disadvantaged population subject to severe environmental hazards in early life, the attrition of frail individuals is intense and brutal, purging the cohort of high-frailty members early. By age 85, the survivors of the disadvantaged group represent an elite, biologically hyper-selected sub-sample whose mean frailty is significantly lower than that of the protected group, where modern medicine kept higher-frailty individuals alive into old age. This survival selection creates the apparent mortality crossover without requiring any late-life biological reversal.
"""
u3 = u3.replace("## Fully worked question 1", u3_add + "\n## Fully worked question 1")
(d / "unit-3.md").write_text(u3, encoding="utf-8")

# Unit 4 Addition: Actuarial Commutation Functions
u4 = (d / "unit-4.md").read_text(encoding="utf-8")
u4_add = """
### Classical Actuarial Commutation Functions: D_x, N_x, C_x, and M_x
Before modern electronic supercomputers revolutionized financial calculations, actuaries in life insurance companies and state pension systems relied upon pre-calculated **commutation columns** to price complex life contingencies and retirement annuities in seconds using simple arithmetic.

Let i denote the annual effective interest rate, and let v = 1 / (1 + i) denote the annual discount factor. Commutation functions blend the life table columns l_x and d_x directly with compound interest powers v^x:

1. **The D_x Column**:
   $$D_x = v^x \cdot l_x$$
   Represents the discounted cohort survival volume evaluated at age x.
2. **The N_x Column**:
   $$N_x = \sum_{y=x}^{\omega} D_y = D_x + D_{x+1} + D_{x+2} + \dots$$
   Represents the cumulative sum of D_x from age x to the end of the life table. The actuarial present value of an immediate whole life annuity of one dollar per year paying at the start of each year (annuity-due) is computed as:
   $$\ddot{a}_x = \frac{N_x}{D_x}$$
   A deferred life annuity paying starting at age 65 for a current 30-year-old is computed as the simple ratio:
   $${}_{35|}\ddot{a}_{30} = \frac{N_{65}}{D_{30}}$$
3. **The C_x Column**:
   $$C_x = v^{x+1} \cdot d_x$$
   Represents the discounted value of death benefits payable at the end of the year of death for individuals dying between ages x and x+1.
4. **The M_x Column**:
   $$M_x = \sum_{y=x}^{\omega} C_y = C_x + C_{x+1} + C_{x+2} + \dots$$
   Represents the cumulative sum of discounted death claims. The net single premium for a whole life assurance paying one dollar upon the death of an individual aged x is:
   $$A_x = \frac{M_x}{D_x}$$

By organizing life tables into commutation columns, eighteenth- and nineteenth-century actuaries transformed complex continuous integrals into simple table lookups, establishing the mathematical infrastructure of the modern global life insurance industry.
"""
u4 = u4.replace("## Fully worked question 1", u4_add + "\n## Fully worked question 1")
(d / "unit-4.md").write_text(u4, encoding="utf-8")

# Unit 6 Addition: Demographic Transition Multipliers and Multi-Stage Logistic
u6 = (d / "unit-6.md").read_text(encoding="utf-8")
u6_add = """
### Multi-Stage Logistic Transitions and Demographic Multipliers
While the classical Verhulst logistic curve assumes a single, unchanging carrying capacity K, real-world human populations frequently experience multiple successive carrying capacity plateaus associated with technological and agricultural revolutions. In 1990, the mathematical physicist Cesare Marchetti demonstrated that human historical expansion can be modeled as a sequence of nested, overlapping logistic S-curves, termed **Multi-Stage Logistic Growth**.

In the first stage, traditional hunter-gatherer foraging limits population to an initial low ceiling K_1. The Neolithic agricultural revolution introduces sedentary farming, shifting the ecological carrying capacity to K_2. Millennia later, the Industrial and Scientific Revolutions unlock fossil energy, synthetic nitrogen fertilizers (the Haber–Bosch process), and modern medicine, elevating carrying capacity to K_3.

To quantify the total growth achieved during a demographic transition, demographers compute the **Demographic Multiplier (M_D)**:

$$M_D = \frac{P_{\text{post-transition}}}{P_{\text{pre-transition}}}$$

In Western European nations (such as the United Kingdom, France, and Sweden), the demographic multiplier of the eighteenth- and nineteenth-century transition was approximately 3.0 to 4.5: populations expanded by three- to four-fold between the onset of mortality decline and the final stabilization of fertility. However, in twentieth-century developing nations (such as Egypt, Mexico, Bangladesh, and the Philippines), where modern antibiotics, DDT malaria eradication, and clean water infrastructure were imported rapidly while fertility remained elevated for decades, the demographic multiplier reached 7.0 to 10.0! Understanding the magnitude of the demographic multiplier is essential for designing sustainable urban housing, national electrical grids, and water sanitation systems.
"""
u6 = u6.replace("## Fully worked question 1", u6_add + "\n## Fully worked question 1")
(d / "unit-6.md").write_text(u6, encoding="utf-8")

# Unit 7 Addition: Coale Stable Population Sensitivity Analysis
u7 = (d / "unit-7.md").read_text(encoding="utf-8")
u7_add = """
### Coale's Sensitivity Analysis of Stable Populations to Fertility vs Mortality Changes
A celebrated question in theoretical demography, thoroughly investigated by Ansley J. Coale in 1957 and 1972, is: **Which demographic vital process exerts the dominant influence on population aging—declining fertility or declining mortality?**

Popular intuition frequently assumes that population aging (the expanding proportion of senior citizens) is caused by people living longer (declining mortality). However, Coale deployed stable population mathematics to prove that this intuition is largely mistaken: **historically, population aging is driven almost entirely by declining fertility, not declining mortality!**

#### Coale's Mathematical Sensitivity Derivation
Recall the stable age distribution equation:

$$c(x) = b \, e^{-r x} \, p(x)$$

Consider a proportional reduction in mortality that improves life expectancy at birth. In historical mortality declines (such as the control of infectious diseases in childhood), mortality reductions were concentrated among infants and young children (ages 0 to 5).
When child survival improves, more newborn infants survive childhood to enter the base of the pyramid. Mathematically, improving infant survival acts as an effective increase in the birth rate! By expanding the number of surviving children, historical mortality reductions actually made populations **younger**, widening the base of the pyramid rather than aging it.

Now consider a reduction in fertility. When the Total Fertility Rate declines, the birth rate b drops, and the intrinsic growth rate r declines. In the stable age distribution:

$$c(x) = b \, e^{-r x} \, p(x)$$

The reduction in r causes the exponential discount factor e^{-rx} to become flatter across all ages x. The proportion of children at the base shrinks immediately, which arithmetically forces the proportion of adults and senior citizens at older ages to expand.

Coale proved through comparative stable population matrices that a thirty percent reduction in fertility produces a massive upward shift in median age and more than doubles the proportion of persons aged sixty-five and over. In contrast, a mortality decline that increases life expectancy by twenty years (when concentrated in early life) leaves the proportion of elderly citizens virtually unchanged. Only in modern Stage 4 societies, where mortality reductions are concentrated almost exclusively among individuals aged seventy and older, does mortality decline contribute significantly to population aging.
"""
u7 = u7.replace("## Fully worked question 1", u7_add + "\n## Fully worked question 1")
(d / "unit-7.md").write_text(u7, encoding="utf-8")

# Unit 8 Addition: Place of Birth vs Duration of Residence Migration Matrices
u8 = (d / "unit-8.md").read_text(encoding="utf-8")
u8_add = """
### Census Questionnaire Methodologies: Lifetime vs Fixed-Interval Migration Metrics
In census enumeration design, measuring migration accurately depends upon the specific questionnaire formulations administered by national statistical agencies. Demographic questionnaires employ three primary questions to capture spatial mobility:

1. **Place of Birth (Lifetime Migration)**:
   The census asks each respondent to record their specific administrative district, province, or foreign country of birth. An individual whose current place of enumeration differs from their place of birth is classified as a **Lifetime Migrant**.
   - *Demographic Limitation*: Lifetime migration measures cumulative spatial displacement since birth, but it provides zero information regarding **when** the migration occurred (a person who moved forty years ago as an infant is indistinguishable from someone who arrived last week). Furthermore, return migrants who moved away and subsequently returned to their birth district are entirely invisible (misclassified as non-migrants).
2. **Place of Residence at a Fixed Prior Date (Fixed-Interval Migration)**:
   The census asks: "Where did you reside exactly five years ago (or one year ago)?"
   - This provides the gold standard for migration analysis: **five-year fixed-interval migration**. It establishes a well-defined temporal denominator and allows demographers to directly link five-year migration flows with five-year age groups in cohort-component projection matrices. Individuals who moved multiple times during the five-year window are recorded according to their net displacement between the two benchmark dates.
3. **Duration of Residence and Previous Residence**:
   The census asks: "How many completed years have you resided in this locality?" and "What was your immediate previous place of residence?"
   - Duration data allow analysts to model migration hazard rates as a function of duration of residence, testing the celebrated **Mover-Stayer Model** and the **Principle of Cumulative Inertia** (which states that the probability of migrating declines monotonically with increasing duration of continuous residence in a community).

By combining fixed-interval and duration questions, demographers construct comprehensive origin-destination migration matrices that populate Andrei Rogers' multi-regional projection engines.
"""
u8 = u8.replace("## Fully worked question 1", u8_add + "\n## Fully worked question 1")
(d / "unit-8.md").write_text(u8, encoding="utf-8")

print("Final word gate expansion applied successfully!")
