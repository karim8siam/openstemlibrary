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

# ==============================================================================
# BOOST UNIT 4: Life Table Construction, Abridged Methods & Actuarial Foundations
# ==============================================================================
u4 = (d / "unit-4.md").read_text(encoding="utf-8")
u4_extra = """
### Comparative Mathematical Evaluation of Abridged Life Table Construction Methods
When transforming empirical central death rates into life table probabilities, demographers can deploy several alternative mathematical graduation paradigms. Understanding the subtle analytical differences between these classical methods is essential for choosing the appropriate technique in national statistical offices.

#### 1. The Chiang Formulation (1968, 1984)
Chin Long Chiang established the standard modern formulation based on the exact separation factor a(x), which represents the mean duration of life lived within the age interval by those who die. Chiang's method assumes that within each adult age group (from age five up to the penultimate age group), the distribution of deaths can be modeled linearly, leading to an average separation factor of exactly half the interval width. Chiang's primary methodological contribution was deriving closed-form mathematical expressions for the variance and covariance of all life table columns, establishing the first rigorous sampling theory for life tables. In Chiang's framework, cohort attrition is treated as a sequence of conditional binomial trials, allowing researchers to compute asymptotic confidence intervals for life expectancy at any age.

#### 2. The Reed–Merrell Formulation (1939)
Lowell J. Reed and Margaret Merrell developed their method at Johns Hopkins University by fitting an empirical exponential relationship between observed central death rates and life table mortality probabilities across a large corpus of historical life tables. Rather than assuming a linear distribution of deaths within the age interval, Reed and Merrell recognized that biological senescence causes the force of mortality to accelerate exponentially within five-year intervals at older ages. Their formula introduces a cubic correction factor that captures this second-order upward curvature. For five-year age intervals, the Reed-Merrell formula provides an exceptionally robust conversion that slightly elevates mortality probabilities at ages sixty and older compared to linear formulas, accurately reflecting accelerated physiological decline.

#### 3. The Greville Formulation (1943)
Thomas N. E. Greville formulated an analytical conversion that directly incorporates the slope of the central death rate curve itself. Greville assumed that the central death rate m(x) follows an exponential trajectory across adjacent age intervals, such that the force of mortality can be expressed as a Gompertz curve. Greville proved that the separation factor a(x) can be computed endogenously from the data by evaluating the difference between the logarithmic death rates of the preceding and succeeding age intervals. Consequently, Greville's method does not require an arbitrary external choice of separation factors; the data themselves determine the degree of curvature within each interval.

#### 4. Keyfitz–Frauenthal Non-Parametric Graduation (1975)
Nathan Keyfitz and James Frauenthal developed a refined numerical quadrature method that estimates the separation factor a(x) by fitting a second-degree polynomial (parabola) through three adjacent values of the living population and death counts. By using numerical integration across the three cohorts, Keyfitz and Frauenthal demonstrated that the separation factor can be expressed as a linear combination of adjacent population counts. This technique eliminates boundary artifacts and provides the highest degree of mathematical fidelity in populations undergoing rapid epidemiological transitions where mortality schedules depart from standard Gompertz models.
"""
u4 = u4.replace("## Fully worked question 1", u4_extra + "\n## Fully worked question 1")
(d / "unit-4.md").write_text(u4, encoding="utf-8")

# ==============================================================================
# BOOST UNIT 6: Non-Linear Logistic Dynamics and Historical Transitions
# ==============================================================================
u6 = (d / "unit-6.md").read_text(encoding="utf-8")
u6_extra = """
### Historical Perspectives on Demographic Growth: Malthusian vs Boserupian Paradigms
Mathematical models of population growth do not operate in an intellectual vacuum; they reflect fundamental philosophical and economic debates regarding the relationship between human reproduction, technological innovation, and finite planetary resources.

#### The Malthusian Classical Trap
In 1798, the English political economist Thomas Robert Malthus published his celebrated Essay on the Principle of Population, formulating the first quantitative law of demographic growth:
1. Population, when unchecked, increases in a geometrical ratio (exponential progression: 1, 2, 4, 8, 16, 32...).
2. Subsistence and food production increases only in an arithmetical ratio (linear progression: 1, 2, 3, 4, 5, 6...).

Because exponential growth inevitably outstrips linear growth, Malthus reasoned that population size must inevitably collide with the agricultural carrying capacity of the land. When this collision occurs, natural equilibrium is restored through two mechanisms:
- **Preventive Checks**: Voluntary behavioral reductions in the birth rate, primarily achieved through moral restraint, delayed marriage (celibacy), and family limitation.
- **Positive Checks**: Involuntary increases in the death rate caused by severe malnutrition, famine, infectious epidemic waves, and resource-driven warfare.

In mathematical terms, Malthus envisioned human society as trapped in a perpetual homeostatic cycle where any temporary improvement in living standards merely stimulates population expansion, which in turn drives wages back down to the bare biological subsistence level—the classical Malthusian Trap.

#### The Boserupian Technological Counter-Theory
In 1965, the Danish agricultural economist Ester Boserup formulated a profound counter-thesis to Malthusian determinism in her seminal work The Conditions of Agricultural Growth. Whereas Malthus viewed agricultural supply as an exogenous, autonomous ceiling that constrains demographic growth from above, Boserup demonstrated that population pressure serves as the primary endogenous catalyst that stimulates agricultural technological innovation and agricultural intensification.

Boserup traced the historical evolution of farming systems through five successive stages of land use intensity: forest fallow (twenty-year fallow cycles), bush fallow (six to eight-year cycles), short fallow (one to two-year cycles), annual cropping, and multi-cropping (producing two or three harvests per year from the same irrigated plot). Under low population densities, primitive slash-and-burn farming yields the highest output per hour of human labor, so farmers have no economic incentive to adopt labor-intensive plowing or irrigation. However, as population growth increases demographic density, the resulting land scarcity forces agriculturalists to invent and adopt intensive techniques: stone terracing, animal-drawn steel plows, organic fertilization, complex canal irrigation, and high-yield crop varieties.

In mathematical modeling, Boserup's insight transforms the carrying capacity K from a fixed, immutable ceiling into a dynamic, endogenous state variable that expands in response to population pressure:

$$\frac{dK}{dt} = \gamma \cdot \frac{dP}{dt}$$

When human intellectual capital and technological innovation expand faster than population numbers (as occurred during the Industrial Revolution and the mid-twentieth-century Green Revolution developed by Norman Borlaug), output per person increases continuously alongside expanding populations, permanently breaking the Malthusian trap.
"""
u6 = u6.replace("## Fully worked question 1", u6_extra + "\n## Fully worked question 1")
(d / "unit-6.md").write_text(u6, encoding="utf-8")

# ==============================================================================
# BOOST UNIT 7: Lotka Renewal Dynamics and Fisher's Reproductive Value
# ==============================================================================
u7 = (d / "unit-7.md").read_text(encoding="utf-8")
u7_extra = """
### Ronald Fisher's Reproductive Value and Evolutionary Demography
A profound theoretical bridge connecting stable population theory with evolutionary biology and life history theory is the concept of **Reproductive Value**, formulated by the mathematical geneticist Ronald A. Fisher in 1930 in The Genetical Theory of Natural Selection.

While the life table survival function p(x) measures an individual's probability of surviving to age x, and age-specific fertility m(x) measures childbearing intensity at age x, Fisher posed a fundamental demographic question: **How much does an individual of exact age x contribute to the future ancestry and genetic lineage of the population?**

#### Mathematical Derivation of Fisher's Reproductive Value
Let a female population grow at constant intrinsic rate r with stable age distribution. Consider a cohort of females alive at exact age x. The expected future offspring that will be born to a female who has already attained age x, discounted back to age x at the continuous rate of population growth r, is defined as the **Reproductive Value** v(x):

$$v(x) = \frac{e^{r x}}{p(x)} \int_x^{\infty} e^{-r t} \, p(t) \, m(t) \, dt$$

where the ratio v(x) / v(0) is normalized so that the reproductive value of a newborn female infant at birth is unity: v(0) = 1.

#### Biological and Demographic Trajectory of Reproductive Value
When v(x) is plotted against age x, it exhibits a dramatic unimodal trajectory that differs fundamentally from both fertility and survival schedules:
1. **At Birth (x = 0)**: By definition, v(0) = 1. A newborn girl possesses reproductive value, but her value is discounted because she faces significant risks of dying during infancy and childhood before reaching childbearing age, and her eventual reproduction lies fifteen to thirty years in the future.
2. **During Childhood (Ages 1 to 14)**: As a girl successfully survives childhood mortality risks, her reproductive value rises continuously! By surviving the hazards of early life, she draws closer to the reproductive age span without having died, maximizing her expected future contribution.
3. **At Puberty and Menarche (Ages 18 to 22)**: Reproductive value reaches its absolute lifetime maximum v_max, often equaling 2.5 to 3.5 times the value at birth. A young woman at age 20 has survived all childhood mortality hurdles and has her entire reproductive career immediately ahead of her.
4. **Throughout Adulthood (Ages 25 to 49)**: As a woman gives birth to children, her remaining reproductive potential is depleted. With each passing birthday, fewer childbearing years remain, causing v(x) to decline monotonically.
5. **At Menopause (Age 50+)**: At age 50, childbearing terminates entirely (m(x) = 0 for x >= 50), and direct reproductive value drops to exactly zero: v(x) = 0 for all x >= 50.

#### The Grandmother Hypothesis and Kin Selection
Why do human females experience menopause and survive for decades with zero direct reproductive value, a trait virtually unique among mammalian species? Evolutionary demographers (such as Kristen Hawkes) formulate the **Grandmother Hypothesis**: post-reproductive older women maximize their inclusive fitness by providing energetic subsidies, food foraging, and child-care assistance to their adult daughters. By reducing the physical burden of nursing and childcare on their daughters, grandmothers enable their daughters to shorten inter-birth intervals and bear more grandchildren, ensuring that post-reproductive longevity possesses immense indirect reproductive value under natural selection.
"""
u7 = u7.replace("## Fully worked question 1", u7_extra + "\n## Fully worked question 1")
(d / "unit-7.md").write_text(u7, encoding="utf-8")

# ==============================================================================
# BOOST UNIT 8: Multi-Regional Demographic Modeling and Gravity Migration Laws
# ==============================================================================
u8 = (d / "unit-8.md").read_text(encoding="utf-8")
u8_extra = """
### Spatial Interaction Modeling: Ravenstein's Laws and the Demographic Gravity Model
While census survival ratio methods measure net intercensal migration flows after they occur, spatial demographers seek to understand and predict the physical volume of gross migratory movements between geographic regions using mathematical spatial interaction models.

#### Ravenstein's Foundational Laws of Migration (1885)
In two landmark papers presented to the Royal Statistical Society, the geographer E. G. Ravenstein formulated the first systematic empirical laws governing human spatial mobility:
1. **Migration and Distance**: The vast majority of migrants travel only short physical distances; the volume of migration declines monotonically with increasing physical distance (distance decay).
2. **Step Migration**: Population redistribution proceeds by a process of gradual absorption: inhabitants of rural hinterlands move first to nearby market towns, whose residents in turn move to larger provincial cities, which feed the major national metropolis.
3. **Counter-Streams (Migration Currents)**: Every major migration flow produces a compensatory counter-current in the opposite direction, as disappointed migrants return home or businesses decentralize.
4. **Urban-Rural Differentials**: Inhabitants of rural agricultural areas exhibit a substantially higher propensity to migrate than residents of large towns.
5. **Sex Selectivity**: Females are more mobile than males over short internal distances (frequently driven by exogamous marriage patterns), whereas males dominate long-distance international migration streams.
6. **Economic Primacy**: While political oppression, religious persecution, and environmental disasters stimulate migration, the overwhelming dominant driver of human movement is the economic desire to improve material living standards.

#### The Mathematical Gravity Model of Migration
Inspired by Isaac Newton's law of universal gravitation in classical physics, demographers and regional scientists (such as George K. Zipf in 1946) formalized spatial interaction into the **Demographic Gravity Model**.

Let i and j denote two distinct metropolitan regions or provinces. The gross migration flow M_ij from origin region i to destination region j is hypothesized to be directly proportional to the product of their population sizes, and inversely proportional to the physical or economic distance separating them:

$$M_{ij} = G \cdot \frac{P_i^{\alpha} \cdot P_j^{\beta}}{D_{ij}^{\gamma}}$$

where:
- P_i is the population of the origin region (measuring the pool of potential migrants).
- P_j is the population of the destination region (measuring the economic attractiveness and labor market capacity).
- D_ij is the spatial distance between the two regions (measured in road kilometers, travel time, or transit costs).
- G is an empirical scaling constant.
- alpha, beta, gamma are calibrated elasticity parameters (in standard Zipf gravity, alpha = beta = 1 and gamma = 1 or 2).

Taking the natural logarithm transforms the gravity model into a linear econometric equation:

$$\ln M_{ij} = \ln G + \alpha \ln P_i + \beta \ln P_j - \gamma \ln D_{ij} + \varepsilon_{ij}$$

Demographers estimate these elasticities via Poisson pseudo-maximum likelihood (PPML) regression. The parameter gamma represents the **distance friction coefficient**: in modern high-speed transportation networks and digital job search environments, gamma has declined from historical values of 2.0 down to 0.8 or 1.0, reflecting the diminishing barrier of physical distance.

### Andrei Rogers' Multi-Regional Mathematical Demography
In 1975, Andrei Rogers revolutionized spatial demographic forecasting by formulating **Multi-Regional Mathematical Demography**. Traditional single-region cohort-component projections treat migration as an exogenous net net residual, which frequently generates mathematical absurdities (such as projecting negative populations in out-migrating rural areas).

Rogers generalized the Leslie matrix into a comprehensive multi-regional matrix operator where individuals transition between age groups and geographic regions simultaneously. Let a nation be partitioned into m interconnected regions. The state vector contains population counts cross-classified by age and region:

$$\mathbf{p}(t+1) = \mathbf{M} \cdot \mathbf{p}(t)$$

where the multiregional projection matrix M contains blocks of age-specific inter-regional mobility probabilities. By enforcing internal consistency—such that out-migration from region i to region j exactly equals in-migration into region j from region i—Rogers' multiregional framework guarantees that national population totals are conserved, providing the theoretical foundation for contemporary state and provincial planning models.
"""
u8 = u8.replace("## Fully worked question 1", u8_extra + "\n## Fully worked question 1")
(d / "unit-8.md").write_text(u8, encoding="utf-8")

print("Finished boosting Units 4, 6, 7, 8!")
