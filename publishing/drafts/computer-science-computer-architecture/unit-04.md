# Computer Architecture — Unit 4: Pipelining

## 4.1 Stage Design

**Core model — Stage Design**

Pipeline stages partition work to allow several instructions in flight. The ideal throughput approaches one completed instruction per cycle after fill, but latency need not shrink.

**Original worked illustration**

For a 5-stage pipeline processing 10 independent instructions with one-cycle stages, the ideal duration is 5+10-1=14 cycles rather than 50 unpipelined stage cycles.

**Boundary conditions and checks**

Unequal stage times, register overhead and memory stalls limit ideal speedup; never compare unequal clock periods without adjustment.

### Extended technical chapter: Stage Design

Pipeline partitioning attempts to overlap different instructions in different phases of their execution. A five-stage instruction pipeline often uses fetch, decode, execute, memory access, and writeback. If each stage requires one clock interval and there are no stalls, processing n instructions takes n+4 cycles once the pipeline begins empty; a non-pipelined design requiring five cycles per instruction takes 5n cycles. For twenty instructions this simplified comparison is 24 versus 100 cycles, a speedup of about 4.17, not exactly five. The startup and drain overhead make the difference particularly large for short traces.

Pipelining improves potential throughput but need not reduce the latency of a single instruction. A pipeline register contributes setup, hold and clock overhead, and the slowest stage limits the clock period. Splitting a combinational path into more stages can raise clock frequency, but it also creates more pipeline-register power, more instructions in flight, and greater penalties when control flow is mispredicted. If five stage delays are 200, 350, 250, 300 and 250 picoseconds, the clock cannot be shorter than the 350-picosecond stage plus register overhead under the simple synchronous model. Repartitioning work so the longest stage is nearer the average may help, but data dependencies and physical routing limit arbitrary splitting.

A robust pipeline experiment separates latency, cycle count and throughput. Start with an ideal instruction stream, then insert dependencies, branch redirections, or variable-latency memory accesses. Explain where bubbles enter the stage diagram and what work is actually wasted. For a pipeline with stages of unequal delay, compare throughput before and after balancing them, including the cost of additional registers. Avoid promising that 'more stages equals more speed': the optimum depends on branch behavior, clock overhead, energy limits and workload characteristics. The useful output is a labeled timing diagram plus a numerical accounting of active cycles, fill, stalls, and drain.

## 4.2 Hazards

**Core model — Hazards**

Data, structural and control hazards prevent the next operation from using required resources or values. A RAW dependency is a true data hazard.

**Original worked illustration**

Instruction I1 writes r3 and I2 immediately reads r3. Without forwarding, I2 may have to wait for I1's writeback.

**Boundary conditions and checks**

WAR and WAW hazards require attention in out-of-order execution but are not the same as a simple in-order RAW stall.

### Extended technical chapter: Hazards

A pipeline hazard is a situation in which overlapping instruction execution would violate a dependency or a shared-resource limit unless the implementation takes corrective action. Structural hazards arise when multiple operations need the same hardware resource in a cycle. Data hazards concern dependencies between instructions, especially a later read of a value produced by an earlier instruction. Control hazards arise when the next instruction address is uncertain because of a branch or other redirection. The remedy may be stalling, forwarding, resource duplication, renaming, speculation or a combination.

Consider ADD r1,r2,r3 followed immediately by SUB r4,r1,r5. The second instruction has a true read-after-write dependency on r1. If the ADD result is not yet available to the SUB at its execute stage, using an old register value would be incorrect. The number of required stall cycles depends on the stage timing and bypass paths; there is no universal stall penalty for such a pair. A load-use pair is different: a load may not produce its data until after a memory stage, so forwarding available for ALU-to-ALU dependencies may not remove every load-use stall. Draw the cycles, do not guess.

False name dependencies matter in out-of-order machines. A write-after-read or write-after-write relationship involving the same architectural register name can restrict scheduling even when the underlying computed values are independent. Register renaming removes those name constraints by assigning different physical destinations, while preserving true data dependencies. When analyzing a trace, list each dependency with producer instruction, consumer instruction, register or memory location, dependency class, and earliest permissible execution cycle. For memory operations, aliasing uncertainty complicates dependence analysis. A load and store using unknown addresses may require ordering or speculation with recovery. A correctness argument must account for both precise results and the machine's memory consistency contract.

## 4.3 Forwarding

**Core model — Forwarding**

Forwarding bypasses a just-produced result to a dependent instruction rather than waiting for its register-file writeback. Some dependencies remain inherently delayed.

**Original worked illustration**

An ALU result may be forwarded from an execute stage to the next instruction's execute input. A load-use dependency may still stall because memory data arrives later.

**Boundary conditions and checks**

Forwarding must select the most recent producer; otherwise two writes to the same register can route an outdated value.

### Extended technical chapter: Forwarding

Forwarding, or bypassing, routes a newly computed result from a pipeline stage directly to a dependent instruction instead of waiting for architectural register writeback. In a classic five-stage integer pipeline, an ALU operation may have its result available at the end of the execute stage. A following ALU instruction can often receive that value through an EX-to-EX bypass network. The control logic must compare source register indices to destination indices of older operations while checking whether those operations really produce register values. A bypass based only on matching register numbers may feed garbage from a store or a suppressed write.

A forwarding network is often explained with a short precedence rule: if the nearest older instruction is writing the required operand, select its result; otherwise test a more distant pipeline stage; otherwise read the register file. The 'nearest' qualification matters when two older instructions write the same register. Suppose ADD r1,... is followed by XOR r1,... and then OR r4,r1,r5. The OR must consume the XOR result, not the older ADD result. Forwarding selection is therefore a dataflow decision with priority, not merely a collection of available wires. The forwarding muxes themselves add delay, area and power to the processor datapath.

Bypassing cannot make unavailable data arrive early. A load whose cache result appears at the end of the memory stage may still force a dependent execute stage to wait. Long-latency multiplication, division or cache miss events require an interlock, reservation stations, or other scheduling machinery. A laboratory timing diagram should include a chain of ALU operations, a load-use dependency, and two consecutive writes to one destination register. Mark for each consumer whether its operand comes from the register file, a bypass, or a later cycle after a stall. Confirm final architectural results against a sequential reference interpreter so that an apparently fast schedule is not accepted when it computes the wrong program.

## 4.4 Branch Prediction

**Core model — Branch Prediction**

Branch prediction guesses control direction so instruction fetch can continue. Accuracy matters alongside penalty and branch frequency.

**Original worked illustration**

If 20% of instructions are branches, 5% of branches are mispredicted, and each miss costs 10 cycles, the expected penalty is 0.2*0.05*10=0.1 cycles per instruction.

**Boundary conditions and checks**

A predictor's reported accuracy on one trace does not establish robustness on changed workloads or security isolation across processes.

### Extended technical chapter: Branch Prediction

Branch prediction allows an instruction pipeline to fetch and often execute instructions along a guessed control-flow path before the branch outcome is known. A simple static predictor might predict that every branch is not taken. A one-bit dynamic predictor remembers the last observed outcome, while a two-bit saturating counter requires stronger evidence before reversing its preferred direction. These small mechanisms illustrate a fundamental tradeoff: better predictions reduce wasted work but prediction logic consumes hardware resources and can introduce new performance and security considerations.

For a repeated loop branch with outcomes T,T,T,T,N, a one-bit last-outcome predictor initially set to N is wrong on the first T and last N. A two-bit predictor can behave differently depending on its initial state and update policy, so a simulation must specify both. If 20 percent of executed instructions are branches, 10 percent of those are mispredicted, and each miss wastes four cycles, a simple additive model predicts 0.2×0.1×4=0.08 extra cycles per instruction. With an ideal base CPI of one, the estimated CPI is 1.08. This is only the isolated branch contribution; cache stalls and overlap can alter real measurements.

Prediction accuracy is not the only useful metric. An indirect branch target predictor must identify the destination; return-address stacks help predict returns; a branch target buffer can provide likely target addresses without waiting for execution. Deep speculative pipelines face larger recovery costs, while sophisticated predictors can leak information through microarchitectural state. Use a fixed sequence of outcomes to compare static, one-bit and two-bit predictors. Show every state transition and count mistakes. Then alter the pattern to demonstrate why a predictor that excels on stable loops might perform poorly on alternating data-dependent branches. Distinguish an educational predictor model from production processors' complex proprietary mechanisms.

### Integrated laboratory: cycle-by-cycle trace of a five-stage pipeline

Use a simplified five-stage pipeline with IF, ID, EX, MEM and WB, one instruction entering the pipeline per cycle when no stall occurs. For n=12 independent instructions, the ideal completion count is n+4=16 cycles if a single cycle has equal stage periods and no other penalties. A corresponding non-overlapped execution taking five cycles per instruction would use sixty cycles. Both numbers are for the constructed model; a production CPU may execute multiple instructions per cycle, have different stage costs, or have out-of-order scheduling. The exercise's advantage is not realism at every detail but a precise baseline that makes each additional stall visible.

Begin with ADD r1,r2,r3 followed by XOR r4,r1,r5. If a bypass from the first instruction's execute result to the second instruction's execute input exists, the dependency can often be resolved without an extra bubble in this teaching pipeline. Remove that bypass: the second instruction must wait until the register write is available under the specified timing convention. Mark occupied and empty slots in a stage diagram for cycles one through eight, then count the difference. The diagram should identify the actual value forwarded, not merely an arrow labeled 'data.' A bypassing implementation that forwards an older overwritten value fails even when it avoids a stall.

Replace the first ADD with LOAD r1,[r2]. In a common five-stage organization, loaded data appears after the memory stage, later than an ALU result. A directly dependent operation may require one bubble despite EX-to-EX forwarding. The exact number of bubbles depends on whether memory is one cycle, where the data is sampled, and what bypasses exist. Add a cache miss of ten extra cycles: now several younger instructions may be blocked or held, and the trace must specify whether independent instructions can proceed elsewhere. The correct performance interpretation depends on the implementation's scheduling policy, not just the mnemonic LOAD.

Introduce a conditional branch resolved during EX. Let a predictor assume not taken, and suppose the branch is actually taken. Instructions already fetched along the wrong path must be discarded or prevented from retiring. If two wrong-path instructions occupy earlier stages, a simple model may charge two cycles of recovery; a different branch-resolution stage produces a different penalty. Build a second trace in which prediction is correct, and distinguish predictor accuracy from total cycle cost. Repeated loop outcomes T,T,T,T,N can produce different misprediction counts for static and two-bit predictors. Write out predictor state transitions before assuming a particular figure.

Pipeline balancing affects clock time separately from cycle count. Suppose nominal stage logic delays are [240, 350, 250, 270, 260] picoseconds and pipeline-register overhead is thirty picoseconds. Under a simplified single-clock design, the clock must be at least 380 picoseconds. Redistributing logic to reduce the longest stage to 300 picoseconds might permit a 330-picosecond clock, but the number of stalls may not change. For an instruction stream completing in one thousand cycles, the cycle time adjustment reduces modeled elapsed time from 380 to 330 nanoseconds. Additional register and routing cost could make the redesign unattractive for a small device.

Finally assemble a cycle-accounting sheet. Begin with n+4 ideal cycles, add data-hazard bubbles, branch recovery cycles and any non-overlapped memory penalties, and subtract nothing without justification. Some penalties may overlap, so blind summation can overestimate real cost. Specify a simple no-overlap assumption if using additive arithmetic. Compare against a sequential architectural reference to ensure all committed register values and memory writes are correct. A faster incorrect pipeline is not a successful implementation. Include one deliberately wrong forwarded-register priority rule and show the exact counterexample that detects it.

### Review lens: bubbles as a symptom, not a diagnosis

Counting pipeline stalls is useful only after labeling their causes. A one-cycle bubble after a load-use dependency has a different remedy from a branch misprediction, structural port conflict or cache miss. Forwarding helps with available computed operands, not with data still in memory. Deeper prediction helps some control hazards, not a saturated memory interface. A performance report should partition cycles into useful work, fill/drain, dependency stalls, branch recovery, resource conflicts and memory delays where mutually exclusive categories can be defined. On sophisticated cores, categories can overlap; simplistic summation may overcount. Carefully state whether measurements came from a deterministic teaching simulator or from hardware event counters with documented limitations. The goal is to select an intervention aligned with the dominant measured cause, rather than treating all wasted cycles as interchangeable.

### Additional guided investigations for pipeline correctness

**Pipeline timing.** Create a five-stage diagram for four independent instructions. The first enters IF in cycle one and completes WB in cycle five; the fourth enters IF in cycle four and completes WB in cycle eight. Thus four instructions finish in 4+4=8 ideal cycles. Add a single one-cycle bubble before the third instruction, and under the simple non-overlap model total completion becomes nine cycles. Annotate where that bubble travels; a bare 'extra cycle' claim lacks the causal information needed to design forwarding.

**Dependency testing.** Set initial r1=99, r2=6, r3=7 and r5=2. The sequence ADD r1,r2,r3 then SUB r4,r1,r5 must finish with r1=13 and r4=11. A pipeline that reads the old r1 computes 97 for r4 and is incorrect. Test the implementation with bypass enabled, bypass disabled with stalling, and bypass miswired to another register. Inspect the first cycle when the source operand is consumed, not only the final counter values.

**Forwarding priority.** Place two consecutive writers to r1 before a consumer. The older writes three, the younger writes nine; a following OR r4,r1,r5 must use nine. Two available bypass paths cannot simply be ORed or selected arbitrarily. The priority logic should use the nearest older architecturally valid producer. Test a load producer where the data is not yet ready, demonstrating why forwarding must defer or stall instead of fabricating an operand.

**Prediction accounting.** A trace of one thousand instructions contains two hundred branches. If ten are mispredicted and each adds five non-overlapped recovery cycles, branch recovery costs fifty cycles and contributes 0.05 extra CPI. Compare this with a case where the same predictor accuracy produces ten-cycle recovery, doubling the contribution. Then explicitly distinguish those model parameters from the sequence of actual taken and not-taken outcomes, which determines whether one-bit or two-bit state machines produce ten mispredictions.

### Diagnostic challenge: separate stage time and stall count

Processor A completes a pipeline trace in 1200 cycles at a 400-picosecond clock, giving 480 nanoseconds. Processor B uses additional pipeline stages and completes the same architectural program in 1450 cycles at 300 picoseconds, giving 435 nanoseconds. B wins despite requiring more cycles. If B suffers an additional 200 cycles of branch recovery on a harder input, its time becomes 495 nanoseconds and A would win if its own cycle count remains unchanged. The comparison proves that shorter clock period and fewer stalls cannot be considered independently. A fair experiment varies branch outcome distributions and dependency patterns while preserving program correctness, calculates time from cycles × cycle period, and reports both stage design assumptions and hazard behavior. The same stage split can be attractive for long streaming loops yet disappointing for short control-heavy routines. Students should distinguish static pipeline depth from the dynamic number of bubbles observed for a particular workload.

## Three worked problems

### Stage Design: worked application 1

For a five-stage ideal pipeline and ten instructions, calculate cycles to completion.

**Set up the model and conditions**

The first instruction finishes after five cycles.

**Carry out the calculation or proof**

Each subsequent independent instruction finishes one cycle later.

**State the result and its scope**

Total is 5+(10−1)=14 cycles, assuming equal one-cycle stages and no hazards.

**Independent verification, conditions, and interpretation**

An ideal five-stage pipeline enters one independent instruction in each cycle, provided all stages have the same cycle duration and no hazards or stalls occur. The first instruction takes five cycles from initial fetch to completion. The next nine instructions enter on successive cycles, so the tenth finishes four stages after its fetch in cycle ten, at cycle fourteen. Algebraically, cycle count = k+(n−1) = 5+9 = 14. Another route counts pipeline fill overhead k−1=4 and one completed instruction per cycle for n=10, giving n+4=14. By comparison, a non-overlapping implementation requiring five cycles per instruction uses fifty cycles, so the idealized cycle speedup is 50/14 ≈ 3.57. The result is less than five because pipeline filling and draining matter when n is small. The model says nothing about actual clock period. If pipeline registers increase cycle time, the runtime ratio differs from the cycle-count ratio. Add a stall of two cycles after a dependency, and the completion count becomes sixteen under the simple additive non-overlap model. The student's timing diagram should show fetch, decode, execute, memory and writeback occupancy rather than assuming every mnemonic has equal work.

### Hazards: worked application 2

Explain the hazard for ADD r1,r2,r3 followed immediately by SUB r4,r1,r5.

**Set up the model and conditions**

The first instruction produces r1; the second consumes it.

**Carry out the calculation or proof**

This is a true read-after-write dependency on r1.

**State the result and its scope**

Forwarding or a stall is needed if the produced value is not yet visible.

**Independent verification, conditions, and interpretation**

The ADD produces a new value for architectural register r1, and the immediately following SUB needs that value as one of its source operands. This is a true read-after-write dependency. A sequential interpreter naturally executes ADD before SUB, but in a pipeline the SUB might reach operand consumption before ADD has completed register writeback. Using the old r1 would violate program semantics. A forwarding path may carry ADD's ALU result directly into SUB's execute input when the timing aligns, avoiding a bubble. Without a suitable bypass, the interlock must stall SUB until the correct value is available. The required stall count cannot be determined from the instruction names alone; it depends on stage boundaries, read/write timing and existing bypass networks. A correct hazard detector checks producer write-enable and destination index alongside consumer source indices. It must also handle destination zero registers appropriately where specified. Build a counterexample by setting old r1=100, r2=7, r3=8, r5=2: correct ADD yields fifteen and SUB yields thirteen, whereas an unprotected early read of old r1 would yield ninety-eight. The final state provides a concrete correctness oracle.

### Forwarding: worked application 3

A branch frequency of 20%, misprediction rate 5%, and penalty 10 cycles: find extra CPI.

**Set up the model and conditions**

Probability of a mispredicted branch per instruction is 0.2×0.05=0.01.

**Carry out the calculation or proof**

Multiply by ten cycles per miss.

**State the result and its scope**

Extra CPI is 0.1 under the simplified additive model.

**Independent verification, conditions, and interpretation**

Branch contribution to CPI is approximated as branches per instruction × wrong predictions per branch × wasted cycles per wrong prediction. Substituting 0.20 × 0.05 × 10 gives 0.10 cycles per instruction. If ideal base CPI is one and penalties do not overlap, predicted CPI is 1.10. For one million instructions, the simple model expects 200,000 branches, 10,000 mispredictions and 100,000 wasted cycles. Each route independently recovers the same extra CPI. This does not mean every branch incurs ten cycles; only the mispredicted five percent do under the assumptions. The predictor's initial state and actual outcome sequence may cause variation for a short program. Also, ten-cycle recovery is architecture-specific, and actual overlap with cache misses or other stalls can make simple penalty addition inaccurate. Changing the misprediction rate to two percent while holding other assumptions fixed reduces the contribution to 0.04 CPI. That sensitivity analysis indicates which measurement would be most valuable for evaluating a proposed predictor change.
