# Unit 1: Survey Design, Target Populations and Sampling Frames

## Foundations of Survey Design and the Finite Population Framework

Statistical inquiry in survey sampling addresses an explicit, physical collection of identifiable entities rather than a purely theoretical, infinitely repeatable mathematical game. In classical mathematical statistics, observations are frequently modeled as independent and identically distributed realizations of an underlying abstract random variable governed by an unknown continuous probability density function or discrete probability mass function. In survey sampling theory, this paradigm is fundamentally transformed: the target of inference is a fixed, concrete finite population of $N$ distinct elements, labeled conventionally by integers in the index set $U = \{1, 2, \dots, N\}$. Attached to each unit $i \in U$ is a fixed vector of real-valued characteristics $\mathbf{y}_i = (y_{i1}, y_{i2}, \dots, y_{ip})^\top$, which are deterministic, fixed constants at the time of inquiry. The uncertainty in probability sampling does not arise from intrinsic stochasticity in the physical measurements themselves, but is deliberately introduced by the statistician through a controlled, randomized sampling mechanism.

A rigorous survey design begins by establishing the primary objectives of the investigation, specifying the inferential targets, identifying the finite universe under study, and formalizing the operational protocols through which empirical evidence will be gathered. Without a disciplined design, the most sophisticated mathematical estimators and computational models become fragile, as no amount of algorithmic post-processing can completely rescue an empirical investigation that has systematically excluded significant portions of its target population or conflated distinct observational units. The survey design serves as the foundational architectural blueprint connecting theoretical research questions to actionable, reproducible empirical data.

Every sound survey investigation must navigate the tension between inferential ambition and operational reality. While researchers frequently pose scientific or policy questions concerning broad, abstract concepts—such as the socioeconomic welfare of households, the ecological health of forest parcels, or the epidemiological vulnerability of rural populations—data collection operations must inevitably engage with concrete, tangible physical units. This operational translation requires precise operational definitions: establishing exactly what constitutes a household, how boundaries of forest tracts are legally and geographically delineated, and which individuals meet temporal residence criteria to qualify as population members. The mathematical rigor of survey sampling theory rests entirely upon this foundation of unambiguous set definitions and traceable unit identities.

Historically, the development of survey design crystallized through the pioneering contributions of Jerzy Neyman, P. C. Mahalanobis, Morris Hansen, William Hurwitz, and William Cochran in the mid-twentieth century. Neyman’s landmark 1934 address to the Royal Statistical Society demonstrated that purposive selection—in which investigators deliberately select "representative" or "typical" units according to expert judgment—lacks objective validity and is susceptible to severe, unquantifiable systematic biases. In contrast, Neyman established that randomized selection with known, strictly positive inclusion probabilities allows the construction of estimators whose sampling distributions, variances, and confidence intervals are mathematically guaranteed under the randomization distribution alone, without requiring unprovable assumptions regarding the distribution of the characteristics in the population.

In modern statistical practice, survey designs are categorized across multiple operational dimensions: cross-sectional designs, which capture a snapshot of a population at a single fixed instant in time; longitudinal panel designs, which repeatedly measure a stable cohort over successive temporal waves to track dynamic transitions; and rolling cross-sections, which continuously refresh samples to monitor temporal trajectories while dampening seasonal volatility. Regardless of the temporal architecture, every design must formalize its target population, construct an operational sampling frame, define the selection mechanism, and specify the estimation strategies that will be deployed once sample data are gathered.

## Geospatial and Area Sampling Frames: Grid Geometries and Segment Protocols

When comprehensive physical or digital registers of individual persons, households, or economic establishments do not exist, statistical agencies construct **area sampling frames**. Area sampling replaces the intractable problem of enumerating mobile or unlisted elements with the tractable problem of partitioning a continuous geographic land surface into identifiable, non-overlapping geometric segments.

The construction of an area frame proceeds through a hierarchical geographical hierarchy. A national territory is initially subdivided into major administrative strata (such as provinces, divisions, or agro-ecological zones). Within each stratum, Primary Sampling Units (PSUs) are delineated using permanent, readily recognizable physical boundaries—such as rivers, highways, railway tracks, ridgelines, and established municipal cadastral lines. In contemporary survey infrastructure, high-resolution satellite remote sensing imagery and geographic information systems (GIS) are combined with census population density grids to construct standardized Primary Stage Units with approximately balanced population sizes or land areas.

Once PSUs are selected into the sample via probability sampling, field mapping teams execute the **segmentation and listing protocol**:
1. **Segment Partitioning**: If a selected PSU contains several hundred households, surveying the entire unit is financially prohibitive. The PSU is further partitioned into smaller, well-defined geographic segments (often containing between 50 and 150 households each), and one or more segments are selected with known probability.
2. **Field Listing Operations**: Trained enumerators physically traverse the boundaries of each selected segment, creating a comprehensive, up-to-date catalog of every residential dwelling, commercial structure, and household cluster. This physical canvassing creates a localized, pristine list frame constructed specifically for the current inquiry.
3. **Boundary Ambiguity and Edge Allocation**: A persistent challenge in area frame execution is the **boundary problem**—determining how to classify households or economic activities that intersect segment borders. Survey methodologists employ three formal operational rules to resolve edge ambiguities:
   - **Open Segment Rule**: An observation is associated with the segment in which the main residential structure or principal dwelling unit is physically located, regardless of where the economic activity (such as farming or retail trading) takes place.
   - **Closed Segment Rule**: Only activities occurring strictly within the geographic confines of the segment boundaries are recorded, regardless of where the operators or owners reside. In agricultural surveys, field interviewers measure the exact crop acreage located inside the segment polygon, even if the farmer lives in an adjacent village.
   - **Weighted Segment Rule**: An agricultural or economic operation that spans multiple segment boundaries is recorded if any part of it touches the sampled segment, but its measured attributes are scaled by an allocation weight $w_i = A_{i,seg} / A_{i,total}$, where $A_{i,seg}$ is the parcel area within the segment and $A_{i,total}$ is the total farm area. This weighting ensures exact design unbiasedness across the continuous geographic domain.

Area sampling provides unmatched coverage robustness because every land parcel belongs to exactly one Primary Sampling Unit, driving the theoretical coverage rate $W_1$ close to $1.0$. However, this coverage completeness comes at substantial operational cost: physical field listing requires extensive logistics, mapping supervision, and strict adherence to geometric protocols to prevent enumerators from cutting corners or omitting hard-to-reach homesteads.

## Administrative Data Registers and Record Linkage: Deterministic and Probabilistic Frames

The digital transformation of national statistical systems has accelerated the integration of administrative registers into survey sampling infrastructure. Governments maintain continuous, high-volume transactional databases: civil birth and death registries, personal tax records, social security rosters, national health insurance accounts, and utility subscriber databases. When these disparate registries can be harnessed, they offer the prospect of near-universal population frames updated with high temporal frequency at a fraction of the cost of physical census operations.

However, transforming administrative registries into scientifically valid sampling frames requires rigorous **record linkage and identity resolution**. Because distinct administrative bodies maintain separate records for their own regulatory mandates, merging datasets invariably encounters missing, inconsistent, or conflicting personal identifiers. Survey statisticians formalize this linkage process using two distinct mathematical frameworks:

### Deterministic Record Linkage
In a deterministic linkage system, records from two independent administrative lists $\mathcal{A}$ and $\mathcal{B}$ are joined if and only if they match exactly on a unique, error-free identifier (such as a 17-digit National Identity Number or a universal corporate tax registration code). When such unique keys exist and are consistently recorded, deterministic linkage is instantaneous and transparent.

In practice, however, unique keys are frequently corrupted by keystroke errors, optical character recognition glitches, missing digits, or fraudulent duplicate filings. When unique identifiers are missing or unreliable, deterministic linkage relies on strict rule-based logic requiring agreement across a vector of quasi-identifiers: full legal name, date of birth, mother's maiden name, and residential postal code. Strict deterministic rules inevitably produce high rates of **false non-links (missed matches)**, artificially introducing severe undercoverage into the linked frame.

### Probabilistic Record Linkage and the Fellegi–Sunter Theory
To overcome the brittleness of deterministic rules, Ivan Fellegi and Alan Sunter (1969) formulated the foundational mathematical theory of probabilistic record linkage. Let $\mathcal{A}$ and $\mathcal{B}$ denote two administrative files of sizes $N_A$ and $N_B$. The Cartesian product space $\mathcal{A} \times \mathcal{B} = \{(a, b) : a \in \mathcal{A}, b \in \mathcal{B}\}$ contains all possible pairs of records. This product space is naturally partitioned into two unobserved states of nature:
- The set of true matches: $\mathcal{M} = \{(a, b) : a = b\}$
- The set of true non-matches: $\mathcal{U} = \{(a, b) : a \ne b\}$

For every candidate pair $(a, b)$, the statistician observes a comparison vector $\boldsymbol{\gamma} = (\gamma_1, \dots, \gamma_K)^\top$, where each component $\gamma_k$ records the level of agreement between specific attributes of record $a$ and record $b$ (e.g., phonetic string similarity of names, exact match on birth month, numeric difference in birth year).

Define the two conditional probabilities:
$$m(\boldsymbol{\gamma}) = P(\boldsymbol{\gamma} \mid (a, b) \in \mathcal{M})$$
$$u(\boldsymbol{\gamma}) = P(\boldsymbol{\gamma} \mid (a, b) \in \mathcal{U})$$
The quantity $m(\boldsymbol{\gamma})$ represents the probability of observing comparison pattern $\boldsymbol{\gamma}$ given that the records truly belong to the same entity (reflecting the reliability and error rates of the attributes). The quantity $u(\boldsymbol{\gamma})$ represents the probability of observing $\boldsymbol{\gamma}$ purely by chance among two completely unrelated entities.

The **Fellegi–Sunter Decision Rule** computes the likelihood ratio:
$$R(\boldsymbol{\gamma}) = \frac{m(\boldsymbol{\gamma})}{u(\boldsymbol{\gamma})}$$
and establishes two optimal threshold values $T_\mu$ and $T_\lambda$ ($T_\mu \ge T_\lambda$):
- **Decision 1 (Link / Match)**: If $R(\boldsymbol{\gamma}) \ge T_\mu$, designate the pair as a true match and merge the records.
- **Decision 2 (Possible Link / Clerical Review)**: If $T_\lambda \le R(\boldsymbol{\gamma}) < T_\mu$, classify the pair as ambiguous, routing it to manual verification.
- **Decision 3 (Non-Link / Distinct Entities)**: If $R(\boldsymbol{\gamma}) < T_\lambda$, designate the pair as distinct entities.

Fellegi and Sunter proved via the Neyman–Pearson lemma that this decision rule minimizes the clerical review zone for pre-specified upper bounds on the false match error rate $\mu$ ($P(\text{Link} \mid (a, b) \in \mathcal{U}) \le \mu$) and the false non-match error rate $\lambda$ ($P(\text{Non-Link} \mid (a, b) \in \mathcal{M}) \le \lambda$).

When an administrative sampling frame is synthesized via probabilistic linkage, the resulting frame retains residual matching errors. A false match creates an artificial duplicate record, introducing multiplicity distortion; a false non-match creates fragmented split records, artificially inflating frame size and distorting first-order inclusion probabilities. Methodologists must model these linkage error probabilities directly in downstream survey weighting equations, linking record linkage theory directly to the Horvitz–Thompson framework.

## Target Populations, Frame Populations and Hierarchical Units

A central source of confusion in empirical research is the failure to distinguish between the conceptual target population, the operational frame population, the selected sample, and the respondent population. These four collections of entities occupy distinct logical and physical spaces, and clear distinctions among them are essential for both mathematical formulation and error analysis.

The **target population** (denoted $\mathcal{U}_{target}$) is the complete collection of units for which inferential conclusions are conceptually desired. For example, in an agricultural survey, the target population might comprise all operational crop-producing agricultural holdings in Bangladesh during the 2026 planting season. In a national demographic survey, it might encompass all civilian, non-institutionalized permanent residents residing within national borders on October 1, 2026. The target population is defined strictly by the research questions and policy objectives, independent of the practical feasibility or cost of contacting individual elements.

The **frame population** (denoted $\mathcal{U}_{frame}$), in contrast, is the collection of units that are actually accessible and listed within the physical or digital infrastructure used to execute sample selection. The sampling frame is the tangible materialization of the population: it may take the form of an administrative register of registered businesses, an address list maintained by a national postal authority, a master sample of enumeration areas compiled during a decennial population census, or a satellite-derived geospatial polygon grid. Because physical registers are invariably subject to administrative lags, bureaucratic omissions, registration thresholds, and geographic constraints, the frame population rarely matches the target population perfectly.

The **selected sample** (denoted $s$) is the specific subset of units drawn from $\mathcal{U}_{frame}$ in accordance with a specified randomized probability sampling mechanism $p(s)$. Finally, the **respondent population** (denoted $s_r$) consists of those sampled units from which complete and usable measurements are actually obtained during fieldwork, reflecting the reality that some selected units cannot be located, refuse to participate, or provide invalid responses. The gap between $\mathcal{U}_{target}$ and $\mathcal{U}_{frame}$ gives rise to **coverage error**; the gap between $\mathcal{U}_{frame}$ and $s$ is governed by **sampling error**; and the gap between $s$ and $s_r$ produces **nonresponse error**.

In complex sampling environments, the definition of an individual unit must also account for hierarchical structures. Three distinct concepts of units must be formally separated:
1. **Sampling Units**: The discrete entities that are selected at various stages of the sampling mechanism. In a single-stage design, sampling units are identical to ultimate population elements. In a multistage design, however, sampling units form a nested hierarchy: Primary Sampling Units (PSUs, such as geographic administrative districts or census enumeration blocks) are selected at the first stage, Secondary Sampling Units (SSUs, such as residential buildings or agricultural villages) are selected at the second stage, and Ultimate Sampling Units (USUs, such as individual households or housing units) are drawn at the final stage.
2. **Reporting Units (or Informant Units)**: The entities that physically provide the data during the measurement process. In household surveys, a single designated adult respondent (such as the household head or primary caregiver) frequently acts as the reporting unit who supplies information regarding all residents within the household.
3. **Observational Units (or Units of Analysis)**: The entities to which the measured attributes belong and about which inferential statements are made. In an education survey, the sampling unit might be an accredited school, the reporting unit might be the school principal completing an administrative questionnaire, but the observational units might be individual enrolled students whose test scores and attendance records are analyzed. Conflating these three tiers of units leads to serious specification errors in weighting, design-effect calculation, and variance estimation.

## Anatomy of Sampling Frames and Frame Pathology

A sampling frame is the physical or operational gateway through which a finite population is observed. Ideal sampling frames exhibit a bijective, one-to-one correspondence with the target population: every target element corresponds to exactly one listed frame unit, and every listed frame unit corresponds to a valid target element. In empirical reality, however, frames inevitably suffer from systemic pathologies that distort inclusion probabilities and introduce systematic bias unless rigorously diagnosed and corrected.

The standard taxonomy of sampling frame defects encompasses four major structural pathologies:
1. **Undercoverage (Omission)**: Target population units that exist in $\mathcal{U}_{target}$ but are completely absent from $\mathcal{U}_{frame}$. In an internet-based survey, individuals lacking digital connectivity or computer literacy are omitted by design. In a business registry, informal microenterprises operating below legal registration thresholds are systematically excluded. Undercoverage is arguably the most insidious frame defect because omitted units have an effective inclusion probability of zero ($\pi_i = 0$), rendering it mathematically impossible to form unbiased design-based estimates for the complete target population without external auxiliary models.
2. **Overcoverage (Ineligible Units)**: Units listed on $\mathcal{U}_{frame}$ that do not belong to the target population $\mathcal{U}_{target}$. Examples include deceased individuals remaining on voter rolls, dissolved corporations remaining on corporate tax registries, or vacant residential structures in a survey of active households. When an ineligible unit is selected into a sample, it can typically be identified during fieldwork and screened out. However, overcoverage reduces the effective sample size, increases fieldwork costs, and inflates the sampling variance of final estimates.
3. **Duplicate Listings (Multiplicity)**: Target population units that appear multiple times on the sampling frame under different identifiers or addresses. For instance, an individual who owns multiple telephone lines or maintains residential addresses in two different cities has multiple opportunities to be sampled in random digit dialing or residential address frames. If an element appears $M_i > 1$ times on the frame and is sampled under standard simple random selection, its true inclusion probability is substantially higher than that of an element appearing only once. Failure to account for multiplicity leads to severe positive bias for characteristics associated with duplicate entries (such as higher wealth or multiple business holdings).
4. **Clustering of Elements (Complex Linkages)**: Situations where a single listed frame unit corresponds to multiple target elements, or conversely, where a single target element is fragmented across multiple frame entries. A prominent example is a list of residential addresses (the frame units), where each address may house multiple distinct families or unrelated individual residents (the target elements). If field interviewers sample an address and arbitrarily interview only one resident without adjusting for the household size, individuals living in large households are systematically underrepresented relative to individuals living alone.

To address frame deficiencies, statisticians employ **dual-frame and multiple-frame designs**. In a classic dual-frame survey, an incomplete but inexpensive list frame (denoted $\mathcal{A}$, such as a digital registry of registered commercial farms) is combined with an expensive but comprehensive area frame (denoted $\mathcal{B}$, such as a geographic grid of land segments covering the entire national territory). Every unit in the target population belongs to one of three mutually exclusive domains: domain $a$ (units accessible only through frame $\mathcal{A}$), domain $b$ (units accessible only through area frame $\mathcal{B}$), or domain $ab$ (units accessible through both frames $\mathcal{A}$ and $\mathcal{B}$).

Let $Y$ denote the finite population total of a target variable $y$. The total decomposes across the three disjoint domains as:
$$Y = Y_a + Y_b + Y_{ab}$$
where $Y_a = \sum_{i \in a} y_i$, $Y_b = \sum_{i \in b} y_i$, and $Y_{ab} = \sum_{i \in ab} y_i$. Independent probability samples are drawn from frame $\mathcal{A}$ and frame $\mathcal{B}$. The domain totals $Y_a$ and $Y_b$ are estimated uniquely from samples $s_A$ and $s_B$, respectively, while the overlap domain total $Y_{ab}$ can be estimated from both samples. A dual-frame composite estimator takes the form:
$$\hat{Y}_{DF} = \hat{Y}_a + \hat{Y}_b + \theta \hat{Y}_{ab}^{(A)} + (1 - \theta) \hat{Y}_{ab}^{(B)}$$
where $\hat{Y}_{ab}^{(A)}$ is the estimator of $Y_{ab}$ computed from the frame $\mathcal{A}$ sample, $\hat{Y}_{ab}^{(B)}$ is the estimator of $Y_{ab}$ computed from the frame $\mathcal{B}$ sample, and $\theta \in [0, 1]$ is a composite blending weight chosen to minimize the sampling variance of $\hat{Y}_{DF}$. Dual-frame theory illustrates the profound interplay between frame structure, mathematical weighting, and optimal estimation.

## Survey Estimands: Finite Descriptive Parameters versus Superpopulation Targets

In any scientific survey, one must define with absolute mathematical precision what quantity is being estimated. In the survey sampling literature, these targets of inference are designated as **survey estimands**. A critical distinction exists between **finite population descriptive estimands** and **superpopulation analytic estimands**.

A **finite population estimand** is a deterministic mathematical summary of the fixed characteristics $\mathbf{y}_1, \dots, \mathbf{y}_N$ of the $N$ units belonging to the finite population $U$. The fundamental descriptive estimands include:
1. **The Finite Population Total**:
   $$Y = \sum_{i=1}^N y_i$$
   representing the aggregate quantity of interest (e.g., total national wheat production in metric tons, aggregate household consumer expenditure, or total number of unemployed individuals).
2. **The Finite Population Mean**:
   $$\bar{Y} = \frac{1}{N} \sum_{i=1}^N y_i = \frac{Y}{N}$$
   representing the average per-capita or per-unit level of the attribute.
3. **The Finite Population Proportion**:
   $$P = \frac{1}{N} \sum_{i=1}^N I(y_i \in A)$$
   where $I(\cdot)$ is the indicator function taking the value 1 if unit $i$ possesses attribute $A$ and 0 otherwise. The proportion is formally a special case of the population mean for a binary indicator variable $y_i \in \{0, 1\}$.
4. **The Finite Population Ratio**:
   $$R = \frac{Y}{X} = \frac{\sum_{i=1}^N y_i}{\sum_{i=1}^N x_i} = \frac{\bar{Y}}{\bar{X}}$$
   where $x_i$ is an auxiliary or denominator characteristic (e.g., ratio of total expenditure $Y$ to total disposable income $X$, or yield per hectare where $y_i$ is crop output and $x_i$ is cultivated land area). Note that a ratio of totals $Y/X$ is generally distinct from the population mean of individual ratios $\frac{1}{N}\sum_{i=1}^N (y_i / x_i)$.
5. **The Finite Population Variance and Covariance**:
   $$S_y^2 = \frac{1}{N - 1} \sum_{i=1}^N (y_i - \bar{Y})^2$$
   $$S_{yx} = \frac{1}{N - 1} \sum_{i=1}^N (y_i - \bar{Y})(x_i - \bar{X})$$
   defined with divisor $N-1$ following classical convention to ensure exact algebraic consistency in unbiased sample variance estimation.

In contrast, **superpopulation (or analytic) estimands** arise when the finite population $U = \{1, \dots, N\}$ is itself conceptualized as a random sample of size $N$ generated by an underlying infinite stochastic process or model $\xi$. Under this model-assisted or model-based perspective, the observed attributes $\mathbf{y}_i$ are realizations of random variables $Y_i \sim F(\cdot; \boldsymbol{\beta}, \sigma^2)$. The inferential targets are not the idiosyncratic finite sums $\sum_{i=1}^N y_i$, but the structural parameters of the generative mechanism, such as regression coefficients $\boldsymbol{\beta}$ in a linear model:
$$Y_i = \mathbf{x}_i^\top \boldsymbol{\beta} + \varepsilon_i, \quad E_\xi[\varepsilon_i] = 0, \quad V_\xi(\varepsilon_i) = \sigma^2 v_i$$
When conducting analytic inference from sample survey data, the sampling design cannot be ignored. If sample selection probabilities depend on auxiliary covariates $\mathbf{x}_i$ or directly on the response $y_i$, standard unweighted ordinary least squares regression yields asymptotically biased and inconsistent estimates of the superpopulation parameter $\boldsymbol{\beta}$. Incorporating survey design weights ensures that the sample estimating equations consistently estimate the census estimating equations, which in turn consistently estimate the underlying superpopulation parameters.

## Probability Sampling Foundations versus Non-Probability Mechanisms

The philosophical and mathematical demarcation between probability sampling and non-probability selection forms the core foundation of modern survey theory. 

A sampling mechanism is formally defined as a **probability sampling design** if and only if it satisfies three rigorous mathematical conditions:
1. **Known Sample Space**: The set $\mathcal{S}$ of all possible samples $s \subseteq U$ that can be generated by the sampling protocol is completely specified in advance.
2. **Specified Probability Distribution**: Every potential sample $s \in \mathcal{S}$ is assigned a well-defined probability of selection $p(s) \ge 0$, such that:
   $$\sum_{s \in \mathcal{S}} p(s) = 1$$
3. **Strictly Positive Inclusion Probabilities**: Every individual unit $i$ in the finite population $U$ possesses a strictly positive, known (or calculable) **first-order inclusion probability**, denoted $\pi_i$:
   $$\pi_i = P(i \in s) = \sum_{s \ni i} p(s) > 0 \quad \forall i \in U$$
Furthermore, for valid design-based variance estimation, every distinct pair of units $(i, j)$ with $i \ne j$ must possess a strictly positive **second-order (or joint) inclusion probability**, denoted $\pi_{ij}$:
$$\pi_{ij} = P(i \in s \text{ and } j \in s) = \sum_{s \ni \{i, j\}} p(s) > 0 \quad \forall i \ne j \in U$$

When these conditions are met, the **Horvitz–Thompson estimator** of the population total $Y$:
$$\hat{Y}_{HT} = \sum_{i \in s} \frac{y_i}{\pi_i} = \sum_{i \in s} d_i y_i$$
where $d_i = 1 / \pi_i$ is the design weight (or expansion factor), is mathematically guaranteed to be **design-unbiased** for $Y$:
$$E_p[\hat{Y}_{HT}] = Y$$
Here, the expectation $E_p[\cdot]$ is evaluated strictly over the discrete randomization distribution induced by $p(s)$ across all possible samples in $\mathcal{S}$. Unbiasedness holds regardless of the shape of the population distribution, the presence of severe skewness, or the existence of non-linear relationships among variables.

In stark contrast, **non-probability sampling mechanisms**—including convenience sampling, voluntary opt-in online panels, snowball sampling, quota sampling, and purposive expert selection—violate these mathematical axioms. Under non-probability selection:
- Inclusion probabilities $\pi_i$ are fundamentally unknown and frequently equal to zero for large segments of the population.
- The sample selection mechanism $p(s)$ cannot be described mathematically or controlled by the investigator.
- Design-based expectations and variances do not exist because there is no known probability space $(\mathcal{S}, p)$ over which to integrate.

Proponents of non-probability samples frequently attempt to justify their conclusions by invoking **superpopulation exchangeability models**, asserting that conditional on observed covariates $\mathbf{x}_i$, the sample selection indicator $I_i$ is conditionally independent of the survey outcome $y_i$ ($Y_i \perp I_i \mid \mathbf{x}_i$). However, this "missing at random" assumption is mathematically untestable using the sample data alone. If unobserved variables influence both the propensity to participate and the survey characteristic $y_i$, non-probability estimates suffer from severe, uncorrectable selection bias. 

This fundamental vulnerability was dramatically demonstrated by the infamous 1936 *Literary Digest* presidential poll, which gathered over 2.3 million voluntary mail-in responses but incorrectly predicted a landslide victory for Alf Landon over Franklin D. Roosevelt. The failure stemmed from massive coverage error (the sampling frame was constructed from automobile registrations and telephone directories, which systematically overrepresented affluent voters during the Great Depression) coupled with severe nonresponse self-selection bias. Simultaneously, George Gallup utilized a scientifically designed probability quota sample of only 50,000 individuals and correctly forecasted the election outcome. The mathematical certainty provided by known inclusion probabilities remains the gold standard for public statistics and scientific inquiry.

## Design-Based versus Model-Based Paradigms of Inference

The debate between design-based and model-based inference represents one of the deepest conceptual dialogues in the history of statistics. Understanding the philosophical architecture of both paradigms is essential for any survey statistician.

In the **Design-Based Paradigm** (also known as the randomization approach):
- The population values $y_1, y_2, \dots, y_N$ are considered fixed, deterministic, non-random constants.
- The only random variables in the analysis are the **sample inclusion indicators**:
  $$I_i = \begin{cases} 1 & \text{if unit } i \in s \\ 0 & \text{if unit } i \notin s \end{cases}$$
- The statistical properties of estimators (such as bias, variance, and mean squared error) are evaluated with respect to the distribution of the random vector $\mathbf{I} = (I_1, \dots, I_N)^\top$, which is entirely determined by the sampling design $p(s)$.
- Properties of estimators hold unconditionally without requiring any assumptions about how the $y_i$ values were generated in nature. A confidence interval constructed under the design-based framework possesses a guaranteed coverage probability under repeated sampling from the fixed population.

In the **Model-Based Paradigm** (also known as the prediction approach):
- The population vector $\mathbf{y} = (y_1, \dots, y_N)^\top$ is treated as a realization of a random vector $\mathbf{Y} = (Y_1, \dots, Y_N)^\top$ generated by a superpopulation probability model $\xi$.
- Once the sample $s$ is drawn, the sample values $\{y_i : i \in s\}$ are observed. The unobserved population values $\{y_k : k \in U \setminus s\}$ remain unknown random variables.
- Survey estimation is recast as a **statistical prediction problem**: estimating the total $Y = \sum_{i \in s} y_i + \sum_{k \notin s} Y_k$ requires predicting the unobserved sum $\sum_{k \notin s} Y_k$ using the observed data and the assumed model $\xi$.
- The properties of estimators are evaluated under the model distribution $\xi$. Under this framework, if the model is correct, estimators can achieve lower mean squared error than purely design-unbiased estimators. However, if the superpopulation model is misspecified, model-based estimators can be catastrophically biased, and claimed confidence interval coverage will fail completely.

The modern consensus among survey statisticians is represented by the **Model-Assisted Design-Based Paradigm**, pioneered by Carl-Erik Särndal, Bengt Swensson, and Jan Wretman (1992). In this synthesis:
- Working regression models $\xi$ are utilized to formulate sophisticated, highly efficient estimators (such as Generalized Regression Estimators and calibration estimators) that exploit auxiliary administrative covariates.
- Crucially, all properties of asymptotic unbiasedness, variance estimation, and confidence interval validity are evaluated strictly under the **design distribution $p(s)$**.
- If the superpopulation model is an accurate representation of reality, the model-assisted estimator achieves dramatic variance reductions. If the model is misspecified, the estimator remains asymptotically design-unbiased and consistent for the true finite population total, protecting the investigator against model failure. This harmonious marriage of model efficiency and design robustness forms the theoretical core of contemporary official statistics.

---

## Fully worked question 1: Quantifying Coverage Error and Net Undercoverage Bias

**Question.** A national statistical bureau conducts a household expenditure survey to estimate the total national monthly consumption expenditure on staple foods, denoted by $Y = \sum_{i \in U} y_i$, and the corresponding population mean per household, $\bar{Y} = Y / N$. The true target population $U$ contains $N = 2,500,000$ households. The sampling frame $\mathcal{U}_{frame}$ is constructed from a national digital utility database containing $N_{frame} = 2,125,000$ households. 

Field verification studies establish that:
1. A total of $N_{cov} = 2,000,000$ households belong to both the target population and the sampling frame (the covered subpopulation $U_1$).
2. A total of $N_{omit} = 500,000$ households belong to the target population but are completely missing from the frame (the omitted subpopulation $U_0$).
3. A total of $N_{inelig} = 125,000$ listings on the frame do not belong to the target population (ineligible/commercial listings).
4. The true mean expenditure in the covered subpopulation is $\bar{Y}_1 = 18,500$ BDT per month, with variance $S_1^2 = 16,000,000$.
5. The true mean expenditure in the omitted subpopulation (consisting largely of remote rural and informal urban settlements) is $\bar{Y}_0 = 11,000$ BDT per month, with variance $S_0^2 = 9,000,000$.

Suppose an unweighted simple random sample without replacement (SRSWOR) of size $n = 4,000$ is drawn from the frame, and all ineligible frame units are screened out upon contact without replacement. 
(a) Derive the algebraic expression for the true population mean $\bar{Y}$ in terms of the covered and omitted stratum means, and calculate its exact numerical value.
(b) Derive the mathematical expectation and the net coverage bias of the standard frame-based sample mean $\bar{y}_1$.
(c) Calculate the absolute bias, the relative bias percentage, and determine the mean squared error (MSE) of $\bar{y}_1$ as an estimator of the true target population mean $\bar{Y}$.

**Solution, step 1: Decompose the target population and calculate the true population mean.**
The target population $U$ of size $N = 2,500,000$ is partitioned into two mutually exclusive and exhaustive subpopulations: the covered subpopulation $U_1$ of size $N_1 = N_{cov} = 2,000,000$ and the omitted subpopulation $U_0$ of size $N_0 = N_{omit} = 500,000$. Notice that $N = N_1 + N_0 = 2,000,000 + 500,000 = 2,500,000$.

Let $W_1 = N_1 / N$ denote the coverage rate of the frame, and $W_0 = N_0 / N$ denote the undercoverage rate:
$$W_1 = \frac{2,000,000}{2,500,000} = 0.80$$
$$W_0 = \frac{500,000}{2,500,000} = 0.20$$

The aggregate population total is the sum of the subtotals across the covered and omitted sectors:
$$Y = Y_1 + Y_0 = N_1 \bar{Y}_1 + N_0 \bar{Y}_0$$
Substituting the provided parameters:
$$Y = (2,000,000)(18,500) + (500,000)(11,000) = 37,000,000,000 + 5,500,000,000 = 42,500,000,000 \text{ BDT}$$

The true target population mean $\bar{Y}$ is the weighted linear combination:
$$\bar{Y} = \frac{Y}{N} = W_1 \bar{Y}_1 + W_0 \bar{Y}_0 = (0.80)(18,500) + (0.20)(11,000) = 14,800 + 2,200 = 17,000 \text{ BDT}$$

**Solution, step 2: Derive the mathematical expectation and coverage bias of the frame estimator.**
The sampling frame contains $N_{frame} = 2,125,000$ listings, of which $N_1 = 2,000,000$ are valid target elements and $N_{inelig} = 125,000$ are ineligible units. When a simple random sample of size $n$ is drawn from $\mathcal{U}_{frame}$, the number of valid target elements $n_1$ appearing in the sample follows a hypergeometric distribution. Conditional on $n_1$, the $n_1$ units constitute an SRSWOR from the covered subpopulation $U_1$.

Because ineligible units are screened out and discarded, the sample mean computed from the retained eligible units is:
$$\bar{y}_1 = \frac{1}{n_1} \sum_{i \in s_1} y_i$$
Taking the conditional design expectation over all samples that yield $n_1 \ge 1$ eligible units:
$$E[\bar{y}_1 \mid n_1] = \bar{Y}_1$$
By the law of total expectation, because $P(n_1 \ge 1) \approx 1$ for $n = 4,000$:
$$E[\bar{y}_1] = E[E[\bar{y}_1 \mid n_1]] = \bar{Y}_1 = 18,500 \text{ BDT}$$

The estimator $\bar{y}_1$ is strictly design-unbiased for the covered population mean $\bar{Y}_1$, but it is deployed to estimate the target population mean $\bar{Y}$. The coverage bias is derived algebraically as:
$$\text{Bias}(\bar{y}_1) = E[\bar{y}_1] - \bar{Y} = \bar{Y}_1 - (W_1 \bar{Y}_1 + W_0 \bar{Y}_0) = \bar{Y}_1 (1 - W_1) - W_0 \bar{Y}_0$$
Since $1 - W_1 = W_0$, we obtain the fundamental coverage bias equation:
$$\text{Bias}(\bar{y}_1) = W_0 (\bar{Y}_1 - \bar{Y}_0)$$

Substituting the numerical values:
$$\text{Bias}(\bar{y}_1) = (0.20)(18,500 - 11,000) = (0.20)(7,500) = +1,500 \text{ BDT}$$
The frame-based estimator exhibits a severe positive bias of $+1,500$ BDT per household.

**Solution, step 3: Calculate relative bias, sampling variance and total Mean Squared Error.**
The relative bias is computed as:
$$\text{RelBias}(\bar{y}_1) = \frac{\text{Bias}(\bar{y}_1)}{\bar{Y}} \times 100\% = \frac{1,500}{17,000} \times 100\% \approx 8.8235\%$$

Next, we evaluate the sampling variance of $\bar{y}_1$. The expected number of eligible units in a sample of size $n = 4,000$ drawn from the frame of size $N_{frame} = 2,125,000$ with $N_1 = 2,000,000$ eligible listings is:
$$E[n_1] = n \times \frac{N_1}{N_{frame}} = 4,000 \times \frac{2,000,000}{2,125,000} = 4,000 \times \frac{16}{17} \approx 3,764.71$$
Approximating the variance of $\bar{y}_1$ using the expected sample size and the finite population correction factor $f_1 = E[n_1] / N_1 = 3,764.71 / 2,000,000 \approx 0.00188$:
$$V(\bar{y}_1) \approx \frac{1 - f_1}{E[n_1]} S_1^2 \approx \frac{1 - 0.00188}{3,764.71} (16,000,000) \approx \frac{0.99812}{3,764.71} \times 16,000,000 \approx 4,242.02 \text{ BDT}^2$$
The standard error of $\bar{y}_1$ is:
$$\text{SE}(\bar{y}_1) = \sqrt{V(\bar{y}_1)} = \sqrt{4,242.02} \approx 65.13 \text{ BDT}$$

The total Mean Squared Error decomposes into variance plus squared bias:
$$\text{MSE}(\bar{y}_1) = V(\bar{y}_1) + [\text{Bias}(\bar{y}_1)]^2 = 4,242.02 + (1,500)^2 = 4,242.02 + 2,250,000 = 2,254,242.02 \text{ BDT}^2$$
The root mean squared error is:
$$\text{RMSE}(\bar{y}_1) = \sqrt{2,254,242.02} \approx 1,501.41 \text{ BDT}$$

Notice that the squared bias ($2,250,000$) accounts for $99.81\%$ of the total MSE, whereas sampling variance ($4,242.02$) contributes less than $0.19\%$. Increasing the sample size $n$ would further reduce the sampling variance towards zero, but the MSE would remain bounded below by $1,500^2 = 2,250,000$. This proves mathematically that when coverage errors exist, large sample sizes provide no defense against severe inferential distortion.

---

## Fully worked question 2: Frame Deduplication, Multiplicity and Inclusion Weight Correction

**Question.** An enterprise survey utilizes an administrative digital registry frame $\mathcal{U}_{frame}$ to estimate the total revenue $Y = \sum_{i \in U} y_i$ across all distinct commercial retail enterprises operating within a metropolitan zone. The true target population $U$ contains $N = 10,000$ distinct enterprises. Due to municipal registration overlaps across multiple commercial activity categories, individual enterprises appear multiple times on the frame:
- $N_{(1)} = 7,000$ enterprises appear exactly once on the frame ($M_i = 1$).
- $N_{(2)} = 2,000$ enterprises appear exactly twice on the frame ($M_i = 2$).
- $N_{(3)} = 1,000$ enterprises appear exactly three times on the frame ($M_i = 3$).

The total number of listings on the frame is therefore:
$$M_{total} = (7,000 \times 1) + (2,000 \times 2) + (1,000 \times 3) = 7,000 + 4,000 + 3,000 = 14,000 \text{ frame listings}$$
Let the true mean revenues for these three groups be:
$$\bar{Y}_{(1)} = 500,000 \text{ BDT}, \quad \bar{Y}_{(2)} = 1,200,000 \text{ BDT}, \quad \bar{Y}_{(3)} = 2,500,000 \text{ BDT}$$
A sample of $m = 280$ listings is selected from the $14,000$ frame entries via simple random sampling with replacement (SRSWR). During the interview, field auditors determine the exact multiplicity $M_i \in \{1, 2, 3\}$ of each selected enterprise.

(a) Calculate the true target population total revenue $Y$ and the true population mean revenue $\bar{Y}$.
(b) Formulate the naive estimator $\hat{Y}_{naive} = \frac{M_{total}}{m} \sum_{k=1}^m y_k$ that fails to account for duplicate listings. Derive its mathematical expectation and calculate its exact bias.
(c) Formulate the Hansen–Hurwitz multiplicity-adjusted estimator $\hat{Y}_{mult}$, demonstrate its design unbiasedness, and calculate its expectation.

**Solution, step 1: Compute true population total and mean revenue.**
The true population total revenue $Y$ is the direct sum across the three multiplicity strata of distinct enterprises:
$$Y = \sum_{i=1}^N y_i = N_{(1)} \bar{Y}_{(1)} + N_{(2)} \bar{Y}_{(2)} + N_{(3)} \bar{Y}_{(3)}$$
Substituting the given values:
$$Y = (7,000)(500,000) + (2,000)(1,200,000) + (1,000)(2,500,000)$$
$$Y = 3,500,000,000 + 2,400,000,000 + 2,500,000,000 = 8,400,000,000 \text{ BDT}$$

The true population mean revenue across all $N = 10,000$ enterprises is:
$$\bar{Y} = \frac{Y}{N} = \frac{8,400,000,000}{10,000} = 840,000 \text{ BDT}$$

**Solution, step 2: Analyze the expectation and bias of the naive uncorrected estimator.**
Let $k \in \{1, 2, \dots, m\}$ index the $m = 280$ random draws from the frame $\mathcal{U}_{frame}$ of size $M_{total} = 14,000$. Under simple random sampling with replacement from the frame listings, each frame entry has an identical selection probability of $1 / M_{total}$ on any single draw.

Because enterprise $i$ appears $M_i$ times on the frame, the probability $p_i$ that enterprise $i$ is selected on any single draw is proportional to its multiplicity:
$$p_i = \frac{M_i}{M_{total}}$$
Let $y_{(k)}$ denote the revenue of the enterprise selected on draw $k$. The expectation of the outcome on a single draw is:
$$E[y_{(k)}] = \sum_{i=1}^N p_i y_i = \sum_{i=1}^N \frac{M_i}{M_{total}} y_i = \frac{1}{M_{total}} \sum_{i=1}^N M_i y_i$$
Evaluating the weighted sum $\sum_{i=1}^N M_i y_i$ across the three groups:
$$\sum_{i=1}^N M_i y_i = 1 \cdot (N_{(1)} \bar{Y}_{(1)}) + 2 \cdot (N_{(2)} \bar{Y}_{(2)}) + 3 \cdot (N_{(3)} \bar{Y}_{(3)})$$
$$= 1 \cdot (3,500,000,000) + 2 \cdot (2,400,000,000) + 3 \cdot (2,500,000,000)$$
$$= 3,500,000,000 + 4,800,000,000 + 7,500,000,000 = 15,800,000,000 \text{ BDT}$$

Thus, the single-draw expected value is:
$$E[y_{(k)}] = \frac{15,800,000,000}{14,000} \approx 1,128,571.43 \text{ BDT}$$

The naive estimator expands the sample mean of the selected frame entries by the frame size $M_{total}$:
$$\hat{Y}_{naive} = M_{total} \left( \frac{1}{m} \sum_{k=1}^m y_{(k)} \right)$$
Taking the expectation:
$$E[\hat{Y}_{naive}] = M_{total} \cdot E[y_{(k)}] = M_{total} \cdot \left( \frac{1}{M_{total}} \sum_{i=1}^N M_i y_i \right) = \sum_{i=1}^N M_i y_i = 15,800,000,000 \text{ BDT}$$

The bias of the naive estimator is:
$$\text{Bias}(\hat{Y}_{naive}) = E[\hat{Y}_{naive}] - Y = 15,800,000,000 - 8,400,000,000 = +7,400,000,000 \text{ BDT}$$
The relative bias of the naive estimator is staggering:
$$\text{RelBias}(\hat{Y}_{naive}) = \frac{7,400,000,000}{8,400,000,000} \times 100\% \approx +88.095\%$$
The massive positive bias occurs because larger, multi-registered enterprises have up to three times the probability of selection, and their revenues are erroneously multiplied by the inflated frame count $M_{total} = 14,000$ instead of the true enterprise count $N = 10,000$.

**Solution, step 3: Formulate and verify the multiplicity-adjusted Hansen–Hurwitz estimator.**
To eliminate multiplicity bias, each sampled observation must be weighted inversely by its multiplicity $M_i$. Define the multiplicity-adjusted variable for enterprise $i$ as:
$$y_i^* = \frac{y_i}{M_i}$$
When draw $k$ selects enterprise $i$, we record $y_{(k)}^* = y_{(k)} / M_{(k)}$.

The multiplicity-adjusted Hansen–Hurwitz estimator of the total $Y$ is defined as:
$$\hat{Y}_{mult} = \frac{M_{total}}{m} \sum_{k=1}^m \frac{y_{(k)}}{M_{(k)}} = \frac{M_{total}}{m} \sum_{k=1}^m y_{(k)}^*$$
We evaluate the expectation of a single draw of $y_{(k)}^*$:
$$E[y_{(k)}^*] = \sum_{i=1}^N p_i y_i^* = \sum_{i=1}^N \left( \frac{M_i}{M_{total}} \right) \left( \frac{y_i}{M_i} \right) = \frac{1}{M_{total}} \sum_{i=1}^N y_i = \frac{Y}{M_{total}}$$

Taking the expectation of $\hat{Y}_{mult}$:
$$E[\hat{Y}_{mult}] = \frac{M_{total}}{m} \sum_{k=1}^m E[y_{(k)}^*] = \frac{M_{total}}{m} \cdot m \cdot \left( \frac{Y}{M_{total}} \right) = Y$$
This proves that $\hat{Y}_{mult}$ is mathematically **design-unbiased** for the true total $Y$.

Numerically:
$$E[\hat{Y}_{mult}] = 8,400,000,000 \text{ BDT}$$
$$\text{Bias}(\hat{Y}_{mult}) = 0 \text{ BDT}$$
By weighting each sampled record by $1 / M_i$, the inflated selection probability $p_i = M_i / M_{total}$ is exactly neutralized by the divisor $M_i$, restoring perfect design unbiasedness without requiring expensive pre-survey deduplication of all 14,000 frame listings.

---

## Fully worked question 3: Specifying Finite Population Estimands versus Superpopulation Regression Parameters

**Question.** An environmental research institute investigates soil salinity ($Y$, measured in parts per thousand, ppt) as a function of distance from the coastline ($X$, measured in kilometers) in a coastal agricultural district. The target population consists of a finite population of $N = 500$ agricultural plots labeled $i = 1, 2, \dots, N$. 

The true finite population attributes satisfy:
$$\sum_{i=1}^{500} x_i = 5,000 \text{ km}, \quad \sum_{i=1}^{500} y_i = 1,750 \text{ ppt}$$
$$\sum_{i=1}^{500} x_i^2 = 65,000, \quad \sum_{i=1}^{500} y_i^2 = 8,125, \quad \sum_{i=1}^{500} x_i y_i = 14,500$$

A superpopulation model $\xi$ assumes that the finite population was generated by the linear relation:
$$Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad E_\xi[\varepsilon_i \mid x_i] = 0, \quad V_\xi(\varepsilon_i \mid x_i) = \sigma^2$$
where $\varepsilon_i$ are uncorrelated random errors.
(a) Calculate the finite population means $\bar{X}, \bar{Y}$, the finite population variances $S_x^2, S_y^2$, the covariance $S_{xy}$, and the Pearson correlation coefficient $R_{xy}$.
(b) Derive and calculate the finite population ordinary least squares regression slope $B_1$ and intercept $B_0$ that define the descriptive census regression line.
(c) Distinguish conceptually between the finite descriptive slope $B_1$ and the superpopulation model parameter $\beta_1$. Prove that the census estimator $B_1$ is model-unbiased for $\beta_1$ under $\xi$, and derive its model variance $V_\xi(B_1 \mid \mathbf{x})$.

**Solution, step 1: Calculate finite population moments and correlation.**
The finite population means are:
$$\bar{X} = \frac{\sum x_i}{N} = \frac{5,000}{500} = 10.0 \text{ km}$$
$$\bar{Y} = \frac{\sum y_i}{N} = \frac{1,750}{500} = 3.5 \text{ ppt}$$

Compute the sums of squares and cross-products around the mean:
$$\sum_{i=1}^{500} (x_i - \bar{X})^2 = \sum x_i^2 - N \bar{X}^2 = 65,000 - 500(10.0)^2 = 65,000 - 50,000 = 15,000$$
$$\sum_{i=1}^{500} (y_i - \bar{Y})^2 = \sum y_i^2 - N \bar{Y}^2 = 8,125 - 500(3.5)^2 = 8,125 - 6,125 = 2,000$$
$$\sum_{i=1}^{500} (x_i - \bar{X})(y_i - \bar{Y}) = \sum x_i y_i - N \bar{X}\bar{Y} = 14,500 - 500(10.0)(3.5) = 14,500 - 17,500 = -3,000$$

The finite population variances and covariance (with divisor $N - 1 = 499$) are:
$$S_x^2 = \frac{15,000}{499} \approx 30.0601 \text{ km}^2$$
$$S_y^2 = \frac{2,000}{499} \approx 4.0080 \text{ ppt}^2$$
$$S_{xy} = \frac{-3,000}{499} \approx -6.0120 \text{ km}\cdot\text{ppt}$$

The finite population correlation coefficient is:
$$R_{xy} = \frac{S_{xy}}{S_x S_y} = \frac{-3,000}{\sqrt{15,000 \times 2,000}} = \frac{-3,000}{\sqrt{30,000,000}} = \frac{-3,000}{5,477.2256} \approx -0.5477$$
The correlation indicates a moderate negative relationship: soil salinity decreases systematically with distance from the sea.

**Solution, step 2: Calculate the finite descriptive regression coefficients.**
The finite population regression slope $B_1$ is defined as the minimizer of the census sum of squared residuals $\sum_{i=1}^N (y_i - B_0 - B_1 x_i)^2$:
$$B_1 = \frac{\sum_{i=1}^N (x_i - \bar{X})(y_i - \bar{Y})}{\sum_{i=1}^N (x_i - \bar{X})^2} = \frac{S_{xy}}{S_x^2} = \frac{-3,000}{15,000} = -0.20 \text{ ppt per km}$$
The finite population intercept is:
$$B_0 = \bar{Y} - B_1 \bar{X} = 3.5 - (-0.20)(10.0) = 3.5 + 2.0 = 5.5 \text{ ppt}$$
The descriptive census regression line is:
$$\hat{y}_i = 5.5 - 0.20 x_i$$
This is a fixed, non-random descriptive property of the 500 plots in existence.

**Solution, step 3: Derive model-unbiasedness and model variance of $B_1$.**
Conceptually:
- $B_1 = -0.20$ is a **finite descriptive estimand**. It describes the exact mathematical slope connecting the 500 specific physical plots in this coastal district. It carries no error of estimation with respect to this finite universe.
- $\beta_1$ is a **superpopulation analytic parameter**. It describes the underlying geophysical law governing marine aerosol deposition and groundwater intrusion across all imaginable coastal land formations under model $\xi$.

Under model $\xi$, the population values $Y_i$ are random variables:
$$Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$$
We treat $B_1$ as an estimator of $\beta_1$ computed from the complete census:
$$B_1 = \frac{\sum_{i=1}^N (x_i - \bar{X}) Y_i}{\sum_{i=1}^N (x_i - \bar{X})^2} = \sum_{i=1}^N c_i Y_i$$
where $c_i = \frac{x_i - \bar{X}}{\sum_{j=1}^N (x_j - \bar{X})^2}$. Note that $\sum c_i = 0$ and $\sum c_i x_i = 1$.

Taking the model expectation $E_\xi[\cdot \mid \mathbf{x}]$:
$$E_\xi[B_1 \mid \mathbf{x}] = \sum_{i=1}^N c_i E_\xi[Y_i \mid x_i] = \sum_{i=1}^N c_i (\beta_0 + \beta_1 x_i) = \beta_0 \sum_{i=1}^N c_i + \beta_1 \sum_{i=1}^N c_i x_i = \beta_0(0) + \beta_1(1) = \beta_1$$
This proves that the finite population slope $B_1$ is **model-unbiased** for the superpopulation slope $\beta_1$.

The model variance of $B_1$ conditional on the fixed covariates $\mathbf{x}$ is:
$$V_\xi(B_1 \mid \mathbf{x}) = V_\xi\left( \sum_{i=1}^N c_i Y_i \;\middle|\; \mathbf{x} \right) = \sum_{i=1}^N c_i^2 V_\xi(Y_i \mid x_i) = \sigma^2 \sum_{i=1}^N c_i^2$$
Evaluating $\sum c_i^2$:
$$\sum_{i=1}^N c_i^2 = \sum_{i=1}^N \frac{(x_i - \bar{X})^2}{[\sum_{j=1}^N (x_j - \bar{X})^2]^2} = \frac{1}{\sum_{i=1}^N (x_i - \bar{X})^2} = \frac{1}{15,000}$$
Therefore:
$$V_\xi(B_1 \mid \mathbf{x}) = \frac{\sigma^2}{15,000}$$

Even if an investigator had access to the complete census of all 500 plots, the census slope $B_1$ would still have non-zero uncertainty ($V_\xi > 0$) as an estimator of the scientific law $\beta_1$. This illustrates the profound boundary between finite population descriptive inference and superpopulation model inference.

---

## Practical Synthesis, Quality Diagnostics and Computational Verification

The execution of a survey design requires continuous quality monitoring at every stage of the survey life cycle. The American Association for Public Opinion Research (AAPOR) and international statistical agencies have established standardized outcome rates to quantify frame and fieldwork performance.

Every unit selected from a sampling frame must be resolved into one of four mutually exclusive operational categories:
1. Complete or usable interviews ($I$).
2. Partial interviews ($P$).
3. Known eligible non-interviews, including refusals ($R$), non-contacts ($NC$), and other non-interviews ($O$).
4. Cases of unknown eligibility ($UH$ for unknown households, $UO$ for unknown other units).
5. Not eligible units screened out during field operations ($NE$).

The standard AAPOR Response Rate 1 (the minimum response rate) is formulated as:
$$\text{RR1} = \frac{I}{(I + P) + (R + NC + O) + (UH + UO)}$$
where cases of unknown eligibility are conservatively assumed to be eligible. The AAPOR Response Rate 3 accounts for estimated eligibility among unresolved cases:
$$\text{RR3} = \frac{I}{(I + P) + (R + NC + O) + e(UH + UO)}$$
where $e$ is an empirical estimate of the proportion of unknown-eligibility cases that are actually eligible, typically estimated from the observed eligibility rate among resolved cases:
$$e = \frac{I + P + R + NC + O}{(I + P + R + NC + O) + NE}$$

Beyond response rate metrics, survey practitioners conduct frame verification audits prior to sample execution. These diagnostics include:
- **Rate of Ineligibility**: Quantifying the proportion of frame entries that fail eligibility screening. An ineligibility rate exceeding 10% signals outdated administrative records and warrants frame cleaning.
- **Multiplicity Checking**: Recording the number of independent frame paths leading to each sampled element, enabling the post-survey application of Hansen–Hurwitz multiplicity weights as proven in Worked Question 2.
- **Coverage Ratio Comparison**: Benchmarking the estimated population total $\hat{N} = \sum_{i \in s} d_i$ against external demographic census totals $N_{census}$. A coverage ratio $\hat{N} / N_{census}$ significantly below 1.0 indicates severe net undercoverage, necessitating post-stratification or calibration weighting.

## The Total Survey Error (TSE) Paradigm and Design Optimization

Modern survey sampling operates within the comprehensive analytical framework known as **Total Survey Error (TSE)**. First articulated conceptually by Morris Hansen, William Hurwitz, and Max Bershad in 1961, and systematically formalized by Robert Groves in 1989, the TSE paradigm recognizes that sampling variance is only one component of the total inferential uncertainty that separates an empirical sample estimate $\hat{\theta}$ from the true target population parameter $\theta$.

The Total Survey Error decomposes along two primary methodological dimensions: errors of representation (determining who is measured) and errors of measurement (determining what is measured).

### Errors of Representation (The "Who" Dimension)
Errors of representation concern the correspondence between the target population and the final dataset of respondents:
1. **Coverage Error**: The gap between the target population $\mathcal{U}_{target}$ and the sampling frame $\mathcal{U}_{frame}$, manifested as undercoverage omissions, overcoverage ineligibles, and duplicate multiplicity. As derived in Worked Question 1, coverage error induces persistent systematic bias that does not vanish with increasing sample size:
   $$\text{Bias}_{cov}(\bar{y}_1) = W_0 (\bar{Y}_1 - \bar{Y}_0)$$
2. **Sampling Error**: The variability that arises because only a subset $s$ of the frame population is observed. Sampling error comprises both variable sampling error (quantified by sampling variance $V_p(\hat{\theta})$, which decays at rate $O(1/n)$) and design-induced sampling bias (which is identically zero under proper probability sampling estimators).
3. **Nonresponse Error**: The gap between the selected sample $s$ and the responding units $s_r$. Unit nonresponse bias arises when the propensity to participate is correlated with the substantive survey measurements, creating systematic distortion:
   $$\text{Bias}_{nr}(\bar{y}_r) \approx \frac{\text{Cov}(Y, R)}{\bar{R}}$$
4. **Adjustment Error**: Post-survey distortions introduced during weighting class adjustments, raking, calibration, or item imputation when auxiliary model assumptions fail to hold.

### Errors of Measurement (The "What" Dimension)
Errors of measurement concern the fidelity of the recorded data relative to the true underlying construct:
1. **Specification Error**: The divergence between the theoretical research concept and the concrete question operationalized in the survey instrument. For instance, inquiring about "household annual income" without clarifying whether capital gains, social transfers, or taxation are included introduces profound construct invalidity.
2. **Measurement Error (Response Error)**: The difference between the true latent value $y_i$ of unit $i$ and the value recorded during the interview $y_i^* = y_i + \mu_i + \varepsilon_i$. Response error stems from respondent cognitive burden, social desirability bias, recall fatigue, interviewer effects, questionnaire wording ambiguities, and mode-dependent recording quirks.
3. **Processing Error**: Anomalies introduced during data ingestion, including manual data entry typos, automated scanning misreads, erroneous coding of open-ended occupational classifications, and software truncation artifacts.

### The Mean Squared Error Criterion and Resource Allocation
The primary operational directive of survey design is to optimize the allocation of finite budgetary and logistical resources across these competing error components. The total error of an estimator $\hat{\theta}$ is evaluated through its **Total Mean Squared Error (TMSE)**:
$$\text{TMSE}(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = V_{samp}(\hat{\theta}) + V_{meas}(\hat{\theta}) + [\text{Bias}_{cov} + \text{Bias}_{samp} + \text{Bias}_{nr} + \text{Bias}_{meas}]^2$$

A common failure in naive survey planning is the over-allocation of resources toward minimizing sampling variance $V_{samp}$ by maximizing sample size $n$, while neglecting frame refinement, nonresponse reduction protocols, and questionnaire pretesting. If an agency expends its entire budget gathering a massive sample of $n = 50,000$ from a defective frame with a $20\%$ undercoverage rate and poor response rates, the sampling variance will be minuscule, but the squared systematic bias $[\text{Bias}_{cov} + \text{Bias}_{nr}]^2$ will dominate the error budget, producing highly precise yet wildly incorrect statistical estimates. 

Conversely, an optimized survey design allocates resources equilibrating error gradients: investing in robust dual-frame construction, multi-contact interviewer field protocols, rigorous translation and cognitive pretesting, and calibrated nonresponse follow-ups, accepting a modest sample size of $n = 2,500$ to achieve an exponentially lower Total Mean Squared Error.

By embedding these diagnostic metrics into the survey architecture, the statistician ensures that the survey design remains robust, transparent, and mathematically defensible. In the following unit, we examine the purest operationalization of this framework: Simple Random Sampling and the exact derivation of the finite population correction factor.
