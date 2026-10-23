# Unit 8: Stochastic Operations Research: Markovian Queueing Systems & Probabilistic Inventory Models

## 8.1 Queueing System Architecture, Kendall–Lee Notation, Poisson-Exponential Laws, and Little's Conservation Law

Whereas Units 1 through 7 focused primarily on deterministic or minimax optimization over convex polyhedra and networks, **Stochastic Operations Research** addresses operational systems governed by continuous-time random processes—most notably **Queueing Theory** (the mathematical study of waiting lines and congestion) and **Inventory Control Theory** (the optimization of stock replenishment under deterministic or random demand). Founded by the Danish mathematician and telephone engineer Agner Krarup Erlang between 1909 and 1917 at the Copenhagen Telephone Company, Queueing Theory models any service facility in which randomly arriving customers (packets, patients, manufacturing jobs, or database queries) compete for service from a finite number of servers.

### Kendall–Lee Symbolic Classification of Queueing Systems

Following David G. Kendall (1953) and Alec M. Lee (1966), a queueing system is classified by a six-part symbolic descriptor:

$$A \, / \, B \, / \, c \, / \, K \, / \, N \, / \, D$$

1. **$A$ (Interarrival Time Distribution)**: The probability law governing the i.i.d. times $T_a$ between consecutive customer arrivals. Standard symbols include **$M$** (*Markovian / Memoryless*, i.e., exponential interarrival times $\iff$ homogeneous Poisson arrival process with rate $\lambda$), **$D$** (*Deterministic* constant interarrival times), **$E_k$** (*Erlang-$k$* gamma distribution with shape $k$), and **$G$** (or **$GI$**, *General Independent* arbitrary distribution).
2. **$B$ (Service Time Distribution)**: The probability law governing i.i.d. customer service durations $T_s$ at each server ($M, D, E_k,$ or $G$, with mean service rate $\mu$ per busy server, so $\mathbb{E}[T_s] = 1/\mu$).
3. **$c$ (Number of Parallel Servers)**: $c \in \{1, 2, \dots, \infty\}$ identical parallel servers drawing from a common queue.
4. **$K$ (System Capacity Limit)**: The maximum total number of customers permitted in the system simultaneously (in queue plus in service). When omitted, $K = \infty$. If a customer arrives when $n = K$ customers are already present, the arriving customer is blocked and lost from the system.
5. **$N$ (Calling Population Size)**: The size of the source population generating arrivals (default $N = \infty$; when $N < \infty$ is finite, as in the *Machine Repairman Model*, the arrival rate depends on the number of machines currently operating outside the repair shop).
6. **$D$ (Queue Discipline)**: The scheduling rule selecting the next customer for service: **FCFS / FIFO** (First-Come, First-Served, the default), **LCFS / LIFO** (Last-Come, First-Served), **SIRO** (Service in Random Order), **PS** (Processor Sharing), or **PR / Priority** (Preemptive or Non-Preemptive Priority).

### Equivalence of Poisson Arrivals and Exponential Interarrival Times (PASTA Property)

A counting process $\{N(t), t \ge 0\}$ is a **homogeneous Poisson process** with arrival rate $\lambda > 0$ (meaning $P(N(t) = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}$ for $k = 0, 1, 2, \dots$, with mean $\mathbb{E}[N(t)] = \lambda t$) **if and only if** the interarrival times $T_1, T_2, \dots$ are i.i.d. **Exponential($\lambda$)** random variables with cumulative distribution function $P(T \le t) = 1 - e^{-\lambda t}$:

$$P(T_1 > t) = P(N(t) = 0) = \frac{(\lambda t)^0 e^{-\lambda t}}{0!} = e^{-\lambda t} \implies f_T(t) = \lambda e^{-\lambda t}, \quad t \ge 0$$

The exponential distribution is the unique continuous distribution possessing the **Memoryless (Markov) Property**: $P(T > t + s \mid T > s) = \frac{e^{-\lambda(t+s)}}{e^{-\lambda s}} = e^{-\lambda t} = P(T > t)$, meaning the residual time until the next arrival (or service completion) is independent of how much time has already elapsed! Furthermore, Poisson arrivals satisfy Ronald Wolff's (1982) **PASTA Property (Poisson Arrivals See Time Averages)**: the steady-state probability $\pi_n$ that an arriving Poisson customer finds $n$ customers already in the system equals the long-run continuous-time fraction of time $P_n$ that the system spends in state $n$.

### Theorem 8.1 (John D. C. Little's Conservation Law, 1961):
In **any** steady-state queueing system ($G/G/c/K/N/D$) regardless of the arrival distribution, service distribution, number of servers, or queue discipline, let $\lambda_{\text{eff}}$ denote the long-run effective arrival rate of customers **actually entering** the system, let $L$ (and $L_q$) denote the time-average expected number of customers in the system (and in the waiting queue), and let $W$ (and $W_q$) denote the customer-average expected time a customer spends in the system (and waiting in queue). Then:

$$L = \lambda_{\text{eff}} W, \qquad L_q = \lambda_{\text{eff}} W_q, \qquad W = W_q + \frac{1}{\mu}, \qquad L = L_q + \frac{\lambda_{\text{eff}}}{\mu}$$

where $\bar{c}_{\text{busy}} = L - L_q = \lambda_{\text{eff}} / \mu$ is the expected number of busy servers in steady state.

## 8.2 Continuous-Time Birth-Death Markov Chains and Steady-State Analysis of M/M/1 and M/M/1/K Queues

Let $N(t) \in \{0, 1, 2, \dots\}$ denote the number of customers in a Markovian queueing system at time $t \ge 0$. When interarrival times and service times are exponential with state-dependent arrival rate $\lambda_n$ (birth rate in state $n$) and state-dependent service rate $\mu_n$ (death rate in state $n$), $\{N(t), t \ge 0\}$ is a continuous-time **Birth–Death Markov Chain**. In an infinitesimal interval $(t, t + \Delta t)$ as $\Delta t \to 0^+$, the transition probabilities are $P_{n, n+1}(\Delta t) = \lambda_n \Delta t + o(\Delta t)$, $P_{n, n-1}(\Delta t) = \mu_n \Delta t + o(\Delta t)$, and $P_{n, n}(\Delta t) = 1 - (\lambda_n + \mu_n)\Delta t + o(\Delta t)$.

### Flow-Balance Cut Equations and the Fundamental Birth–Death Product Formula

In statistical equilibrium ($\lim_{t \to \infty} P_n(t) = P_n$ with $\frac{dP_n}{dt} = 0$), the **Global Balance Equations** equate the total probability flow out of state $n$ to the total flow into state $n$:
- State $n = 0$: $\lambda_0 P_0 = \mu_1 P_1$
- State $n \ge 1$: $(\lambda_n + \mu_n) P_n = \lambda_{n-1} P_{n-1} + \mu_{n+1} P_{n+1}$

Even more directly, consider a virtual cut between adjacent states $n$ and $n + 1$: in steady state, the mean rate of upward transitions $n \to n+1$ across the cut must equal the mean rate of downward transitions $n+1 \to n$, yielding the **Detailed (Local) Balance Equations**:

$$\lambda_n P_n = \mu_{n+1} P_{n+1} \implies P_{n+1} = \frac{\lambda_n}{\mu_{n+1}} P_n, \qquad n = 0, 1, 2, \dots$$

Iterating this two-term recursion from $n = 0$ expresses every steady-state probability $P_n$ in terms of $P_0$:

$$P_n = \left( \frac{\lambda_0 \lambda_1 \cdots \lambda_{n-1}}{\mu_1 \mu_2 \cdots \mu_n} \right) P_0 = C_n P_0 \quad (n \ge 1), \qquad P_0 = \left( 1 + \sum_{n=1}^\infty \frac{\lambda_0 \lambda_1 \cdots \lambda_{n-1}}{\mu_1 \mu_2 \cdots \mu_n} \right)^{-1}$$

provided the normalizing series converges ($\sum_{n=1}^\infty C_n < \infty$).

### 1. The Classical Single-Server $M/M/1/\infty/\infty$ Queue

In the $M/M/1$ queue, $\lambda_n = \lambda$ for all $n \ge 0$ and $\mu_n = \mu$ for all $n \ge 1$. Define the dimensionless **traffic intensity (server utilization factor)** $\rho = \frac{\lambda}{\mu}$. Then $C_n = \left(\frac{\lambda}{\mu}\right)^n = \rho^n$. The geometric series $1 + \sum_{n=1}^\infty \rho^n = \frac{1}{1 - \rho}$ converges **if and only if $\rho = \frac{\lambda}{\mu} < 1$** ($\lambda < \mu$), yielding the **Geometric Steady-State Distribution**:

$$P_0 = 1 - \rho, \qquad P_n = (1 - \rho) \rho^n, \qquad n = 0, 1, 2, \dots \quad (\rho < 1)$$

Using the geometric series derivative identity $\sum_{n=0}^\infty n \rho^n = \frac{\rho}{(1 - \rho)^2}$ and Little's Law ($\lambda_{\text{eff}} = \lambda$), we obtain the four canonical **$M/M/1$ Performance Measures**:

$$L = \mathbb{E}[N] = \sum_{n=0}^\infty n (1 - \rho)\rho^n = \frac{\rho}{1 - \rho} = \frac{\lambda}{\mu - \lambda}, \qquad L_q = L - \rho = \frac{\rho^2}{1 - \rho} = \frac{\lambda^2}{\mu(\mu - \lambda)}$$

$$W = \frac{L}{\lambda} = \frac{1}{\mu - \lambda}, \qquad W_q = \frac{L_q}{\lambda} = \frac{\rho}{\mu - \lambda} = \frac{\lambda}{\mu(\mu - \lambda)}$$

Furthermore, because $N$ given $N \ge 1$ is geometrically distributed and the sum of a Geometric($1-\rho$) number of i.i.d. Exponential($\mu$) service times is Exponential($\mu(1-\rho) = \mu - \lambda$), the total sojourn time $S$ in the system follows an **exact Exponential($\mu - \lambda$) distribution**: $P(S > t) = e^{-(\mu - \lambda)t}$ for all $t \ge 0$, while the waiting time in queue satisfies $P(W_q = 0) = P_0 = 1 - \rho$ and $P(W_q > t) = \rho e^{-(\mu - \lambda)t}$ for $t > 0$! Notice the critical managerial insight of $L_q = \frac{\rho^2}{1 - \rho}$: as server utilization $\rho \to 1^-$, queue length and waiting time explode to infinity hyperbolically!

### 2. The Finite-Capacity $M/M/1/K$ Queue (Blocking and Loss System)

When the waiting room is finite so the system holds at most $K$ customers ($n \in \{0, 1, \dots, K\}$), $\lambda_n = \lambda$ for $0 \le n \le K-1$ and $\lambda_K = 0$ (arriving customers when $n = K$ are blocked and turned away), while $\mu_n = \mu$ for $1 \le n \le K$. Because the state space is finite ($K + 1$ states), the $M/M/1/K$ queue is **ergodic and stable for EVERY $\rho = \lambda / \mu > 0$** (even when $\rho = 1$ or $\rho > 1$!):

$$P_n = \begin{cases} \dfrac{1 - \rho}{1 - \rho^{K+1}} \rho^n, & \text{if } \rho \ne 1 \\[10pt] \dfrac{1}{K + 1}, & \text{if } \rho = 1 \end{cases} \qquad (n = 0, 1, \dots, K)$$

The mean number in system is $L = \frac{\rho}{1 - \rho} - \frac{(K + 1)\rho^{K+1}}{1 - \rho^{K+1}}$ (for $\rho \ne 1$, and $L = K/2$ for $\rho = 1$). Crucially, because arrivals occurring during state $K$ (which occurs a fraction $P_K$ of the time by PASTA) are blocked, the **effective arrival rate** of customers actually entering the system is:

$$\lambda_{\text{eff}} = \lambda (1 - P_K) = \mu (1 - P_0)$$

from which Little's Law immediately gives $L_q = L - (1 - P_0) = L - \frac{\lambda_{\text{eff}}}{\mu}$, $W = \frac{L}{\lambda_{\text{eff}}}$, and $W_q = \frac{L_q}{\lambda_{\text{eff}}}$.

## 8.3 Multi-Server M/M/c Queues, Erlang-C Delay, Erlang-B Loss Systems, and the Pollaczek–Khinchine M/G/1 Formula

When a service facility operates $c \ge 2$ identical parallel servers, each with service rate $\mu$ (and arrival rate $\lambda$), the birth–death service rate increases linearly with the number of busy servers up to $c$, and plateaus at $c\mu$ when all $c$ servers are busy:

$$\lambda_n = \lambda \quad (\forall n \ge 0), \qquad \mu_n = \min(n, c)\mu = \begin{cases} n \mu, & 1 \le n \le c \\ c \mu, & n \ge c \end{cases}$$

### 1. The Multi-Server $M/M/c/\infty$ Queue and Erlang's Delay Formula ($C(c, a)$)

Define the **offered load** $a = \frac{\lambda}{\mu}$ (the expected number of busy servers) and the **per-server utilization** $\rho = \frac{\lambda}{c\mu} = \frac{a}{c}$. Steady-state stability requires **$\rho = \frac{\lambda}{c\mu} < 1$** ($\lambda < c\mu$). Substituting $\lambda_n$ and $\mu_n$ into the Birth–Death product formula gives:

$$P_n = \begin{cases} \dfrac{a^n}{n!} P_0 = \dfrac{(c\rho)^n}{n!} P_0, & 0 \le n \le c \\[10pt] \dfrac{a^n}{c! \, c^{n-c}} P_0 = \dfrac{c^c \rho^n}{c!} P_0, & n \ge c \end{cases}$$

where $P_0$ is determined by $\sum_{n=0}^\infty P_n = 1$:

$$P_0 = \left[ \sum_{n=0}^{c-1} \frac{(c\rho)^n}{n!} + \frac{(c\rho)^c}{c! (1 - \rho)} \right]^{-1}$$

The probability that an arriving customer must wait in queue ($N \ge c$) is given by **Agner Erlang's Delay Formula (Erlang-C Formula)**:

$$C(c, a) = P(N \ge c) = \sum_{n=c}^\infty P_n = \frac{(c\rho)^c}{c! (1 - \rho)} P_0$$

from which all four $M/M/c$ steady-state performance measures follow directly via geometric series summation and Little's Law:

$$L_q = \sum_{n=c}^\infty (n - c) P_n = \frac{\rho}{1 - \rho} C(c, a) = \frac{(c\rho)^c \rho}{c! (1 - \rho)^2} P_0, \qquad W_q = \frac{L_q}{\lambda}, \qquad W = W_q + \frac{1}{\mu}, \qquad L = L_q + \frac{\lambda}{\mu}$$

### 2. Special Cases: $M/M/c/c$ (Erlang-B Loss) and $M/M/\infty$ (Infinite Server)

- **The $M/M/c/c$ Trunk Loss System and Erlang-B Formula**: When there is zero waiting room ($K = c$, as in $c$ telephone trunk lines or $c$ ICU hospital beds where blocked arrivals are diverted), the states are truncated to $0 \le n \le c$. The steady-state distribution is the **truncated Poisson distribution** $P_n = \frac{a^n / n!}{\sum_{k=0}^c a^k / k!}$, and the **blocking (loss) probability $P_c$** is **Erlang's B Formula ($B(c, a)$)**:
  $$B(c, a) = P_c = \frac{\dfrac{a^c}{c!}}{\sum_{k=0}^c \dfrac{a^k}{k!}}, \qquad a = \frac{\lambda}{\mu}$$
  Remarkably, as proved by Boris Sevastyanov (1957), the Erlang-B formula holds for **arbitrary service time distributions ($M/G/c/c$)**—a profound structural property known as **Insensitivity** (depends on the service distribution solely through its mean $1/\mu$)!
- **The $M/M/\infty$ (and $M/G/\infty$) Self-Service System**: Letting $c \to \infty$ gives $\mu_n = n\mu$ for all $n \ge 1$, so $P_n = \frac{a^n e^{-a}}{n!}$ is an **exact Poisson($a = \lambda/\mu$) distribution** with $L = a = \lambda/\mu$, $L_q = 0$, $W_q = 0$, and $W = 1/\mu$.

### 3. Non-Markovian Service: The Pollaczek–Khinchine Formula for $M/G/1$ Queues

What if arrivals are Poisson($\lambda$), a single server operates ($c = 1$), but the service time $S$ follows an **arbitrary general distribution $G$** with mean $\mathbb{E}[S] = 1/\mu$ and finite **variance $\text{Var}(S) = \sigma_s^2$** ($\rho = \lambda \mathbb{E}[S] = \lambda/\mu < 1$)? Using David Kendall's **embedded discrete-time Markov chain** at customer departure epochs $N_{k+1} = (N_k - 1)^+ + A_{k+1}$ (where $A_{k+1}$ is the number of Poisson arrivals during the $(k+1)$-st service time), Felix Pollaczek (1930) and Aleksandr Khinchine (1932) derived the exact **$M/G/1$ Pollaczek–Khinchine (P-K) Mean Value Formula**:

$$L_q = \frac{\lambda^2 \sigma_s^2 + \rho^2}{2(1 - \rho)} = \frac{\rho^2 (1 + C_s^2)}{2(1 - \rho)}, \qquad W_q = \frac{L_q}{\lambda} = \frac{\lambda \sigma_s^2 + \rho / \mu}{2(1 - \rho)}, \qquad L = L_q + \rho, \qquad W = W_q + \frac{1}{\mu}$$

where $C_s^2 = \frac{\sigma_s^2}{(1/\mu)^2} = \mu^2 \sigma_s^2$ is the **squared coefficient of variation** of the service time! Notice two monumental insights of the Pollaczek–Khinchine formula:
1. **Exponential Service ($M/M/1$)**: Since an Exponential($\mu$) random variable has $\sigma_s^2 = 1/\mu^2$ ($C_s^2 = 1$), substituting $C_s^2 = 1$ yields $L_q = \frac{\rho^2(1 + 1)}{2(1 - \rho)} = \frac{\rho^2}{1 - \rho}$, recovering our $M/M/1$ formula!
2. **Deterministic Constant Service ($M/D/1$)**: If service times are completely deterministic and constant ($\sigma_s^2 = 0 \implies C_s^2 = 0$), then:
   $$L_q^{(M/D/1)} = \frac{\rho^2}{2(1 - \rho)} = \frac{1}{2} L_q^{(M/M/1)}$$
   **Eliminating service-time variance cuts average queue length and average waiting time in half**, proving mathematically that operational variability—not merely average utilization—is a primary driver of congestion!

## 8.4 Deterministic Inventory Control: Harris–Wilson EOQ, Finite Production Rate EPQ, and Planned Shortages

**Inventory Control Theory** addresses a fundamental operational trade-off across manufacturing, healthcare supply chains, and retail logistics: ordering or producing goods in very large batches minimizes fixed order-setup frequency, but inflates physical storage, insurance, and capital-opportunity holding costs; conversely, ordering tiny batches frequently minimizes holding costs, but inflates cumulative ordering and setup expenditures. Every inventory optimization model balances four core cost parameters:
1. **Annual Demand Rate ($D$)**: Total units of the item demanded per year (units/year).
2. **Unit Purchase or Production Cost ($c$)**: Direct variable cost per unit acquired (\$/unit).
3. **Fixed Ordering / Setup Cost ($K$)**: Fixed administrative, shipping, or machine-tooling setup cost incurred each time a replenishment order is placed, strictly independent of the batch size $Q$ (\$/order).
4. **Unit Holding (Carrying) Cost ($h$)**: Cost of holding one unit of inventory in storage for one full year (\$/unit/year), often expressed as $h = i \cdot c$ where $i$ is the annual capital opportunity + warehousing interest rate.
5. **Unit Shortage / Backorder Penalty Cost ($p$)**: Penalty cost incurred per unit of unmet demand backordered for one full year (\$/unit/year).

### 1. The Classical Harris–Wilson Economic Order Quantity (EOQ) Model (1913 / 1934)

Formulated by Ford W. Harris (1913) and popularized by R. H. Wilson (1934), the classical **EOQ Model** assumes constant deterministic demand rate $D$ units/year, instantaneous replenishment (or fixed known lead time $L$ with reorder point $\text{ROP} = (D \cdot L) \bmod Q^*$), no shortages permitted ($p = \infty$), and no quantity discounts. If an order of batch size $Q > 0$ arrives whenever inventory hits zero, the inventory trajectory forms a periodic **sawtooth wave** of cycle length $T = Q / D$ years, dropping linearly from peak $Q$ to $0$ with time-average inventory level $\bar{I} = \frac{Q + 0}{2} = \frac{Q}{2}$ units and $N = \frac{D}{Q}$ orders placed per year. The **Total Annual Cost Function $TC(Q)$** is:

$$TC(Q) = \text{Purchase Cost} + \text{Ordering Cost} + \text{Holding Cost} = c D + K \frac{D}{Q} + h \frac{Q}{2}$$

Because $\frac{d^2 TC}{dQ^2} = \frac{2KD}{Q^3} > 0$ for all $Q > 0$, $TC(Q)$ is strictly convex on $(0, \infty)$. Setting the first derivative $\frac{d TC}{dQ} = -\frac{KD}{Q^2} + \frac{h}{2} = 0$ (which occurs precisely where annual ordering cost $KD/Q$ equals annual holding cost $hQ/2$!) yields the celebrated **Harris–Wilson Square-Root EOQ Formula**:

$$Q^* = \sqrt{\frac{2 D K}{h}}, \qquad T^* = \frac{Q^*}{D} = \sqrt{\frac{2 K}{D h}}, \qquad TVC(Q^*) = \frac{KD}{Q^*} + \frac{h Q^*}{2} = \sqrt{2 D K h}$$

Notice the remarkable **insensitivity (robustness) of the EOQ curve** to parameter estimation errors: for any suboptimal batch size $Q$, the ratio of variable cost $TVC(Q)$ to the minimum variable cost $TVC(Q^*) = \sqrt{2DKh}$ is:

$$\frac{TVC(Q)}{TVC(Q^*)} = \frac{1}{2} \left( \frac{Q^*}{Q} + \frac{Q}{Q^*} \right)$$

Thus, even if statistical misestimation of $D, K,$ or $h$ causes $Q$ to deviate by $+20\%$ from $Q^*$ ($Q / Q^* = 1.2$), the variable cost increases by only $\frac{1}{2}(1/1.2 + 1.2) - 1 = 1.0167 - 1 = 1.67\%$!

### 2. Economic Production Lot-Size (EPQ) Model with Finite Replenishment Rate $P > D$

When batches of size $Q$ are manufactured internally at a **finite production rate $P > D$** units/year rather than delivered instantaneously, inventory builds up during the production run of length $t_p = Q / P$ at the net accumulation rate $P - D$ up to a **maximum peak inventory** $I_{\max} = (P - D) t_p = Q\left(1 - \frac{D}{P}\right)$. Consequently, average inventory is $\bar{I} = \frac{I_{\max}}{2} = \frac{Q}{2}\left(1 - \frac{D}{P}\right)$, replacing $h$ by the effective holding cost $h' = h\left(1 - \frac{D}{P}\right)$:

$$Q_{\text{EPQ}}^* = \sqrt{\frac{2 D K}{h \left(1 - \dfrac{D}{P}\right)}}, \qquad TVC_{\text{EPQ}}^* = \sqrt{2 D K h \left(1 - \frac{D}{P}\right)}$$

### 3. EOQ Model with Planned Shortages (Backorders Allowed, $p < \infty$)

When temporary backorders are permitted at shortage cost $p$ \$/unit/year, let $Q$ be the order quantity and $S \in [0, Q]$ be the **maximum backorder (shortage) level** reached just before a replenishment arrives, so the peak positive on-hand inventory immediately after clearing backorders is $I_{\max} = Q - S$. Over each cycle $T = Q/D$, positive inventory exists for fraction $\frac{Q-S}{Q}$ of the cycle with average on-hand stock $\frac{(Q-S)^2}{2Q}$, while shortages exist for fraction $\frac{S}{Q}$ of the cycle with average backorder level $\frac{S^2}{2Q}$. Minimizing $TVC(Q, S) = \frac{KD}{Q} + \frac{h(Q-S)^2}{2Q} + \frac{p S^2}{2Q}$ via $\frac{\partial TVC}{\partial S} = 0$ and $\frac{\partial TVC}{\partial Q} = 0$ yields:

$$Q^* = \sqrt{\frac{2 D K}{h}} \sqrt{\frac{p + h}{p}}, \qquad I_{\max}^* = Q^* - S^* = \sqrt{\frac{2 D K}{h}} \sqrt{\frac{p}{p + h}}, \qquad S^* = Q^* \left(\frac{h}{p + h}\right), \qquad TVC^* = \sqrt{2 D K h \left(\frac{p}{p + h}\right)}$$

## 8.5 Quantity-Discount EOQ Schedules and the Stochastic Single-Period Newsvendor (Critical Fractile) Model

We now transition from constant unit prices and deterministic demand to two essential extensions in applied operations research: **All-Units Quantity Discount Schedules** and the **Stochastic Single-Period Newsvendor Model**.

### 1. EOQ Optimization under All-Units Quantity Discounts

Suppliers frequently offer piecewise-constant **all-units price breaks**:

$$c(Q) = \begin{cases} c_1, & \text{if } q_1 = 0 \le Q < q_2 \\ c_2, & \text{if } q_2 \le Q < q_3 \\ \vdots & \vdots \\ c_m, & \text{if } q_m \le Q < \infty \end{cases} \qquad \text{with } c_1 > c_2 > \dots > c_m > 0$$

When holding cost is proportional to item value ($h_j = i \cdot c_j$), the total annual cost curve $TC_j(Q) = c_j D + \frac{KD}{Q} + \frac{i c_j Q}{2}$ is a family of $m$ vertically shifted convex curves ($TC_1(Q) > TC_2(Q) > \dots > TC_m(Q)$), each valid only on its designated price-break interval $[q_j, q_{j+1})$. Because the global total cost function $TC(Q)$ is discontinuous with downward jumps at the price-break thresholds $q_2, \dots, q_m$, the global minimum occurs either at a **feasible interior EOQ point** $Q_j^* = \sqrt{\frac{2DK}{i c_j}} \in [q_j, q_{j+1})$ or at a **lower price-break boundary threshold $q_j$** (where $Q_j^* < q_j$):
1. For each price bracket $j = m, m-1, \dots, 1$ (starting from the lowest unit price $c_m$), compute the unconstrained minimizer $Q_j^* = \sqrt{\frac{2DK}{h_j}}$.
2. If $Q_j^* \in [q_j, q_{j+1})$, then $Q_j^*$ is **valid (realizable)**, and because $TC_j(Q)$ lies strictly below all higher-price curves $TC_1, \dots, TC_{j-1}$, no bracket $k < j$ with higher unit price $c_k > c_j$ need ever be checked!
3. Compare $TC_j(Q_j^*)$ for the lowest-price valid EOQ against the boundary costs $TC_r(q_r)$ at all lower-price break thresholds $r > j$ (where $Q_r^* < q_r$), and select the order quantity achieving the minimum total annual cost $TC^*$.

### 2. The Stochastic Single-Period Newsvendor (Newsboy) Problem and the Critical Fractile

Consider perishable or single-season items—such as daily newspapers, fresh blood platelets, seasonal fashion apparel, or airline overbooking seats—where a single order quantity $Q \ge 0$ must be chosen **before** observing a random single-period demand $X$ governed by cumulative distribution function $F(x) = P(X \le x)$ and density $f(x)$ (or discrete PMF $p(x)$).

Let every unit ordered in excess of realized demand ($Q > X$) incur an **unit overage cost $c_o > 0$** (the loss on each unsold leftover unit: $c_o = c - v$, where $c$ is unit purchase cost and $v < c$ is unit salvage value), and let every unit of demand exceeding the stocked quantity ($X > Q$) incur a **unit underage (shortage) cost $c_u > 0$** (lost net profit plus any goodwill penalty: $c_u = p_{\text{sell}} - c + \pi$, where $p_{\text{sell}} > c$ is unit selling price). For a chosen stock level $Q$ and realized demand $X$, the realized cost of mismatch (expected opportunity loss) is:

$$L(Q, X) = c_o \max(Q - X, 0) + c_u \max(X - Q, 0) = \begin{cases} c_o (Q - X), & \text{if } X \le Q \\ c_u (X - Q), & \text{if } X > Q \end{cases}$$

Taking the mathematical expectation with respect to the continuous demand density $f(x)$ on $[0, \infty)$:

$$\mathbb{E}[L(Q, X)] = c_o \int_0^Q (Q - x) f(x) \, dx + c_u \int_Q^\infty (x - Q) f(x) \, dx$$

### Theorem 8.2 (The Newsvendor Critical Fractile / Quantile Optimality Theorem):
The expected mismatch loss $\mathbb{E}[L(Q, X)]$ is a strictly convex function of $Q$ whose unique global minimizer $Q^*$ is the **Critical Fractile (Quantile)** of the demand distribution $F(x)$:

$$F(Q^*) = P(X \le Q^*) = \frac{c_u}{c_u + c_o} \implies Q^* = F^{-1}\left( \frac{c_u}{c_u + c_o} \right)$$

For a discrete integer demand distribution $P(X \le Q)$, the optimal integer stock $Q^*$ is the smallest integer satisfying:

$$F(Q^* - 1) < \frac{c_u}{c_u + c_o} \le F(Q^*)$$

#### Proof via Leibniz's Rule for Differentiation under the Integral Sign:
Differentiating $\mathbb{E}[L(Q, X)]$ with respect to $Q$ using Leibniz's integral rule (noting that the boundary integrand terms $(Q - Q)f(Q) = 0$ vanish at $x = Q$):

$$\frac{d}{dQ} \mathbb{E}[L(Q, X)] = c_o \int_0^Q 1 \cdot f(x) \, dx - c_u \int_Q^\infty 1 \cdot f(x) \, dx = c_o F(Q) - c_u [1 - F(Q)] = (c_o + c_u) F(Q) - c_u = 0$$

Solving $(c_o + c_u)F(Q^*) = c_u$ immediately gives $F(Q^*) = \frac{c_u}{c_u + c_o}$. Moreover, the second derivative is $\frac{d^2}{dQ^2}\mathbb{E}[L(Q, X)] = (c_o + c_u) f(Q) \ge 0$, confirming a global minimum! (Notice the deep link to Unit 3 and Unit 1: choosing $Q^*$ to minimize $\mathbb{E}[c_o(Q-X)^+ + c_u(X-Q)^+]$ is mathematically identical to estimating the $\tau = \frac{c_u}{c_u + c_o}$ **population quantile** under Koenker–Bassett asymmetric check loss!).

## 8.6 Continuous-Review Stochastic (Q, r) Inventory Policies, Safety Stock, and Service-Level Constraints

In multi-period continuous-review inventory systems with random demand and positive replenishment lead time $L > 0$, the inventory position is monitored continuously; whenever the **on-hand plus on-order inventory position** drops to a designated **reorder point $r$**, a replenishment order of batch size **$Q$** is triggered—defining a **$(Q, r)$ Continuous-Review Policy**.

### Lead-Time Demand Distribution, Reorder Point $r$, and Safety Stock $SS$

Let $X_L$ denote the **random total demand during the replenishment lead time $L$**, possessing mean $\mu_L = \mathbb{E}[X_L]$, standard deviation $\sigma_L = \sqrt{\text{Var}(X_L)}$, cumulative distribution function $F_L(x) = P(X_L \le x)$, and density $f_L(x)$ (frequently modeled as Gaussian $X_L \sim \mathcal{N}(\mu_L, \sigma_L^2)$ by the Central Limit Theorem). Notice that if daily demand $D_t$ is i.i.d. with mean $\mu_d$ and variance $\sigma_d^2$, and lead time $L$ is a deterministic constant (in days), then:

$$\mu_L = L \mu_d, \qquad \sigma_L = \sqrt{L} \, \sigma_d$$

More generally, if lead time $L$ is itself a random variable with mean $\mathbb{E}[L] = \mu_{\text{lead}}$ and variance $\text{Var}(L) = \sigma_{\text{lead}}^2$ independent of daily demands, **Wald's Law of Total Variance** ($\text{Var}(X_L) = \mathbb{E}[\text{Var}(X_L \mid L)] + \text{Var}(\mathbb{E}[X_L \mid L])$) yields the exact composite lead-time variance:

$$\mu_L = \mu_{\text{lead}} \mu_d, \qquad \sigma_L = \sqrt{\mu_{\text{lead}} \sigma_d^2 + \mu_d^2 \sigma_{\text{lead}}^2}$$

Once an order of size $Q$ is placed at inventory level $r$, a **stockout occurs during the lead time if and only if lead-time demand $X_L$ exceeds the reorder point $r$ ($X_L > r$)**. We decompose the reorder point $r$ into the **expected lead-time demand $\mu_L$** plus a buffer called the **Safety Stock ($SS$)**:

$$r = \mu_L + SS = \mu_L + z_\alpha \sigma_L \implies SS = r - \mu_L = z_\alpha \sigma_L$$

where $z_\alpha$ is the safety factor corresponding to the desired **Cycle Service Level (Type-1 Service Level)** $1 - \alpha = P(X_L \le r) = F_L(r)$ (the probability of experiencing **zero stockout** during a replenishment cycle).

### Joint $(Q, r)$ Optimization and Type-1 vs. Type-2 (Fill Rate) Service Levels

Let $n(r) = \mathbb{E}[\max(X_L - r, 0)] = \int_r^\infty (x - r) f_L(x) \, dx$ denote the **expected number of shortage units per replenishment cycle**. For a Gaussian lead-time demand $X_L \sim \mathcal{N}(\mu_L, \sigma_L^2)$ with standardized threshold $z = (r - \mu_L)/\sigma_L$, integration by parts expresses $n(r)$ in terms of the **Standard Normal Unit Loss Function $L(z)$**:

$$n(r) = \sigma_L L(z), \qquad \text{where } L(z) = \int_z^\infty (u - z) \phi(u) \, du = \phi(z) - z [1 - \Phi(z)]$$

Here $\phi(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}$ is the standard normal PDF and $\Phi(z)$ is the standard normal CDF. Under the standard backorder $(Q, r)$ approximation ($\bar{I} \approx \frac{Q}{2} + (r - \mu_L) = \frac{Q}{2} + SS$ and $\frac{D}{Q}$ cycles per year, each incurring expected shortage cost $\pi_s n(r)$ where $\pi_s$ is the penalty per unit short), the expected annual variable cost is:

$$EAC(Q, r) = \frac{K D}{Q} + h \left( \frac{Q}{2} + r - \mu_L \right) + \frac{\pi_s D}{Q} \int_r^\infty (x - r) f_L(x) \, dx$$

Setting $\frac{\partial EAC}{\partial Q} = 0$ and $\frac{\partial EAC}{\partial r} = 0$ yields the coupled optimality equations for $(Q^*, r^*)$:

$$Q^* = \sqrt{\frac{2 D [K + \pi_s n(r^*)]}{h}}, \qquad 1 - F_L(r^*) = P(X_L > r^*) = \frac{h Q^*}{\pi_s D}$$

Finally, operations managers distinguish two distinct service-level metrics:
1. **Type-1 Service Level (Cycle Service Level, $\text{CSL} = 1 - \alpha$)**: The fraction of replenishment cycles that end with zero stockout: $\text{CSL} = P(X_L \le r) = F_L(r) = \Phi(z)$.
2. **Type-2 Service Level (Fill Rate, $\beta$)**: The **fraction of total annual unit demand that is satisfied immediately from on-hand stock** without backordering or lost sales:
   $$\beta = 1 - \frac{\text{Expected Shortage Units per Cycle}}{\text{Order Quantity per Cycle}} = 1 - \frac{n(r)}{Q} = 1 - \frac{\sigma_L L(z)}{Q}$$

## Worked Questions and Solutions

### Question 1: Steady-State Performance Analysis of M/M/1 and M/M/2 Queueing Systems and Server Pooling Efficiency

A university statistical consulting center currently operates two separate, independent walk-in desks: Desk A and Desk B. At each desk, student arrivals follow an independent Poisson process with arrival rate $\lambda_1 = 6$ students/hour, and each consultant provides service with independent exponentially distributed durations at rate $\mu = 8$ students/hour (so each desk operates as an independent **$M/M/1$ queue**). The director proposes pooling the two desks into a single unified waiting line served by both consultants in parallel (a single **$M/M/2$ queue** with combined arrival rate $\lambda = 2\lambda_1 = 12$ students/hour and $c = 2$ servers, each with $\mu = 8$ students/hour).

1. For one of the unpooled **$M/M/1$ desks** ($\lambda_1 = 6, \mu = 8$), compute the utilization $\rho$, idle probability $P_0$, mean number in system $L^{(M/M/1)}$, mean queue length $L_q^{(M/M/1)}$, mean waiting time in queue $W_q^{(M/M/1)}$, and mean total sojourn time $W^{(M/M/1)}$. Notice that across the two separate $M/M/1$ desks combined, the total expected number of students present is $2 L^{(M/M/1)}$.
2. For the pooled **$M/M/2$ system** ($c = 2, \lambda = 12, \mu = 8$), compute the utilization $\rho$, idle probability $P_0$, Erlang-C delay probability $C(2, a)$, mean queue length $L_q^{(M/M/2)}$, mean total number in system $L^{(M/M/2)}$, $W_q^{(M/M/2)}$, and $W^{(M/M/2)}$.
3. Quantify the exact percentage reduction in average waiting time in queue ($W_q$) achieved simply by pooling the two queues into a single $M/M/2$ line without hiring any additional staff!

### Solution, step 1: Analyze the Unpooled M/M/1 Queueing System

For each individual $M/M/1$ desk with $\lambda_1 = 6\text{ hr}^{-1}$ and $\mu = 8\text{ hr}^{-1}$:
- **Utilization & Idle Probability**: $\rho = \frac{\lambda_1}{\mu} = \frac{6}{8} = 0.75 = 75\% < 1$, and $P_0 = 1 - \rho = 0.25$.
- **Queue and System Lengths**:
  $$L^{(M/M/1)} = \frac{\rho}{1 - \rho} = \frac{0.75}{0.25} = 3.0\text{ students per desk} \quad \left(\text{Total across both desks} = 2 \times 3.0 = 6.0\text{ students}\right)$$
  $$L_q^{(M/M/1)} = \frac{\rho^2}{1 - \rho} = \frac{0.75^2}{0.25} = \frac{0.5625}{0.25} = 2.25\text{ students per desk} \quad \left(\text{Total waiting across both desks} = 4.50\text{ students}\right)$$
- **Waiting and Sojourn Times**:
  $$W_q^{(M/M/1)} = \frac{L_q^{(M/M/1)}}{\lambda_1} = \frac{2.25}{6} = \frac{3}{8}\text{ hr} = 0.375\text{ hr} = 22.50\text{ minutes}$$
  $$W^{(M/M/1)} = \frac{1}{\mu - \lambda_1} = \frac{1}{8 - 6} = 0.50\text{ hr} = 30.00\text{ minutes}$$

### Solution, step 2: Analyze the Pooled M/M/2 Queueing System

For the pooled $M/M/2$ system with $c = 2$ servers, $\lambda = 12\text{ hr}^{-1}$, and $\mu = 8\text{ hr}^{-1}$:
- **Offered Load & Per-Server Utilization**: $a = \frac{\lambda}{\mu} = \frac{12}{8} = 1.5 = \frac{3}{2}$, and $\rho = \frac{\lambda}{c\mu} = \frac{12}{16} = 0.75 = 75\%$ (identical server utilization!).
- **Idle Probability $P_0$**: For $c = 2$, the normalizing formula gives:
  $$P_0 = \left[ 1 + a + \frac{a^2}{2!(1 - \rho)} \right]^{-1} = \left[ 1 + 1.5 + \frac{2.25}{2(0.25)} \right]^{-1} = \left[ 2.5 + 4.5 \right]^{-1} = \frac{1}{7} \quad \left(\text{Note: } \frac{1 - \rho}{1 + \rho} = \frac{0.25}{1.75} = \frac{1}{7}\right)$$
- **Erlang-C Delay Probability $C(2, 1.5)$**:
  $$C(2, 1.5) = P(N \ge 2) = \frac{a^2}{2!(1 - \rho)} P_0 = 4.5 \times \frac{1}{7} = \frac{9}{14} \approx 0.6429$$
- **Pooled Queue Length and Waiting Times**:
  $$L_q^{(M/M/2)} = \frac{\rho}{1 - \rho} C(2, 1.5) = \frac{0.75}{0.25} \times \frac{9}{14} = 3 \times \frac{9}{14} = \frac{27}{14} \approx 1.9286\text{ students}$$
  $$L^{(M/M/2)} = L_q^{(M/M/2)} + \frac{\lambda}{\mu} = \frac{27}{14} + \frac{21}{14} = \frac{48}{14} = \frac{24}{7} \approx 3.4286\text{ students}$$
  $$W_q^{(M/M/2)} = \frac{L_q^{(M/M/2)}}{\lambda} = \frac{27/14}{12} = \frac{9}{56}\text{ hr} \approx 0.1607\text{ hr} = 9.643\text{ minutes}$$
  $$W^{(M/M/2)} = W_q^{(M/M/2)} + \frac{1}{\mu} = \frac{9}{56} + \frac{7}{56} = \frac{16}{56} = \frac{2}{7}\text{ hr} \approx 0.2857\text{ hr} = 17.143\text{ minutes}$$

### Solution, step 3: Compare Unpooled vs. Pooled Performance (Statistical Pooling Effect)

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Performance Metric</th><th>Two Separate $M/M/1$ Queues</th><th>Single Pooled $M/M/2$ Queue</th><th>Improvement / Reduction</th></tr></thead><tbody><tr><td>Server Utilization $\rho$</td><td>$75.0\%$</td><td>$75.0\%$</td><td>Unchanged ($0\%$)</td></tr><tr><td>Total Mean Queue Length ($L_q$)</td><td>$2 \times 2.25 = 4.50\text{ students}$</td><td>$27/14 \approx 1.929\text{ students}$</td><td><strong>$-57.14\%$ reduction</strong></td></tr><tr><td>Mean Wait in Queue ($W_q$)</td><td>$3/8\text{ hr} = 22.50\text{ min}$</td><td>$9/56\text{ hr} = 9.643\text{ min}$</td><td><strong>$-57.14\%$ reduction</strong></td></tr><tr><td>Mean Time in System ($W$)</td><td>$1/2\text{ hr} = 30.00\text{ min}$</td><td>$2/7\text{ hr} = 17.143\text{ min}$</td><td><strong>$-42.86\%$ reduction</strong></td></tr></tbody></table></div>

The ratio of pooled queue waiting time to unpooled queue waiting time is $\frac{9/56}{3/8} = \frac{3}{7} \approx 0.4286$. Thus, **simply merging two separate $M/M/1$ queues into a single pooled $M/M/2$ queue slashes average waiting time in queue by $4/7 \approx 57.14\%$**—because in a pooled queue, a server can never sit idle while students are waiting in the other server's line!

### Question 2: Pollaczek–Khinchine M/G/1 Analysis and All-Units Quantity-Discount EOQ Optimization

This two-part problem examines variance effects in $M/G/1$ queues and discontinuous cost optimization in quantity-discount inventory schedules:

**Part A ($M/G/1$ Queue)**: Automated diagnostic blood analyzers receive sample trays according to a Poisson process at rate $\lambda = 4$ trays/hour. Each tray requires a mean processing time of $\mathbb{E}[S] = 12\text{ minutes} = 0.20\text{ hours}$ ($\mu = 5$ trays/hour). Compare the steady-state mean queue length $L_q$ and mean waiting time $W_q$ under three service time distributions having the exact same mean $1/\mu = 0.20\text{ hr}$:
1. Exponential service times ($M/M/1$, $\sigma_s = 0.20\text{ hr}$).
2. Deterministic constant service times ($M/D/1$, $\sigma_s = 0\text{ hr}$).
3. Erlang-$4$ service times ($M/E_4/1$, $\sigma_s^2 = \frac{1}{4\mu^2} = 0.01\text{ hr}^2$).

**Part B (Quantity-Discount EOQ)**: A hospital pharmacy uses $D = 5{,}000$ boxes of sterile syringes per year. The fixed ordering cost is $K = \$100$ per order, and the annual holding cost is $i = 20\%$ of the unit purchase price ($h_j = 0.20 c_j$). The supplier offers the following **all-units quantity discount schedule**:
- Bracket 1: $0 \le Q < 500$ boxes $\implies c_1 = \$10.00$/box ($h_1 = \$2.00$)
- Bracket 2: $500 \le Q < 1{,}000$ boxes $\implies c_2 = \$9.50$/box ($h_2 = \$1.90$)
- Bracket 3: $Q \ge 1{,}000$ boxes $\implies c_3 = \$9.20$/box ($h_3 = \$1.84$)

Determine the globally optimal order quantity $Q^*$ and minimum total annual cost $TC(Q^*)$.

### Solution, step 1: Part A: Evaluate M/G/1 Queue Performance via the Pollaczek-Khinchine Formula

Here $\lambda = 4\text{ hr}^{-1}$, $\mu = 5\text{ hr}^{-1}$, so $\rho = \lambda / \mu = 0.80$. By the Pollaczek–Khinchine formula (Section 8.3), $L_q = \frac{\lambda^2 \sigma_s^2 + \rho^2}{2(1 - \rho)} = \frac{16 \sigma_s^2 + 0.64}{0.40}$:
1. **Exponential Service ($M/M/1$, $\sigma_s^2 = 1/\mu^2 = 0.04\text{ hr}^2, C_s^2 = 1$)**:
   $$L_q^{(M/M/1)} = \frac{16(0.04) + 0.64}{0.40} = \frac{1.28}{0.40} = 3.20\text{ trays}, \qquad W_q^{(M/M/1)} = \frac{3.20}{4} = 0.80\text{ hr} = 48.0\text{ minutes}$$
2. **Deterministic Constant Service ($M/D/1$, $\sigma_s^2 = 0, C_s^2 = 0$)**:
   $$L_q^{(M/D/1)} = \frac{0 + 0.64}{0.40} = 1.60\text{ trays}, \qquad W_q^{(M/D/1)} = \frac{1.60}{4} = 0.40\text{ hr} = 24.0\text{ minutes}$$
3. **Erlang-$4$ Service ($M/E_4/1$, $\sigma_s^2 = 0.01\text{ hr}^2, C_s^2 = 1/4 = 0.25$)**:
   $$L_q^{(M/E_4/1)} = \frac{16(0.01) + 0.64}{0.40} = \frac{0.80}{0.40} = 2.00\text{ trays}, \qquad W_q^{(M/E_4/1)} = \frac{2.00}{4} = 0.50\text{ hr} = 30.0\text{ minutes}$$

### Solution, step 2: Part B, Step 1: Compute Unconstrained EOQ Values Across Price Brackets

Starting from the lowest unit price (Bracket 3) and moving upward:
1. **Bracket 3 ($Q \ge 1{,}000$, $c_3 = \$9.20, h_3 = \$1.84$)**:
   $$Q_3^* = \sqrt{\frac{2 D K}{h_3}} = \sqrt{\frac{2(5{,}000)(100)}{1.84}} = \sqrt{543{,}478.26} \approx 737.21\text{ boxes}$$
   Because $737.21 < 1{,}000$, $Q_3^*$ is **not realizable** in Bracket 3; the best feasible quantity in Bracket 3 is the lower threshold **$q_3 = 1{,}000$ boxes**.
2. **Bracket 2 ($500 \le Q < 1{,}000$, $c_2 = \$9.50, h_2 = \$1.90$)**:
   $$Q_2^* = \sqrt{\frac{2 D K}{h_2}} = \sqrt{\frac{2(5{,}000)(100)}{1.90}} = \sqrt{526{,}315.79} \approx 725.48\text{ boxes}$$
   Because $500 \le 725.48 < 1{,}000$, **$Q_2^* = 725.48$ boxes is valid (realizable)**! Since $Q_2^*$ is valid in Bracket 2, Bracket 1 ($c_1 = \$10.00 > c_2$) is strictly dominated and need not be checked.

### Solution, step 3: Part B, Step 2: Compare Total Annual Costs and Identify Global Optimum

We compare $TC(Q) = c_j D + \frac{KD}{Q} + \frac{h_j Q}{2}$ at the two candidate quantities $Q_2^* = 725.48$ and $q_3 = 1{,}000$:
1. **At $Q_2^* = 725.48$ boxes ($c_2 = \$9.50, h_2 = \$1.90$)**:
   $$TC_2(725.48) = 9.50(5{,}000) + \sqrt{2(5{,}000)(100)(1.90)} = 47{,}500.00 + 1{,}378.40 = \$48{,}878.40$$
2. **At Price-Break Threshold $q_3 = 1{,}000$ boxes ($c_3 = \$9.20, h_3 = \$1.84$)**:
   $$TC_3(1{,}000) = 9.20(5{,}000) + \frac{100(5{,}000)}{1{,}000} + \frac{1.84(1{,}000)}{2} = 46{,}000.00 + 500.00 + 920.00 = \$47{,}420.00$$

Because $\$47{,}420.00 < \$48{,}878.40$, the $\$1{,}500$ annual purchase-price savings of Bracket 3 outweighs the slight increase in holding cost! The globally optimal order quantity is **$Q^* = 1{,}000$ boxes per order** with minimum total annual cost **$TC^* = \$47{,}420.00$**.

### Question 3: Stochastic Newsvendor Critical Fractile and Continuous-Review (Q, r) Safety-Stock Optimization

This problem analyzes single-period and continuous-review stochastic inventory decisions under Gaussian demand:

**Part A (Single-Period Newsvendor Model)**: A biomedical supply center stocks a single-batch flu vaccine prior to the winter epidemic peak. Each vaccine dose costs $c = \$25$ to acquire, sells to clinics for $p_{\text{sell}} = \$65$ during the season, and any unsold dose remaining after the season is salvaged for $v = \$5$ for archival testing. Unmet demand incurs an additional public-health shortage penalty of $\pi = \$10$ per dose. Demand $X$ is normally distributed with mean $\mu = 2{,}000$ doses and standard deviation $\sigma = 300$ doses ($X \sim \mathcal{N}(2000, 300^2)$). Compute the unit overage cost $c_o$, unit underage cost $c_u$, critical fractile, and optimal stock quantity $Q^*$.

**Part B (Continuous-Review $(Q, r)$ Policy)**: For a year-round reagent with annual demand $D = 10{,}000$ units, daily demand has mean $\mu_d = 40$ units/day and standard deviation $\sigma_d = 12$ units/day. The replenishment lead time is a constant $L = 9$ days.
1. Compute the mean $\mu_L$ and standard deviation $\sigma_L$ of lead-time demand $X_L$.
2. Determine the safety stock $SS$ and reorder point $r$ required to guarantee a **$99\%$ Cycle Service Level ($\text{CSL} = 0.99$, $z_{0.01} = 2.326$)**.
3. If the order quantity is $Q = 600$ units and the standard normal loss function at $z = 2.326$ is $L(2.326) \approx 0.0034$, calculate the expected shortage units per cycle $n(r)$ and the **Type-2 Service Level (Fill Rate $\beta$)**.

### Solution, step 1: Part A: Compute Overage/Underage Costs, Critical Fractile, and Optimal Newsvendor Stock Q*

- **Unit Overage Cost ($c_o$)**: Cost per leftover unit ($Q > X$) is purchase cost minus salvage value:
  $$c_o = c - v = 25 - 5 = \$20\text{ per dose}$$
- **Unit Underage Cost ($c_u$)**: Cost per unit of unmet demand ($X > Q$) is lost margin plus shortage penalty:
  $$c_u = (p_{\text{sell}} - c) + \pi = (65 - 25) + 10 = 40 + 10 = \$50\text{ per dose}$$
- **Critical Fractile (Theorem 8.2)**:
  $$F(Q^*) = \frac{c_u}{c_u + c_o} = \frac{50}{50 + 20} = \frac{50}{70} = \frac{5}{7} \approx 0.7143$$
- **Optimal Order Quantity $Q^*$**: From the standard normal CDF table, $\Phi(z^*) = 0.7143 \implies z^* \approx +0.566$. Therefore:
  $$Q^* = \mu + z^* \sigma = 2{,}000 + 0.566(300) = 2{,}000 + 169.8 \approx 2{,}170\text{ doses}$$

### Solution, step 2: Part B, Steps 1 & 2: Lead-Time Demand Moments, Safety Stock, and Reorder Point

With i.i.d. daily demand ($\mu_d = 40, \sigma_d = 12$) over a constant lead time of $L = 9$ days:
- **Mean Lead-Time Demand**:
  $$\mu_L = L \mu_d = 9 \times 40 = 360\text{ units}$$
- **Standard Deviation of Lead-Time Demand**:
  $$\sigma_L = \sqrt{L} \, \sigma_d = \sqrt{9} \times 12 = 3 \times 12 = 36\text{ units}$$
- **Safety Stock ($SS$) and Reorder Point ($r$) for $99\%$ Cycle Service Level ($z = 2.326$)**:
  $$SS = z_{0.01} \sigma_L = 2.326 \times 36 \approx 83.74 \approx 84\text{ units}$$
  $$r = \mu_L + SS = 360 + 83.74 = 443.74 \approx 444\text{ units}$$

### Solution, step 3: Part B, Step 3: Expected Shortages per Cycle and Type-2 Fill Rate beta

Using the Standard Normal Loss Function $L(2.326) \approx 0.0034$ with $\sigma_L = 36$ units:
- **Expected Shortage Units per Replenishment Cycle $n(r)$**:
  $$n(r) = \sigma_L L(z) = 36 \times 0.0034 = 0.1224\text{ units short per cycle}$$
- **Type-2 Service Level (Fill Rate $\beta$) for Batch Size $Q = 600$**:
  $$\beta = 1 - \frac{n(r)}{Q} = 1 - \frac{0.1224}{600} = 1 - 0.000204 = 0.999796 \approx 99.98\%$$

Notice that a $99.00\%$ Type-1 Cycle Service Level corresponds to an extraordinary **$99.98\%$ Type-2 Unit Fill Rate**, because even in the $1\%$ of cycles where a stockout occurs, the average shortage magnitude is only a tiny fraction of the $Q = 600$-unit order batch!
