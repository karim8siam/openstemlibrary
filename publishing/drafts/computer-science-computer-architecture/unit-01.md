# Computer Architecture — Unit 1: Representation and performance

## 1.1 Binary Arithmetic

**Core model — Binary Arithmetic**

Positional binary represents a nonnegative integer as a weighted sum of powers of two. Two's complement represents signed integers in a fixed bit width using the top bit's negative weight.

**Original worked illustration**

The 8-bit pattern 11111101 represents -3 in two's complement because its unsigned value is 253 and 253-256=-3.

**Boundary conditions and checks**

Overflow is a width-dependent phenomenon: computing 127+1 in signed 8-bit arithmetic wraps to -128 at the bit level, not mathematical integer 128.

### Extended technical chapter: Binary Arithmetic

A numeral is not an integer until an interpretation rule and a width have been supplied. Consider 1111: it denotes fifteen as an unsigned four-bit word but negative one as a signed four-bit two's-complement word. An engineer documenting an interface must therefore specify width, byte order, signedness, and overflow convention. These details are not decoration. They determine which physical bit patterns correspond to which mathematical objects. For a w-bit unsigned number, the representation maps the integers zero through 2^w−1 to binary strings. Under two's complement, the same strings represent integers from −2^(w−1) through 2^(w−1)−1. Addition performed by a w-bit datapath naturally computes residues modulo 2^w; whether overflow is an error depends on the surrounding program's contract. A signed comparison is different from an unsigned comparison even though the inputs are identical wires.

A conversion trace should keep mathematical value, bit pattern, and interpretation separate. Start with −13 in an eight-bit register. The residue is 256−13=243, which is 11110011. Reading 11110011 unsigned gives 243; reading it signed gives −13. Negating −13 can be implemented by bit inversion followed by addition of one: 00001101 invert to 11110010, then add one. That recipe is useful only after the width is known. A hypothetical machine with a nine-bit word produces a different pattern for −13. To check the conversion, assign bit seven weight −128 and sum the positive contributions of bits six through zero: −128+64+32+16+2+1=−13. This second route independently verifies the result rather than merely repeating the algorithm.

Some architectures report a carry flag and a signed-overflow flag. They are different. In eight-bit unsigned arithmetic, 250+10 produces a low byte of four and a carry-out. In eight-bit signed arithmetic, 120+20 produces the low byte 140, interpreted as −116; the mathematical result 140 is not representable and signed overflow occurred. A carry-out need not signal signed overflow, and a signed overflow need not produce the carry interpretation a novice expects. For the lab, create an eight-bit addition table with the operands, unbounded sum, low byte, carry-out, signed operands, signed result, and overflow flag. Include pairs near both signed boundaries, not just ordinary positive inputs. Avoid inferring processor instruction behavior from a language whose signed-overflow semantics may differ from modular hardware addition.

## 1.2 Instruction Costs

**Core model — Instruction Costs**

Instruction cost depends on instruction count, average cycles per instruction and clock period; these factors interact under compiler optimizations.

**Original worked illustration**

If a program executes 2 billion instructions at CPI 1.5 on a 3 GHz clock, CPU time = 2e9*1.5/(3e9)=1 second.

**Boundary conditions and checks**

Instruction count is not interchangeable with lines of code; wall time also includes I/O, scheduling and stalls outside simplified CPU models.

### Extended technical chapter: Instruction Costs

The familiar execution-time identity CPU time = instruction count × cycles per instruction × cycle time is an accounting decomposition. It does not declare that CPI is a constant of the instruction set or that instructions are all equally expensive. A measured program contains an instruction mix; multiply the number of instructions in each class by its effective cycles per instruction to estimate total cycles. For instance, a simplified processor running 600 million integer operations at one cycle, 200 million loads at two cycles, and 100 million branches at three cycles consumes 600+400+300=1300 million cycles. At two gigahertz, the model predicts 0.65 seconds of CPU time. The average CPI is 1.3 billion divided by 900 million, or about 1.444. If cache misses delay some loads, the load-class CPI changes, and that change must be included rather than hidden under frequency.

Optimization can reduce instruction count while worsening per-instruction cost. Suppose a compiler replaces a simple loop with vector instructions: dynamic count falls from 800 million to 400 million, but the measured effective CPI rises from one to 1.5 due to serialization and port contention. At an unchanged two-gigahertz frequency the first version takes 0.4 seconds and the second 0.3 seconds, so it is faster despite a higher CPI. If effective CPI instead rises to 2.2, the new version takes 0.44 seconds and loses. A useful investigation therefore measures instructions, cycles, stalls, and elapsed time together. Profiling tools also distinguish user mode, kernel mode, and waiting, so CPU time should not be confused with end-to-end response latency.

An instruction count obtained from static source inspection is generally the wrong quantity. Branches, loop trip counts, library calls, vectorization, and cache-sensitive control paths determine dynamic execution. Before comparing two machines, hold the input workload fixed, identify compiler options and instruction-set features, and make clear whether results include startup, system calls, or data transfer. A student laboratory can estimate dynamic instruction mix from a small trace and then compute three scenarios: a baseline mix, a load latency penalty, and a compiler transformation. A sound conclusion names the scenario, the assumptions behind the effective CPI, and at least one unmeasured factor that could reverse the ranking.

## 1.3 Benchmarking

**Core model — Benchmarking**

Benchmarking requires representative inputs, repetitions, warm-up and controlled measurement. A speed ratio should state both hardware and workload.

**Original worked illustration**

A routine taking 4 ms versus 10 ms on the same input has measured speedup 10/4=2.5; the absolute time saving is 6 ms.

**Boundary conditions and checks**

Single short timings are noisy, and averaging ratios across workloads without weights can distort conclusions; use appropriate aggregation.

### Extended technical chapter: Benchmarking

Benchmarking starts by defining the quantity of interest. Throughput measures how many jobs a system completes per unit time, while latency measures how long one job takes. A database accelerator can improve operations per second and simultaneously worsen individual tail latency under queuing. A CPU microbenchmark might instead report cycles per operation, instructions retired, memory bandwidth, or energy per query. The choice must match the decision: a web service facing users with strict timeouts should not be selected solely by mean throughput. Measurements taken on different input sizes or software configurations do not answer the same question.

Short-running benchmarks are vulnerable to clock drift, dynamic frequency scaling, page faults, filesystem caches, JIT warm-up, and scheduler interruptions. A defensible protocol records hardware, operating system, compiler, input distribution, run order, ambient conditions when relevant, sample count, and a clear summary statistic. Suppose a baseline operation reports 5.0, 5.1, 5.2, 5.1, and 5.0 milliseconds, while the candidate reports 4.7, 4.8, 4.9, 4.8, and 7.4 milliseconds. The candidate's best runs are faster but its outlier changes the mean substantially. Reporting only the minimum would conceal a potential tail-latency regression; reporting only the maximum would also be misleading. Repeat tests and inspect distributions before drawing a conclusion.

For performance ratios across workloads, compute per-workload speedups consistently as baseline time divided by candidate time. If the benchmarks are equally weighted and multiplicative changes matter, the geometric mean is often more interpretable than an arithmetic average of the speedups. But equal weighting is an editorial choice, not a universal law: representative production traffic might demand weights proportional to actual workload frequencies. Work through a case in which two jobs receive 90% and 10% of traffic, and observe how an improvement in the rare job can obscure regression in the common one if the aggregate weights are wrong. The laboratory report should separate measured evidence, confidence in repeatability, and extrapolation beyond the test environment.

## 1.4 Performance Equations

**Core model — Performance Equations**

The CPU-time equation exposes tradeoffs: runtime = instructions * cycles per instruction * seconds per cycle. A higher clock rate can lose if CPI grows substantially.

**Original worked illustration**

Processor A uses 1e9 instructions, CPI 2, 2 GHz and takes 1 second. B uses same count, CPI 1.5, 1 GHz and takes 1.5 seconds.

**Boundary conditions and checks**

Frequency alone does not measure performance; compare completed work under comparable resource and energy constraints.

### Extended technical chapter: Performance Equations

Amdahl's law describes a fixed workload containing a serial fraction s and a parallelizable fraction 1−s. With p workers, idealized speedup is 1/[s+(1−s)/p]. The formula is a bound under its assumptions, not a prediction of a real multicore system. If 15 percent is serial, infinitely many workers cannot deliver speedup greater than 1/0.15, approximately 6.67. With eight workers the idealized speedup is 1/[0.15+0.85/8], about 3.90. Adding workers beyond eight still helps but yields progressively smaller incremental gains. Communication, synchronization, scheduling, and memory bandwidth generally make the real outcome worse.

Performance can also be decomposed in a way that identifies optimization leverage. In a program using total time T, speeding up a fraction f by factor k changes total time to T[(1−f)+f/k]. A routine that consumes 10 percent of time cannot cut whole-program latency by half regardless of its local improvement. If that routine becomes 20 times faster, the total speedup is 1/(0.9+0.1/20), about 1.105. This explains why an impressive isolated kernel speedup can have little value to the application. Conversely, a modest improvement to the dominant workload can deliver large practical benefits.

Check the denominator before comparing formulas. Instructions × CPI / frequency estimates CPU execution time for a specified instruction stream; Amdahl's law estimates the effect of accelerating a fraction of a workload. They answer different questions. Real systems may be constrained by I/O, memory capacity, concurrency, power budgets, or service-level objectives. A performance worksheet should name the baseline metric, a proposed change, the fraction affected, and the fraction untouched. If the model assumes perfect scaling, challenge it with a plausible overhead term and recompute. When the conclusion depends strongly on the overhead, the next step is measurement rather than confident projection.

### Integrated laboratory: evaluating two fictional processors

A research team wants to choose a processing platform for a fixed batch of numerical jobs. The first temptation is to compare clock frequencies: machine A advertises three gigahertz and machine B two gigahertz. That comparison omits instruction count and CPI. Assume the same compiled workload on A executes 1.2 billion instructions at an observed average CPI of 1.8. Its modeled CPU time is 1.2 billion × 1.8 / 3 billion = 0.72 seconds. On B, a different compiler build executes 0.9 billion instructions at CPI 1.4 on a two-gigahertz clock. Its CPU time is 0.63 seconds, making B faster despite the lower frequency. The calculation depends on actual per-workload counts; nothing about the advertised frequency alone settles the choice.

The team checks whether these CPU-time figures also describe total service latency. Suppose each job spends 0.25 seconds waiting for a network response that cannot be overlapped with computation. The modeled response times are 0.97 and 0.88 seconds. B still wins on this particular job, but the relative difference has shrunk. If the network component varies unpredictably between runs, observed end-to-end results may have substantial variance. To avoid conflating causes, benchmark CPU-intensive stages separately while also measuring the complete transaction. The report should include both metrics, since a business selecting a machine may care about service time rather than isolated CPU cycles.

Now test whether signed arithmetic behaves as the program expects. An eight-bit sensor value arrives as hexadecimal F3. Treating it as unsigned produces 243; treating it as signed two's complement produces negative thirteen. If one machine's input-conversion layer interprets signedness differently, the processors are no longer running equivalent computations, so any timing comparison is invalid until the semantic defect is corrected. A benchmark is useful only if the same input produces acceptable results. Include a set of boundary cases with 0x00, 0x7F, 0x80 and 0xFF. State explicitly whether saturation, wraparound, exceptions or wider intermediates are required by the application.

A more detailed instruction mix can explain why machine B's CPI is lower. On machine A suppose half of all dynamic instructions are simple arithmetic averaging one cycle, 30 percent are loads averaging two cycles, and 20 percent are control operations averaging 3.5 cycles. Its weighted CPI is 0.5×1+0.3×2+0.2×3.5 = 1.8. Machine B might retire a different mix with fewer slow operations. This accounting is a model of an observed average, not a promise of additivity in a superscalar core; overlap and stalls are already folded into the effective CPI values. Double counting a stall both in class cost and in a separate stall term would distort the estimate.

The team also questions a claim that one optimized routine is six times faster. If the routine consumed only five percent of baseline time, the maximum whole-program speedup under Amdahl's fixed-workload model is 1/(0.95+0.05/6), about 1.043. This remains a useful improvement at scale, but it cannot justify a statement that the entire application is six times faster. Optimization decisions should begin with measurements of time fractions. The costs of changing compiler options, maintaining architecture-specific code and verifying numeric equivalence belong in the engineering recommendation, not in a footnote.

For the reproducible notebook, record four layers of evidence. First, specify executable input and expected mathematical output. Second, collect cycle and instruction counters with their sampling limitations. Third, repeat elapsed-time observations after warm-up and report median and spread. Fourth, evaluate power or energy if the intended deployment cares about operating cost. A final table should state which conclusions survive changing the workload distribution, which are sensitive to unmeasured I/O, and which remain only hypothetical. That is a stronger architecture analysis than declaring the largest clock number the winner.

### Review lens: reproducibility and hidden confounders

If machine A finishes one benchmark run faster than machine B, the observation is still conditional on that run's input, compilation, operating temperature and measurement method. CPU frequencies can vary during a test; a power-constrained device may deliver short bursts that it cannot sustain. Benchmark repetition detects some variability but does not automatically remove systematic bias, such as testing A after its cache is warm and B after a reboot. Randomizing run order and defining warm-up is more persuasive than collecting many identically biased samples. Compare a throughput workload with a latency-sensitive one to discover whether the ranking changes. State whether a result is based on elapsed time, CPU counters or estimated cycle counts, since the same numerical unit can conceal a different measurement procedure. A careful researcher also checks that no overflow, dropped work or different numeric precision makes one implementation appear faster by doing less correct work.

### Additional guided investigations for representation and speed

**Bit-level investigation.** Encode negative twenty-one into an eight-bit register. Its unsigned residue is 256−21=235, so the pattern is 11101011. Verify using negative top-bit weight: −128+64+32+8+2+1=−21. Then add +30; the low-byte result represents +9. Under signed interpretation no overflow occurs. Ask what changes if the operands are treated as unsigned; the raw bit operation is the same, but the mathematical descriptions differ. Repeat with −120+−20 and discover a signed overflow because −140 lies below the representable minimum.

**Instruction-mix investigation.** Construct a workload with four hundred million arithmetic operations averaging one cycle each, two hundred million loads averaging three cycles each, and one hundred million branches averaging two cycles each. Total cycles are 0.4+0.6+0.2=1.2 billion, and total instructions are seven hundred million. The average effective CPI is approximately 1.714. At two gigahertz the predicted CPU time is 0.6 seconds. Change the load-class CPI from three to four and obtain 0.7 seconds. This models sensitivity to memory stalls while acknowledging that a real CPI breakdown may not be independent because of overlap.

**Benchmarking investigation.** Compare five paired observations rather than two unrelated averages. If the baseline times are [10,11,9,10,10] milliseconds and the candidate times are [8,8,8,9,8] milliseconds, compute per-pair absolute differences and check whether every pair favors the candidate. Record ambient conditions and verify equal work. Then introduce one candidate run at twenty milliseconds and explain why median and tail observations convey different information. Do not discard a slow observation without a documented cause.

**System-level investigation.** If a CPU stage accounts for forty percent of total request latency and receives a factor-of-two acceleration, normalized end-to-end time becomes 0.6+0.4/2=0.8. The best modeled speedup is 1.25. Now suppose an added data conversion stage costs 0.1 of the former total time: net normalized time becomes 0.9 and speedup only about 1.111. The calculation shows why a change that wins a CPU benchmark may disappoint at application level.

### Diagnostic challenge: distinguish clocks from delivered work

Two hypothetical processors both run at 2.5 GHz. The first executes 600 million instructions at CPI 1.25, consuming 750 million cycles or 0.30 seconds. The second executes 500 million instructions at CPI 1.8, consuming 900 million cycles or 0.36 seconds. A shorter instruction stream therefore loses because its observed average cycle cost is larger. To make this an honest diagnostic, test both implementations for the same mathematical output, then verify that the instruction counts and CPI measurements come from compatible profiler definitions. An out-of-order processor can overlap independent operations, so effective CPI is an aggregate counter relation, not the intrinsic cost of each instruction. If the second processor uses lower power, it may still have lower energy per job; compare watts multiplied by duration. Students should submit a table with dynamic instructions, cycles, frequency, CPU time, energy and at least one unmeasured uncertainty. If a benchmark conclusion changes when realistic input sizes are substituted, prefer a workload distribution over a single convenient example.

## Three worked problems

### Binary Arithmetic: worked application 1

Interpret 11111101 as signed 8-bit two's complement.

**Set up the model and conditions**

Its most significant bit is one, so the value is negative.

**Carry out the calculation or proof**

Unsigned value is 253; subtract 2^8=256.

**State the result and its scope**

The signed value is -3.

**Independent verification, conditions, and interpretation**

Eight-bit two's-complement representation has a negative weight for its most significant bit. The pattern 11111101 has bit seven equal to one, so its value is −128+64+32+16+8+4+0+1=−3. An independent conversion converts the same bits to unsigned 253 and subtracts 256 because the sign bit is set. Both routes yield negative three. Another independent check writes +3 as 00000011, flips the eight bits to 11111100, adds one to obtain 11111101, and confirms that negating the result restores +3 modulo 256. The distinction is crucial: when a program reads the same raw byte as unsigned, it obtains 253, not −3. Its binary representation has not changed; the interpretation has. For the range check, the smallest eight-bit signed integer is −128 and the largest is +127. The pattern 10000000 therefore denotes −128 and cannot be negated into +128 within eight signed bits. If a conversion or negation routine uses wider intermediates, document the width at each operation. This question tests the interpretation contract as much as the arithmetic.

### Instruction Costs: worked application 2

A program executes 2e9 instructions at CPI 1.5 and clock 3 GHz. Compute CPU time.

**Set up the model and conditions**

Total cycles = instruction count × CPI = 3e9 cycles.

**Carry out the calculation or proof**

CPU seconds = 3e9 / 3e9 cycles per second.

**State the result and its scope**

CPU time is 1 second.

**Independent verification, conditions, and interpretation**

The CPU-time identity requires consistent dimensions. The instruction count is 2×10^9 instructions and CPI is 1.5 cycles per instruction; multiplication gives 3×10^9 cycles. Frequency of 3 GHz means 3×10^9 clock cycles per second. Dividing yields one second of modeled CPU time. The dimensional cancellation instructions × (cycles/instruction) × (seconds/cycle) is an additional sanity check. If CPI rises to 2 without changing frequency or instruction count, the result becomes 4/3 seconds; if frequency instead doubles at unchanged CPI, the model gives half a second. Neither modification asserts anything about total wall-clock time, which can include I/O waits, blocked tasks and competing processes. To compare different compiler builds, remeasure the dynamic instruction count rather than assuming it is fixed. To compare processors, be cautious about effective CPI: a superscalar implementation can retire multiple instructions per cycle, while stalls may raise the measured average. The calculation is an accounting result under stated inputs, not a direct prediction of a system's observed response latency.

### Benchmarking: worked application 3

Processor A takes 4 ms, B takes 10 ms on identical work. What is A's speedup relative to B?

**Set up the model and conditions**

Define speedup as old time divided by new time.

**Carry out the calculation or proof**

Compute 10/4=2.5; saved time is 6 ms.

**State the result and its scope**

A is 2.5 times faster for that workload.

**Independent verification, conditions, and interpretation**

Speedup compares time required for equal completed work. Taking B as the baseline and A as the candidate, speedup is T_B/T_A = 10 milliseconds/4 milliseconds = 2.5. The unit cancels, so the ratio is dimensionless. The absolute saving is six milliseconds per completed operation, while percentage time reduction relative to B is 6/10 = sixty percent. A claim of 150 percent faster is ambiguous because it uses a different interpretation of percentages; state the ratio or elapsed-time reduction instead. If throughput is inversely proportional to operation time and requests are run serially with no extra overhead, A could complete 250 operations per second and B 100 operations per second. That throughput conclusion does not automatically hold with batching, pipelining or concurrency, where total system capacity has other constraints. Repeat the workload across different input sizes and distributions; a quick algorithm might not dominate a slow one at all scales. The reference measurements should exclude unrelated initialization or include it consistently. Benchmark comparisons are credible when the work, result correctness and timing boundaries are matched.
