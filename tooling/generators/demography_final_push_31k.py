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

# Unit 6: Empirical Ecological Validation and Drosophila Experiments
u6 = (d / "unit-6.md").read_text(encoding="utf-8")
u6_add = """
### Empirical Ecological Validation: Raymond Pearl's Drosophila Laboratory Experiments
In the 1920s, the biologist Raymond Pearl and his colleagues at Johns Hopkins University sought empirical experimental verification of the Verhulst logistic law under strictly controlled biological laboratory conditions. Pearl recognized that testing mathematical carrying capacities in human populations is inherently complicated by technological innovations, international trade, agricultural breakthroughs, and institutional changes that dynamically alter carrying capacities over time.

To isolate the pure biological mechanisms of logistic growth, Pearl designed controlled laboratory experiments using populations of the common fruit fly, *Drosophila melanogaster*. Fruit flies were introduced into standardized glass culture bottles containing a fixed, unreplenished quantity of nutrient agar medium (banana yeast agar) maintained at a constant temperature of twenty-five degrees Celsius. Starting with an initial breeding pair (P_0 = 2), Pearl recorded census counts of adult flies every three days over a forty-day period until the population stabilized and ultimately declined.

Pearl's experimental results provided a breathtaking confirmation of the logistic S-curve:
1. **Initial Exponential Phase (Days 0 to 12)**: At low fly densities, food and space were effectively infinite. Mortality was minimal, and the fly population expanded exponentially at a constant intrinsic rate r.
2. **Inflection Point (Day 16)**: At approximately sixteen days, corresponding to half the carrying capacity of the culture bottle (P ~ K/2 ~ 450 flies), the rate of absolute daily increase reached its peak.
3. **Deceleration and Saturation (Days 18 to 32)**: As adult fly density escalated, competition for space and egg-laying surfaces intensified. Female fecundity declined sharply: crowded female flies laid fewer eggs per day, and larval competition in the agar substrate caused high juvenile mortality. The population smoothly decelerated, asymptotically plateauing at an environmental carrying capacity of approximately K ~ 950 adult flies.

Pearl subsequently fitted the logistic equation to historical human census series for the United States, France, England and Wales, and Algeria. While the logistic curve fitted 19th-century counts with remarkable mathematical precision, Pearl's subsequent projections for the mid-20th century substantially underestimated actual population expansion. Pearl projected that the United States population would asymptotically plateau at K = 197 million people around the year 2000. In reality, the US population exceeded 280 million by 2000!

This historic divergence highlights the fundamental boundary between bio-ecology and human demography: whereas fruit flies cannot alter the dimensions or nutrient content of their glass bottle, human beings continuously reinvent their ecological niche through chemical fertilizers, high-yield seed hybridization, vertical urban architectural construction, and international commercial supply chains, transforming K from an ecological prison into an expanding technological horizon.
"""
u6 = u6.replace("## Fully worked question 3", u6_add + "\n## Fully worked question 3")
(d / "unit-6.md").write_text(u6, encoding="utf-8")

# Unit 7: Stable Population Dynamics under Migratory Shocks
u7 = (d / "unit-7.md").read_text(encoding="utf-8")
u7_add = """
### Open Stable Populations and Constant Influx Migration Models
While classical Lotka theory assumes a strictly closed population (zero net migration), modern sovereign states experience substantial, ongoing international immigration streams. In 1974 and 1982, the mathematical demographers Nathan Keyfitz and Frans Willekens generalized stable population theory to open populations subject to constant age-specific immigrant influx.

Let an open population experience a constant annual influx of I(x) immigrants at age x per year, subject to the domestic mortality schedule p(x) and fertility schedule m(x). The fundamental renewal integral becomes an inhomogeneous Volterra integral equation:

$$B(t) = G(t) + \int_0^t B(t - x) \, p(x) \, m(x) \, dx$$

where G(t) represents the births produced by surviving immigrants who arrived prior to time t.

Keyfitz established that:
1. If the host population has below-replacement fertility (NRR < 1, so that intrinsic growth r < 0), a constant absolute annual influx of immigrants prevents the population from extinguishing. The population does not expand exponentially; instead, it converges toward a stationary equilibrium whose absolute size is proportional to the annual immigrant stream divided by the intrinsic deficit (1 - NRR).
2. The age distribution of the immigrant-receiving population stabilizes into an asymptotic stable age distribution governed by the weighted convolution of the immigrant entry age schedule with domestic survival functions.
3. Because international migrants are overwhelmingly young adults in peak reproductive ages (ages 20 to 35), sustained immigration provides an immediate structural rejuvenation of the labor force, dampening old-age dependency ratios far more effectively than equivalent natural birth increases.
"""
u7 = u7.replace("## Fully worked question 2", u7_add + "\n## Fully worked question 2")
(d / "unit-7.md").write_text(u7, encoding="utf-8")

# Unit 3: Poisson Regression and Excess Mortality
u3 = (d / "unit-3.md").read_text(encoding="utf-8")
u3_add = """
### Poisson Log-Linear Regression for Age-Specific Death Rates and Excess Mortality
In modern public health surveillance and biostatistical modeling, age-specific mortality is modeled using Generalized Linear Models (GLMs), specifically **Poisson Log-Linear Regression**.

Let D_x denote the observed number of deaths in age group x, and let P_x denote the person-years of exposure. Because death is a rare event occurring within a large exposed population, the count of deaths follows a Poisson distribution:

$$D_x \sim \text{Poisson}(\mu_x \cdot P_x)$$

where mu_x is the true underlying mortality rate. Taking the natural logarithm of the expected death count:

$$\ln(\mathbb{E}[D_x]) = \ln(P_x) + \ln(\mu_x)$$

Here, ln(P_x) enters the regression model as an **offset variable** with a fixed coefficient of unity, transforming the model into a regression on log-rates.
By expressing ln(mu_x) as a linear combination of age factors, calendar periods, sex indicators, and environmental covariates, statisticians can estimate adjusted rate ratios and test epidemiological hypotheses with full maximum likelihood rigor.

#### Measuring Excess Mortality in Epidemiological Crises
During infectious pandemic waves (such as the 1918 influenza pandemic or the 2020–2022 COVID-19 pandemic) or extreme heatwaves, registered cause-of-death reporting is frequently lagged, under-reported, or distorted by diagnostic testing capacity constraints. Demographers measure the true lethal impact through **Excess Mortality**.

Excess mortality is defined as the difference between the total observed deaths from all causes during a crisis period and the baseline expected deaths projected from pre-crisis historical seasonal trends:

$$\text{Excess Deaths} = D_{\text{observed}} - \hat{D}_{\text{expected}}$$

Because total all-cause mortality requires no cause-of-death certification, excess mortality provides an objective, unvarnished measure of total pandemic mortality, capturing both direct viral fatalities and indirect deaths caused by healthcare system collapse.
"""
u3 = u3.replace("## Fully worked question 3", u3_add + "\n## Fully worked question 3")
(d / "unit-3.md").write_text(u3, encoding="utf-8")

print("Demography final push complete!")
