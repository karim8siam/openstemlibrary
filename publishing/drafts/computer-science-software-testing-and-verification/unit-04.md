# Unit 4: Test-design techniques

*Editorial length-qualified draft. Automated local tests performed; specialist academic review pending.*

## 4.1 Equivalence Partitions

### Core reasoning and definitions

Equivalence partitioning groups inputs into sets expected to behave alike under a defined rule, allowing one representative from each class to provide useful evidence. The groups come from the specification, not arbitrary intuition. A discount code might be valid, expired, already redeemed, unknown, or malformed; each class may map to a different rejection. Partitions should be mutually exclusive for one classification dimension and cover the relevant declared domain. Some partitions interact with system state, such as a valid coupon that exceeds remaining redemption capacity. Partitioning reduces redundant tests but does not prove that every value in a partition is treated identically. Boundary checks and property tests complement it by targeting places where behavior can change. Document why two inputs were grouped and which output relation justifies that grouping.

### Original investigative exercise

An exam score accepts integers in [0,100]. Define partitions: below range, valid range, above range, noninteger, missing, and nonnumeric text. Test a representative such as -4, 62, 114, 3.5, absent, and “abc”, then test 0 and 100 separately as boundaries. If policy permits decimal scores, change the partition definition rather than silently coercing 3.5 to an integer. For each case assert both the validation outcome and whether storage was mutated. Distinguish rejection from silent clamping because they have different learning and audit consequences.

### Limits and counterexamples

Two values within a purportedly valid partition can still expose an unanticipated special case, such as leading-zero parsing or integer overflow. Partitions are a test design hypothesis, not a mathematical guarantee of equivalence.


### Deep dive: test selection as an optimization problem

Exhaustive testing is sometimes possible for tiny finite domains and usually impossible for realistic systems. An integer grade classifier accepting values zero through one hundred can be tested at all 101 valid scores, but an API accepting an arbitrary Unicode student name, multipart file, locale, network state, and concurrent requests has an enormous state space. The purpose of test-design techniques is not to guarantee correctness from a small sample; it is to make explicit why chosen examples are likely to expose defects. Partitioning, boundary analysis, properties, and covering arrays all rely on assumptions about where behavior changes and which interactions matter.

Suppose an assessment API accepts scores as integers, a course identifier, and an authorization token. Derive partitions from requirements: valid versus invalid score type, inside versus outside inclusive numeric range, known versus unknown course, authorized versus unauthorized caller, active versus archived course. Within the valid score range, grade thresholds generate additional subpartitions. A naive Cartesian product of all values becomes large, so isolate pure grade logic for exhaustive boundary checking and reserve a smaller selection of integrated endpoint tests for authorization and persistence interactions. Do not allow an easier pure-function test to stand in for the authentication gate.

Boundary tests exploit common faults in comparisons. For an inclusive range from zero to one hundred, test negative one, zero, one, ninety-nine, one hundred, and one hundred one. For thresholds fifty, seventy, and eighty-five, test an adjacent value on each side. If decimal scores are prohibited, testing 49.5 is a type/domain test rather than an adjacent integer boundary. Document the type semantics: JSON does not preserve arbitrary integer precision, and some languages coerce strings or booleans to numbers. A test that sends the string "50" should assert rejection or acceptance according to the API contract, never according to implementation convenience.

Property-based testing adds relations that hold for broad families of inputs. The grade classification must be total over valid integer scores, monotone in grade rank, and deterministic for the same version of the grading policy. A generator can explore many valid inputs, and a shrinker can reduce a failure near a threshold to a compact counterexample. If the property requires monotonicity, it should use `<=`, not `<`: increasing the score does not always change the grade category. Stateful property tests can generate sequences of enrollment and cancellation operations and compare an abstract model's invariant with the implementation's observations.

Pairwise testing targets interactions rather than all full combinations. For factors of size two, three, and four, there are 24 complete assignments but only 26 distinct pair targets distributed across AB, AC, and BC. Those 26 targets can be covered by far fewer than 26 rows because each assignment covers one pair from each factor pair. A valid covering array must be checked by enumerating its covered projections; quoting only the theoretical target count is not evidence the array covers them. Constrained values complicate generation: a payment method may be unavailable in a particular country, making some combinations invalid by design. The generator must respect constraints while clearly reporting pairs that are impossible, rather than treating missing impossible pairs as coverage failures.

Risk-driven higher-order interactions matter. Imagine an old API client, a particular locale, and a mobile browser trigger a parsing error only when all three coincide. A two-way array may not contain this triple even though every pair appears somewhere. Based on incident history, augment the pairwise suite with targeted three-way combinations. Likewise, concurrency, time, and retry state often interact in ways not represented by a simple factor table. Combining combinatorial testing with model-based state sequences makes those transitions explicit.

Use mutation analysis to test the strength of oracles. Deliberately change `>=85` to `>85`; the test at exactly 85 should fail. Deliberately remove authorization from a grade-update endpoint; a negative authentication test should fail while a pure grade-function test remains green. These mutations show why independent boundaries require distinct tests. A high test count, branch-coverage number, or mutation score cannot compensate for entirely missing requirements. A good design document explains which fault families each group of tests addresses and which remain out of scope.


### Unit synthesis: every selected test has a fault hypothesis

A boundary test at eighty-five in a grading classifier targets the difference between inclusive and exclusive comparison; a test at ninety does not. A property test asserting that category rank is nondecreasing covers a broader relationship but can still miss an incorrect threshold value if the resulting rank order remains monotone. A pairwise covering array targets interactions between any two factors, but not necessarily a particular three-factor interaction. These methods answer different questions and are stronger together. In the practical assessment, first write an independent grade oracle from an approved decision table; then test all 101 valid integer scores and a selected set of malformed payloads. Next create an interaction matrix with authentication status, API version and client platform; record exactly what pair targets each chosen row covers. Finally introduce a deliberate threshold mutation and explain which assertion detects it. This combination tests behavior rather than merely increasing the test count.

## 4.2 Boundary Analysis

### Core reasoning and definitions

Boundary-value analysis concentrates on values where classification or algorithmic behavior changes. Conventional faults occur at edges because developers use the wrong comparison operator, convert representations incorrectly, or miss an empty collection. For an inclusive range [L,U] the natural test set includes L-1, L, L+1, U-1, U, U+1 when the type admits those values. For a string length range the edges are measured in the relevant units: bytes, Unicode code points, or user-perceived grapheme clusters can differ. Boundaries may also be temporal, such as one moment before a deadline, exactly at the deadline, or one moment after. Test the most consequential transition and state what comparison semantics the implementation uses. Avoid creating invalid boundary arithmetic through type overflow.

### Original investigative exercise

A course registration closes at 17:00 local campus time. Specify a time zone and whether a submission exactly at 17:00:00 is valid. Freeze the server clock at 16:59:59.999, 17:00:00.000, and 17:00:00.001, then submit the same eligible request against clean fixtures. Consider that a browser clock differs from the server and cannot serve as the authoritative deadline. If submissions are queued, define whether arrival at the API or durable acceptance into the queue determines punctuality. Save expected transitions in the test oracle, including the effect on reservation capacity.

### Limits and counterexamples

A boundary test built with a fixed date string but an unfixed system clock may pass or fail in different time zones. The test should control the interpretation, not just the visible timestamp.


### Applied laboratory: designing tests for an examination-scoring API

A scoring service takes an integer between zero and one hundred and assigns a grade. Suppose the published rule is: scores below zero or above one hundred are invalid; scores from zero through forty-nine are Fail; scores fifty through sixty-nine are Pass; scores seventy through eighty-four are Merit; scores eighty-five through one hundred are Distinction. Define the intervals with inequalities rather than conversational phrases. If the implementation parses decimal strings or permits fractional scores, resolve that as a separate policy. Otherwise the input domain is all valid JSON integers, and values such as 49.5, null, a missing key, the string "50", and a boolean must be rejected rather than silently coerced.

An equivalence partition is a hypothesis that members behave similarly, not a proof of identical execution paths. For the grade rule, sensible positive representatives include zero, twenty-five, fifty, seventy, eighty-five, and one hundred. Out-of-range integers form separate invalid partitions; nonintegral numbers and wrong JSON types form additional partitions because they exercise different validation logic. At each boundary, select both the last value below and the first value at the threshold: forty-nine/fifty, sixty-nine/seventy, eighty-four/eighty-five. Also include zero and one hundred together with their invalid neighbors. A suite that tests forty, sixty, and ninety would demonstrate normal cases but not the most likely comparison-operator mistakes.

Construct a reference function independently of the implementation. A direct decision table is preferable to copying source-code branches into the test. For example, an explicit array of disjoint intervals with expected grade labels can generate oracle values. A sound reference should reject the same declared invalid domain but need not use the same conditional ordering as the application. Compare all valid integer inputs from zero to one hundred against the oracle; that is 101 exhaustive cases for this finite subdomain. This bounded exhaustive test gives stronger evidence than sampling ten arbitrary scores, but it still says nothing about how the HTTP layer handles malformed JSON or an invalid authentication token.

Add property-based tests. For valid integers, the result must be one of four grade categories; increasing a score must never decrease the category rank; and serialization followed by deserialization should preserve the input integer. A metamorphic relation checks an expected transformation even where a precise output oracle is inconvenient. For example, if a normalized score is mapped through an explicitly approved linear scale, certain order relations should be preserved. Take care: the grade need not change under a one-point increase, so a property demanding strictly increasing grade would be false. Shrinking an unexpected failure toward a minimal counterexample helps diagnosis. If the service assigns Merit to sixty-nine, the smallest failing case near the threshold reveals the defect more clearly than a huge randomly generated test batch.

Introduce interacting factors: authenticated versus anonymous, request sent by browser versus mobile client, locale preference, and an application version using a revised threshold. Pairwise combinatorial testing can cover every pair of factor values more economically than the full Cartesian product. But domain-specific risks may require three-way or higher-order combinations. A legacy threshold activated only when a mobile client uses a particular locale and an old API version will evade pairwise coverage if the full triple is not in any selected case. Risk analysis determines where combinations deserve exhaustive attention. In the accompanying pairwise simulation, the sum of pair targets is not the minimum number of test cases; distinguish targets from an actual covering-array construction.

Finally evaluate a hidden state dependence. The service records a grade publication timestamp and sends a notification; a retry using the same request token should not duplicate the notification. Check both returned grade and persisted event count. Mutation testing can intentionally change `>=` to `>` at the eighty-five boundary and confirm a test fails. If no test detects that mutation, improve the oracle instead of reporting a superficial rise in line coverage. The result is a compact suite with documented partitions, exact boundary tests, properties, interaction factors, state assertions, and an honest statement of what remains untested.


## 4.3 Property Testing

### Core reasoning and definitions

Property-based testing describes an invariant that should hold for a broad space of generated inputs rather than listing only concrete examples. Generators sample structured inputs under explicit constraints; shrinkers reduce a failing input into a smaller counterexample that exposes the defect. Good properties originate in domain mathematics or externally specified behavior. Sorting should preserve multiset membership and produce a nondecreasing order; round-trip serialization should preserve agreed semantic values, although byte-for-byte equality may be inappropriate when fields are normalized. A generator that produces only conventional positive integers can miss edge cases involving empty data, limits, sign changes, or unusual encodings. Seed control aids reproducibility but multiple seeds and targeted boundary examples improve breadth. Generated count measures effort, not a proof of correctness.

### Original investigative exercise

For a ledger operation, generate nonnegative transfers between accounts subject to sufficient funds. Assert total balance conservation and absence of negative balances after every accepted transfer, including repeated attempts with the same idempotency key. Introduce zero amounts, large values, and cancellations as separate classes. When a counterexample appears, reduce the transaction sequence while preserving the failure. Replay the minimized case with exact starting balances and operation order. Compare the property with a separately implemented reference model rather than checking a production helper against itself.

### Limits and counterexamples

An overbroad property such as “output always increases when input increases” may be false for valid nonlinear domains. Test the property premise against the specification before interpreting a failed case as a product defect.

### How to interpret the interactive model: boundary cases

For a score valid in the inclusive integer range zero to U, the simulator selects candidate tests at minus one, zero, one, U minus one, U, and U plus one. It removes duplicates when the upper bound is one, so case count decreases. At U=80, it produces the six expected neighbors; at U=1, zero and U minus one coincide, and U plus one equals two. Do not interpret candidate count as a complete test count for every implementation. Thresholds inside the accepted range, malformed JSON types, noninteger values, and authorization errors require their own tests. An inclusive upper bound differs from a strict one only at U, so exact-boundary testing is particularly diagnostic. The model's target is limited to integers and does not simulate rounding or locale-specific parsing.

## 4.4 Combinatorial Testing

### Core reasoning and definitions

Combinatorial testing addresses interactions among several input factors without necessarily enumerating the full Cartesian product. A pairwise covering array guarantees that every allowed pair of factor values appears somewhere in the test set; higher-strength arrays cover triples or larger interactions at greater cost. This is useful when many bugs are activated by combinations such as browser engine plus login status, locale plus timestamp format, or permission plus action type. Constraints matter: an impossible combination must not be forced into a test suite just to satisfy a mathematical covering target. Factor values must represent meaningful classes; treating every browser version as identical hides version-specific risks. Pairwise coverage is neither code coverage nor a guarantee against three-way defects.

### Original investigative exercise

Consider factors browser={Chromium,Firefox}, role={visitor,student,staff}, and connection={online,offline}. There are 2×3×2=12 full combinations. Build a smaller candidate suite and check which browser-role, browser-connection, and role-connection pairs occur. If the application prohibits offline staff actions, encode that constraint explicitly and report uncovered impossible pairs separately. Select extra full combinations for security-sensitive staff operations even if pairwise mathematics says they are redundant. Track the suite's concrete versions, seeded account state, and expected outcomes.

### Limits and counterexamples

A pairwise suite constructed from an invalid data model can still attain 100% pair coverage while every test proves the wrong requirement. Use risk-based cases for interactions with known higher-order failure modes.

### How to interpret the interactive model: pairwise targets

Given factor sizes two, three, and k, full Cartesian product size is six times k. Distinct pair targets comprise six AB pairs, two-k AC pairs, and three-k BC pairs: six plus five-k. At k=4, the full product has twenty-four rows while there are twenty-six distinct pair targets. This does not imply twenty-six tests are required. Each full assignment simultaneously covers an AB, AC, and BC pair. A valid covering array is a concrete selection of rows whose projected pairs cover every reachable target. The model calculates target obligations only and intentionally does not generate such an array. Constrained combinations, e.g., a payment method unavailable in one region, complicate construction. Domain-critical three-way triggers should be tested directly even if all pair targets are covered.

## Fully worked questions

### Worked problem 4.1: Equivalence Partitions

An integer grade endpoint accepts 0 through 100 and assigns Distinction at 85. Design the smallest targeted boundary set to detect a `>` versus `>=` mutation at the distinction boundary.

**Define the property and assumptions.** Write the contract as `score >= 85` for Distinction among valid integer scores. The mutated implementation incorrectly uses `score > 85`. Tests far from the boundary such as 90 and 20 cannot distinguish the predicates.

**Compute or execute the reasoning.** A single input exactly equal to 85 distinguishes the two implementations: the original returns Distinction and the mutation returns the lower grade. Include 84 and 86 as context to detect a shifted or discontinuous boundary. For the whole endpoint, test input -1 and 101 for validation, but they are not necessary solely to kill this one mutation.

**Interpret the conclusion and limitations.** The minimal targeted set depends on the fault hypothesis. A single 85 test kills the declared mutation, but it does not establish all other grade boundaries or JSON type validation. Separate narrow mutation adequacy from overall test-plan completeness.

### Worked problem 4.2: Boundary Analysis

A decision model has factors of sizes 2, 3, and 4. Calculate the complete Cartesian product size and number of distinct value pairs across factor pairs. Can this latter number be used as the required test count?

**Define the property and assumptions.** Label factors A, B, and C with |A|=2, |B|=3, and |C|=4. A complete product enumerates every assignment, so its size is 2*3*4. Distinct pairwise targets are combinations of values from each unordered pair of factors.

**Compute or execute the reasoning.** The complete suite has 24 assignments. There are 2*3=6 targets for AB, 2*4=8 for AC, and 3*4=12 for BC, totalling 26 pair targets. A single full assignment covers one target in each of the three factor-pair projections, so 26 is emphatically not a lower bound of 26 tests.

**Interpret the conclusion and limitations.** Constructing a covering array requires actual assignments that collectively cover every pair; the achievable row count depends on factor sizes and constraints. Risk-relevant triples may remain absent even in a valid pairwise design. Treat the simulation's target total as an obligation count, not a test-count answer.

### Worked problem 4.3: Property Testing

A property test of a grade classifier fails for inputs x=82 and y=85 because the output rank decreases. State a shrinking strategy and the invariant that a sound oracle checks.

**Define the property and assumptions.** The monotonicity requirement is: for any valid integers x<=y, grade_rank(x)<=grade_rank(y). This is non-strict; adjacent numeric scores may share one grade. The reported failure should include the exact pair, expected rank order, and application version.

**Compute or execute the reasoning.** Shrink the counterexample by reducing the gap y-x while preserving the failure. Try y=x, then nearby threshold values and binary-search over the interval. A minimal counterexample around 84 and 85 would point to a transition bug at Distinction, whereas a case involving 82 and 85 might be caused by a broader mapping error.

**Interpret the conclusion and limitations.** A property runner should store a reproducible seed, but seed alone may not recreate differences caused by global state or data races. If classification depends on a locale, timestamp, or version, include those parameters in the generated domain and shrink while respecting their constraints.

