# Unit 8: Migration Analysis, Intercensal Estimation & Cohort-Component Projections

Demographic change over time is governed by the continuous interaction of three fundamental demographic processes: fertility, mortality, and migration. While fertility and mortality represent universal biological events experienced once or repeatedly by all human beings, migration is a purely spatial, social, and economic phenomenon. Individuals can migrate multiple times throughout their lives, or never at all, and their movement can occur across diverse administrative, provincial, and national boundaries. In this final foundational unit of demography, we formalize the mathematics of the demographic balancing equation, census survival ratio techniques for estimating unobserved migration, and the celebrated **Cohort-Component Method** and **Leslie Matrix** projection pipelines.

## 8.1 The Demographic Balancing Equation and Migration Metrics

The fundamental accounting identity of demographic science is the **Demographic Balancing Equation**, which states that the change in population size over any calendar interval $[t_1, t_2]$ must equal the net sum of biological natural increase and net spatial migration.

### The Accounting Identity
Let $P(t_1)$ and $P(t_2)$ denote the enumerated population counts at the beginning and end of the interval, and let $\Delta t = t_2 - t_1$. The balancing equation is:

$$P(t_2) = P(t_1) + B[t_1, t_2] - D[t_1, t_2] + I[t_1, t_2] - O[t_1, t_2]$$

where:
- $B[t_1, t_2]$ is the total number of live births occurring within the territory during the interval.
- $D[t_1, t_2]$ is the total number of deaths occurring within the territory during the interval.
- $I[t_1, t_2]$ is the total number of in-migrants (or immigrants) entering the territory.
- $O[t_1, t_2]$ is the total number of out-migrants (or emigrants) leaving the territory.

Define:
- **Natural Increase ($NI$)**: $NI = B - D$
- **Net Migration ($NM$)**: $NM = I - O$
- **Gross Migration (Migration Turnover, $GM$)**: $GM = I + O$

Then the balancing equation simplifies to:

$$P(t_2) - P(t_1) = NI + NM = (B - D) + (I - O)$$

The residual method uses this identity to estimate unrecorded net migration between two censuses when civil registration records births and deaths:

$$\hat{NM} = [P(t_2) - P(t_1)] - (B - D)$$

### Summary Migration Rates
To express migratory movements relative to population exposure, demographers divide counts by total person-years lived, approximated by the mid-period population $P_{\text{mid}}$:
1. **Crude In-Migration Rate ($CMR_I$)**:
   $$CMR_I = \frac{I}{P_{\text{mid}}} \times 1{,}000$$
2. **Crude Out-Migration Rate ($CMR_O$)**:
   $$CMR_O = \frac{O}{P_{\text{mid}}} \times 1{,}000$$
3. **Net Migration Rate ($NMR$)**:
   $$NMR = \frac{I - O}{P_{\text{mid}}} \times 1{,}000 = CMR_I - CMR_O$$
4. **Gross Migration Rate ($GMR$)**:
   $$GMR = \frac{I + O}{P_{\text{mid}}} \times 1{,}000$$
5. **Migration Effectiveness Ratio ($MER$)**:
   $$MER = \frac{|I - O|}{I + O} \times 100$$
   The effectiveness ratio ranges from $0\%$ (where in-migration and out-migration exactly balance, yielding high turnover with zero net population redistribution) to $100\%$ (where movement is completely unidirectional).

## 8.2 Indirect Estimation of Migration: Census Survival Ratio (CSR) Methods

While vital registration frequently fails to track internal migration between provinces, national decennial censuses record the age distribution of regional populations at consecutive ten-year intervals. In 1952, the United Nations formalized the **Census Survival Ratio (CSR)** methodology to estimate age-specific net migration indirectly.

### The Forward Survival Ratio Method
Consider a regional population enumerated in two consecutive censuses separated by $n$ years (e.g., $n = 10$).
Let $P_1(x)$ denote the enumerated population aged $x$ to $x+k$ at the first census, and let $P_2(x+n)$ denote the enumerated population aged $x+n$ to $x+n+k$ in the second census (the same birth cohort ten years older!).

Let $S(x, x+n)$ denote the survival probability for this cohort over the $n$-year intercensal period.
In the absence of net migration, the expected number of survivors living in the region at the second census would be:

$$\hat{P}_2(x+n) = P_1(x) \cdot S(x, x+n)$$

The estimated **Net Migration** for this cohort is the difference between the observed second-census population and the expected survivors:

$$\hat{NM}_{x+n}^{\text{forward}} = P_2(x+n) - \hat{P}_2(x+n) = P_2(x+n) - P_1(x) \cdot S(x, x+n)$$

### The Reverse Survival Ratio Method
Alternatively, an analyst can project the second-census population backward in time to estimate the initial cohort size at the first census:

$$\hat{P}_1(x) = \frac{P_2(x+n)}{S(x, x+n)}$$

The reverse-survival estimate of net migration is:

$$\hat{NM}_{x}^{\text{reverse}} = \hat{P}_1(x) - P_1(x) = \frac{P_2(x+n)}{S(x, x+n)} - P_1(x) = \frac{P_2(x+n) - P_1(x) \cdot S(x, x+n)}{S(x, x+n)}$$

Notice the exact algebraic relationship:

$$\hat{NM}^{\text{reverse}} = \frac{\hat{NM}^{\text{forward}}}{S(x, x+n)}$$

Because $S < 1$, the reverse estimate is always numerically larger than the forward estimate. Forward survival measures migrants surviving at the second census date, while reverse survival includes migrants who entered the region and died before the second census.

### National Census Survival Ratios (NCSR)
When regional life tables are unavailable, demographers use the **National Census Survival Ratio** computed from the closed national population:

$$NCSR(x, x+n) = \frac{P_2^{\text{national}}(x+n)}{P_1^{\text{national}}(x)}$$

The national ratio has a decisive mathematical advantage: it automatically absorbs and neutralizes nationwide census undercount errors, provided the undercount rate is relatively uniform across regions.

## 8.3 The Cohort-Component Method of Population Projections

The **Cohort-Component Method**, formulated by P. K. Whelpton in 1928 and standardized by the United Nations, is the universal gold standard for professional demographic forecasting used by the UN Population Division, the US Census Bureau, and national planning commissions worldwide.

Unlike mathematical growth curves which treat the population as an undifferentiated aggregate, the cohort-component method models the demographic life course of every individual age-sex cohort separately, advancing cohorts through time in discrete projection steps (typically five-year intervals).

### The Four Computational Steps of the Projection Pipeline
Let the projection step be $h = 5$ years. The baseline population is structured by sex and five-year age intervals: $_5 M_x(t)$ and $_5 F_x(t)$.
1. **Surviving the Existing Cohorts (Mortality Step)**:
   Each cohort is advanced five years in age and multiplied by the five-year survival ratio from the projected life table:
   $$_5 M_{x+5}(t+5) = {_5 M_x(t)} \times {_5 S_x^M}$$
   $$_5 F_{x+5}(t+5) = {_5 F_x(t)} \times {_5 S_x^F}$$
   where $_5 S_x = \frac{_5 L_{x+5}}{_5 L_x}$ is the life table survival ratio between adjacent five-year age groups.
2. **Factoring Net Migration (Migration Step)**:
   Projected age-specific net migrants are added to each surviving cohort:
   $$_5 M_{x+5}^*(t+5) = {_5 M_{x+5}(t+5)} + {_5 NM_x^M} \times \left( 1 + \frac{_5 S_x^M}{2} \right)$$
3. **Forecasting Future Births (Fertility Step)**:
   The female population in childbearing age groups ($15-49$) over the five-year projection interval is approximated by the average of the initial and projected female populations:
   $$_5 \bar{F}_x = \frac{_5 F_x(t) + {_5 F_x^*(t+5)}}{2}$$
   The total number of births occurring during the five-year interval is:
   $$B[t, t+5] = 5 \times \sum_{x=15}^{45} \left( _5 \bar{F}_x \times {_5 f_x} \right)$$
   where $_5 f_x$ is the projected age-specific fertility rate.
4. **Surviving Newborn Births to Age 0–4 (New Cohort Step)**:
   Total births are divided into male and female births using the sex ratio at birth:
   $$B_M = B \times \left( \frac{SRB}{100 + SRB} \right) \quad \text{and} \quad B_F = B \times \left( \frac{100}{100 + SRB} \right)$$
   Newborn infants are survived to the end of the five-year projection step using the life table survival ratio from birth to age 0–4:
   $$_5 M_0(t+5) = B_M \times \left( \frac{_5 L_0^M}{5 \cdot l_0^M} \right)$$
   $$_5 F_0(t+5) = B_F \times \left( \frac{_5 L_0^F}{5 \cdot l_0^F} \right)$$

This completes one five-year cycle. The updated population distribution at $t+5$ becomes the input for the subsequent step, projecting forward recursively across multiple decades.

## 8.4 The Leslie Matrix: Linear Algebraic Population Dynamics

In 1945 and 1948, P. H. Leslie synthesized the discrete cohort-component projection into an elegant, powerful linear algebraic system: the **Leslie Matrix**.

### Matrix Formulation
Let $\mathbf{p}(t)$ denote the vector of female population counts in five-year age groups at time $t$:

$$\mathbf{p}(t) = \begin{pmatrix} P_0(t) \\ P_1(t) \\ P_2(t) \\ \vdots \\ P_{k-1}(t) \end{pmatrix}$$

The demographic projection over step $\Delta t = 5$ years is expressed as a matrix multiplication:

$$\mathbf{p}(t+1) = \mathbf{L} \, \mathbf{p}(t)$$

where $\mathbf{L}$ is the square **Leslie Matrix** of dimension $k \times k$:

$$\mathbf{L} = \begin{pmatrix} F_0 & F_1 & F_2 & \dots & F_{k-2} & F_{k-1} \\ S_0 & 0 & 0 & \dots & 0 & 0 \\ 0 & S_1 & 0 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & S_{k-2} & 0 \end{pmatrix}$$

### Structure of the Leslie Matrix
The Leslie matrix contains non-zero entries in only two locations:
1. **The First Row (Effective Fertility Coefficients $F_i$)**:
   $F_i$ represents the average number of surviving female daughters aged 0–4 alive at time $t+1$ born per female entering age group $i$ at time $t$:
   $$F_i = S_0^* \cdot \frac{f_i + f_{i+1} \cdot S_i}{2}$$
   where $S_0^* = \frac{_5 L_0}{5 \cdot l_0}$ is survival from birth to age 0–4.
2. **The Sub-Diagonal (Survival Probabilities $S_i$)**:
   $S_i = \frac{_5 L_{5(i+1)}}{_5 L_{5i}}$ is the transition probability that a female in age group $i$ survives to enter age group $i+1$ in the next five-year step.
3. All other matrix elements are strictly zero.

### Asymptotic Dynamics via Perron–Frobenius Theorem
Because the Leslie matrix $\mathbf{L}$ is a non-negative, irreducible, and primitive matrix (provided there are at least two consecutive fertile age groups), the celebrated **Perron–Frobenius Theorem** governs its long-term dynamics:
1. The matrix possesses a unique, real, strictly positive dominant eigenvalue $\lambda_1 > 0$ that is strictly greater in absolute value than all other eigenvalues ($|\lambda_j| < \lambda_1$ for all $j \ne 1$).
2. The dominant eigenvalue $\lambda_1$ represents the long-term discrete multiplication factor per five-year step. It is related to Lotka's continuous intrinsic rate of natural increase $r$ by:
   $$\lambda_1 = e^{5 r} \implies r = \frac{\ln \lambda_1}{5}$$
3. The right eigenvector $\mathbf{u}_1$ associated with $\lambda_1$ (satisfying $\mathbf{L} \mathbf{u}_1 = \lambda_1 \mathbf{u}_1$) defines the unique **asymptotic stable age distribution**. Regardless of initial population $\mathbf{p}(0)$:
   $$\lim_{t \to \infty} \frac{\mathbf{p}(t)}{\lambda_1^t} = c \, \mathbf{u}_1$$
4. The left eigenvector $\mathbf{v}_1$ (satisfying $\mathbf{v}_1^T \mathbf{L} = \lambda_1 \mathbf{v}_1^T$) defines the **Fisher Reproductive Value** vector across age groups.

This establishes an unbreakable mathematical bridge unifying discrete projection algorithms, linear algebra, and Lotka's continuous renewal theory.


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

$$M_{ij} = G \cdot rac{P_i^{lpha} \cdot P_j^{eta}}{D_{ij}^{\gamma}}$$

where:
- P_i is the population of the origin region (measuring the pool of potential migrants).
- P_j is the population of the destination region (measuring the economic attractiveness and labor market capacity).
- D_ij is the spatial distance between the two regions (measured in road kilometers, travel time, or transit costs).
- G is an empirical scaling constant.
- alpha, beta, gamma are calibrated elasticity parameters (in standard Zipf gravity, alpha = beta = 1 and gamma = 1 or 2).

Taking the natural logarithm transforms the gravity model into a linear econometric equation:

$$\ln M_{ij} = \ln G + lpha \ln P_i + eta \ln P_j - \gamma \ln D_{ij} + arepsilon_{ij}$$

Demographers estimate these elasticities via Poisson pseudo-maximum likelihood (PPML) regression. The parameter gamma represents the **distance friction coefficient**: in modern high-speed transportation networks and digital job search environments, gamma has declined from historical values of 2.0 down to 0.8 or 1.0, reflecting the diminishing barrier of physical distance.

### Andrei Rogers' Multi-Regional Mathematical Demography
In 1975, Andrei Rogers revolutionized spatial demographic forecasting by formulating **Multi-Regional Mathematical Demography**. Traditional single-region cohort-component projections treat migration as an exogenous net net residual, which frequently generates mathematical absurdities (such as projecting negative populations in out-migrating rural areas).

Rogers generalized the Leslie matrix into a comprehensive multi-regional matrix operator where individuals transition between age groups and geographic regions simultaneously. Let a nation be partitioned into m interconnected regions. The state vector contains population counts cross-classified by age and region:

$$\mathbf{p}(t+1) = \mathbf{M} \cdot \mathbf{p}(t)$$

where the multiregional projection matrix M contains blocks of age-specific inter-regional mobility probabilities. By enforcing internal consistency—such that out-migration from region i to region j exactly equals in-migration into region j from region i—Rogers' multiregional framework guarantees that national population totals are conserved, providing the theoretical foundation for contemporary state and provincial planning models.


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


### Multiregional Migration Matrix Inversion and Life Expectancy Allocation
In Andrei Rogers’ multiregional demographic accounts, life expectancy is generalized into spatial origin-destination allocations. When a child is born in Province A, how many total years of life will that individual spend living in Province A versus migrating and living in Province B, Province C, or overseas?

By integrating the multiregional transition probability matrix across all ages, Rogers derived the **Multiregional Expectation of Life Matrix**:

$$\mathbf{E} = egin{pmatrix} e_{AA} & e_{AB} \\ e_{BA} & e_{BB} \end{pmatrix}$$

where e_{AB} represents the expected person-years an individual born in Region A will spend residing in Region B over their lifetime.
In highly mobile federal nations (such as the United States, Australia, or Canada), e_{AB} frequently accounts for thirty to forty percent of total life expectancy at birth! These spatial person-year decompositions are used by national health ministries and transportation departments to allocate inter-provincial infrastructure transfers and regional healthcare subsidies fairly.

## Fully worked question 1: Census Survival Ratio Estimation of Intercensal Net Migration

### Question
A regional statistical office estimates intercensal net migration into an expanding industrial metropolis between two decennial censuses (2010 and 2020). The regional population in 2010 and 2020, along with the official National Census Survival Ratios ($NCSR$) computed from the closed national population, are summarized below for three successive cohorts:

| Cohort Identity | Age in 2010 ($x$) | 2010 Regional Pop ($P_1$) | Age in 2020 ($x+10$) | 2020 Regional Pop ($P_2$) | National Survival Ratio ($S_{10}$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Cohort A** | **10–19** | $120{,}000$ | **20–29** | $165{,}000$ | $0.9850$ |
| **Cohort B** | **20–29** | $140{,}000$ | **30–39** | $155{,}000$ | $0.9750$ |
| **Cohort C** | **30–39** | $110{,}000$ | **40–49** | $102{,}000$ | $0.9500$ |

1. Calculate the expected number of 2020 regional survivors ($\hat{P}_2$) for each cohort under the assumption of zero net migration using the forward survival method.
2. Compute the estimated intercensal Net Migration ($\hat{NM}$) for each cohort using the Forward Survival Ratio method.
3. Compute the Net Migration using the Reverse Survival Ratio method, explain the mathematical discrepancy between forward and reverse estimates, and compute the cohort-specific Net Migration Rate per $1{,}000$ person-years.

### Solution, step 1: Compute Expected Survivors (Forward Method)
The expected survivors living in the region at the 2020 census in the absence of net migration are given by:

$$\hat{P}_2(x+10) = P_1(x) \times S_{10}(x)$$

We compute $\hat{P}_2$ for each cohort:
1. **Cohort A (Ages 10–19 in 2010 $\to$ 20–29 in 2020)**:
   $$\hat{P}_2 = 120{,}000 \times 0.9850 = 118{,}200$$
2. **Cohort B (Ages 20–29 in 2010 $\to$ 30–39 in 2020)**:
   $$\hat{P}_2 = 140{,}000 \times 0.9750 = 136{,}500$$
3. **Cohort C (Ages 30–39 in 2010 $\to$ 40–49 in 2020)**:
   $$\hat{P}_2 = 110{,}000 \times 0.9500 = 104{,}500$$

### Solution, step 2: Calculate Net Migration (Forward Survival)
The forward estimate of net migration is:

$$\hat{NM}_{\text{forward}} = P_2(x+10) - \hat{P}_2(x+10)$$

1. **Cohort A**:
   $$\hat{NM}_{\text{forward}} = 165{,}000 - 118{,}200 = +46{,}800$$
   *(Cohort A gained a net influx of $46{,}800$ young adult migrants entering for university and employment).*
2. **Cohort B**:
   $$\hat{NM}_{\text{forward}} = 155{,}000 - 136{,}500 = +18{,}500$$
   *(Cohort B gained a net influx of $18{,}500$ migrants).*
3. **Cohort C**:
   $$\hat{NM}_{\text{forward}} = 102{,}000 - 104{,}500 = -2{,}500$$
   *(Cohort C experienced a net out-migration of $2{,}500$ residents moving to suburban regions).*

**Total Net Intercensal Migration across the Three Cohorts (Forward)**:

$$\hat{NM}_{\text{total}}^{\text{forward}} = 46{,}800 + 18{,}500 - 2{,}500 = +62{,}800$$

### Solution, step 3: Reverse Survival Estimates and Analytical Comparison
The reverse survival formula is:

$$\hat{NM}_{\text{reverse}} = \frac{P_2(x+10)}{S_{10}} - P_1(x) = \frac{\hat{NM}_{\text{forward}}}{S_{10}}$$

We evaluate the reverse estimates:
1. **Cohort A**:
   $$\hat{NM}_{\text{reverse}} = \frac{46{,}800}{0.9850} \approx 47{,}512.69 \implies +47{,}513$$
2. **Cohort B**:
   $$\hat{NM}_{\text{reverse}} = \frac{18{,}500}{0.9750} \approx 18{,}974.36 \implies +18{,}974$$
3. **Cohort C**:
   $$\hat{NM}_{\text{reverse}} = \frac{-2{,}500}{0.9500} \approx -2{,}631.58 \implies -2{,}632$$

**Total Reverse Net Migration**:
$$\hat{NM}_{\text{total}}^{\text{reverse}} = 47{,}513 + 18{,}974 - 2{,}632 = +63{,}855$$

**Mathematical Rationale for Discrepancy**:
- $\hat{NM}_{\text{forward}} = +62{,}800$ counts the net migrants who survived to the 2020 census enumeration date.
- $\hat{NM}_{\text{reverse}} = +63{,}855$ includes the estimated $1{,}055$ net migrants ($63{,}855 - 62{,}800 = 1{,}055$) who migrated into the metropolis during the decade but died prior to the 2020 census.

Now compute the annual Net Migration Rate for Cohort A:
The mid-period population exposure for Cohort A is:
$$P_{\text{mid}} = \frac{P_1 + P_2}{2} = \frac{120{,}000 + 165{,}000}{2} = 142{,}500$$
Total person-years over the decade:
$$PY = 10 \times 142{,}500 = 1{,}425{,}000 \text{ person-years}$$
Annual Net Migration Rate:
$$NMR = \frac{46{,}800}{1{,}425{,}000} \times 1{,}000 \approx 32.84 \text{ net in-migrants per 1,000 person-years}$$

Cohort A experienced an extraordinary migration influx rate of nearly $33$ net in-migrants per thousand annually.


### Everett Lee's Analytical Theory of Migration and Intervening Obstacles
In 1966, the American sociologist and demographer Everett S. Lee formalized Ravenstein's historical observations into the definitive conceptual framework of migration: **A Theory of Migration**.

Lee conceptualized every migration decision as the net outcome of four interacting factors:
1. **Factors Associated with the Area of Origin (Push Factors)**: Negative attributes at the current place of residence that stimulate out-migration, including high unemployment, depressed wages, agricultural drought, soil exhaustion, social stigma, housing shortages, and lack of educational opportunities for children.
2. **Factors Associated with the Area of Destination (Pull Factors)**: Positive attributes at the prospective receiving locality that attract in-migrants, such as abundant employment vacancies, higher wage premia, superior healthcare facilities, universities, cultural diversity, and political freedoms.
3. **Intervening Obstacles**: Physical, economic, and legal friction barriers that separate origin and destination, including physical travel distance, financial transit costs, immigration visa quotas, language barriers, occupational credentialing restrictions, and discrimination against newcomer groups.
4. **Personal Factors**: Individual characteristics that modulate how push and pull factors are perceived, including age, marital status, risk aversion, personality traits, and psychological attachment to home communities.

#### Mathematical Formulation of Intervening Opportunities (Stouffer)
In 1940, Samuel A. Stouffer formulated a mathematical law that refined the classical gravity model by replacing physical distance with social interaction barriers: **The Theory of Intervening Opportunities**.

Stouffer asserted that the number of migrants moving from origin city i to destination city j is not inversely proportional to the physical distance between them, but directly proportional to the number of economic opportunities (e.g., job vacancies, housing units) available at city j, and inversely proportional to the number of **intervening opportunities** encountered along the route between city i and city j:

$$M_{ij} = k \cdot rac{\Delta Y_j}{X_{ij}}$$

where:
- Delta Y_j is the volume of available opportunities at destination j.
- X_ij is the cumulative volume of intervening opportunities located between origin i and destination j.
- k is a proportionality constant.

Stouffer's formulation explains why two cities separated by identical road distances can record vastly different migration flows: if vibrant intermediate towns lie between them, potential migrants are absorbed by the intervening opportunities, sharply dampening long-distance transit.

## Fully worked question 2: Step-by-Step Cohort-Component Five-Year Projection Execution

### Question
A provincial planning ministry executes a five-year population projection from baseline Year $t$ to Year $t+5$. The baseline population, five-year survival ratios ($S_x$), and age-specific fertility rates ($ASFR_x$) are recorded in the canonical three-age-group model:
- Age 0–14 (Youth, Cohort 0): $P_0(t) = 600{,}000$ (300,000 M, 300,000 F)
- Age 15–44 (Reproductive Adults, Cohort 1): $P_1(t) = 1{,}000{,}000$ (500,000 M, 500,000 F)
- Age 45+ (Older Adults, Cohort 2): $P_2(t) = 400{,}000$ (180,000 M, 220,000 F)

The demographic parameters over the projection step are:
- Survival ratio of Cohort 0 to Cohort 1: $S_0 = 0.980$
- Survival ratio of Cohort 1 to Cohort 2: $S_1 = 0.950$
- Survival ratio of Cohort 2 (remaining in 45+): $S_2 = 0.700$
- Survival ratio of newborns to age 0–14: $S_b = 0.960$
- Mean annual fertility rate among Cohort 1 females: $f_1 = 0.060$ births per woman per year
- Sex ratio at birth: $SRB = 105$ males per 100 females
- Net migration is zero.

1. Project the survivors of the existing baseline cohorts to Year $t+5$.
2. Calculate the total live births produced over the five-year projection interval.
3. Survive the newborn births to determine Cohort 0 at $t+5$, and compile the complete projected population distribution at Year $t+5$.

### Solution, step 1: Survive Existing Baseline Cohorts
In this aggregated projection model, the cohorts advance as follows:
1. **Surviving to Cohort 1 (Adults 15–44 at $t+5$)**:
   Cohort 0 advances into Cohort 1:
   $$M_1(t+5) = M_0(t) \times S_0 = 300{,}000 \times 0.980 = 294{,}000$$
   $$F_1(t+5) = F_0(t) \times S_0 = 300{,}000 \times 0.980 = 294{,}000$$
   $$P_1(t+5) = 294{,}000 + 294{,}000 = 588{,}000$$

2. **Surviving to Cohort 2 (Older Adults 45+ at $t+5$)**:
   Cohort 2 receives the survivors of Cohort 1, plus the surviving remainder of baseline Cohort 2:
   - Male survivors from Cohort 1: $500{,}000 \times 0.950 = 475{,}000$
   - Male survivors from Cohort 2: $180{,}000 \times 0.700 = 126{,}000$
   $$M_2(t+5) = 475{,}000 + 126{,}000 = 601{,}000$$
   - Female survivors from Cohort 1: $500{,}000 \times 0.950 = 475{,}000$
   - Female survivors from Cohort 2: $220{,}000 \times 0.700 = 154{,}000$
   $$F_2(t+5) = 475{,}000 + 154{,}000 = 629{,}000$$
   $$P_2(t+5) = 601{,}000 + 629{,}000 = 1{,}230{,}000$$

### Solution, step 2: Calculate Births over the Five-Year Interval
The childbearing population consists of Cohort 1 females.
The initial female population in Cohort 1 is $F_1(t) = 500{,}000$.
The projected female population in Cohort 1 is $F_1(t+5) = 294{,}000$.
The average person-years of exposure for reproductive women over the 5-year step is:

$$\bar{F}_1 = \frac{F_1(t) + F_1(t+5)}{2} = \frac{500{,}000 + 294{,}000}{2} = 397{,}000$$

With annual fertility $f_1 = 0.060$, the total births over the 5-year interval are:

$$B[t, t+5] = 5 \times \bar{F}_1 \times f_1 = 5 \times 397{,}000 \times 0.060 = 119{,}100 \text{ total births}$$

Now partition births by sex using $SRB = 105$:
- Proportion male: $p_m = \frac{105}{205} = 0.512195$
- Proportion female: $p_f = \frac{100}{205} = 0.487805$
$$B_M = 119{,}100 \times 0.512195 \approx 61{,}002$$
$$B_F = 119{,}100 \times 0.487805 \approx 58{,}098$$
Check sum: $61{,}002 + 58{,}098 = 119{,}100$.

### Solution, step 3: Survive Newborns and Compile the $t+5$ Population
The newborn infants are survived to Year $t+5$ using $S_b = 0.960$:
$$M_0(t+5) = B_M \times S_b = 61{,}002 \times 0.960 = 58{,}562$$
$$F_0(t+5) = B_F \times S_b = 58{,}098 \times 0.960 = 55{,}774$$
$$P_0(t+5) = 58{,}562 + 55{,}774 = 114{,}336$$

**Complete Projected Population Summary at Year $t+5$**:
- **Cohort 0 (Ages 0–14)**: $114{,}336$ (58,562 M, 55,774 F)
- **Cohort 1 (Ages 15–44)**: $588{,}000$ (294,000 M, 294,000 F)
- **Cohort 2 (Ages 45+)**: $1{,}230{,}000$ (601,000 M, 629,000 F)
- **Total Population at $t+5$**:
  $$P(t+5) = 114{,}336 + 588{,}000 + 1{,}230{,}000 = 1{,}932{,}336$$

Compare with baseline:
$$P(t) = 600{,}000 + 1{,}000{,}000 + 400{,}000 = 2{,}000{,}000$$
The population contracted from $2{,}000{,}000$ to $1{,}932{,}336$ ($-3.38\%$) while aging rapidly, as Cohort 2 expanded from $400k$ to $1.23M$.


### Multi-State Life Tables and the Mathematics of Health Transitions
While classical life tables treat death as the single absorbing exit state from life, human existence involves frequent, reversible transitions among multiple social, legal, and biological states throughout the life course. In 1973 and 1980, Robert Schoen, Frans Willekens, and Andrei Rogers formalized the mathematics of **Multi-State Life Tables** (increment-decrement life tables).

#### The Continuous Markov Multi-State System
Let an individual move among K distinct living states (e.g., Never-Married, Currently Married, Divorced, Widowed; or Active Labor Force, Unemployed, Retired; or Healthy, Chronically Ill, Severely Disabled) plus one absorbing death state.
Let mu_ij(x) denote the continuous instantaneous force of transition from state i to state j at age x.
The probability vector l(x) = (l_1(x), l_2(x), ..., l_K(x))^T represents the expected number of survivors residing in each respective state at exact age x.

The system of continuous differential equations governing the multi-state life table is:

$$rac{d \mathbf{l}(x)}{dx} = -oldsymbol{\mu}(x) \cdot \mathbf{l}(x)$$

where the transition rate matrix mu(x) contains the total force of exit on the diagonal and the negative transition forces -mu_ji(x) on the off-diagonals.
Solving this matrix differential equation across age intervals yields the multi-state transition probability matrix:

$$\mathbf{P}(x, x+n) = \exp\left( -\int_x^{x+n} oldsymbol{\mu}(t) \, dt 
ight)$$

Multi-state life tables allow demographers to compute profound actuarial metrics:
- The expected duration of a marriage from wedding to divorce or widowhood.
- The average number of working years remaining for an employed individual versus an unemployed jobseeker.
- The lifetime probability that a healthy 65-year-old will eventually require skilled nursing facility care before death.

#### Probabilistic Bayesian Population Projections (Adrian Raftery and the UN)
Until the early twenty-first century, international statistical agencies generated population projections using deterministic high, medium, and low scenarios. The medium variant assumed an arbitrary trajectory, while the high and low variants arbitrarily adjusted total fertility rates by plus or minus half a child (e.g., TFR +/- 0.5).

In 2012 and 2014, Adrian Raftery, Patrick Gerland, and the United Nations Population Division revolutionized demographic forecasting by establishing fully probabilistic Bayesian projections based on Markov Chain Monte Carlo (MCMC) simulations:
1. **Bayesian Hierarchical Fertility Models**: Projecting future TFR trajectories through double-logistic decline curves whose parameters are sampled from joint posterior distributions calibrated against all historical global fertility declines.
2. **Bayesian Mortality Models**: Projecting future gains in life expectancy at birth e_0 using random walk models with non-linear drift.
3. **Probabilistic Intervals**: Instead of arbitrary scenarios, the UN now publishes probabilistic prediction intervals (80% and 95% uncertainty intervals) for future national populations. For example, the UN can state with 95% mathematical confidence that the world population in 2100 will fall between 9.4 and 12.2 billion people, providing rigorous quantitative risk assessments for climate change planning, water resource infrastructure, and global food security.

## Fully worked question 3: Leslie Matrix Eigenvalues, Asymptotic Growth, and Stable Age Vectors

### Question
A theoretical demographer constructs a two-age-group Leslie projection matrix $\mathbf{L}$ for a female population partitioned into Youth (Ages 0–19, Group 0) and Adults (Ages 20–39, Group 1). The projection time step is $h = 20$ years:

$$\mathbf{L} = \begin{pmatrix} F_0 & F_1 \\ S_0 & 0 \end{pmatrix} = \begin{pmatrix} 0.40 & 1.20 \\ 0.80 & 0.00 \end{pmatrix}$$

where $F_0 = 0.40$ and $F_1 = 1.20$ are effective fertility coefficients, and $S_0 = 0.80$ is the 20-year survival probability from Group 0 to Group 1.

1. Formulate the characteristic polynomial $\det(\mathbf{L} - \lambda \mathbf{I}) = 0$ and solve for the eigenvalues $\lambda_1$ and $\lambda_2$. Identify the dominant Perron–Frobenius eigenvalue.
2. Calculate the corresponding continuous intrinsic annual rate of natural increase $r$ associated with the dominant eigenvalue ($h = 20$ years).
3. Compute the right eigenvector $\mathbf{u}_1$ associated with $\lambda_1$ to determine the unique asymptotic stable percentage age distribution.

### Solution, step 1: Solve the Characteristic Equation
The matrix equation is:

$$\det(\mathbf{L} - \lambda \mathbf{I}) = \det \begin{pmatrix} 0.40 - \lambda & 1.20 \\ 0.80 & -\lambda \end{pmatrix} = 0$$

Evaluating the determinant:

$$(0.40 - \lambda)(-\lambda) - (1.20)(0.80) = 0$$

$$\lambda^2 - 0.40 \lambda - 0.96 = 0$$

Applying the quadratic formula:

$$\lambda = \frac{-(-0.40) \pm \sqrt{(-0.40)^2 - 4(1)(-0.96)}}{2(1)}$$

$$(-0.40)^2 = 0.16$$
$$-4 \times (-0.96) = +3.84$$
$$\text{Discriminant} = 0.16 + 3.84 = 4.00$$
$$\sqrt{4.00} = 2.00$$

Evaluating the two roots:
$$\lambda_1 = \frac{0.40 + 2.00}{2} = \frac{2.40}{2} = 1.20$$
$$\lambda_2 = \frac{0.40 - 2.00}{2} = \frac{-1.60}{2} = -0.80$$

**Eigenvalue Analysis**:
- The dominant Perron–Frobenius eigenvalue is **$\lambda_1 = 1.20$**.
- Because $\lambda_1 = 1.20 > 1.00$, the population expands by $20.0\%$ every 20-year projection cycle.
- Notice that $|\lambda_2| = 0.80 < \lambda_1 = 1.20$. Because the subdominant eigenvalue has modulus strictly less than 1, any transient demographic oscillations will decay to zero at rate $(0.80 / 1.20)^t = (2/3)^t \to 0$.

### Solution, step 2: Calculate Continuous Intrinsic Growth Rate
The elapsed time for one projection step is $h = 20$ years.
The relationship between discrete multiplication factor $\lambda_1$ and continuous rate $r$ is:

$$\lambda_1 = e^{20 r} \implies r = \frac{\ln \lambda_1}{20}$$

$$\ln(1.20) \approx 0.18232156$$

$$r = \frac{0.18232156}{20} = 0.009116 \implies 0.912\% \text{ per annum}$$

The asymptotic intrinsic rate of natural increase is $0.912\%$ per year.

### Solution, step 3: Calculate the Stable Age Distribution Eigenvector
The right eigenvector $\mathbf{u}_1 = \begin{pmatrix} u_{11} \\ u_{12} \end{pmatrix}$ satisfies:

$$\mathbf{L} \mathbf{u}_1 = \lambda_1 \mathbf{u}_1$$

$$\begin{pmatrix} 0.40 & 1.20 \\ 0.80 & 0.00 \end{pmatrix} \begin{pmatrix} u_{11} \\ u_{12} \end{pmatrix} = 1.20 \begin{pmatrix} u_{11} \\ u_{12} \end{pmatrix}$$

From the second row:

$$0.80 \, u_{11} = 1.20 \, u_{12}$$

$$u_{12} = \frac{0.80}{1.20} \, u_{11} = \frac{2}{3} \, u_{11}$$

Set $u_{11} = 1.00$. Then:

$$u_{12} = \frac{2}{3} \approx 0.6667$$

$$\mathbf{u}_1 = \begin{pmatrix} 1.000 \\ 0.6667 \end{pmatrix}$$

Total relative sum:
$$1.000 + 0.6667 = 1.6667 = \frac{5}{3}$$

Normalize to percentages:
- **Group 0 (Youth, 0–19)**:
  $$\frac{1.000}{1.6667} \times 100 = \frac{3}{5} \times 100 = 60.00\%$$
- **Group 1 (Adults, 20–39)**:
  $$\frac{0.6667}{1.6667} \times 100 = \frac{2}{5} \times 100 = 40.00\%$$

**Asymptotic Conclusion**:
Regardless of the initial demographic distribution, in the long run the population will converge stably to a state where exactly **$60\%$** of individuals are Youth (Ages 0–19) and **$40\%$** are Adults (Ages 20–39), expanding continuously at an intrinsic rate of $0.912\%$ per year.
