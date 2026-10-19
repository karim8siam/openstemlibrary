# Unit 8: Statistical Demand, Supply & Econometric Elasticity Analysis

## Microeconomic Foundations of Demand and Supply Functions

The empirical estimation of market demand and supply relationships bridges abstract microeconomic theory and real-world commercial and macroeconomic policy. In competitive markets, resource allocation, consumer welfare, tax incidence, and monopoly markups hinge on the precise quantitative responsiveness of consumers and producers to shifts in prices and incomes.

Under Marshallian consumer optimization, an individual consumer maximizes an ordinal utility function $U(q_1, q_2, \dots, q_n)$ subject to the linear budget constraint $\sum p_i q_i \le M$, where $M$ denotes nominal money income. The resulting first-order conditions yield the **Marshallian Demand Functions**:

$$q_i = D_i(p_1, p_2, \dots, p_n, M), \quad i = 1, 2, \dots, n$$

Marshallian demand functions satisfy three fundamental mathematical properties:
1. **Homogeneity of Degree Zero**: Multiplying all prices and money income by an arbitrary positive scalar $\lambda > 0$ leaves physical quantity demanded unchanged (absence of money illusion):
   $$D_i(\lambda p, \lambda M) = D_i(p, M)$$
2. **Engel Aggregation**: The income-weighted sum of income elasticities equals unity:
   $$\sum_{i=1}^{n} w_i \eta_{i,M} = 1$$
   where $w_i = (p_i q_i)/M$ is the expenditure budget share of good $i$.
3. **Cournot Aggregation**: The expenditure-weighted sum of price elasticities across goods satisfies:
   $$\sum_{i=1}^{n} w_i \eta_{ij} = -w_j$$

---

## Mathematical Elasticity Metrics

In statistical economics, elasticity is defined as the dimensionless ratio of the proportional change in quantity to the proportional change in an underlying economic driver.

### 1. Own-Price Elasticity of Demand ($\eta_p$)
- **Point Elasticity**: For a continuous, differentiable demand curve $Q = D(P)$:
  $$\eta_p = \lim_{\Delta P \to 0} \left( \frac{\Delta Q / Q}{\Delta P / P} \right) = \frac{dQ}{dP} \times \frac{P}{Q} = \frac{d \ln(Q)}{d \ln(P)}$$
  By the Law of Demand, $dQ/dP < 0$, so $\eta_p$ is typically negative. In empirical economic literature, analysts either report the signed value (e.g., $-1.5$) or reference its absolute magnitude $|\eta_p|$.
  - $|\eta_p| > 1$: Price Elastic (proportional quantity response exceeds price change).
  - $|\eta_p| = 1$: Unitary Elastic (total expenditure $P \times Q$ remains constant).
  - $0 \le |\eta_p| < 1$: Price Inelastic (proportional quantity response is smaller than price change).

- **Arc Elasticity (Midpoint Formula)**: When evaluating discrete price changes between $(P_1, Q_1)$ and $(P_2, Q_2)$, calculating elasticity relative to the initial point yields different results than calculating relative to the final point. To guarantee symmetry and path-invariance, economists use the **Allen-Bowley Midpoint Arc Elasticity Formula**:
  $$\eta_{\text{arc}} = \frac{Q_2 - Q_1}{\frac{Q_1 + Q_2}{2}} \div \frac{P_2 - P_1}{\frac{P_1 + P_2}{2}} = \frac{Q_2 - Q_1}{P_2 - P_1} \times \frac{P_1 + P_2}{Q_1 + Q_2}$$

### 2. Income Elasticity of Demand ($\eta_M$)
Income elasticity measures consumer responsiveness to changes in real household income $M$:

$$\eta_M = \frac{dQ}{dM} \times \frac{M}{Q} = \frac{d \ln(Q)}{d \ln(M)}$$

- **Normal Goods** ($\eta_M > 0$): Consumption expands as income increases.
  - **Necessities** ($0 < \eta_M \le 1$): Expenditure increases slower than income; budget share $w_i$ contracts.
  - **Luxuries** ($\eta_M > 1$): Expenditure expands faster than income; budget share $w_i$ rises.
- **Inferior Goods** ($\eta_M < 0$): Consumption contracts as income increases (e.g., coarse staple grains, low-cost transit).

### 3. Cross-Price Elasticity of Demand ($\eta_{ij}$)
Cross-price elasticity measures the percentage shift in quantity demanded of commodity $i$ induced by a one-percent change in the price of a separate commodity $j$:

$$\eta_{ij} = \frac{\partial Q_i}{\partial P_j} \times \frac{P_j}{Q_i} = \frac{\partial \ln(Q_i)}{\partial \ln(P_j)}$$

- **Substitutes** ($\eta_{ij} > 0$): A price hike in good $j$ shifts demand toward good $i$ (e.g., tea and coffee, gasoline and electric vehicles).
- **Complements** ($\eta_{ij} < 0$): A price hike in good $j$ depresses demand for good $i$ (e.g., automobiles and motor fuel, hardware and software).
- **Independent Goods** ($\eta_{ij} = 0$).

---

## Engel Curves and Engel's Law

An **Engel Curve** traces the equilibrium relationship between the quantity demanded (or expenditure) of a specific commodity and household income $M$, holding all market prices constant.

In 1857, the German statistician Ernst Engel discovered the empirical regularity known as **Engel's Law**: as household income rises, the proportion of income allocated to food declines, even if the absolute monetary expenditure on food increases:

$$\frac{d}{dM} \left( \frac{p_{\text{food}} q_{\text{food}}}{M} \right) < 0 \iff \eta_{\text{food}, M} < 1$$

To fit empirical consumer survey data, economists deploy several parametric functional specifications:

| Functional Form | Mathematical Equation | Implied Income Elasticity ($\eta_M$) | Economic Characteristics |
| :--- | :--- | :--- | :--- |
| **Linear** | $Q = a + b M$ | $\eta_M = b \frac{M}{Q} = \frac{b M}{a + b M}$ | Approaches 1 as $M \to \infty$; lacks asymptotic saturation. |
| **Semi-Logarithmic** | $Q = a + b \ln(M)$ | $\eta_M = \frac{b}{Q}$ | Elasticity declines as consumption grows; suitable for basic necessities. |
| **Double-Logarithmic** | $\ln(Q) = a + b \ln(M)$ | $\eta_M = b = \text{constant}$ | Constant elasticity across all income brackets; widespread in empirical studies. |
| **Inverse** | $Q = a - \frac{b}{M}$ | $\eta_M = \frac{b}{M Q}$ | Possesses an upper physical saturation asymptote ($Q \to a$ as $M \to \infty$). |

---

## Econometric Estimation and the Identification Problem

In empirical research, estimating demand and supply parameters from observational market data introduces deep econometric challenges.

### The Double-Log Econometric Demand Specification
A standard Cobb-Douglas type empirical demand function is formulated as:

$$Q_t = A P_t^{\beta_1} M_t^{\beta_2} P_{c,t}^{\beta_3} e^{u_t}$$

Taking natural logarithms linearizes the parameters:

$$\ln(Q_t) = \beta_0 + \beta_1 \ln(P_t) + \beta_2 \ln(M_t) + \beta_3 \ln(P_{c,t}) + u_t$$

where:
- $\beta_0 = \ln(A)$ is the intercept.
- $\beta_1 = \frac{\partial \ln(Q)}{\partial \ln(P)}$ is the constant own-price elasticity of demand.
- $\beta_2 = \frac{\partial \ln(Q)}{\partial \ln(M)}$ is the constant income elasticity of demand.
- $\beta_3 = \frac{\partial \ln(Q)}{\partial \ln(P_c)}$ is the cross-price elasticity.
- $u_t \sim \text{iid}(0, \sigma^2)$ is the random disturbance term.

Because variables are in logarithmic units, the estimated OLS regression coefficients directly yield the theoretical elasticities without requiring post-estimation conversion.

### The Simultaneity and Identification Problem (Working's Theorem)
First formalized by E. J. Working in 1927, the **Identification Problem** warns that observable market data $(P_t, Q_t)$ represent simultaneous equilibrium intersections of shifting supply and demand curves:

$$\begin{cases}
Q_t^D = \alpha_0 + \alpha_1 P_t + u_t \\
Q_t^S = \beta_0 + \beta_1 P_t + v_t
\end{cases}$$

If an analyst simply runs an OLS regression of $Q_t$ on $P_t$, the resulting regression line traces neither the demand curve nor the supply curve, but a meaningless hybrid path of moving intersection points.

#### Conditions for Identification:
1. **Identification of the Demand Curve**: The demand curve is statistically identified if and only if there exists an exogenous instrument or supply-shifter variable (such as rainfall, agricultural fertilizer costs, or manufacturing wage shocks) that enters the supply equation but is strictly excluded from the demand equation. Shifting the supply curve back and forth across a stable demand curve traces out the demand schedule.
2. **Identification of the Supply Curve**: The supply curve is identified if and only if there exists an exogenous demand-shifter (such as consumer income or demographic population size) that shifts the demand curve across a stable supply curve.

---


---

## Advanced Demand Systems: The Almost Ideal Demand System (AIDS)

While single-equation log-log demand models provide convenient elasticity estimates, microeconomic theory dictates that multi-commodity demand functions must satisfy system-wide consumer optimization restrictions: Slutsky symmetry, homogeneity of degree zero, and budget exhaustion. In 1980, Angus Deaton and John Muellbauer revolutionized applied consumer economics by introducing the **Almost Ideal Demand System (AIDS)**.

### Mathematical Specification of the AIDS Model
Derived from the Price-Independent Generalized Logarithmic (PIGLOG) expenditure function, the AIDS model expresses the expenditure budget share $w_i = (p_i q_i) / M$ of good $i$ as a linear function of the logarithms of individual commodity prices and real household expenditure:

$$w_i = \alpha_i + \sum_{j=1}^{n} \gamma_{ij} \ln(p_j) + \beta_i \ln\left( \frac{M}{P^*} \right) + u_i, \quad i = 1, 2, \dots, n$$

where:
- $w_i$ is the budget share of good $i$ ($\sum w_i = 1$).
- $p_j$ is the price of commodity $j$.
- $M$ is total nominal household expenditure.
- $P^*$ is an aggregate translog price index, commonly approximated in empirical research by the **Stone Price Index**:
  $$\ln(P^*) \approx \sum_{k=1}^{n} w_k \ln(p_k)$$

### Theoretical Restrictions on AIDS Parameters:
To conform to neoclassical utility maximization, the parameter matrices must satisfy three sets of linear restrictions:
1. **Adding-Up (Budget Exhaustion)**:
   $$\sum_{i=1}^{n} \alpha_i = 1, \quad \sum_{i=1}^{n} \gamma_{ij} = 0, \quad \sum_{i=1}^{n} \beta_i = 0$$
2. **Homogeneity of Degree Zero in Prices and Income**:
   $$\sum_{j=1}^{n} \gamma_{ij} = 0 \quad \text{for each good } i$$
3. **Slutsky Symmetry**:
   $$\gamma_{ij} = \gamma_{ji} \quad \text{for all } i \ne j$$

### Elasticity Formulas in the AIDS Model:
- **Expenditure (Income) Elasticity**:
  $$\eta_{i, M} = 1 + \frac{\beta_i}{w_i}$$
  - If $\beta_i > 0$, good $i$ is a **Luxury** ($\eta_{i,M} > 1$); its budget share expands as total expenditure rises.
  - If $\beta_i < 0$, good $i$ is a **Necessity** ($\eta_{i,M} < 1$); its budget share contracts as total expenditure rises, conforming to Engel's Law.
- **Uncompensated (Marshallian) Own-Price Elasticity**:
  $$\eta_{ii} = -1 + \frac{\gamma_{ii}}{w_i} - \beta_i$$
- **Cross-Price Elasticity**:
  $$\eta_{ij} = \frac{\gamma_{ij}}{w_i} - \beta_i \left( \frac{w_j}{w_i} \right)$$

The AIDS framework allows econometricians to test whether empirical consumer choices conform to utility theory while estimating rich price and income substitution matrices across large consumer baskets.

---

## Consumer Welfare and Deadweight Loss Quantification

When governments introduce excise taxes, import tariffs, or environmental carbon fees, consumer prices rise and equilibrium consumption contracts. Econometric demand equations enable precise mathematical quantification of the resulting welfare impacts.

### Compensating and Equivalent Variation
Let $v(p, M)$ denote the indirect utility function, and let $e(p, u)$ denote the expenditure function.
When prices rise from $p^0$ to $p^1$:
1. **Compensating Variation ($CV$)**: The additional monetary compensation a consumer requires at the new prices $p^1$ to restore their original baseline utility level $u^0$:
   $$CV = e(p^1, u^0) - e(p^0, u^0) = e(p^1, u^0) - M^0$$
2. **Equivalent Variation ($EV$)**: The monetary reduction in base income at initial prices $p^0$ that would reduce the consumer's welfare by the same amount as the price hike:
   $$EV = e(p^1, u^1) - e(p^0, u^1) = M^0 - e(p^0, u^1)$$

### Marshallian Consumer Surplus and Harberger Deadweight Loss
For moderate price changes where income effects are small, consumer welfare loss is approximated by the change in **Marshallian Consumer Surplus ($\Delta CS$)**:

$$\Delta CS = -\int_{P^0}^{P^1} Q(P) dP$$

When an ad valorem tax rate $t$ is levied on a competitive commodity with initial price $P_0$ and quantity $Q_0$:
- Price paid by buyers: $P_1 = P_0 (1 + t)$
- New quantity demanded: $Q_1 = Q_0 [1 - |\eta_p| t]$
- Government Tax Revenue:
  $$TR = t P_0 Q_1 = t P_0 Q_0 (1 - |\eta_p| t)$$
- **Deadweight Loss (Harberger Excess Burden)**:
  $$DWL = -\Delta CS - TR = \frac{1}{2} \Delta P \Delta Q = \frac{1}{2} (t P_0) (|\eta_p| t Q_0) = \frac{1}{2} |\eta_p| P_0 Q_0 t^2$$

The deadweight loss of taxation increases with the **square of the tax rate ($t^2$)** and proportionally with the **price elasticity of demand ($|\eta_p|$)**. This foundational statistical theorem underpins optimal tax policy: to minimize societal welfare loss, governments should levy higher tax rates on highly price-inelastic necessities and lower rates on highly elastic goods (the Ramsey Tax Rule).


---

## Dynamic Market Equilibria: The Cobweb Model and Price Oscillations

In many agricultural and raw commodity markets, production decisions require an extended biological gestation period: farmers decide how many acres of crops to plant or livestock to breed based on current market prices, but the resulting harvest output cannot reach the market until the following season. This temporal production lag produces dynamic price-quantity oscillations formalized by the **Cobweb Theorem** (Mordecai Ezekiel, 1938).

### 1. Mathematical Formulation
Consider a market with an instantaneous linear demand curve and a lagged linear supply curve:

$$\text{Demand}: \quad Q_t^D = \alpha - \beta P_t, \quad \beta > 0$$
$$\text{Supply}: \quad Q_t^S = -\gamma + \delta P_{t-1}, \quad \delta > 0$$

In competitive market clearing at period $t$, quantity demanded must equal quantity supplied:

$$Q_t^D = Q_t^S \implies \alpha - \beta P_t = -\gamma + \delta P_{t-1}$$

Rearranging yields a first-order linear difference equation in market price $P_t$:

$$P_t = -\left( \frac{\delta}{\beta} \right) P_{t-1} + \frac{\alpha + \gamma}{\beta}$$

### 2. Long-Run Equilibrium and Stability Analysis
The long-run static equilibrium price $P^*$ satisfies $P_t = P_{t-1} = P^*$:

$$P^* = \frac{\alpha + \gamma}{\beta + \delta}$$

Subtracting $P^*$ from the dynamic difference equation defines the deviation $p_t = P_t - P^*$:

$$p_t = -\left( \frac{\delta}{\beta} \right) p_{t-1}$$

Iterating backwards from an initial price displacement $p_0$:

$$p_t = \left( -\frac{\delta}{\beta} \right)^t p_0$$

Because the base ratio $(-\delta / \beta)$ is strictly negative, the price trajectory inevitably alternates signs from period to period, producing cyclical oscillations around the equilibrium.

#### Three Stability Regimes:
1. **Convergent (Damped) Cobweb**: $\delta < \beta \iff |-\delta/\beta| < 1$.
   The supply curve is steeper than the demand curve ($|dQ^S/dP| < |dQ^D/dP|$). Price oscillations dampen over time, spiraling inward toward equilibrium $P^*$.
2. **Divergent (Explosive) Cobweb**: $\delta > \beta \iff |-\delta/\beta| > 1$.
   The supply curve is flatter than the demand curve. Price fluctuations amplify progressively outward, destabilizing the market.
3. **Continuous (Perpetual) Cobweb**: $\delta = \beta \iff |-\delta/\beta| = 1$.
   The system cycles indefinitely in a closed rectangular loop with constant amplitude.

---

## Simultaneous Equation Estimation: Two-Stage Least Squares (2SLS)

As established by Working's identification problem, estimating market demand and supply equations via Ordinary Least Squares yields biased and inconsistent estimates due to the simultaneity of price and quantity: price is endogenous ($E[P_t u_t] \ne 0$).

To consistently estimate structural demand and supply parameters, econometricians deploy **Two-Stage Least Squares (2SLS)** with instrumental variables.

### The Structural Demand-Supply System
Consider an agricultural commodity market:

$$\text{Demand}: \quad Q_t = \alpha_0 + \alpha_1 P_t + \alpha_2 Y_t + u_t$$
$$\text{Supply}: \quad Q_t = \beta_0 + \beta_1 P_t + \beta_2 W_t + v_t$$

where:
- $Q_t$ (quantity) and $P_t$ (price) are endogenous variables.
- $Y_t$ (consumer income) is an exogenous demand-shifter.
- $W_t$ (weather rainfall index or fertilizer cost) is an exogenous supply-shifter.

### The Two-Stage Estimation Algorithm:
1. **Stage 1: Reduced-Form Regression**:
   Regress the endogenous price $P_t$ on all exogenous variables in the entire system ($Y_t$ and $W_t$) using OLS:
   $$P_t = \pi_0 + \pi_1 Y_t + \pi_2 W_t + \nu_t$$
   Compute the fitted (predicted) values:
   $$\hat{P}_t = \hat{\pi}_0 + \hat{\pi}_1 Y_t + \hat{\pi}_2 W_t$$
   The predicted price $\hat{P}_t$ captures only the exogenous variation in price driven by weather and income, purging the correlation with the structural demand disturbance $u_t$.
2. **Stage 2: Structural Estimation**:
   Replace the endogenous price $P_t$ with its fitted instrument $\hat{P}_t$ in the structural demand equation and estimate via OLS:
   $$Q_t = \alpha_0 + \alpha_1 \hat{P}_t + \alpha_2 Y_t + u_t^*$$

The resulting 2SLS estimator $\hat{\alpha}_1$ is asymptotically consistent, providing unbiased estimates of true market demand price elasticity.


---

## Discrete Choice Demand Analysis: The McFadden Random Utility Model

In modern industrial economics, marketing science, and transportation planning, consumers do not choose continuous quantities of homogeneous goods along a smooth marginal utility curve. Instead, they choose a single, indivisible discrete alternative from a finite choice set (e.g., choosing whether to commute by personal automobile, subway, bus, or bicycle; or choosing which brand of smartphone to purchase).

To model these decisions, Nobel laureate Daniel McFadden (1974) developed the **Random Utility Maximization (RUM) Framework**.

### 1. Mathematical Formulation
Let consumer $n$ face a choice set of $J$ discrete alternatives: $\mathcal{C} = \{1, 2, \dots, J\}$.
The utility consumer $n$ derives from choosing alternative $i$ is decomposed into a deterministic systematic component $V_{ni}$ and a random idiosyncratic stochastic component $\epsilon_{ni}$:

$$U_{ni} = V_{ni} + \epsilon_{ni}$$

The systematic utility $V_{ni}$ is a linear function of observable attributes of the alternative (price $P_i$, travel time $T_i$, comfort quality $Q_i$) and socioeconomic characteristics of the consumer (income $M_n$, age, household size):

$$V_{ni} = \beta^T X_{ni}$$

Consumer $n$ chooses alternative $i$ if and only if it provides the highest utility among all available options:

$$P_{ni} = P(U_{ni} > U_{nj} \quad \forall j \ne i) = P(\epsilon_{nj} - \epsilon_{ni} < V_{ni} - V_{nj} \quad \forall j \ne i)$$

### 2. The Multinomial Logit (MNL) Model
McFadden proved that if the random disturbances $\epsilon_{ni}$ are independently and identically distributed according to the **Type I Extreme Value (Gumbel) Distribution**:
$$F(\epsilon) = \exp(-\exp(-\epsilon))$$

the choice probability takes the celebrated closed-form **Multinomial Logit (MNL)** formula:

$$P_{ni} = \frac{\exp(V_{ni})}{\sum_{j=1}^{J} \exp(V_{nj})} = \frac{\exp(\beta^T X_{ni})}{\sum_{j=1}^{J} \exp(\beta^T X_{nj})}$$

### 3. The Independence of Irrelevant Alternatives (IIA) Property
A fundamental mathematical property of the standard multinomial logit model is the **Independence of Irrelevant Alternatives (IIA)**: the ratio of the choice probabilities between any two alternatives $i$ and $k$ depends strictly on the attributes of those two options and is completely independent of the presence, absence, or attributes of any other alternative $j$:

$$\frac{P_{ni}}{P_{nk}} = \frac{\frac{\exp(V_{ni})}{\sum \exp(V_j)}}{\frac{\exp(V_{nk})}{\sum \exp(V_j)}} = \frac{\exp(V_{ni})}{\exp(V_{nk})} = \exp(V_{ni} - V_{nk})$$

#### The Red Bus / Blue Bus Paradox:
While computationally elegant, IIA imposes rigid, unrealistic cross-price substitution patterns. In McFadden's famous thought experiment, if commuters choose between driving a car ($P_{\text{car}} = 0.50$) and taking a blue bus ($P_{\text{blue}} = 0.50$), introducing a red bus that is identical to the blue bus in every respect should split the bus ridership equally, leaving car ridership at 50%. Under IIA, however, the model forces all three alternatives to equal 33.3%, erroneously predicting that the introduction of a red bus causes half of all drivers to abandon their cars.

To resolve IIA distortions, modern econometrics deploys the **Nested Logit Model** (grouping close substitutes into hierarchical branches) and the **Random Coefficients Mixed Logit Model (BLP: Berry, Levinsohn, and Pakes 1995)**, which allows consumer preference parameters $\beta$ to vary continuously across the population, accommodating realistic, flexible cross-price elasticity matrices across differentiated product markets.


---

## Econometric Identification of Market Power: The Bresnahan-Lau Model

In applied microeconomics and antitrust regulatory proceedings, competition authorities must assess whether firms in concentrated industries (such as commercial banking, telecommunications, or airline transport) behave competitively or exploit market power to extract monopoly rents. Because proprietary marginal cost data are rarely disclosed to econometricians, Timothy Bresnahan (1982) and Lawrence Lau (1982) developed an econometric methodology to identify market conduct directly from observable aggregate market price and quantity data.

### 1. Structural Formulation
Consider an oligopolistic market with aggregate demand:

$$Q_t = \alpha_0 + \alpha_1 P_t + \alpha_2 Y_t + \alpha_3 (P_t \cdot Z_t) + u_t$$

where $Y_t$ is consumer income, and $Z_t$ is an exogenous demand rotator (such as the price of a complementary service) that alters the slope of the demand curve.

The industry marginal revenue perceived by a representative firm is:

$$MR_t(\theta) = P_t + \theta \left( \frac{\partial P}{\partial Q} \right) Q_t = P_t + \frac{\theta}{\alpha_1 + \alpha_3 Z_t} Q_t$$

where $\theta \in [0, 1]$ is the unobserved **Conduct Parameter**:
- $\theta = 0$: Perfect Competition (Price equals Marginal Cost, $P = MC$).
- $\theta = 1/N$: Symmetric Cournot-Nash Oligopoly with $N$ firms.
- $\theta = 1$: Perfect Collusion / Joint Monopoly Profit Maximization.

Assuming a linear marginal cost curve:
$$MC_t = \beta_0 + \beta_1 Q_t + \beta_2 W_t + v_t$$
where $W_t$ is an exogenous input cost (e.g., labor wages, energy prices).

In profit-maximizing supply equilibrium ($MR_t = MC_t$):

$$P_t = -\theta Q_t^* + \beta_0 + \beta_1 Q_t + \beta_2 W_t + v_t$$

where $Q_t^* = \frac{Q_t}{\alpha_1 + \alpha_3 Z_t}$ is the rotated effective quantity variable.

### 2. Simultaneous Estimation and Hypothesis Testing
By estimating the demand equation and the supply relation simultaneously via Two-Stage Least Squares or Full Information Maximum Likelihood (FIML), the econometrician identifies $\alpha_1, \alpha_3$ from the demand curve, which allows the construction of $Q_t^*$.
The regression coefficient on $Q_t^*$ in the supply relation directly identifies the conduct parameter $\theta$.
Statistical agencies can then formally test the null hypothesis of perfect competition ($H_0: \theta = 0$) against the alternative of oligopolistic collusion ($H_1: \theta > 0$), providing court-admissible empirical evidence of market anti-competitive conduct.


---

## Flexible Production Frontiers: The Transcendental Logarithmic (Translog) Function

In empirical microeconomics and production economics, researchers often reject the classical Cobb-Douglas production function ($Y = A K^\alpha L^\beta$) and Constant Elasticity of Substitution (CES) function because they impose restrictive a priori constraints: Cobb-Douglas forces the elasticity of substitution between capital and labor to equal unity ($\sigma = 1$), while CES forces it to remain constant across all output levels.

To model unrestricted substitution dynamics, Laurits Christensen, Dale Jorgenson, and Lawrence Lau (1973) developed the **Transcendental Logarithmic (Translog) Production Frontier**.

### Mathematical Formulation
The translog production function represents a second-order Taylor series approximation to an arbitrary, twice continuously differentiable production function:

$$\ln(Y) = \alpha_0 + \sum_{i=1}^{m} \alpha_i \ln(X_i) + \frac{1}{2} \sum_{i=1}^{m} \sum_{j=1}^{m} \beta_{ij} \ln(X_i) \ln(X_j)$$

where:
- $Y$ is total physical output.
- $X_i, X_j$ are input factors (e.g., Capital $K$, Labor $L$, Energy $E$, Materials $M$).
- By Young's theorem on the symmetry of cross-partial derivatives:
  $$\beta_{ij} = \beta_{ji} \quad \forall i \ne j$$

### 1. Output Elasticities with Respect to Inputs
The output elasticity of factor $i$ is:

$$\epsilon_i = \frac{\partial \ln(Y)}{\partial \ln(X_i)} = \alpha_i + \sum_{j=1}^{m} \beta_{ij} \ln(X_j)$$

Notice that unlike Cobb-Douglas (where elasticity is the constant parameter $\alpha_i$), the translog output elasticity varies continuously with the levels of all inputs deployed.
Under constant returns to scale:
$$\sum_{i=1}^{m} \alpha_i = 1 \quad \text{and} \quad \sum_{j=1}^{m} \beta_{ij} = 0 \quad \forall i$$

### 2. Allen-Uzawa and Morishima Elasticities of Substitution
The elasticity of substitution between factor $i$ and factor $j$ in the translog cost dual function $C(w, Y)$ is given by the **Allen-Uzawa Partial Elasticity of Substitution (AES)**:

$$\sigma_{ij}^{\text{AES}} = \frac{C \cdot \frac{\partial^2 C}{\partial w_i \partial w_j}}{\frac{\partial C}{\partial w_i} \frac{\partial C}{\partial w_j}} = \frac{\gamma_{ij} + s_i s_j}{s_i s_j}, \quad i \ne j$$

where $s_i = w_i X_i / C$ is the cost share of input $i$.
Because the Allen-Uzawa elasticity can produce ambiguous signs in multi-factor settings, modern econometrics prefers the **Morishima Elasticity of Substitution (MES)**:

$$\sigma_{ij}^{\text{MES}} = \frac{\partial \ln(X_i / X_j)}{\partial \ln(w_j)} = s_j (\sigma_{ij}^{\text{AES}} - \sigma_{jj}^{\text{AES}})$$

The Morishima elasticity measures the percentage change in the input ratio $(X_i / X_j)$ induced by a one-percent change in the price of factor $j$ ($w_j$). It is inherently asymmetric ($\sigma_{ij}^{\text{MES}} \ne \sigma_{ji}^{\text{MES}}$), accurately capturing that adjusting capital equipment in response to a wage hike is structurally different from adjusting labor hiring in response to an interest rate shock.


---

## Hedonic Property Pricing and Environmental Amenity Valuation

In environmental and urban economics, public goods such as clean atmospheric air, urban green canopy, quiet residential neighborhoods, and high-performing public schools do not trade in separate private markets. To quantify consumer valuation and willingness to pay for these non-market amenities, Sherwin Rosen (1974) formulated the **Hedonic Property Pricing Method**.

### 1. The Hedonic Price Function
Let $P_i$ denote the market sale price of residential property $i$. A house is viewed as a heterogeneous bundle of structural attributes $S_i$ (square footage, bedrooms, bathrooms, lot size), neighborhood socioeconomic characteristics $N_i$ (crime rates, school test scores), and environmental amenities $Z_i$ (ambient particulate pollution $\text{PM}_{2.5}$, proximity to parks, highway traffic noise):

$$\ln(P_i) = \alpha_0 + \sum_{j=1}^{s} \beta_j S_{ij} + \sum_{k=1}^{m} \gamma_k N_{ik} + \theta Z_i + u_i$$

The parameter $\theta = \frac{\partial \ln(P)}{\partial Z}$ represents the percentage change in property value resulting from a one-unit change in environmental quality.
The **Marginal Implicit Price (Marginal Willingness to Pay, MWTP)** for amenity $Z$ is:

$$\text{MWTP}_Z = \frac{\partial P}{\partial Z} = \theta \times P_i$$

### 2. Capitalization and Welfare Evaluation
When a public infrastructure project or clean air regulation reduces local air pollution from $Z_0$ to $Z_1$:
- Housing values in the affected zone appreciate, a phenomenon known as **Amenity Capitalization**.
- Under the first-stage Rosen hedonic equilibrium, the aggregate capitalized property value increase across all $H$ affected homes provides an empirical measure of the societal welfare benefit:
  $$\Delta W \approx \sum_{i=1}^{H} \text{MWTP}_{Z, i} \times \Delta Z_i$$

By analyzing thousands of real estate mortgage and title transfer records via hedonic regression, economic statisticians supply court-tested cost-benefit valuations for environmental policy mandates and public infrastructure projects.


---

## Price Elasticity and Public Utility Regulation: Ramsey-Boiteux Pricing

In natural monopoly utility markets (such as national electrical power grids, municipal water supply networks, postal networks, and passenger railway infrastructure), high fixed infrastructure costs mean that average costs decline continuously over relevant market demand (economies of scale). If regulators force the utility to price at marginal cost ($P = MC$), the firm incurs severe operational deficits and bankrupts ($P < AC$). If the utility is left unregulated, it charges monopoly prices, generating massive deadweight welfare loss.

To resolve this dilemma, Frank Ramsey (1927) and Marcel Boiteux (1956) formulated the theory of **Optimal Second-Best Regulated Pricing (Ramsey-Boiteux Pricing)**.

### Mathematical Formulation
Consider a multi-product regulated public utility producing $n$ distinct services (e.g., residential peak electricity, commercial off-peak electricity, industrial power).
The regulator seeks to maximize total societal consumer surplus subject to the financial self-sufficiency constraint that the utility earns zero economic loss (total revenues cover total costs):

$$\max_{\{p_1, \dots, p_n\}} W(p_1, \dots, p_n) \quad \text{subject to } \sum_{i=1}^{n} p_i q_i(p_i) - C(q_1, \dots, q_n) \ge 0$$

Formulating the Lagrangian with shadow multiplier $\lambda > 0$:
$$\mathcal{L} = W(p) + \lambda \left[ \sum_{i=1}^{n} p_i q_i(p_i) - C(q) \right]$$

Differentiating with respect to each price $p_i$ and assuming zero cross-price substitution across independent services yields the **Inverse Elasticity Rule for Optimal Taxation and Regulation**:

$$\frac{p_i - MC_i}{p_i} = \left( \frac{\lambda}{1 + \lambda} \right) \frac{1}{|\eta_{i, p}|}$$

where:
- $\frac{p_i - MC_i}{p_i}$ is the proportional markup over marginal cost.
- $|\eta_{i, p}|$ is the absolute own-price elasticity of demand for service $i$.
- $\frac{\lambda}{1 + \lambda} \in (0, 1)$ is the normalized Ramsey shadow price of the public utility's budget constraint.

### Economic and Equity Implications:
The Ramsey rule establishes that to minimize societal deadweight loss while balancing the utility's budget:
- Services with highly **price-inelastic demand** (e.g., basic residential lighting where $|\eta_p| \approx 0.2$) must bear a **high percentage markup** over marginal cost.
- Services with highly **price-elastic demand** (e.g., industrial manufacturing power with competitive on-site alternatives where $|\eta_p| \approx 1.5$) must receive a **low percentage markup** close to marginal cost.

While mathematically efficient in minimizing Harberger deadweight triangles, pure Ramsey pricing can produce regressive distributional consequences by charging captive residential households higher markups than footloose corporate consumers, requiring regulators to integrate distributional equity weights into statutory rate-setting tariffs.

## Worked Questions and Solutions

### Question 1: Econometric Estimation of a Double-Log Demand Curve
An econometrician estimates the aggregate domestic demand for residential electrical power (in megawatt-hours, $Q$) as a function of average retail electricity price per kilowatt-hour ($P$, in cents) and median household disposable income ($M$, in thousands of dollars). A five-year historical dataset provides the following paired observations:

| Year ($t$) | Consumption ($Q_t$) | Price ($P_t$) | Income ($M_t$) |
| :---: | :---: | :---: | :---: |
| 1 | $120.0$ | $12.0$ | $40.0$ |
| 2 | $112.0$ | $14.0$ | $42.0$ |
| 3 | $105.0$ | $16.0$ | $44.0$ |
| 4 | $108.0$ | $15.0$ | $48.0$ |
| 5 | $118.0$ | $13.0$ | $50.0$ |

1. Formulate the log-linear empirical demand regression model $\ln(Q_t) = \beta_0 + \beta_1 \ln(P_t) + \beta_2 \ln(M_t) + u_t$.
2. Transform the observations into natural logarithms and formulate the OLS normal equations.
3. Given the estimated parameter vector $[\hat{\beta}_0 = 3.652, \; \hat{\beta}_1 = -0.684, \; \hat{\beta}_2 = +0.521]$, state the own-price elasticity and income elasticity of demand.
4. Classify electricity according to economic elasticity criteria (elastic vs inelastic, necessity vs luxury), and predict the percentage change in power consumption if retail electricity prices rise by $8.0\%$ while median household income rises by $4.0\%$.

### Solution, step 1: Model Formulation
The empirical Cobb-Douglas demand specification is:
$$Q_t = A P_t^{\beta_1} M_t^{\beta_2} e^{u_t}$$

Taking the natural logarithm of both sides:
$$\ln(Q_t) = \beta_0 + \beta_1 \ln(P_t) + \beta_2 \ln(M_t) + u_t$$

where:
- $\beta_0 = \ln(A)$ is the autonomous intercept.
- $\beta_1 = \frac{\partial \ln(Q)}{\partial \ln(P)}$ is the constant own-price elasticity of demand.
- $\beta_2 = \frac{\partial \ln(Q)}{\partial \ln(M)}$ is the constant income elasticity of demand.

### Solution, step 2: Logarithmic Transformation of Data
Let us compute the natural logarithms:
- $y_t = \ln(Q_t)$
- $x_{1t} = \ln(P_t)$
- $x_{2t} = \ln(M_t)$

Computations:
- **Year 1**:
  - $y_1 = \ln(120.0) \approx 4.7875$
  - $x_{11} = \ln(12.0) \approx 2.4849$
  - $x_{21} = \ln(40.0) \approx 3.6889$
- **Year 2**:
  - $y_2 = \ln(112.0) \approx 4.7185$
  - $x_{12} = \ln(14.0) \approx 2.6391$
  - $x_{22} = \ln(42.0) \approx 3.7377$
- **Year 3**:
  - $y_3 = \ln(105.0) \approx 4.6540$
  - $x_{13} = \ln(16.0) \approx 2.7726$
  - $x_{23} = \ln(44.0) \approx 3.7842$
- **Year 4**:
  - $y_4 = \ln(108.0) \approx 4.6821$
  - $x_{14} = \ln(15.0) \approx 2.7081$
  - $x_{24} = \ln(48.0) \approx 3.8712$
- **Year 5**:
  - $y_5 = \ln(118.0) \approx 4.7707$
  - $x_{15} = \ln(13.0) \approx 2.5649$
  - $x_{25} = \ln(50.0) \approx 3.9120$

Summing each vector across the $N = 5$ observations:
$$\sum y = 23.6128, \quad \sum x_1 = 13.1696, \quad \sum x_2 = 18.9940$$

The standard matrix OLS estimator is:
$$\hat{\beta} = (X^T X)^{-1} X^T y$$

### Solution, step 3: Elasticity Parameter Interpretation
From the estimated regression:
$$\ln(Q) = 3.652 - 0.684 \ln(P) + 0.521 \ln(M)$$

- **Own-Price Elasticity of Demand**:
  $$\eta_p = \hat{\beta}_1 = \mathbf{-0.684}$$
  A $1.0\%$ increase in retail electricity prices leads to a $0.684\%$ reduction in power consumption.
- **Income Elasticity of Demand**:
  $$\eta_M = \hat{\beta}_2 = \mathbf{+0.521}$$
  A $1.0\%$ increase in household disposable income leads to a $0.521\%$ increase in power consumption.

### Solution, step 4: Economic Classification and Forecast Shock
1. **Economic Classification**:
   - Price Elasticity: $|\eta_p| = 0.684 < 1.0$, indicating that residential electricity demand is **Price Inelastic**. Electricity has few short-run substitutes for lighting, refrigeration, and home appliances. An increase in price will raise total revenue for utilities ($d(PQ)/dP > 0$).
   - Income Elasticity: $0 < \eta_M = 0.521 < 1.0$, indicating that electricity is a **Normal Necessity Good**. As households become wealthier, their electricity use expands, but its share in the total household budget declines, conforming to Engel's Law.

2. **Forecasting Demand Response under Simultaneous Shocks**:
   Taking the total differential of the log demand function:
   $$\frac{dQ}{Q} \approx \beta_1 \left( \frac{dP}{P} \right) + \beta_2 \left( \frac{dM}{M} \right)$$

   With a price increase $\frac{dP}{P} = +8.0\%$ and an income increase $\frac{dM}{M} = +4.0\%$:
   $$\frac{dQ}{Q} \approx (-0.684)(+8.0\%) + (+0.521)(+4.0\%)$$
   $$\frac{dQ}{Q} \approx -5.472\% + 2.084\% = \mathbf{-3.388\%}$$

Residential electricity consumption is projected to contract by approximately **$3.39\%$**. The contractionary price effect ($-5.47\%$) outweighs the expansionary income effect ($+2.08\%$).

---

### Question 2: Point vs Arc Elasticity and Cross-Price Interdependence
A telecommunications conglomerate analyzes subscriber plans for mobile streaming services and fiber broadband. A price adjustment produces the following market response:

- Phase 1: Fiber broadband price is $P_1 = \$50.00$ per month; subscription volume is $Q_1 = 100{,}000$ households.
- Phase 2: Fiber broadband price is reduced to $P_2 = \$40.00$ per month; subscription volume expands to $Q_2 = 140{,}000$ households.
- Simultaneously, subscriptions to an affiliated 5G Home Wireless service ($Q_{\text{wireless}}$) drop from $40{,}000$ to $32{,}000$ subscribers, despite its own price remaining fixed at $\$45.00$.

1. Compute the price elasticity of demand for fiber broadband using the initial point formula, the final point formula, and the Bowley-Allen Midpoint Arc Elasticity formula.
2. Explain why the midpoint arc elasticity is theoretically preferred for non-marginal price changes.
3. Compute the **Cross-Price Elasticity of Demand** between 5G Home Wireless and fiber broadband using the midpoint formula.
4. Classify the relationship between fiber broadband and 5G Home Wireless (substitutes or complements), and evaluate whether the broadband price cut maximized total broadband revenue.

### Solution, step 1: Price Elasticity Computation
We have:
$$P_1 = 50, \quad P_2 = 40 \implies \Delta P = P_2 - P_1 = -10$$
$$Q_1 = 100{,}000, \quad Q_2 = 140{,}000 \implies \Delta Q = Q_2 - Q_1 = +40{,}000$$

1. **Initial Point Elasticity**:
   $$\eta_{\text{initial}} = \frac{\Delta Q}{\Delta P} \times \frac{P_1}{Q_1} = \frac{40{,}000}{-10} \times \frac{50}{100{,}000} = -4{,}000 \times 0.0005 = \mathbf{-2.00}$$

2. **Final Point Elasticity**:
   $$\eta_{\text{final}} = \frac{\Delta Q}{\Delta P} \times \frac{P_2}{Q_2} = \frac{40{,}000}{-10} \times \frac{40}{140{,}000} = -4{,}000 \times 0.0002857 \approx \mathbf{-1.14}$$

3. **Midpoint Arc Elasticity (Bowley-Allen Formula)**:
   $$\bar{P} = \frac{P_1 + P_2}{2} = \frac{50 + 40}{2} = 45.00$$
   $$\bar{Q} = \frac{Q_1 + Q_2}{2} = \frac{100{,}000 + 140{,}000}{2} = 120{,}000$$
   $$\eta_{\text{arc}} = \frac{\Delta Q}{\Delta P} \times \frac{\bar{P}}{\bar{Q}} = \frac{40{,}000}{-10} \times \frac{45}{120{,}000} = -4{,}000 \times 0.000375 = \mathbf{-1.50}$$

### Solution, step 2: Methodological Superiority of Midpoint Arc Formula
The point elasticity formula yields contradictory results depending on the arbitrary choice of baseline: $\eta = -2.00$ moving from $\$50$ to $\$40$, but $\eta = -1.14$ moving from $\$40$ to $\$50$.
The Midpoint Arc Elasticity formula averages the end-points, ensuring path symmetry: the elasticity between two prices is identical whether the price rises or falls. For non-marginal price shifts (such as a $20\%$ price cut), the midpoint formula provides an unbiased estimate of average responsiveness.

### Solution, step 3: Cross-Price Elasticity Computation
Let $Q_w$ denote 5G Home Wireless subscriptions, and $P_b$ denote fiber broadband price:
- $P_{b1} = 50, \; P_{b2} = 40 \implies \Delta P_b = -10, \; \bar{P}_b = 45$
- $Q_{w1} = 40{,}000, \; Q_{w2} = 32{,}000 \implies \Delta Q_w = 32{,}000 - 40{,}000 = -8{,}000$
- $\bar{Q}_w = \frac{40{,}000 + 32{,}000}{2} = 36{,}000$

Applying the midpoint formula:
$$\eta_{w, b} = \frac{\Delta Q_w}{\Delta P_b} \times \frac{\bar{P}_b}{\bar{Q}_w} = \frac{-8{,}000}{-10} \times \frac{45}{36{,}000} = (+800) \times 0.00125 = \mathbf{+1.00}$$

### Solution, step 4: Economic Classification and Total Revenue Analysis
1. **Classification**:
   The cross-price elasticity is positive ($\eta_{w, b} = +1.00 > 0$). When fiber broadband became cheaper, consumers abandoned 5G wireless in favor of fiber. Hence, fiber broadband and 5G Home Wireless are **Substitutes**. Because $\eta_{w, b} = 1.00$, the substitution response is unitary: a $1.0\%$ drop in fiber prices induces a $1.0\%$ contraction in wireless subscribers.

2. **Total Revenue Impact**:
   - Initial Total Revenue:
     $$\text{TR}_1 = P_1 \times Q_1 = \$50.00 \times 100{,}000 = \mathbf{\$5{,}000{,}000} \text{ per month}$$
   - New Total Revenue:
     $$\text{TR}_2 = P_2 \times Q_2 = \$40.00 \times 140{,}000 = \mathbf{\$5{,}600{,}000} \text{ per month}$$
   - Revenue Change:
     $$\Delta \text{TR} = \$5{,}600{,}000 - \$5{,}000{,}000 = \mathbf{+\$600{,}000} \quad (+12.0\%)$$

Because demand is price elastic ($|\eta_{\text{arc}}| = 1.50 > 1.0$), the $40\%$ surge in volume comfortably outstripped the $20\%$ price reduction, successfully increasing total corporate revenue.

---

### Question 3: Empirical Engel Curve Fitting and Saturation Limits
A socio-demographic study investigates the relationship between monthly household disposable income ($M$, in hundreds of dollars) and monthly expenditure on fresh dairy and meat products ($E$, in dollars). Data from six representative household income cohorts are recorded:

| Cohort ($i$) | Income ($M$) | Food Expenditure ($E$) | Food Share ($w = E / (100 M)$) |
| :---: | :---: | :---: | :---: |
| 1 | $10$ | $150$ | $150 / 1{,}000 = 15.0\%$ |
| 2 | $20$ | $240$ | $240 / 2{,}000 = 12.0\%$ |
| 3 | $30$ | $300$ | $300 / 3{,}000 = 10.0\%$ |
| 4 | $40$ | $340$ | $340 / 4{,}000 = 8.5\%$ |
| 5 | $50$ | $370$ | $370 / 5{,}000 = 7.4\%$ |
| 6 | $60$ | $390$ | $390 / 6{,}000 = 6.5\%$ |

1. Examine whether the empirical food budget shares conform to Engel's Law.
2. Consider an inverse Engel curve specification: $E_i = a - \frac{b}{M_i}$. Formulate the variable transformation $z_i = 1 / M_i$ to express the model in linear OLS form $E_i = a - b z_i$.
3. Compute the OLS estimates of $a$ and $b$, and state the fitted inverse Engel curve equation.
4. Calculate the theoretical upper expenditure saturation ceiling ($a$) as income approaches infinity, and compute the expenditure elasticity of demand at an income of $M = 20$ versus $M = 60$.

### Solution, step 1: Verification of Engel's Law
Looking at the fourth column of the empirical schedule:
- As monthly income rises from $\$1{,}000$ ($M = 10$) to $\$6{,}000$ ($M = 60$), absolute food expenditure rises from $\$150$ to $\$390$.
- Simultaneously, the food budget share falls monotonically from **$15.0\%$ down to $6.5\%$**.
Because the proportion of income spent on food diminishes as income expands, the data rigorously conform to **Engel's Law**. Fresh food behaves as an essential necessity.

### Solution, step 2: Linear Transformation of the Inverse Model
The inverse Engel specification is:
$$E = a - b \left( \frac{1}{M} \right)$$

Defining the reciprocal variable $z = 1/M$, the model becomes a standard bivariate linear equation:
$$E = a - b z$$
where $a$ represents the asymptotic saturation limit as $M \to \infty$ ($z \to 0$), and $-b$ is the slope with respect to $z$.

### Solution, step 3: OLS Parameter Estimation
Let us compute $z_i = 1/M_i$, $z_i^2$, and $z_i E_i$ for each cohort:
- Cohort 1: $M_1 = 10 \implies z_1 = 0.1000$; $E_1 = 150$; $z_1^2 = 0.010000$; $z_1 E_1 = 15.00$
- Cohort 2: $M_2 = 20 \implies z_2 = 0.0500$; $E_2 = 240$; $z_2^2 = 0.002500$; $z_2 E_2 = 12.00$
- Cohort 3: $M_3 = 30 \implies z_3 = 0.0333$; $E_3 = 300$; $z_3^2 = 0.001109$; $z_3 E_3 = 10.00$
- Cohort 4: $M_4 = 40 \implies z_4 = 0.0250$; $E_4 = 340$; $z_4^2 = 0.000625$; $z_4 E_4 = 8.50$
- Cohort 5: $M_5 = 50 \implies z_5 = 0.0200$; $E_5 = 370$; $z_5^2 = 0.000400$; $z_5 E_5 = 7.40$
- Cohort 6: $M_6 = 60 \implies z_6 = 0.0167$; $E_6 = 390$; $z_6^2 = 0.000279$; $z_6 E_6 = 6.50$

Summing over the $N = 6$ observations:
- $\sum z = 0.1000 + 0.0500 + 0.0333 + 0.0250 + 0.0200 + 0.0167 = 0.2450$
- $\bar{z} = 0.2450 / 6 \approx 0.040833$
- $\sum E = 150 + 240 + 300 + 340 + 370 + 390 = 1{,}790$
- $\bar{E} = 1{,}790 / 6 \approx 298.333$
- $\sum z^2 = 0.010000 + 0.002500 + 0.001109 + 0.000625 + 0.000400 + 0.000279 = 0.014913$
- $\sum z E = 15.00 + 12.00 + 10.00 + 8.50 + 7.40 + 6.50 = 59.40$

Computing the sample slope:
$$\text{Numerator} = \sum z E - \frac{(\sum z)(\sum E)}{N} = 59.40 - \frac{(0.2450)(1{,}790)}{6} = 59.40 - 73.0917 = -13.6917$$
$$\text{Denominator} = \sum z^2 - \frac{(\sum z)^2}{N} = 0.014913 - \frac{(0.2450)^2}{6} = 0.014913 - 0.010004 = 0.004909$$

The regression slope with respect to $z$ is:
$$\text{Slope} = \frac{-13.6917}{0.004909} \approx -2{,}789.10$$

Since the model is $E = a - b z$, the parameter $b$ is:
$$b = -(\text{Slope}) = \mathbf{2{,}789.10}$$

Solving for intercept $a$:
$$a = \bar{E} - (\text{Slope}) \bar{z} = 298.333 - (-2{,}789.10 \times 0.040833) = 298.333 + 113.888 \approx \mathbf{412.22}$$

The fitted inverse Engel curve is:
$$E = 412.22 - \frac{2{,}789.10}{M}$$

### Solution, step 4: Saturation Ceiling and Income Elasticity Dynamics
1. **Theoretical Saturation Ceiling**:
   As household income approaches infinity ($M \to \infty$), the term $\frac{2{,}789.10}{M} \to 0$.
   The asymptotic upper limit of fresh food expenditure is:
   $$E_{\max} = a = \mathbf{\$412.22} \text{ per month}$$
   No matter how wealthy a household becomes, physical stomach capacity and food consumption limits ceiling their dairy and meat expenditure at $\$412.22$.

2. **Income Elasticity Formula for Inverse Model**:
   Differentiating $E = a - b M^{-1}$ with respect to $M$:
   $$\frac{dE}{dM} = b M^{-2} = \frac{b}{M^2}$$
   The income elasticity of expenditure is:
   $$\eta_M = \frac{dE}{dM} \times \frac{M}{E} = \left( \frac{b}{M^2} \right) \frac{M}{E} = \frac{b}{M \times E}$$

3. **Elasticity at $M = 20$**:
   - Fitted expenditure: $E_{20} = 412.22 - \frac{2{,}789.10}{20} = 412.22 - 139.46 = 272.76$
   - Income elasticity:
     $$\eta_M(20) = \frac{2{,}789.10}{20 \times 272.76} = \frac{2{,}789.10}{5{,}455.20} \approx \mathbf{0.511}$$

4. **Elasticity at $M = 60$**:
   - Fitted expenditure: $E_{60} = 412.22 - \frac{2{,}789.10}{60} = 412.22 - 46.49 = 365.73$
   - Income elasticity:
     $$\eta_M(60) = \frac{2{,}789.10}{60 \times 365.73} = \frac{2{,}789.10}{21{,}943.80} \approx \mathbf{0.127}$$

**Economic Interpretation**:
For lower-income households ($M = 20$), a $1.0\%$ increase in income boosts food spending by $0.51\%$. For affluent households ($M = 60$), the elasticity collapses to $0.13\%$, demonstrating that demand nears complete biological saturation.
