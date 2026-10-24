# Unit 6: Optimization

*Draft; not approved for public deployment. Eight-unit manuscript with source-specific cases and independent verification pending.*

## Dataflow Analysis
**Dataflow Analysis: conceptual explanation**

Classical dataflow analysis turns control-flow into equations. For reaching definitions, each block B has GEN[B] definitions created inside the block and KILL[B] definitions overwritten by it. A common forward may-analysis uses OUT[B]=GEN[B] union (IN[B] minus KILL[B]), and IN[B] is the union of predecessors' OUT sets. Repeatedly update sets until a fixed point is reached. Termination follows on a finite-height lattice with monotone transfer functions; one execution of the loop is not generally enough. Liveness is a backward analysis: a value is live before an instruction if its current value might be used later along some path.

Explain why union and intersection matter. A may-analysis asks whether a property can occur on at least one path and commonly uses union at joins; a must-analysis asks whether it holds on all paths and often uses intersection. The initial boundary values and lattice ordering are part of the mathematical problem. A mistaken join operator can cause an optimizer to delete an assignment needed only along a rare path. Build a diamond CFG where one branch assigns x=1 and the other leaves x unchanged. Compute reaching definitions at the join by hand and compare to an iterative solver. To test the solver, shuffle traversal order; the final fixed point should not change though the number of iterations may.

### Design investigation: calculate a fixed point
Use a diamond CFG where B0 sets x=1, B1 changes x=2, B2 leaves x=1, and B3 merges paths. Define a constant-propagation lattice with unknown, constant c and nonconstant elements. At B3, x must be treated as nonconstant because incoming values disagree. Demonstrate the transfer function and join explicitly. Then change B1 to also set x=1 and verify that x becomes the known constant one at the join. Add a loop and iterate the work list until no facts change. Shuffle processing order as a robustness check; the final solution should agree though iteration counts may differ. A one-pass algorithm that returns the first predecessor's fact is not valid general dataflow analysis. State how unreachable predecessors are handled by your chosen analysis.

## Constant Propagation
**Constant Propagation: conceptual explanation**

Constant propagation identifies values that are provably fixed at certain program points. In a simple lattice, a variable may be unknown, known to equal a constant c, or varying; merging two different known values produces varying. If branches assign x=5 and x=5, x may remain known to equal 5 after the join. If branches assign 5 and 7, replacing x with either one is unsound. Sparse conditional constant propagation combines value inference with feasible-edge discovery and can eliminate a branch after its condition becomes constant.

Arithmetic semantics are critical. Folding `2147483647+1` in a signed 32-bit language may wrap, trap, be undefined, or promote depending on the language and operation. A compiler cannot substitute the host language’s floating-point behavior for source-language integer rules. Side effects constrain evaluation: it is not safe to replace an expression with a constant if doing so removes a required function call or changes exception behavior. Test propagation under variables modified through pointers, unknown function calls, volatile accesses, numeric conversions and control-flow joins. Compare the optimized program against a simple interpreter for small generated inputs and vary optimization passes to detect incorrectly assumed invariants.

### Design investigation: overflow exposes an invalid fold
Assume a source language with checked 32-bit signed addition. Folding `2147483647+1` to a wrapped negative number would be unsound because the specified behavior is to trap. In a wrapping variant it may produce the minimum signed integer, while an arbitrary-precision variant produces 2147483648. Write three reference interpreter modes and ask which transformation preserves each mode. Add a call `readAndLog()` to one operand and prove that removing or reordering it may change visible side effects. Test constant propagation through `if` branches that assign the same value and branches that disagree. Record optimized IR and result traces for each source semantics mode. The optimizer should be driven by explicit operator flags describing width, signedness and overflow policy, not by the host scripting language’s numeric defaults.

## Loop Optimization
**Loop Optimization: conceptual explanation**

Loop optimizations try to reduce executed work without changing observable behavior. Loop-invariant code motion identifies a computation whose operands and effects remain unchanged across iterations, then moves it to a preheader when executing it earlier is safe. Consider `for i in 0..n-1: y[i]=x*a+b` with x, a and b immutable throughout the loop. Computing `x*a+b` once may save repeated arithmetic. But if the loop executes zero times and the expression could throw, hoisting it out changes program behavior. Alias analysis and effect information determine whether supposedly invariant loads really remain unchanged.

Loop unrolling duplicates the body to reduce branch overhead and expose instruction parallelism, at the cost of larger code and greater register pressure. Vectorization groups independent element operations into SIMD instructions, but loop-carried dependencies may prohibit this. A reduction `sum += a[i]` can be parallelized under some mathematical assumptions; strict floating-point reproducibility may make reassociation observable. Build a loop benchmark with warm-up, varied input sizes and controlled compiler flags. Inspect emitted instructions and validate all outputs, especially for n=0, n=1, odd tails and aliasing arrays. Explain why one speedup measured on one processor is not a universal semantic or performance law.

### Design investigation: hoist only when safe
Begin with a loop computing `(a*b)+i` for each i where a and b are invariant exact integers and multiplication cannot throw. Hoisting a*b outside the loop can reduce repeated work. Now add a zero-trip case and make multiplication an overloaded operation with side effects: hoisting causes an observable call that would not have happened. Explain why the transformation fails unless the compiler can prove the operation is safe to speculate. In another example, a pointer alias modifies a inside the loop, so a*b is no longer invariant. Design a conservative alias test and compare outputs. Add loop unrolling by two and verify odd-length tails. Do not infer speedup from the number of source lines removed: inspect generated code and measure a controlled workload after semantic equivalence tests pass.

## Register Allocation
**Register Allocation: conceptual explanation**

Register allocation maps an unbounded collection of virtual values onto a finite set of physical registers. A value is live from its definition until its last possible use, and two simultaneously live values generally cannot occupy the same register. An interference graph connects values whose live ranges conflict; graph coloring allocators attempt to assign registers without adjacent conflicts. Linear scan is commonly used for fast compilation and allocates by intervals. When pressure exceeds capacity, a compiler may spill values to memory, split live ranges or recompute cheap values.

Calling conventions restrict allocations: caller-saved registers may be clobbered by calls, while callee-saved registers impose save/restore costs. Register classes matter as well; integer and floating-point operations may require different register banks or aligned groups. A naive model with eight registers and ten simultaneously live values suggests at least two values cannot reside in those eight at once, but does not specify exactly two stack stores, because spills may be reloaded many times. Draw live intervals for a basic block with an internal call, identify conflicts, assign registers and note save costs. After allocation, run a machine-level checker to ensure no operand refers to an unallocated virtual register and no live values share an incompatible register.

### Design investigation: liveness versus register count
Consider values a,b,c,d whose definitions precede a call, but only a and c are used after it. Construct live-in and live-out sets around each instruction. If a caller-saved register holds a live value across the call, the compiler must protect it by saving, moving or reallocating. Build an interference graph from overlapping live intervals and color it with three physical registers. Add a fourth simultaneously live value to force a spill or split under the simplified model. Distinguish spill slots from dynamic memory traffic: one spilled value may need several loads. Test a generated program that runs a function call between definition and use; incorrect caller-save handling can produce a wrong result even if the register allocator's graph coloring succeeds in isolation.

## Integrated Case Study and Model Limitations
A compiler sees `y = 2*7 + x`; constant propagation can fold the product to 14, provided evaluation has the intended arithmetic semantics. If multiplication has user-defined side effects or checked-overflow behavior, an apparently valid algebraic rewrite may not preserve observables. Build a simple control-flow graph with a loop and identify a computation that is loop invariant only when all operands are stable and the computation is safe to hoist. Next, mark live ranges for nine variables on a target with eight registers; at least one simultaneous live value needs another storage location or a different representation.

### Laboratory: optimization under observable semantics

Write an optimizer for three-address integer IR with if/else control flow, loops and explicit call instructions. Define the source integer behavior before transforming arithmetic: whether addition wraps, traps or has unbounded precision is part of correctness. Add annotations distinguishing pure operations from calls or loads with possible effects. Perform reaching-definitions and constant propagation on a CFG containing two predecessors. When both set x=7, the join knows x=7; when one sets x=8, the join value is not a unique constant. A pass that uses the value from whichever predecessor was visited last is incorrect.

Implement a work-list solver over a finite lattice. Show at least three iterations on a loop with a carried variable. The solver's result should not depend on the order in which blocks happen to be visited. For each block, print IN and OUT facts and confirm that reapplying transfer functions does not change the final solution. Make a regression where the lattice mistakenly treats unknown as a constant and watch a wrong branch elimination; this demonstrates why monotonicity, join direction and boundary conditions matter more than a visually plausible trace.

Add constant folding, unreachable-block removal, dead assignment elimination and loop-invariant code motion, one pass at a time. After each pass, check that IR invariants still hold and interpret both before and after programs for an enumerated input set. Introduce a loop that executes zero times and contains an expression that can throw. Hoisting the expression outside the loop changes the exception behavior and must be rejected unless the language semantics permits speculative evaluation. Introduce an aliasing store into a loop to demonstrate why an invariant-looking memory load may not be invariant. A conservative optimizer may miss a speedup; an unsound optimizer changes the program.

Model liveness at a call site and draw live intervals for values a, b, c, d and e. With only a few registers available, the allocator may need to spill or split a range. Examine the generated loads and stores rather than interpreting a single integer “number of spills” as a runtime cost. Different allocation strategies can trade compilation time, code size and execution performance. The simplest allocation for a teaching compiler can be correct even if inefficient, as long as its use-def and calling-convention invariants are checked.

Measure the optimizer with a transparent workload. Select small numerical kernels, branches and loop nests; include n=0, n=1, nonmultiples of vector width and inputs near arithmetic limits. Use repeated measurements, a warm-up policy and one fixed target environment when making speed observations. Record slowdown cases rather than discarding them. Preserve compiler flags and IR snapshots so a result can be reproduced. Finally run a mutation test: deliberately delete one side-effect condition in a transformation and demonstrate a case that catches it. This makes the testing argument stronger than a raw count of passing programs.

### Failure clinic: an optimizer that speeds up the wrong program

An optimizer moves a computation `readSensor()` outside a loop after noticing that its source arguments do not change. The call, however, reads external state and records an event. It is not a pure expression merely because it takes no parameters. After optimization the application reports the same sensor value for every iteration, and the event log contains one read rather than many. Explain which analysis was too weak: the pass confused syntactic invariance of operands with semantic invariance of effects. The optimization requires an explicit effect model, alias information and a proof that changing evaluation count and timing is permitted.

A second defect appears in constant folding. The compiler uses its implementation language’s arbitrary-precision integers to fold an expression in a checked 32-bit source language. For input near the maximum signed value, the optimized build returns a large integer where the unoptimized program throws. A compiler must evaluate constants using the source operation’s width, overflow and exception rules. Write boundary tests for minimum and maximum values, zero division, shifts by invalid amounts and conversions. Different operations have different source semantics; do not assume one generic host arithmetic function is adequate.

Design a staged repair. First preserve an IR interpreter as a reference. Each optimization pass receives a set of preconditions and records why a transformation was applied. Run each program before and after one pass; compare values, side effects and allowed exceptions. Test zero-trip loops and programs containing calls, volatile memory or aliasing. Then check all passes together, because a transformation may invalidate a fact used by a later optimization if analysis caches are stale. A test harness should save random seeds, IR snapshots and target details so failures can be reproduced.

The team proposes disabling all optimization tests in release mode because they slow CI. Reject that conclusion as unsupported. Instead separate fast deterministic regression tests from heavier differential and fuzzing runs, and prioritize cases with known semantic risk. Track mutation tests that remove an effect guard or overflow check: the suite should fail on the intentionally wrong compiler. No fixed number of passed tests proves the optimizer correct, but targeted tests and explicit proof obligations can make defects harder to hide.

### Worked comparative study: optimization as conditional proof

A textbook compiler pass often appears as a pattern replacement: if instructions resemble A, replace them with B. A correct optimizer needs more than resemblance. It needs a semantic precondition and evidence that the precondition holds. Folding `2*7` to fourteen is sound in many integer models. Folding `x*0` to zero may remove evaluation of x, which matters if x is a function call with side effects or a floating-point value for which NaN or signed-zero behavior is observable. Hoisting a loop expression can introduce evaluation on a zero-trip path. Reordering a load across a store can read a different memory value when pointers alias. These are not obscure academic objections; they are common reasons compilers maintain effect and alias analyses.

Formalize an optimization obligation: for all source states satisfying the pass preconditions, the observable behavior before and after the transformation must agree under the chosen semantics. Observable behavior can include returned values, memory writes visible to callers, I/O, allowed exceptions and termination. A real proof for a complex language is difficult, but stating the obligation clarifies testing. A differential test samples states and may find a counterexample; it cannot enumerate an infinite state space. Translation validation can check particular transformed outputs using symbolic methods or independent interpretation, with clear limits.

Analyze a loop optimization under three models. In a pure exact-integer language, hoisting a constant expression may be straightforward if it does not alter termination. In a checked-integer language, hoisting a trapping expression requires attention to zero-trip loops. In a language with calls and mutable aliases, additional effect proofs are needed. A pass should either carry adequate annotations or remain conservative. Refusing a questionable optimization is a performance limitation; applying an unsound transformation is a semantic bug.

Build an optimization test matrix by crossing normal and exceptional inputs with zero/one/many loop iterations, aliasing and nonaliasing pointers, and boundary integer values. Run both transformed and untransformed programs through independent execution paths. Then inspect machine code and benchmark repeated workloads, recording input sizes and variance. Correctness checking and performance testing answer different questions: an optimization may be semantically legal but slower due to register pressure or code size. A research-minded report preserves both success and failure cases rather than calling every transformation an improvement.

### Unit review: ask when the optimization is legal

Select one transformation that reduces operation count and try to invalidate it with a zero-trip loop, aliasing memory, a trapping expression or observable I/O. For each candidate, identify the exact precondition that must be proved. Recompute dataflow facts after editing CFG edges, rather than assuming cached analysis results remain correct. Add integer extremes and explicit overflow policy to constant-folding tests. After correctness tests pass, inspect emitted code and benchmark a controlled input set: a legal optimization can make a program slower because of instruction-cache pressure, spills or branch behavior. Academic conclusions should name both the semantic model and empirical target configuration; they are different sources of evidence.

### Worked question: Constant propagation join
If one CFG branch assigns x=5 and the other assigns x=7, can a compiler fold `x+1` at their join into one constant?

**Set up definitions and premises**
Along the first path, x+1 is six; along the second path, it is eight. A path-insensitive analysis at the join must conservatively represent x as varying or not a single known constant.

**Derive the result**
A sound constant-propagation lattice uses a join that does not arbitrarily select one predecessor value. Substituting x=5 globally would change the second path.

**Validate limits and interpretation**
If both branches instead assign x=5, the join fact becomes a known constant five, and folding x+1 to six can be legal if integer semantics and side effects permit it.

**Answer:** No single constant is valid for 5 versus 7; same-value branches permit constant propagation.

### Worked question: Zero-trip hoisting
A loop may execute zero times, and its body computes an expression that may throw. May an optimizer hoist that expression unconditionally before the loop?

**Set up definitions and premises**
The original program does not evaluate the body when the loop’s trip count is zero. Therefore no exception arises from the body expression on that input.

**Derive the result**
Hoisting the computation outside the loop evaluates it even when the loop is skipped and may raise an exception that the original program would not raise. This changes observable behavior.

**Validate limits and interpretation**
Hoisting becomes possible only if the compiler proves the expression safe to speculate, guards evaluation by a condition ensuring at least one iteration, or has an explicit source semantic rule allowing the changed behavior.

**Answer:** Unconditional hoisting is unsound under possible zero trips and effectful/trapping expressions.

### Worked question: Register pressure versus spills
Assume ten values are simultaneously live but only eight compatible registers are available. State the guaranteed pressure and the limits of a simple spill-count model.

**Set up definitions and premises**
At a single point at most eight of ten simultaneously live independent values can occupy the eight registers under the simplified model; at least two require alternative handling at that point.

**Derive the result**
The compiler may spill some values to stack slots, recompute a cheap value, or split live ranges so that storage moves over time. A count of two pressure excesses is not the same as exactly two runtime memory accesses.

**Validate limits and interpretation**
Calling convention restrictions or register classes can reduce the usable set further. Measure emitted loads and stores and inspect liveness rather than equating virtual value count with performance.

**Answer:** Pressure exceeds capacity by at least two concurrent values; exact spill traffic is not determined.
