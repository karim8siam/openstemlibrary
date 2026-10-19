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

# Expand Unit 2
u2 = (d / "unit-2.md").read_text(encoding="utf-8")
u2_add = """
### Sociological and Biological Mechanisms of Sex Differentials Across the Lifespan
To understand why the age-specific sex ratio shifts from a substantial male surplus at birth to an overwhelming female majority in extreme old age, mathematical demographers examine the interplay between biological vulnerabilities and behavioral determinants.

From the moment of conception, the human male exhibits greater biological frailty. Geneticists observe that because human males possess only a single X chromosome (hemizygosity), any deleterious recessive allele situated on the X chromosome is directly expressed phenotypically without the masking protection of a homologous normal allele, as occurs in females. Consequently, spontaneous miscarriages, intrauterine fetal deaths, and stillbirths occur at systematically higher rates among male fetuses. Furthermore, during early infancy, male neonates suffer higher incidence of respiratory distress syndrome due to delayed fetal lung surfactant maturation regulated by androgenic hormones, as well as higher susceptibility to neonatal sepsis and congenital heart disease.

As individuals progress into adolescence and young adulthood, behavioral and sociological factors compound this biological baseline. Demographers refer to the localized surge in male mortality between ages 15 and 29 as the accident hump. Young adult males experience markedly higher exposure to occupational hazards in heavy construction, mining, maritime transit, and industrial manufacturing. Furthermore, elevated circulating testosterone levels, cultural norms of bravado, and risk-taking behaviors contribute to substantially higher rates of fatal motor vehicle collisions, drownings, alcohol and substance overdoses, interpersonal violence, and suicide among young men compared to women of the same age.

In mid-life and advanced old age (ages 45 through 80), chronic lifestyle-related diseases dominate mortality schedules. Historically, higher rates of cigarette smoking, industrial pollution exposure, and cardiovascular atherogenesis led to massive male excess mortality from ischemic heart disease, stroke, and chronic obstructive pulmonary disease. Although modern lifestyle convergence in post-industrial nations has reduced the cardiovascular mortality gap, women continue to retain an intrinsic survival advantage. Biological demographers attribute this persistent longevity gap to the anti-inflammatory and cardioprotective effects of endogenous estrogens during pre-menopausal years, superior cellular DNA repair mechanisms, and lower lifelong visceral fat accumulation in females.

Consequently, in populations with high life expectancy, the survival curve for females is shifted noticeably to the right relative to males. By age 85, surviving women outnumber men by more than two to one, and among supercentenarians aged 110 and older, over ninety percent are female. This severe structural imbalance has profound societal ramifications, requiring specialized health systems, elder-care infrastructure, and pension survivor protections tailored to long-surviving elderly widows.
"""
u2 = u2.replace("## Fully worked question 3", u2_add + "\n## Fully worked question 3")
(d / "unit-2.md").write_text(u2, encoding="utf-8")

# Expand Unit 3
u3 = (d / "unit-3.md").read_text(encoding="utf-8")
u3_add = """
### Epidemiological Transition Theory and the Changing Architecture of Causes of Death
To place mortality measures and cause-deleted life tables into long-term historical context, demographers rely upon Abdel Omran's celebrated **Epidemiological Transition Theory** (1971). Omran conceptualized human mortality history as progressing through three distinct evolutionary stages, subsequently expanded by S. Jay Olshansky and A. Brian Ault (1986) into four stages:

1. **The Age of Pestilence and Famine**: Characterized by catastrophic, volatile mortality driven by infectious pandemics (such as the Black Death, cholera, typhus, and smallpox), endemic tuberculosis, and malnutrition. Life expectancy at birth fluctuated violently between twenty and thirty-five years, and children under age five accounted for nearly half of all deaths.
2. **The Age of Receding Pandemics**: Spanning the mid-nineteenth through early twentieth centuries in industrializing territories. Public health engineering—including piped chlorinated water supplies, modern municipal sewage treatment, pasteurization of commercial milk supplies, swamp drainage for malaria control, and improved residential ventilation—dramatically curtailed waterborne and airborne pathogens prior to the widespread commercial availability of antibiotics. Mortality stabilized, and life expectancy rose steadily toward fifty and sixty years.
3. **The Age of Degenerative and Man-Made Diseases**: Infectious diseases retreated to minor causes of death, replaced by chronic degenerative conditions associated with biological aging, sedentary occupations, high-calorie processed diets, and tobacco usage. Cardiovascular diseases (coronary artery disease, myocardial infarction, ischemic stroke) and malignant neoplasms (cancers) became responsible for over seventy percent of all recorded deaths.
4. **The Age of Delayed Degenerative Diseases**: Emerging in the late twentieth century across advanced industrial economies. Breakthroughs in medical technology (such as coronary artery bypass grafting, statins, antihypertensive pharmacotherapy, thrombolysis, and targeted oncology treatments), coupled with dramatic declines in adult tobacco smoking, postponed the fatal onset of cardiovascular disease and stroke into extreme old age. The mortality curve underwent substantial rectangularization, pushing median age at death into the eighties and nineties.

Understanding these epidemiological transitions is essential for mathematical demographers constructing Cause-Deleted Life Tables. In Stage 3 societies, eliminating cardiovascular disease generates immense gains in life expectancy because deaths occur in mid-adulthood. In Stage 4 societies, eliminating a single disease yields smaller gains because older individuals suffer from multiple competing comorbidities (frailty, cognitive dementia, multiple organ failure), so that preventing a cardiovascular death quickly exposes the surviving individual to mortality from another degenerative pathology.
"""
u3 = u3.replace("## Fully worked question 3", u3_add + "\n## Fully worked question 3")
(d / "unit-3.md").write_text(u3, encoding="utf-8")

# Expand Unit 4
u4 = (d / "unit-4.md").read_text(encoding="utf-8")
u4_add = """
### Analytical Properties of the Life Table: Rectangularization and Compression of Morbidity
A foundational topic in theoretical demography is the mathematical shape of the survival curve $l(x)$ and its evolution over the past two centuries. When demographers plot the cohort survivor column $l(x)$ against age $x$ across successive historical epochs, a striking geometric metamorphosis becomes apparent: the survival curve transforms from a gentle, steeply descending convex slope into an increasingly high, flat plateau that plunges almost vertically at advanced ages. This phenomenon is known as the **Rectangularization of the Survival Curve** (or the compression of mortality).

#### Mathematical Measurement of Rectangularization
To quantify the degree of rectangularization rigorously, mathematical demographers deploy several analytic metrics:
1. **The Interquartile Range of Age at Death ($IQR$)**: Let $x_{75}, x_{50}, x_{25}$ denote the ages at which the synthetic cohort survivor function $l(x)$ equals $75{,}000, 50{,}000,$ and $25{,}000$ respectively (corresponding to the 25th percentile, median, and 75th percentile of the life table distribution of deaths). The interquartile range is defined as:
   $$IQR = x_{25} - x_{75}$$
   In historical high-mortality populations, deaths were dispersed widely across the entire life span, resulting in an $IQR$ exceeding fifty or sixty years. In modern post-industrial societies with highly rectangularized survival curves, deaths are heavily concentrated into a narrow chronological band between ages 75 and 92, compressing the $IQR$ down to twelve or fourteen years.
2. **The Keyfitz Entropy Parameter ($H$)**: Nathan Keyfitz formulated a dimensionless measure of mortality entropy that characterizes the convexity of the survival curve:
   $$H = \\frac{\\int_0^{\\infty} e(x) l(x) \\mu(x) \\, dx}{e_0 \\cdot l_0} = -\\frac{\\int_0^{\\infty} l(x) \\ln l(x) \\, dx}{\\int_0^{\\infty} l(x) \\, dx}$$
   The entropy parameter $H$ possesses a profound biological interpretation: it represents the percentage increase in life expectancy at birth that would result from a uniform one percent proportional reduction in the force of mortality at all ages:
   $$\\frac{d e_0 / e_0}{-d \\mu / \\mu} = H$$
   - For an idealized completely rectangular survival schedule where everyone lives to exact age $\\omega$ and dies simultaneously, $H = 0$. In this limit, reducing mortality yields zero gain in life expectancy because lifespan is already maximal.
   - For a population subject to constant force of mortality $\\mu(x) = \\mu$ across all ages (an exponential survival curve $l(x) = l_0 e^{-\\mu x}$), $H = 1$.
   - In modern developed countries, $H$ has declined steadily from approximately $0.80$ in the nineteenth century down to $0.15$ or $0.18$ today, demonstrating that human survival curves are approaching a highly rectangular state.

#### The Compression of Morbidity Hypothesis
In 1980, James F. Fries proposed the influential **Compression of Morbidity** hypothesis in medicine and actuarial science. Fries asserted that because maximum human biological lifespan is genetically bounded by teleomeric attrition, cellular oxidative damage, and physiological senescence, life expectancy cannot expand indefinitely. However, if the onset of chronic debilitating diseases (osteoarthritis, vascular dementia, cardiovascular impairment) can be delayed more rapidly than the modest gains in maximum life expectancy, the average duration of lifetime disability will be compressed into a very brief period immediately preceding death.

Testing Fries's hypothesis requires constructing **Health-Adjusted Life Tables (HALEs)** and **Disability-Free Life Tables (Sullivan Method)**, which partition total life table person-years $_n L_x$ into years lived in good functional health versus years lived with moderate or severe functional limitations. Actuaries and health economists use Sullivan's method to calculate the proportion of total life expectancy spent free of disability, providing vital empirical data for long-term care insurance and state pension sustainability.
"""
u4 = u4.replace("## Fully worked question 2", u4_add + "\n## Fully worked question 2")
(d / "unit-4.md").write_text(u4, encoding="utf-8")

print(f"Unit 2 now: {prose_count((d / 'unit-2.md').read_text(encoding='utf-8'))} words")
print(f"Unit 3 now: {prose_count((d / 'unit-3.md').read_text(encoding='utf-8'))} words")
print(f"Unit 4 now: {prose_count((d / 'unit-4.md').read_text(encoding='utf-8'))} words")
