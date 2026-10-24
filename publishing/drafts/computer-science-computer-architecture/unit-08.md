# Computer Architecture — Unit 8: Architecture evaluation

## 8.1 Power

**Core model — Power**

Dynamic and leakage power contribute to processor energy. A common simplified dynamic-power model is P proportional to alpha*C*V squared*f.

**Original worked illustration**

Reducing voltage from 1.0 to 0.9 at unchanged frequency gives 0.81 of the dynamic switching power in this model.

**Boundary conditions and checks**

Lower voltage may require lower frequency; leakage, memory and cooling costs mean total-system energy does not follow this simple formula exactly.

### Extended technical chapter: Power

Dynamic CMOS switching power is often approximated as P_dynamic = alpha × C × V² × f, where alpha is the switching activity factor, C the effective switched capacitance, V supply voltage and f clock frequency. This formula isolates an important quadratic sensitivity to voltage under fixed activity, capacitance and frequency. For example, reducing voltage from one volt to 0.9 volts produces a dynamic-power ratio of 0.81, or a 19 percent reduction, if the other factors truly remain constant. But voltage reduction can require a lower frequency for timing closure, and leakage or static power contributes differently. A real energy budget must include both power and execution time.

Energy for a task is the integral of power over time. If one processor performs a task in two seconds at ten watts, it consumes twenty joules. Another completes the task in one second at fifteen watts and consumes fifteen joules, so it is both faster and lower-energy for this task despite higher instantaneous power. Conversely, a low-power core running much longer could consume more total energy. Engineers distinguish performance per watt, energy per operation, idle power, thermal design power, and peak electrical demand rather than treating them as synonyms. They also account for external memory, fans, accelerators and regulators when the system rather than the chip is the comparison target.

Clock gating reduces unnecessary switching activity. Power gating can cut leakage in unused regions but introduces wake-up costs and possible state-retention requirements. Dynamic voltage and frequency scaling chooses operating points based on workload and thermal limits. A laboratory should plot a hypothetical voltage–frequency curve and compute power, execution time and energy for several operating points, making clear which values are assumptions. Include the temperature dimension qualitatively: sustained thermal throttling can erase a short benchmark's advertised advantage. The design decision should specify battery life, data-center energy, peak throughput or deadline compliance as the real objective.

## 8.2 Reliability

**Core model — Reliability**

Reliability concerns soft errors, wear, thermal events and failure recovery. Redundancy and error correction can detect or correct some classes of faults.

**Original worked illustration**

A single-error-correcting code adds check bits to enable detection and correction of one bit error within a protected word.

**Boundary conditions and checks**

No finite code protects against every possible corruption, and silent faults in control paths may escape data-only checks.

### Extended technical chapter: Reliability

Computer architecture reliability concerns correct service despite faults, failures or adverse operating conditions. A transient bit flip differs from a permanent stuck-at fault, and a software-visible failure differs from a detected and corrected hardware error. Error-detecting codes append redundancy that can identify certain corruptions; error-correcting codes add enough structure to reconstruct data for specified error patterns. A simple parity bit detects any odd number of flipped bits in a protected word, but it misses even numbers of flips and does not generally locate the erroneous bit. Stronger ECC systems trade storage and computation overhead for stronger coverage.

Availability is the fraction of time a system is operational, not the probability that it never fails over its entire life. In an ideal repairable system with mean time between failures of 1000 hours and mean repair time of ten hours, steady-state availability is 1000/(1000+10), about 99.01 percent. This expression assumes a simplified regenerative failure-and-repair process. It ignores correlated failures, planned maintenance, workload-induced fault rates, and the loss of a shared power supply. Redundant components can improve availability only when they do not all depend on the same failing resource and when failover actually works.

Architectural fault tolerance includes duplicated computation, checkers, parity/ECC, retries, watchdogs and isolation domains. Each technique has a detection coverage and residual risk. A cache protected by ECC may correct a single-bit error but still fail under an uncorrectable multi-bit pattern; the processor or operating system needs an explicit policy for such an event. A lab failure table should distinguish error detected, error corrected, operation retried, component isolated and service lost. Test failures at startup, during a write, and during recovery, and verify that data-integrity guarantees are preserved. Do not confuse a high mean time between failures with a deterministic guarantee for individual devices.

## 8.3 Security Implications

**Core model — Security Implications**

Microarchitectural security arises when performance features expose information across intended protection boundaries. Timing and cache state can become side channels.

**Original worked illustration**

An attacker observing cache-hit versus cache-miss latency may infer whether a shared address was recently accessed, even without direct permission to read its contents.

**Boundary conditions and checks**

An architectural access check can be correct while speculative transient activity leaks information; threat models must include microarchitectural state.

### Extended technical chapter: Security Implications

Computer architecture exposes security properties through privilege modes, memory protection, isolation mechanisms and speculative microarchitectural state. The architectural contract says which memory and registers a program may access; implementation features such as caches, predictors and shared execution units may create side channels that reveal information without directly returning forbidden values. A robust treatment separates architectural permission enforcement from timing or resource-observation leakage. Correct access control is necessary but does not by itself guarantee confidentiality against every physical or microarchitectural attacker.

A timing side channel exploits a correlation between secret-dependent behavior and an externally measurable quantity. Cache access time provides one broad class of examples: accessing a resident line tends to be faster than fetching it from farther down the hierarchy under comparable conditions. A teaching exercise can compare two fictional traces with different numbers of cache hits and misses, calculate modeled total access time, and discuss how measurement noise affects distinguishability. It should not provide an exploitation recipe or pretend timing observations uniquely determine a secret. The educational objective is to show that performance mechanisms can influence the security boundary and that threat models must identify the attacker’s observations.

Architectural mitigations range from process isolation and permission checks to constant-time software patterns, memory partitioning and careful handling of speculative state. Their costs can include extra memory, reduced sharing, synchronization overhead or lower performance. The security effect is never universal; it depends on a concrete attacker model, hardware implementation and software usage. For verification, list protected assets, entry points, attack assumptions and observable outputs, then check whether each proposed mitigation addresses the named leakage path. An effective review avoids generic claims that one feature 'makes a processor secure.' Security is a system property involving processor, firmware, operating system, compiler, libraries and application behavior.

## 8.4 Hardware–Software Tradeoffs

**Core model — Hardware–Software Tradeoffs**

Hardware-software co-design weighs ISA capabilities, compilers, kernels and workloads together. A useful optimization improves the deployed application's relevant metric, not a synthetic proxy alone.

**Original worked illustration**

Replacing a software checksum with a vector instruction reduces instructions but may lose if loads dominate memory bandwidth; measure complete runtime and energy.

**Boundary conditions and checks**

Portability, compiler behavior and maintenance matter alongside peak microbenchmarks; a feature that benefits one target may be detrimental elsewhere.

### Extended technical chapter: Hardware–Software Tradeoffs

Hardware–software co-design determines where a capability belongs and how it interacts with an application. Implementing an operation in custom hardware may reduce latency or energy for a stable, frequently used workload, but hardware design, validation, manufacturing, portability and update costs can be large. Software remains easier to revise and often benefits from general-purpose parallelism or existing accelerators. The decision should begin with a measured workload profile and a clearly stated objective rather than the assumption that dedicated circuitry is always faster.

Suppose a service spends 30 percent of request time in a compression routine and a proposed accelerator makes only that routine ten times faster. The new normalized total time is 0.7+0.3/10=0.73, yielding a whole-request speedup of approximately 1.37. That is valuable in some settings but far below the accelerator's local tenfold improvement. Data transfers between host memory and an accelerator may further lower gain. A larger input batch can amortize transfer setup, whereas small interactive requests may not. An accelerator may also consume additional memory bandwidth that slows the rest of the system. These constraints can turn a benchmark victory into an application-level regression.

ISA extensions, coprocessors, vector units, operating-system interfaces and compiler transformations are alternative design locations for a feature. A new instruction may require compiler recognition and software fallbacks; a peripheral accelerator may require drivers and buffer-management discipline. Co-design exercises should specify portability requirements, the expected lifetime of the algorithm, software maintenance burden, fault behavior, energy budget, and available verification skills. Create a tradeoff matrix with measured baseline, predicted benefit, integration cost and principal uncertainty. Then identify the cheapest experiment capable of overturning the proposed decision. The aim of architecture is not maximum component complexity but an effective, reliable computation system.

### Integrated laboratory: selecting an accelerator under power, risk and security constraints

A software service performs image transformations and spends thirty percent of its response time in a filter kernel. An accelerator vendor advertises that the filter is ten times faster, measured on a stand-alone batch. Apply the fixed-workload Amdahl equation to the whole service: unchanged fraction 0.7 plus accelerated fraction 0.3/10 gives normalized elapsed time 0.73, so ideal total speedup is about 1.37. This upper-level result immediately limits expectations. The real speedup could be lower if copies between host and accelerator add latency, or higher only if the accelerator also changes other phases of the workload. A benchmark restricted to the filter cannot establish end-to-end request performance.

Suppose transferring inputs and results adds 0.06 of the old response time. The new normalized time becomes 0.79, with speedup about 1.27. If batching eliminates half the transfers, the model improves. But batching can delay single urgent requests while a group accumulates; latency percentiles may worsen even if overall throughput rises. The team must therefore specify whether it values throughput, average response, 99th-percentile latency or deadlines. It should also measure the input sizes used by actual clients, not just the vendor's best-case large-batch dataset. The optimization's value is a function of its deployment context.

Now compare energy. Suppose the original service consumes ten watts of relevant compute power for one second, using ten joules. If the optimized service consumes sixteen watts for 0.79 seconds, it uses 12.64 joules despite being faster. This simplified calculation suggests an energy regression. A second optimized design consuming twelve watts for 0.79 seconds would use 9.48 joules, improving both time and energy. These power numbers are hypothetical; the decision process is what matters. Idle draw, cooling, host CPU power and external memory should be included when the actual financial objective is whole-system energy cost.

The proposed accelerator also introduces a new device and driver attack surface. Its DMA engine should only access designated memory mappings; descriptor lengths and buffer ownership must be validated. If the accelerator shares caches, queues or predictors with software from different trust domains, the team should consider whether timing variation could reveal protected data. No single switch or instruction can guarantee security. A review should record the assets, allowed access paths, untrusted inputs, isolation mechanisms and evidence from tests. Performance gains do not justify exposing client data to a device with inadequate protection or update procedures.

Reliability changes with extra components. If the accelerator fails, does the service stop, silently return incorrect outputs, or fall back to the CPU? A fallback can preserve availability but may violate a strict response-time objective. A watchdog can detect a stalled device but does not guarantee recovery. Error-correcting memory can protect some classes of bit corruption while leaving others uncovered. Model a recovery timeline that includes error detection, device reset, retry policy, and user-visible failure reporting. Include duplicate submission tests so retries cannot accidentally execute a side-effecting job twice.

The final decision matrix should separate verified measurements from model-derived estimates. Record baseline latency distribution, actual transfer overhead, accelerated-kernel speedup, complete-request speedup, joules per completed request, correctness coverage, failure behavior and security assumptions. Assign each uncertainty a cheap discriminating test: a prototype batch benchmark, an A/B shadow deployment, an error-injection run, a power-meter sample or a driver fuzz test. If the resulting evidence is insufficient, a conditional recommendation is more useful than premature certainty. Hardware–software co-design succeeds when the resulting service is measurably better under its real constraints, not merely when its custom hardware looks impressive.

### Review lens: accountable engineering decisions

A processor selection is a multidimensional decision under uncertainty. A chip might win a peak-throughput contest yet fail a deadline under thermal throttling. An accelerator may improve average response while introducing a device-driver failure mode or increasing energy per request. Reliability estimates depend on explicit repair and failure assumptions, while security assurances depend on a defined attacker model. Put measurement date, software versions, test inputs, error bars and power boundary in the evidence record so that someone else can repeat the comparison. Record untested concerns as risks rather than granting them a pass. The best next experiment is often one that can disprove the preferred design cheaply: a small real-data benchmark, a fault-injection test or a measurable energy trial. Architectural elegance is not an acceptable substitute for an implemented, verified advantage.

### Additional guided investigations for architecture decisions

**Voltage model.** Under fixed activity, capacitance and frequency, reducing voltage from 1.0 to 0.8 predicts dynamic switching power factor 0.64. A baseline switching component of five watts would fall to 3.2 watts under those assumptions. If frequency must also fall from 2 GHz to 1.5 GHz, the multiplicative dynamic ratio becomes 0.64×0.75=0.48, but execution time may lengthen. Compare modeled energy for a job whose cycle count remains constant, and remember that leakage and thermal behavior are outside the simple equation.

**Availability model.** A repairable component with MTBF 2000 hours and mean repair time twenty hours has ideal steady-state availability 2000/2020≈0.9901. Halving repair time to ten hours yields 2000/2010≈0.9950. The improvement is material but neither number means the component cannot fail tomorrow. Correlated power failure and maintenance outage make redundant system-level availability more complicated. Identify which failure events belong inside the model's boundary.

**Security model.** A speculative processor may influence cache state before an instruction retires. The fact that a disallowed architectural read does not return secret data to a user program does not establish that timing patterns reveal nothing. Model two hypothetical access sequences containing different numbers of hits and misses; compute a time difference and then vary the measurement noise. Discuss how noise can obscure or reveal a statistical signal over repeated observations without prescribing an attack sequence.

**Accelerator decision.** A proposed fixed-function unit improves a code segment occupying one-quarter of a job by factor five. Ideal normalized total time is 0.75+0.25/5=0.8, giving a whole-job speedup 1.25. Add 0.08 of old time for transfer and synchronization, and total becomes 0.88, speedup≈1.136. If failure requires CPU fallback and the latency deadline cannot tolerate that fallback, the device may not be suitable despite benchmark gains. Record performance, energy, maintenance and correctness together.

### Diagnostic challenge: inspect a decision at three boundaries

A hypothetical accelerator improves one important kernel from twelve milliseconds to three, saving nine milliseconds locally. But host-to-device copies take four milliseconds and dispatch adds two; a single request saves only three milliseconds relative to the original kernel if no work overlaps. For a batch of one hundred requests that can share dispatch and transfers, amortized overhead might be much lower, changing the decision. Meanwhile the accelerator may consume higher instantaneous power, so compute joules per completed request rather than assuming reduced latency equals reduced energy. Finally, examine failure recovery: if a device timeout forces CPU fallback and doubles tail latency, the system may violate a strict deadline even if average throughput improves. Create a matrix with baseline latency, optimized kernel latency, fixed and per-request overhead, energy and error recovery. Rank recommendations separately for interactive single requests and large batch jobs, and explain which measurements would falsify the choice.

## Three worked problems

### Power: worked application 1

If dynamic power scales as V² at fixed f and activity, evaluate reducing V from 1.0 to 0.9.

**Set up the model and conditions**

New-to-old ratio is (0.9/1.0)^2.

**Carry out the calculation or proof**

Square 0.9 to obtain 0.81.

**State the result and its scope**

Dynamic switching power becomes 81% of baseline, ignoring leakage and frequency changes.

**Independent verification, conditions, and interpretation**

Under the specified dynamic-power model, power is proportional to squared supply voltage when activity factor, effective capacitance and frequency stay fixed. The voltage ratio is 0.9/1.0=0.9, and squaring yields 0.81. Predicted switching power is therefore 81 percent of baseline, a 19 percent reduction. If baseline dynamic switching power were ten watts, the modeled new dynamic component would be 8.1 watts. This result does not apply to total processor power without accounting for leakage, regulators and other components. Voltage reduction also affects achievable timing; a machine may require a lower clock or may fail to meet its design's critical-path delay if voltage is reduced arbitrarily. For energy per completed task, multiply actual power by execution time or integrate a changing power profile. A slower operating point may conserve instantaneous watts yet run long enough to increase total joules. The calculation is a useful sensitivity relation, not a general guarantee that undervolting a working device improves reliability, battery life or performance under all conditions.

### Reliability: worked application 2

For a cache side channel, explain why a correct memory permission check alone is insufficient.

**Set up the model and conditions**

Permission checks constrain architectural reads of protected data.

**Carry out the calculation or proof**

Shared cache state can nevertheless change timing visible to another context.

**State the result and its scope**

Timing observations may leak access patterns; countermeasures must cover the threat model.

**Independent verification, conditions, and interpretation**

Memory access permissions control which architectural loads, stores and instruction fetches are allowed, but shared microarchitectural resources can expose differences in timing even when forbidden data are never returned directly. A cache hit under a simplified model may require one unit of time, while a miss requires many units. If a program's access pattern depends on secret state, an observer with appropriate timing capability might infer information from repeated timing differences. The existence and exploitability of that information channel depend on the attacker's placement, noise, isolation and the detailed hardware behavior. A correct permission check does not necessarily clear all cache or predictor traces created by speculative or permitted activity. Mitigation therefore starts with an explicit threat model and may combine constant-time software discipline, resource partitioning, speculation restrictions and careful isolation. None should be claimed sufficient for every device or attacker. A valid security review explains the observable side channel, the assumptions enabling observation, and what the proposed defense removes or reduces. This is a conceptual risk analysis, not an assertion that every cached access leaks a useful secret.

### Security Implications: worked application 3

Compare CPU time: A uses 1e9 instructions, CPI 2, 2GHz; B uses 1e9, CPI 1.5, 1GHz.

**Set up the model and conditions**

A cycles=2e9, time=2e9/2e9=1s.

**Carry out the calculation or proof**

B cycles=1.5e9, time=1.5e9/1e9=1.5s.

**State the result and its scope**

A is faster despite B's smaller CPI.

**Independent verification, conditions, and interpretation**

Compute A's cycles: 1×10^9 instructions × CPI 2 = 2×10^9 cycles. Dividing by 2×10^9 cycles per second gives one second. For B, the same instruction count at CPI 1.5 uses 1.5×10^9 cycles; at 1×10^9 cycles per second, this takes 1.5 seconds. A therefore completes the modeled work faster despite B's smaller average CPI. A comparison based only on CPI would be wrong because effective frequency differs. A comparison based only on clock rate would also be inadequate if instruction counts or instruction mixes changed. The dimensional form instructions × cycles/instruction ÷ cycles/second is a built-in check. Doubling B's frequency while holding its CPI constant would reduce its modeled time to 0.75 seconds and reverse the ranking, but such a frequency increase may not be physically attainable at the same power or voltage. For actual products, measure completed-work latency, correctness and energy under a representative workload. The question demonstrates that performance is jointly determined by several factors rather than one advertised number.
