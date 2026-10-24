# Unit 8: Language implementation

*Draft; not approved for public deployment. Eight-unit manuscript with source-specific cases and independent verification pending.*

## Interpreters
**Interpreters: conceptual explanation**

An interpreter evaluates a source or intermediate representation directly according to an explicit semantic function. A tree-walking interpreter dispatches on AST node kind; a small-step abstract machine maintains a current expression, environment, store and control stack. For `let x=2 in x*3+1`, an interpreter allocates a binding for x, evaluates the multiplication and returns seven. If evaluation can throw, the interpreter needs explicit exception propagation or a consistent host-exception mapping. A language implementation should distinguish its own run-time values from the host’s objects so booleans are not accidentally treated as integers and integer overflow semantics do not leak from the host language.

Separating parser, resolver and evaluator makes debugging easier. First produce an AST from source text, then resolve identifiers, then evaluate. Test each phase separately, including malformed source, scope shadowing and recursive definitions. A reference interpreter is useful as an executable semantics but is not necessarily a formal oracle if it shares implementation bugs with the compiler. Keep it small, clear and intentionally unoptimized. To test expression evaluation with side effects, record a trace of environment lookups, store writes, calls and returns. Compare the trace against documented evaluation order rather than checking only the final result, which can hide illegal reordering.

### Design investigation: trace a small interpreter
Construct an AST evaluator for integer literals, addition, multiplication, variables and let bindings. Evaluate `let x=5 in (x+2)*3` and produce a trace showing environment creation, identifier lookup, addition and multiplication; the final result is twenty-one. Add a nested let shadowing x and verify that the inner binding does not overwrite the outer variable. Then introduce a function call with an observable print and check evaluation order. Run the interpreter with a fuel limit and report exhaustion rather than hanging on an infinite recursive term. If the source language has checked overflow, compare its result with the host language’s default arithmetic behavior and add a conversion layer. An interpreter is a reference only to the degree that its code and specifications are independently reliable.

## Virtual Machines
**Virtual Machines: conceptual explanation**

A stack-based virtual machine executes instructions such as PUSH_CONST, LOAD_LOCAL, ADD, JUMP_IF_FALSE, CALL and RETURN using a stack and instruction pointer. Compiling `3 + 4 * 2` might emit PUSH 3, PUSH 4, PUSH 2, MUL, ADD, RETURN. A stack-depth verifier checks that every control-flow merge receives compatible stack shapes and that no instruction can pop more operands than available. A bytecode format also needs versioning, literal pools and bounds checks so malformed input cannot corrupt the host runtime.

A register-based VM stores temporaries in explicit virtual registers, potentially reducing instruction dispatch count at the cost of larger operand encodings. Bytecode is not automatically portable: runtime libraries, object representation, endianness of serialized bytecode, and feature versions still matter. A VM may interpret, baseline compile hot functions, or use a JIT optimizer; JIT compilation carries warm-up and code-cache overhead and requires deoptimization when speculative assumptions fail. Design a simple debugger mapping bytecode program counters back to source spans. Step through a function call, exception path and conditional jump while checking stack invariants and error messages. The VM implementation is part of the trusted runtime surface and therefore needs fuzz testing.

### Design investigation: bytecode stack effects
Compile `3+4*2` to `PUSH 3; PUSH 4; PUSH 2; MUL; ADD; RETURN`. Track stack state after each instruction: [3], [3,4], [3,4,2], [3,8], [11], then the return value eleven. Now introduce conditional jumps and define for each instruction whether it pops the condition. Two control-flow paths joining with different stack depths must be rejected by a verifier. Test an invalid bytecode stream beginning with ADD before any PUSH and one jumping past the final instruction; both must fail safely before execution. Add source-location metadata to each emitted instruction and trace a runtime error back to a source span. Compare a stack VM with a register VM based on instruction encoding and execution trace, not a blanket assertion that one is faster.

## Compiler Validation
**Compiler Validation: conceptual explanation**

Compiler validation asks whether generated code preserves the specified behavior of the source program. A differential test runs a program through a reference interpreter and a compiler and compares defined outputs, return values, observable side effects and exception behavior. Randomly generated programs are effective when their types and evaluation bounds are constrained, but they must avoid relying on undefined source behavior as a false oracle. Metamorphic testing compares variations that should be equivalent, such as renaming a bound variable without capture or adding a harmless parenthesis. Translation validation checks particular optimized outputs rather than proving the optimizer implementation correct for all inputs.

Test reduction is essential: when a 1,000-line fuzz case fails, simplify it to the smallest program preserving the discrepancy. Save compiler flags, random seed, target architecture, standard-library version and output traces. Use multiple independent tools when possible so the oracle and implementation do not share one bug. Incorrect optimizations often appear only near integer boundaries, aliasing, floating-point NaNs, concurrency operations, and exception paths. A validation report should say how many programs were tested, what subset of semantics they exercised and what remains uncovered; passing millions of arithmetic programs does not establish safe lowering of destructors or data races.

### Design investigation: distinguish oracle and implementation
Generate random expressions from a small grammar and evaluate them with both an AST interpreter and bytecode VM. Fix random seeds and store the exact source whenever a discrepancy appears. Include zero, negative numbers, deeply nested expressions, shadowed variables and invalid inputs. Add metamorphic renaming of bound variables with freshness checks: the renamed program should behave the same unless the rename accidentally captures another variable. Intentionally swap the operands of subtraction during compilation and ensure the test catches `2-5` producing three instead of negative three. Reduce the failing program automatically where possible, then restore correct order. Do not describe the suite as proof of compiler correctness; it samples a bounded semantic subset and may share bugs between the interpreter and VM.

## Language Interoperability
**Language Interoperability: conceptual explanation**

Interoperability joins language systems whose type layouts, calling conventions, exceptions and memory ownership may differ. A foreign-function interface often exposes a limited ABI-compatible set of primitives and opaque handles instead of trying to share every language object directly. Crossing from a garbage-collected runtime into native code requires protecting referenced objects from collection, pinning or updating pointers when objects move, and managing callbacks that may outlive their original scope. A borrowed pointer must not be freed by the receiver if ownership remains with the caller.

C strings illustrate representation mismatches: a zero-terminated byte sequence differs from a length-counted Unicode string; embedded zeros, encoding errors and lifetime management require explicit conversion policy. A foreign exception should generally not unwind through code compiled with an incompatible exception model unless the platform defines and tests that behavior. Make a boundary contract documenting argument types, widths, alignment, ownership, thread-safety, error channels and reentrancy. Add tests with empty strings, embedded nulls, huge buffers, concurrent callbacks and early cancellation. The interface is not correct merely because the simplest `add(2,3)` demonstration works. Stable ABI design also matters for library upgrades: a changed structure layout may break downstream binaries without a source-level compile error.

### Design investigation: boundary contracts for two runtimes
Specify an FFI accepting a byte buffer and its length. The native function must not read past the supplied length or assume a terminal null byte; the VM must validate bounds and preserve or pin memory for the duration of the call. Test the empty buffer, embedded null bytes, multibyte UTF-8, and a buffer with a length intentionally larger than the actual allocation. If the VM string represents Unicode characters, clarify why the byte count differs from a character count. Add a callback that retains a handle beyond its original call; define how the garbage collector sees it as a root and who releases it. Return errors through a specified status/result representation rather than allowing incompatible exception unwind models to cross an ABI. The final report identifies memory ownership, thread confinement, callback lifetime and version compatibility.

## Integrated Case Study and Model Limitations
A simple arithmetic interpreter reads an AST and updates an environment. A bytecode compiler instead emits instructions such as LOAD, ADD and STORE that a virtual machine executes. Both can implement the same language semantics but have different instrumentation and performance tradeoffs. Validate an optimization by comparing interpreter results with compiled results over generated inputs, including exceptions and overflow boundaries. Then expose the bytecode evaluator through a foreign-function interface: specify string encoding, memory ownership and how exceptions propagate across the language boundary. Without those details, the link may succeed while the system remains unsafe.

### Laboratory: build and validate two independent execution paths

Create a language implementation with one scanner, parser and resolver but two backends: an AST interpreter and a small stack-bytecode compiler plus VM. Keep both backends intentionally simple. Define arithmetic, booleans, local variables, lexical closures, conditionals and errors. Each instruction has an explicit stack effect. For example, ADD pops two numeric operands and pushes one result, while RETURN consumes or preserves a result according to the VM convention. A bytecode verifier should reject malformed jump targets and paths that merge with incompatible stack heights.

Compile `let x=3 in if x>2 then x*4 else 0`. Dump bytecode and annotate stack contents at each instruction. The conditional jump consumes a Boolean value, and exactly one branch pushes the selected result. At the join, stack depth must agree. Add function calls with frames and local slots; record instruction pointer, operand stack, local values and environment at each step. Make debug source spans a first-class part of the bytecode or its debug table so a runtime exception can point back to the source rather than reporting only a numeric instruction address.

Define an observation record for differential testing: final result, printed output, ordered store writes visible to the program, exception class and message category. Generate small typed programs with bounded recursion and deterministic inputs. Run every program through the AST interpreter and the VM and compare observation records. An output match can hide wrong evaluation order when side effects cancel, so include traces for programs with mutation or printing. Use consistent fuel limits or handle divergence separately, since different implementations may take different instruction counts to perform equivalent source-level work.

Introduce metamorphic tests. Rename a bound variable to a fresh identifier and confirm unchanged behavior; add parentheses that do not alter precedence; replace an arithmetic literal with an equivalent constant expression under the source arithmetic semantics. Now inject a compiler bug that swaps operands during subtraction. The differential suite should discover `2-5`, minimize the failure, and preserve the random seed. Inject another bug in closure capture so an inner function uses its caller's x; a scoped test should detect the discrepancy. State which mutation tests survive, because failures in the test suite reveal missing evidence rather than proving the compiler already works.

Add an interoperability boundary by calling a narrowly defined host function such as length-of-byte-string. Specify encoding, lifetime, return type and error policy. Test empty, long and non-ASCII data, including embedded null bytes. A byte-string length is not necessarily a Unicode character count. If a host callback stores a pointer after the VM returns, the runtime needs an ownership and rooting strategy; do not silently provide a dangling pointer. Conclude with a release gate: scanner/parser tests, type and scope tests, VM verification, differential semantics, mutation effectiveness, memory checks, and ABI boundary tests. A JIT would add assumptions, deoptimization and executable-memory security requirements that are deliberately out of scope for this first implementation.

### Failure clinic: two execution engines disagree only under side effects

A bytecode VM and a tree-walking interpreter agree on thousands of arithmetic expressions, but differ on `f() - g()` when both functions modify a shared variable. The interpreter evaluates operands left-to-right, while one compiler pass emits the right operand first to reduce register pressure. In pure arithmetic the results often match, concealing the defect. Evaluation order is a language semantic rule, not an optimizer preference. Construct a minimal program whose trace records the exact call sequence and whose return value depends on that sequence. Comparing just final output is less informative than comparing the trace of visible side effects.

The bytecode verifier also misses one malformed control-flow merge. The true branch pushes an integer, the false branch pushes two integers, and both jump to an ADD instruction. One path has insufficient or incompatible stack state after subsequent operations. A sound verifier should compute the abstract stack height and type for every reachable instruction and require compatible incoming states at joins. For loops, iterate to a fixed point or otherwise establish that a consistent state exists. Reject unknown opcodes, invalid indices and illegal jumps before executing untrusted bytecode.

The implementation adds a foreign string-length function whose native side expects a null-terminated byte string, while the VM supplies length-counted UTF-8 that may contain embedded zero bytes. The result differs between interpreters that happen to use different host representations. Specify whether the function counts bytes, code points or grapheme clusters; all are different concepts. Use explicit buffer length and ownership rather than relying on accidental termination rules. Test empty input, embedded zeros, malformed encoding and buffers whose lifetime ends before the native call returns.

Finally distinguish warm-up and steady-state performance. A JIT compiler may have higher initial latency yet run repeated hot code faster; an interpreter may perform better for tiny one-shot programs. Any comparison must specify workload, startup policy, target hardware and what was measured. No performance advantage permits a backend to violate the language contract. A reliable release process demands independently checked semantics, bytecode validity, resource limits, FFI ownership and regression tests on both execution paths.

### Worked comparative study: reference execution, validation and portability

A language implementation should be understood as several mutually checking systems. The scanner and parser recognize a source program. The resolver assigns identifier meanings. The type checker enforces static constraints. The interpreter supplies a straightforward execution path. The compiler lowers the same semantics into an intermediate representation and a VM or target backend executes it. Each stage can have a bug; a single successful demonstration does not reveal which stages were exercised. Design tests with independent oracles wherever practical so the same mistaken helper function is not shared by the reference and the optimized implementation.

Differential testing compares two implementations on the same source programs. It is powerful for arithmetic, control flow, closure capture and exception ordering but depends on agreement about source semantics. If behavior is unspecified or undefined for some input, a mismatch may not establish a compiler defect. A constrained generator should produce valid, terminating programs where possible, recording random seeds and evaluation budgets. When a discrepancy appears, minimize the program and preserve all relevant flags. Metamorphic tests add relations such as consistent alpha-renaming and insertion of redundant parentheses that should preserve behavior.

Portability requires more than bytecode. A VM's observable behavior depends on numeric widths, string representation, standard library and foreign calls. Bytecode serialization should specify version, endianness and valid operand ranges. A verifier should reject untrusted or corrupted bytecode safely before execution. Just-in-time compilation introduces speculative assumptions, deoptimization and executable-memory policies, adding a separate correctness and security surface. A simple interpreter may be preferable for small one-shot workloads despite lower peak throughput.

Prepare a release checklist that names actual evidence: parse corpus results, binding/type tests, interpreter trace tests, bytecode stack verification, differential comparisons, FFI boundary checks, malformed-input fuzzing, performance measurements and tested target configurations. Identify unresolved coverage explicitly. For a library exposed to students, readable errors and stable examples also matter: a perfectly fast VM that reports only “segmentation fault” when given a malformed expression is not a satisfactory teaching implementation. The goal is a reproducible language system whose guarantees can be located at the correct abstraction boundary.

### Unit review: verify both execution paths and the boundary between them

Generate a collection of small well-typed programs and run it through a reference interpreter and a bytecode VM. Compare values, permitted exceptions and visible side-effect traces. Seed malformed bytecode separately to test verifier rejection and stack-depth consistency at jumps. A mismatched result should be minimized to a reproducible source and a saved compilation seed. When calling host functions, include byte length, encoding, ownership and callback lifetime in the contract; check embedded NUL bytes and resource release. If a JIT is introduced, its speculative assumptions and deoptimization paths need their own tests. A passing differential suite is finite evidence, not a proof that every semantic feature has been covered.

### Worked question: Stack bytecode execution
Execute `PUSH 3; PUSH 4; PUSH 2; MUL; ADD; RETURN` and list stack values after each arithmetic instruction.

**Set up definitions and premises**
PUSH instructions create stacks [3], [3,4], and [3,4,2]. MUL pops the top two values 2 and 4 and pushes eight, leaving [3,8].

**Derive the result**
ADD pops eight and three, computes eleven, and leaves [11]. RETURN consumes or delivers this value according to the VM return protocol.

**Validate limits and interpretation**
A verifier should reject MUL if fewer than two operands are available, and should ensure all control-flow paths reach each instruction with compatible stack states.

**Answer:** The result is 11; after MUL stack [3,8], after ADD stack [11].

### Worked question: Differential validation
A compiler accidentally swaps the operands of subtraction. Design a minimal input that exposes the bug and explain why addition tests missed it.

**Set up definitions and premises**
Choose a noncommutative expression, such as `2-5`. A reference evaluator computes negative three; the faulty compiler computes 5-2=3.

**Derive the result**
Addition is commutative for ordinary mathematical integers, so a suite testing only a+b with simple values may not detect operand swapping. Random test generation should include operations with order-sensitive behavior.

**Validate limits and interpretation**
Save the minimized program, compiler flags and both traces. Add side-effectful operands to test evaluation order independently of arithmetic commutativity.

**Answer:** Use 2-5: reference -3 versus swapped result 3.

### Worked question: FFI buffer ownership
A VM supplies a byte buffer containing `A`, NUL, `B` to a native function. Explain why a null-terminated string API and length-aware buffer API disagree.

**Set up definitions and premises**
A C-style null-terminated string routine stops at the NUL byte and observes only the first byte as string content. The actual buffer contains three bytes.

**Derive the result**
A length-aware byte-buffer API supplied with length three can process all three bytes, provided bounds are checked. This difference is not a Unicode issue alone; even ASCII with an embedded NUL demonstrates it.

**Validate limits and interpretation**
Define encoding, length, owner and lifetime in the FFI contract. If a callback stores the pointer beyond the call, an explicit retention or copying rule is needed to prevent dangling references.

**Answer:** NUL-terminated length is 1, explicit byte length is 3 under the specified buffer.
