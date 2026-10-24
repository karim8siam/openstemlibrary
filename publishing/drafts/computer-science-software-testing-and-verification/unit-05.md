# Unit 5: Static verification

*Editorial length-qualified draft. Automated local tests performed; specialist academic review pending.*

## 5.1 Type Systems

### Core reasoning and definitions

A type system statically rejects or classifies programs according to rules about permitted values and operations. Types can encode primitive shapes, interfaces, ownership, nullability, units, generics, and sometimes refinements such as bounded integers. Soundness in a formal language has a precise meaning relative to the type semantics: often progress and preservation show that well-typed programs do not reach a selected class of stuck states. Real programming languages can trade strict guarantees for gradual typing, unsafe escapes, reflection, or foreign-function calls. A successful type check is not evidence that business logic is correct; the program can add the wrong two numbers while maintaining valid types. Static nullability analysis can exclude certain dereferences while leaving exceptions, resource leaks, and authorization mistakes untouched.

### Original investigative exercise

Model a payment amount as a nonnegative integer number of minor currency units instead of an unconstrained floating-point value. Create an API signature that distinguishes an authenticated user identifier from an arbitrary string and prevents accidental swapping of order and payment identifiers. Write tests showing which invalid values the type checker rejects and which still require runtime validation because external JSON can violate compiled assumptions. Audit escape hatches such as `any` and unchecked casts. Compare a function's static accepted domain with actual runtime inputs from an HTTP boundary.

### Limits and counterexamples

Annotating every parameter with the broad type `string` does not prevent mixing identifiers with different semantics. Types describe certain invariants; they do not automatically implement server authorization or input sanitation.


### Deep dive: what static analysis can and cannot establish

A static analyzer reasons about program structure without exploring every concrete execution. That does not make it purely syntactic. Modern tools can build control-flow graphs, propagate symbolic constraints, approximate types, and track potentially dangerous information flow between sources and sinks. The strength of a result depends on the programming language semantics, analyzer configuration, abstract domain, and modeling of third-party code. To interpret a finding, ask what property was analyzed, under which assumptions, and whether the tool established a proof of absence, a possible violation, or merely a pattern requiring human investigation.

Construct a control-flow graph for a parser receiving an optional `limit` parameter. The parser branches on whether the value is present, validates it is an integer, then uses it as a slice bound. If the code checks type but not sign, a negative integer may alter behavior or produce a runtime error depending on language semantics. A type checker that proves `limit` is an integer cannot prove it is nonnegative. A refinement type or explicitly checked contract can establish the stronger property. Document the distinction between a type's representation, its accepted domain, and the semantic unit attached to it.

Intervals demonstrate abstraction. Suppose `x` is known to lie in [2,5] and the program sets `y=3x+1`. The interval abstraction computes y in [7,16]. If a later branch enforces `x<=3`, the branch-sensitive interval becomes [2,3] and y in [7,10]. When paths merge, the analyzer may lose relations between x and y and conservatively allow combinations that never occur together. This creates a precision problem, not necessarily a soundness problem. A warning may arise from an over-approximation that includes an impossible state; a proof of safety remains meaningful when the over-approximated reachable set excludes an error condition.

Now consider integer overflow. In a language using fixed-width signed integer arithmetic, `3x+1` may overflow for sufficiently large x. An interval proof over mathematical integers is not automatically valid over machine semantics. In languages where overflow is defined to wrap, the transfer function must account for wraparound. In languages where checked overflow throws, the analysis must establish that the exception does not occur. If the analyzer silently treats integers as unbounded, the result must be qualified. Similar semantic traps arise from floating-point NaN, division by zero, memory aliasing, and concurrency.

Dataflow analysis follows potentially sensitive values. A public CSV importer receives a path parameter and passes it through decoding, validation, and filesystem access. A source-to-sink trace can flag possible path traversal or information exposure. Its accuracy depends on which functions are modeled as sanitizers and whether those functions genuinely enforce a security condition under the chosen platform. Rejecting the literal substring `..` is not sufficient in every environment because canonicalization, alternate encodings, absolute paths, and symbolic links may change how a path resolves. The analyzer may be unable to prove safety even when a secure directory-handle API is used, or may miss a custom wrapper not configured as a sink.

Contracts provide a bridge from static facts to intended behavior. A pure function may have a precondition `amount >= 0` and a postcondition relating returned balance to input balance. A payment service also requires persistent atomicity: if any step fails, either all account entries are committed or none are. A proof about arithmetic on local values cannot establish transactional atomicity unless the abstract model includes durable storage transitions. Match each proof obligation with its correct level of abstraction and pair it with runtime tests at boundaries where the model is incomplete.

When tools disagree, do not average their warnings or blindly choose the most confident one. Reproduce the reported path with a minimized input if possible, inspect configuration, check feasibility of constraints, and identify which claims were sound proofs versus heuristic alerts. Report false positives separately from confirmed defects; measure false negatives where a seeded benchmark permits it. Static verification adds value when its mathematical or semantic claim is precise, its evidence can be repeated, and its limitations are not hidden behind an impressive dashboard.


### Unit synthesis: qualified proof statements from static tools

When a static analyzer reports that an array index may equal eight for an eight-element array, determine whether the path is feasible before labeling it a concrete defect. When an interval analyzer reports y in [7,16] from x in [2,5] and y=3x+1, ask whether machine arithmetic semantics could invalidate that interval at other bounds. When a taint tool reports a flow from request input to filesystem access, determine whether path validation and filesystem constraints actually block unauthorized files. A warning is not necessarily exploitation, and a clean report is not proof that unmodeled sinks are safe. The student deliverable should cite the source and sink or violated invariant, state the abstract domain and assumptions, give a concrete test when feasible, and identify which behaviors the tool omits. The skill is to convert analyzer output into precise, actionable evidence rather than treating a severity badge as the final answer.

## 5.2 Dataflow Checks

### Core reasoning and definitions

Dataflow analysis approximates how values and facts propagate through a program's control-flow graph. Reaching-definitions analysis identifies which assignments may reach a use; liveness shows whether a variable's current value may be used on some later path; definite assignment checks whether a variable is initialized on every path to a read. Security-oriented taint analysis tracks sources of untrusted data toward sensitive sinks, but results depend heavily on correct source, sink, and sanitizer models. Analyses use abstractions to trade computational feasibility for precision. A may-analysis may conservatively include impossible flows and produce false positives; a must-analysis derives facts guaranteed on every modeled path. Transfer functions and fixed-point iteration ensure stable results over loops.

### Original investigative exercise

For code receiving a user-controlled SQL filter, mark the request field as a tainted source. Follow its path through string concatenation to an SQL execution sink. Compare the result when the code instead passes the value as a bound parameter under a parameterized query API. Draw a small control-flow graph with a branch that sanitizes only one path and explain why the join point may remain tainted. Record an uninitialized local used after a conditional assignment and check whether the static tool warns. Verify whether the tool's model recognizes a project-specific wrapper around the actual database API.

### Limits and counterexamples

A dataflow warning is a potential path under its abstraction, not proof that exploitation is possible. Conversely, an analyzer that lacks a framework sink model may miss a dangerous flow and still report no findings.


### Applied laboratory: analyzing static safety of a configurable data importer

A configurable CSV importer accepts columns, transforms them into typed records, and writes rows into a datastore. Static verification can reveal some failures without running every input, but its findings depend on what program behaviors the analyzer models. Begin with a type system. A column designated as an integer should be parsed through a function returning either a validated integer or an explicit error, not an unchecked cast that treats invalid text as zero. Differentiate a runtime type claim from proof that a string conforms to the domain: the type `number` alone does not establish that a temperature is within a reasonable physical range or that a monetary quantity has two decimal places. Use distinct validated types or contract predicates for domain constraints.

Model a tainted data path. An untrusted filename arrives from the import request, passes through a helper, and reaches a filesystem operation. A dataflow analyzer should track the taint from source to sink and recognize validation or canonicalization operations only when their semantics actually prevent unsafe use. A call named `sanitize` is not automatically sufficient. If a path is checked before a symbolic link is changed, a time-of-check/time-of-use race may still exist. Static tracing can flag flows requiring review, but a reported path might be infeasible due to a guard not understood by the analyzer. Conversely, a custom framework source or sink omitted from the configuration could conceal an exploitable flow. Inspect the analyzer's model coverage before interpreting a clean report.

Add contracts to the parser. A successful parsing function must return a record whose schema matches a declared version, whose required fields are present, and whose values satisfy specified bounds. A failed parse must not leave a half-written row. For a normalized student identifier, a precondition may require UTF-8 input of limited length and a postcondition may assert canonical representation. However, expecting the caller to satisfy every precondition can be unsafe at a public API; validation must occur at the trust boundary. Record which preconditions are caller responsibilities and which are checked defensively. The importer should also ensure that logging an invalid row does not copy secrets or personal data into diagnostic reports.

Use abstract interpretation to approximate array-index safety. Suppose there are eight configured columns, indexed zero through seven. When an index originates from a loop `for i from 0 while i < 8`, a sound analyzer can often prove `0 <= i <= 7`. Change the bound to `i <= 8` and the abstract range includes the invalid value eight. If two branches assign `i=2` and `i=7`, an interval domain merges them into [2,7], potentially admitting values that cannot occur. That imprecision may produce a warning without a concrete counterexample. More relational domains can retain constraints between variables but cost computational resources. A warning must therefore be classified as an actual defect, a true risk needing runtime protection, or a limitation of the chosen abstraction after evidence is inspected.

Explore integer arithmetic. For a total-price calculation `unit_price * quantity`, unbounded mathematical integers may produce a large exact result, whereas a fixed-width type may wrap or raise on overflow. A static proof written over integers is only transferable if the target language uses compatible semantics or explicit checked arithmetic. Likewise, analyzing a non-null type does not prove a remote service will respond before timeout. State the trust assumptions, environmental invariants, and unsupported program features. Pair static checks with runtime boundary tests: malformed CSV quoting, Unicode normalization, duplicate headers, maximum field length, and interrupted database commits exercise behaviors a type checker alone cannot settle.

The laboratory deliverable is a triage ledger recording each warning, the source and sink or violated invariant, concrete feasibility evidence, severity under the actual application threat model, and a regression test where one can be built. A low alert count is not itself a sign of high correctness; a poorly configured analyzer can produce zero reports by ignoring the relevant paths. Good static verification means the claims are scoped, reproducible, and linked to the semantics of the actual language and build settings.


## 5.3 Contracts

### Core reasoning and definitions

Design by contract expresses assumptions and guarantees around components, often as preconditions, postconditions, and invariants. A caller is responsible for meeting documented preconditions; the callee promises its postconditions if those preconditions hold, subject to exceptional behavior stated in the contract. A loop invariant is a property maintained before and after each iteration and can support a formal correctness argument. Runtime assertions can detect deviations early, while formal proof tools can establish certain implications symbolically. Contracts must identify permitted state changes and side effects, not only return values. Inheritance and interface substitution complicate contracts: a replacement component must not unexpectedly demand stronger preconditions or promise weaker postconditions than callers depend upon.

### Original investigative exercise

Specify a transfer function with `amount>=0`, sufficient source balance, and distinct account identities as preconditions. Postconditions preserve total funds, decrease the source by `amount`, increase the destination by `amount`, and reject an invalid transfer without partial mutation. Construct an example with source=80, destination=20, amount=35; the expected final state is 45 and 55. Check both return result and persisted balances, then inject an exception between debit and credit to evaluate atomicity. A function that passes the arithmetic but commits one side early still breaks the contract.

### Limits and counterexamples

A precondition simply written in comments is not enforced by the runtime. Conversely, checking a contract only during one test cannot show it holds for every reachable state.

### How to interpret the interactive model: interval transform

The interval transform assumes a mathematical integer x in [2,U] and computes y=3x+1. Monotonicity permits exact lower and upper transformed bounds: [7, 3U+1]. With U=5, y is confined to [7,16]; with U=50, the upper bound reaches 151 and an assertion that every value is below 100 is false. An interval domain tracks ranges but loses relationships between independent variables. The same reasoning is not automatically sound for fixed-width integer wraparound or floating-point overflow. The slider is an explanatory static-analysis example, not a source-code analyzer. When a warning remains because an abstract interval includes a hazardous value, distinguish a concrete failing input from an impossible combination introduced by over-approximation.

## 5.4 Abstract Interpretation

### Core reasoning and definitions

Abstract interpretation computes a tractable approximation of program behavior in an abstract domain. An interval domain, for example, might summarize a variable as lying between lower and upper bounds instead of enumerating every integer value. Transfer functions approximate the effect of assignments and tests, and join operators merge information from multiple control-flow paths. A fixed-point computation handles loops, often using widening to guarantee termination. Sound over-approximation can prove an undesirable state unreachable when the abstract reachable set excludes it, but a warning that the set includes an error does not prove a concrete path exists. Precision depends on domain choice; intervals lose correlations such as `x=y` across independently tracked variables.

### Original investigative exercise

Take `x` from [2,5] and compute `y=3*x+1`. Interval arithmetic gives y in [7,16]. If the program branches on `x<4`, a path-sensitive analyzer can narrow the ranges in each branch. Examine an array index known to be in [0,7] when the length is 8; the tool can conclude bounds safety under the model. Then merge a branch that permits index 8, and observe how the proof fails. Distinguish the concrete counterexample from a conservative warning caused by lost relational information. Check integer overflow semantics before adopting real-number interval arithmetic.

### Limits and counterexamples

An interval bound derived over mathematical integers may be invalid for a fixed-width machine type if overflow wraps. Abstract results inherit the assumptions of their semantics.

### How to interpret the interactive model: transfer invariant

Two accounts begin with balances eighty and twenty; the model transfers an allowed amount x between zero and eighty. It computes the new balances as eighty minus x and twenty plus x. Their sum remains exactly one hundred for every permitted slider position, illustrating a conservation invariant. Real transaction correctness also requires atomic persistence, authorization, concurrency isolation, and a policy on fees. If an exception occurs after source debit but before destination credit, the arithmetic displayed here cannot certify a database system's rollback behavior. Use the model to derive expected successful postconditions, then construct fault-injection and concurrency tests at the durable boundary. At x=0 the state is unchanged; at x=80 the source is exhausted but conservation still holds. Do not allow negative transfers unless the contract explicitly defines their semantics.

## Fully worked questions

### Worked problem 5.1: Type Systems

A loop accesses an array with length 8 using `for i=0; i<=8; i++`. Derive the possible index interval and explain what a sound interval analyzer must report.

**Define the property and assumptions.** Array indices are legal from zero to seven. Under an integer loop beginning at zero and checking `i<=8`, each iteration body may see a value from zero through eight inclusive. The abstract interval at the access is therefore [0,8], assuming no other guards.

**Compute or execute the reasoning.** The abstract interval intersects the invalid index region at exactly 8, so a sound analyzer that understands the array size cannot prove bounds safety. A concrete witness is the final iteration i=8. Changing the condition to i<8 narrows the body index interval to [0,7] and removes this particular error.

**Interpret the conclusion and limitations.** Check the target language: in some languages an out-of-bounds access throws, while in others memory is accessed unsafely. If array size changes dynamically or arithmetic overflows, the simple interval proof requires additional assumptions. A static warning can be a real counterexample, but not every warning is equally concrete.

### Worked problem 5.2: Dataflow Checks

Suppose an untrusted filename enters a service, is checked with a substring `..` filter, and is passed to a filesystem read. Why is the filter not a sufficient proof of path safety?

**Define the property and assumptions.** The source is the untrusted filename and the sink is filesystem access. The filter rules out one literal character sequence but may ignore absolute paths, alternate separators, Unicode normalization, encoded representations, or symbolic-link behavior. The precise set of hazards depends on the operating system and decoding layers.

**Compute or execute the reasoning.** Resolve the requested path under a fixed authorized root using safe filesystem APIs and verify the resolved target remains within that root under the chosen threat model. Prefer opening relative to a directory handle with protections against symlink escapes where supported. Test encoded traversal and race conditions separately rather than assuming string substitution proves safety.

**Interpret the conclusion and limitations.** A static dataflow report identifies a path worth investigating; it does not imply arbitrary code execution or prove exploitation. Conversely, a clean report can miss custom sinks or unsafe filesystem semantics. Record the analyzer's configuration and runtime checks as distinct pieces of evidence.

### Worked problem 5.3: Contracts

A transfer begins with balances 80 and 20 and moves 35. Derive a postcondition and describe an exception test that distinguishes atomicity from correct arithmetic.

**Define the property and assumptions.** The precondition requires an allowed nonnegative amount no greater than source balance and valid distinct accounts. Conservation requires source+destination remain 100, while successful postcondition requires source'=80-35 and destination'=20+35.

**Compute or execute the reasoning.** A correct committed result is 45 and 55, preserving total 100. Inject failure immediately after debit and before credit. A nontransactional implementation could leave 45 and 20, violating conservation. A correct atomic implementation must either commit both 45 and 55 or roll back to 80 and 20.

**Interpret the conclusion and limitations.** Checking only the returned numerical result does not prove persistence atomicity. Query durable balances after the injected fault, and exercise the actual database transaction boundary. If fees are permitted, rewrite the conservation equation to include the fee account rather than secretly assuming money disappears.

