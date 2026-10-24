# Unit 1: Computational thinking

## Problem Decomposition

## Problem Decomposition: the computational contract

**Core idea.** Separate the pricing operation into named responsibilities. A requirement change, such as discount-before-tax, alters the algorithm; changing the output label does not. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def final_price(subtotal, tax_rate, shipping):
    tax = round(subtotal * tax_rate, 2)
    return round(subtotal + tax + shipping, 2)
print(final_price(100, 0.05, 10))
```

**Expected result:** `115.0`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For problem decomposition, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Before implementation, identify which facts are input data and which are policy. A function that hardcodes mutable policy is fragile even when its first output is correct. Try a case where the given value is missing or physically impossible; decide whether to reject, default or request clarification. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 1

# Extended laboratory: computational thinking from a vague request to a testable solution

A useful first lesson in programming is that a plausible answer is not necessarily the answer to the problem that was asked. Consider a small academic club that collects registrations for workshops. Students select a session, some students receive a fee waiver, a limited number of seats are available, and the organizer wants to know who should receive confirmation emails. A beginner may immediately write a list, loop through applicants, and print their names. Yet the most consequential decisions are not syntax decisions. They are questions about what the registration system promises, which facts are known, and what events might invalidate an earlier decision. A system that accepts a hundred registrations into a room with forty seats is not correct merely because each line of its Python code executes successfully.

Start by describing the participants and the state. There is an applicant with an identifier, an event with a capacity, a registration request with an arrival time, a waiver rule, a payment state, and an observable registration result. Define whether the same applicant may register twice; whether an unpaid registration reserves a seat; whether an organizer may adjust the capacity; and what happens if a request arrives after registration closes. Two developers who disagree on one of those points may write two internally consistent algorithms that nevertheless produce incompatible results. The difference is a missing requirement, not a disagreement about Python style. A written contract converts such questions into decisions that can be reviewed before implementation.

## Decomposing the work without hiding the difficult part

Break the task into functions along meaningful boundaries. One function validates a request; one checks eligibility; one evaluates current capacity; one records an accepted registration; one assembles the notification. This decomposition does not imply that every function requires a separate file or class. It does imply that input parsing, domain rules, storage, and presentation are not silently mixed. Suppose a waiver rule changes from giving discounts to first-year students to giving discounts to financial-aid recipients. If the rule is concentrated in an eligibility function, it can change without rewriting the notification format or sorting algorithm. A good decomposition identifies which decisions tend to change together and which should remain independent.

There is an important trap in splitting a problem into many tiny functions: decomposing the code is not automatically decomposing the reasoning. If `process_registration()` delegates to `check()` and `handle()` without specifying what either function guarantees, complexity has merely been renamed. Each component needs a contract. A validator might promise that the returned record contains a nonempty identifier and a recognized session code. A capacity checker might promise only to read availability, not to reserve a seat. A persistence operation might promise an atomic transition from pending to confirmed; that last promise is stronger than a simple dictionary update when several users can register concurrently. The component boundaries should expose such differences explicitly.

Use a data-flow diagram before writing a full program. A request arrives as text, is parsed into typed values, checked against the event catalogue, evaluated under business rules, and either rejected with a reason or committed as a registration. Only after the state has been committed should the application announce an irreversible confirmation. This ordering illustrates why outputs are not merely printed strings. Sending a confirmation is an observable side effect that can become inconsistent with stored records. Even a single-user prototype benefits from stating which steps are calculations and which steps cause external effects.


## Algorithms are sequences of justified decisions

An algorithm is not just any procedure that appears to produce the desired output on one example. It must have a clearly stated input domain, a finite set of instructions, a defined result, and a correctness argument relative to that domain. Consider selecting the first available applicant from a queue of registrations. If the rule is first-come-first-served, sorting by applicant name is incorrect even if the resulting list is perfectly sorted. If the rule prioritizes accessibility accommodations, strict arrival order may also be incorrect. Algorithm design starts after the rule has been chosen, not before.

For a list of arrival times and corresponding requests, suppose the policy is to accept at most the first `capacity` eligible requests in arrival order. A simple algorithm scans the sequence once, maintains a counter of accepted registrations, and appends an eligible applicant while the counter is below capacity. Its loop invariant can be stated precisely: after processing the first `k` requests, the accepted list contains exactly those accepted by the stated policy among those first `k` requests, in arrival order, and its length is no greater than capacity. Initialization holds for an empty prefix. The next request either fails eligibility or finds capacity full and leaves the list unchanged, or succeeds and appends one eligible request. Under the policy, the invariant is maintained. At termination, all requests have been processed, so the output satisfies the rule for the complete input.

This proof is conditional. It assumes the input sequence is already in arrival order, each eligibility decision is stable during the run, and registrations are processed serially. If requests arrive concurrently and capacity is checked independently by two workers, both may observe one remaining seat and both may confirm it. No local loop invariant prevents that race condition. The system needs a transaction, a lock, a single queue consumer, or another concurrency mechanism enforcing the capacity invariant across independent executions. Identifying an assumption that invalidates a proof is part of understanding the proof, not an embarrassment to be concealed.



## Algorithms

## Algorithms: the computational contract

**Core idea.** The candidate is initialized from actual data, not an invented sentinel. The loop maintains that best is the smallest examined element. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def smallest(values):
    best = values[0]
    for item in values[1:]:
        if item < best:
            best = item
    return best
print(smallest([9, 4, 12, 2]))
```

**Expected result:** `2`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For algorithms, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Make a trace table with at least four rows: the initial state, two transitions and the final state. If a proposed shortcut skips a state, show why the output remains equivalent. The trace is a method of reasoning, not a substitute for full testing. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 2

## Correctness before cleverness

Imagine two algorithms for finding the minimum of a nonempty list. The first examines every value and maintains a running minimum. The second sorts the entire list and reads the first element. Both give the same minimum if the comparison relation is defined consistently. Their computational costs differ. A direct scan requires a number of comparisons proportional to the list length and needs constant extra space if the result is a single scalar. A comparison sort generally requires time proportional to `n log n` and may allocate additional storage, depending on the implementation. The scan is preferable if only the minimum is needed. Sorting may be sensible if an ordering is required for several later operations. The objective should be specified before describing one approach as faster.

A second comparison reveals a more subtle concern: what happens when the list is empty? Initializing a candidate minimum from the first element raises an index error. Initializing it to zero silently gives the wrong answer for a list of positive values. Returning infinity may be mathematically convenient in an optimization routine but surprising in a user-facing application. There is no universal best answer. The function should either reject an empty input with a documented error, return an optional value indicating absence, or accept a caller-supplied default. These represent distinct contracts. A test suite should make the choice visible rather than accidentally accepting whichever behavior a loop happens to produce.


## Abstraction as an engineering decision

Abstraction removes details that are irrelevant to a particular operation while preserving the details needed for correctness. In a seat allocator, the caller may need only `can_register(request, event_state)`. The caller should not have to know how payment is represented or how the waiver rule is stored. Yet the abstraction must not conceal information that a correct decision requires. If capacity checks may be stale, returning a boolean `True` without any reservation guarantee invites misuse. A better interface might return a reservation token that represents a committed allocation, or distinguish `eligible` from `seat_reserved`. Good abstractions simplify use without making false promises.

Compare a function that converts Celsius to Fahrenheit with a function that estimates thermal energy. Both accept numbers, yet their contracts are very different. The conversion `F = 9C/5 + 32` is affine: differences between temperatures scale by `9/5`, but the zero point shifts by 32. Thermal energy calculations typically require material properties, masses, and assumptions about processes. Reusing a generic function named `convert()` for both can hide those distinctions. A type or unit annotation, descriptive function name, and parameter documentation make the model clearer. Abstraction should preserve physical and semantic dimensions that are essential for reliable computation.


## Inputs are not assumptions

A program that receives `"42"` receives a string, not an integer. Converting it with `int()` performs parsing under language-specific rules. Converting `"4.2"` to an integer raises an exception rather than rounding to four. An application might permit whitespace, a plus sign, or localized digits, but these should be explicit choices. Once parsing succeeds, validation is still needed: a syntactically valid integer may be negative when a seat count must be nonnegative. Parsing answers whether the input can be represented as a value of a given type; validation answers whether that value is permitted by the application contract.

For a robust input pipeline, separate four stages. First acquire raw data without treating it as trusted. Second parse that data into an intentional representation. Third validate ranges, relationships, and uniqueness. Fourth apply the domain operation. When a stage fails, return information the caller can act upon. For example, `"capacity must be a whole number between 1 and 500"` is more useful than a generic `"invalid input"` message. It is also more honest than replacing a malformed value with a default that may allocate the wrong number of seats. Defaults are appropriate only when the domain has specified a meaningful default.



## Abstraction

## Abstraction: the computational contract

**Core idea.** The caller sees a clear predicate rather than the internal boolean expression, helping isolate business rules. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def is_eligible(age, enrolled):
    return age >= 18 and enrolled
print(is_eligible(20, True))
```

**Expected result:** `True`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For abstraction, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Test a normal input, an empty input where meaningful, a boundary input and a malformed input. Explain whether the program should return a result, raise an exception or ask for a new value. This separates mathematical domain assumptions from interface behavior. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 3

## A running example: weighted assessment

Build a small function to compute an assessment mark from homework, laboratory work, and a final examination. Suppose the policy is twenty percent homework, thirty percent laboratory work, and fifty percent final examination. Represent the weights as numbers that sum to one and restrict all scores to a documented interval such as zero through one hundred. The calculation is a weighted sum: `0.2 * homework + 0.3 * lab + 0.5 * exam`. For scores of eighty, ninety, and seventy respectively, the result is sixteen plus twenty-seven plus thirty-five, or seventy-eight. That arithmetic is the easy part. The more interesting choices are whether missing homework counts as zero, whether bonus points can exceed one hundred, how rounding should work, and whether a changed weight policy should retroactively alter published results.

A good interface takes both the scores and the policy as explicit inputs. The policy should be validated before calculating. A weight vector that sums to one point two is not valid under the stated weighted-average interpretation. Floating-point addition may yield a value very close to one without being exactly equal, so choose an appropriate tolerance for checking the sum. If exact decimal accounting matters, a decimal representation or integer basis-point weights may be preferable. A function that prints the final result rather than returning it is harder to reuse in a class statistics report or a test. Return the calculation; display it in a separate step.

The case also illustrates controlled change. If the exam weight decreases from one half to two fifths, decide which of the other components gains the remaining tenth before editing the code. Changing one number without restoring the sum-to-one invariant makes the weighting policy inconsistent. After updating the policy, rerun tests that use hand-calculated examples, including the all-zero vector, the all-maximum vector, and a case where only one component is nonzero. Those tests establish useful boundary behavior and help detect accidental swaps of component positions.


## Trace tables and counterexamples

A trace table records how an algorithm changes state. For the simple minimum-finding scan over `[9, 4, 12, 2]`, the candidate begins at nine, changes to four, remains four after twelve, and becomes two after the final element. The invariant says that the candidate is the minimum among all values examined so far. This is stronger than simply observing that the final answer is two. It describes why every intermediate update is justified and permits a correctness argument independent of this one list. Write a second trace for a list containing equal values and a third for negative values; the invariant should survive both.

Counterexamples are especially useful when an assumption is unspoken. If a function chooses the first element as the minimum and never updates on equality, that is correct for finding a minimum value but not sufficient for finding the last index of the minimum. A function designed to return an index requires a tie-breaking rule. Suppose the input is `[3, 1, 1, 4]`. A strict less-than comparison returns the position of the first one; a less-than-or-equal comparison can return the last. Neither is inherently wrong without an index contract. The failure occurs when the implementation and the intended tie policy differ.



## Input–Output Models

## Input–Output Models: the computational contract

**Core idea.** Define input units and output units explicitly. A numeric function without a documented unit convention can be mathematically correct yet scientifically unusable. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
print(celsius_to_fahrenheit(0))
```

**Expected result:** `32.0`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For input–output models, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Compare readability, asymptotic work and memory use with a plausible alternative. For small datasets, clarity may dominate micro-optimization. For huge datasets, count the operations rather than relying on a vague claim that one language construct is faster. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 4

## Design the evidence before implementation

The most useful tests arise from the claims made in a contract. For a grade converter, test the endpoints and just below or above each threshold. For a registration system, test zero remaining seats, one remaining seat, duplicate identities, invalid identifiers, events with different capacities, and concurrent requests if concurrency is supported. For a conversion function, test known reference points and a negative temperature. These are not merely random cases; each probes a specific boundary, invariant, or model assumption. Give a test a name that describes the behavior it checks, such as `reject_duplicate_registration`, instead of `test_two`.

During review, distinguish an example from a proof and a proof from an integration test. An example demonstrates one execution. A proof establishes a property for a specified set of inputs under stated assumptions. An integration test checks whether components actually interact as promised in a concrete environment. For instance, a correct seat-allocation function may still be wired to a web form that uses the wrong event identifier. Conversely, passing a few end-to-end tests does not prove that all capacity races are impossible. Reliable software uses several forms of evidence because they answer different questions.


## Failure-first exercise: the double-confirmation incident

Two registration requests arrive almost simultaneously with one seat remaining. The service checks capacity in a first step and writes a confirmation in a second step. Each request sees capacity equal to one; each then confirms the applicant. The system reports two confirmations for a single seat. Explain the failure using a timeline: worker A reads available seats, worker B reads the same state, worker A commits, and worker B commits based on an obsolete observation. The defect is not primarily a slow loop or a weak name. It is a missing atomicity guarantee between the check and the reservation.

A repair must change the state transition. In a single-process teaching example, place both the capacity check and the mutation behind one lock. In a database-backed system, use a transaction with suitable isolation or an atomic conditional update that succeeds only if capacity is still available. The output should distinguish an accepted request from a rejected request after the atomic operation. Retest with many concurrent attempts and verify that the number of confirmed places never exceeds the capacity. Even then, examine whether the test environment exercises the actual storage semantics used in deployment. A mock lock is not evidence that a remote database behaves identically.


## Final synthesis

Computational thinking is an approach to reducing ambiguity. Problem decomposition isolates responsibilities and policies. Algorithms provide steps whose correctness can be argued. Abstraction separates interfaces from internal machinery while preserving essential guarantees. Input–output models make representations, units, errors, and observable effects explicit. All four are needed even for short scripts, because complexity is not measured only by the number of lines written. A five-line program can produce an irreversible incorrect payment; a larger implementation with explicit contracts and checks can be easier to understand and maintain.

Before moving to variables and expressions, produce three artifacts for the registration case. Write a one-paragraph contract listing valid and invalid inputs. Draw the data flow from raw request to committed registration and notification. Finally, give an invariant and a set of tests that would expose a capacity violation. Those artifacts define what success means and make the implementation reviewable by someone who did not write the code. They are the bridge between an informal request and an engineering result.


### Specify an algorithm that accepts three test scores, drops the lowest and returns the average of the remaining two. Explain behavior on ties.

**Define the input contract**
Scores are three finite numbers on a documented scale. Ties are permitted, and exactly one occurrence of the minimum is dropped.

**Derive the computation**
Sort the three scores or compute (sum(scores) - min(scores))/2. The subtraction removes exactly one lowest occurrence.

**Verify**
For [80,80,100], (260-80)/2 = 90. For [0,10,20] result is 15. The algorithm requires exactly three inputs.

### Compare a sequential scan and a full sort for finding a minimum of n items.

**Scan**
Initialize current minimum with first element; compare each remaining element once. There are n-1 comparisons.

**Sort**
Comparison sorting takes O(n log n) comparisons in the general case and changes order or creates an auxiliary collection.

**Decide**
If only the minimum is needed, an O(n) scan is simpler; sorting may be justified if an ordered list is needed later.

### Give a precise input-output contract for Celsius-to-Fahrenheit conversion.

**Define**
Input is a finite numeric temperature in degrees Celsius. Output is F = 9C/5 + 32, in degrees Fahrenheit.

**Compute**
For 25°C, F = 9·25/5 + 32 = 77°F.

**Validate**
At 0°C output is 32°F and at -40°C output is -40°F. Make the unit conversion explicit in the interface.


### Applied investigation: Specification-driven decomposition and minimum scanning

Break a text-file statistics utility into a parser, a validator, a numerical accumulator and an output formatter. These are distinct responsibilities because each has a different contract. The parser converts bytes to tokens; the validator rejects malformed numbers; the accumulator applies a numeric operation; the formatter handles user-visible presentation. Merging validation and accumulation would allow a malformed token to corrupt state before an error is reported. If a design uses n separate responsibilities, neither the simulator nor the count alone proves the program is modular: cohesion, coupling, input contracts and error propagation matter.

A linear minimum scan of eight values must compare seven values with the running minimum after initializing it from the first element. Consider [8, 2, 5, 2, 9, 1, 4, 6]. After the seventh comparison the result is one. Replacing that list with a sorted list does not change the seven-comparison count if the implementation always scans the entire input. A truly empty list needs an explicit policy such as returning None or throwing a documented exception; initializing from element zero would otherwise be invalid.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.
