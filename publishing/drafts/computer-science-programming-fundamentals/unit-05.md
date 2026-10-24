# Unit 5: Data collections

## Strings

## Strings: the computational contract

**Core idea.** Unicode text, whitespace, normalization and case folding may affect matching. State whether punctuation and locale matter. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
text = '  DNA, RNA, DNA  '
cleaned = text.strip().lower()
print(cleaned.count('dna'))
```

**Expected result:** `2`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For strings, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Before implementation, identify which facts are input data and which are policy. A function that hardcodes mutable policy is fragile even when its first output is correct. Try a case where the given value is missing or physically impossible; decide whether to reject, default or request clarification. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 1

# Extended laboratory: choosing and reasoning about data collections

Data structures determine how information can be accessed, updated, ordered, and related. A program that stores only one temperature reading can use a numeric value; a program that stores a thousand readings with timestamps needs a representation for a collection of related measurements. Choosing that representation affects correctness as well as performance. If a dataset contains duplicate course identifiers, storing the identifiers in a set will erase information about how many times each appeared. If input order records the sequence of events, sorting it may destroy evidence. The most important question is not which structure is fashionable but which properties the application must preserve.

## Strings are sequences with linguistic and technical constraints

A string is a sequence of Unicode code points in Python, not necessarily a sequence of human-perceived characters. Some visible characters can be represented as one code point or as a base character combined with a mark. Two strings can look identical on screen while having different internal representations. This matters when text is used as a search key, an identifier, or a validation input. A system matching names or academic titles should state whether case differences, punctuation, spacing, and normalization are significant.

For simple text processing, methods such as splitting on whitespace and converting case are useful, but they embody assumptions. A phrase like `"A B A C"` splits cleanly into tokens by spaces. Scientific text, names, formulas, and multilingual writing may require a more careful tokenizer. Splitting a sentence on spaces does not reliably remove punctuation; treating a hyphenated expression as one token or two may affect search counts. Case conversion also has language-specific edge cases. When exact equality matters, decide whether normalization is performed before comparison and whether the original value is preserved for display.

Strings are immutable. A function that appears to modify a string generally constructs a new string. This contrasts with lists, which can be changed in place. The difference affects how memory and aliases behave. Repeatedly concatenating strings in a large loop may allocate substantial intermediate data depending on the interpreter and pattern. Joining an existing sequence of fragments is often clearer and more predictable when building a long result. As with any performance claim, measure a representative workload before treating a small implementation detail as a major bottleneck.


## Indexing requires a position convention

Python sequences use zero-based indices. The first element of a list has index zero; the last has index `len(values)-1` for a nonempty list. Negative indices count backward from the end. These conventions make some operations concise but cause errors when a program's domain uses one-based numbering. A textbook may refer to chapter one while a program stores the chapter at index zero. Convert explicitly at the interface. Do not mix user-visible chapter numbers and storage indices in the same calculation without documenting the conversion.

A slice such as `values[2:5]` includes indices two, three, and four but excludes index five. The half-open convention simplifies length calculations because the slice contains `5-2` positions. It also supports adjacent partitions without overlap: `values[:k]` and `values[k:]` together cover the sequence. Off-by-one errors arise when developers treat the end index as inclusive or forget that an empty slice is a legitimate result. Test boundaries at index zero, sequence length, and empty sequences.

An array or list index also carries a precondition. `values[0]` fails when a sequence is empty. A function computing the smallest element of a list should either reject emptiness or return an explicit absence indicator. Writing code that never encounters an empty list in one demonstration is not proof that the function supports every caller. Data structure semantics and input contracts have to be considered together.


## Lists support order and duplicates

Python lists are ordered collections that preserve duplicate elements and permit mutation. They are appropriate for event sequences, readings, records awaiting processing, and many other tasks. Appending to the end is typically efficient for Python's dynamic-array implementation, although occasional resizing can allocate additional storage. Removing the first element requires shifting subsequent elements, so repeated front removals can become expensive. If a program needs efficient insertion and removal at both ends, a deque may be more appropriate.

Lists do not automatically enforce uniqueness, sorting, or a schema. If an application stores registrations as dictionaries in a list, nothing prevents two dictionaries from having the same participant identifier unless validation adds that rule. Finding a particular identifier may require scanning records one by one. For a small roster this may be adequate and easy to understand; for repeated lookups over a large dataset, a dictionary keyed by identifier can reduce average lookup work. The decision depends on access patterns, not just collection size.

Mutation introduces aliasing risks. Suppose `current = original` and the program updates `current[1]`. Both names refer to the same list and the original changes. A shallow copy avoids sharing the outer list but may still share nested dictionaries or lists. If a transformation must not alter source records, state whether nested objects may be shared and test that property. Conversely, copying a huge dataset unnecessarily consumes memory. Use copying as a deliberate decision about ownership, not a reflexive attempt to avoid understanding references.



## Arrays

## Arrays: the computational contract

**Core idea.** An indexed sequence uses zero-based positions in Python; negative indices count from the end. Index errors need deliberate handling. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
values = [10, 20, 30]
values[1] = 21
print(values[-1], values[1])
```

**Expected result:** `30 21`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For arrays, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Make a trace table with at least four rows: the initial state, two transitions and the final state. If a proposed shortcut skips a state, show why the output remains equivalent. The trace is a method of reasoning, not a substitute for full testing. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 2

## Dictionaries map keys to values

A dictionary represents a relationship from keys to associated values. For a word-frequency counter, each word is a key and its occurrence count is the value. When processing `red, blue, red, green, blue, red`, the final mapping contains counts three, two, and one respectively. The sum of counts should equal the number of processed tokens, which gives an independently checkable invariant. Unlike a list, the dictionary does not represent one entry per observation once counts have been aggregated. Aggregation preserves some questions, such as frequency, while losing original sequence information.

Dictionary lookup is based on hashing and equality. Under ordinary implementation and workload assumptions, insertion and lookup often have expected constant time. That expectation is not a guarantee against every pathological input, nor does it mean that hashing is a cryptographically secure operation. A dictionary key must satisfy hashability requirements. Mutable lists are generally not suitable as keys because their contents can change in ways that would undermine stable hashing. An immutable tuple can be used as a composite key when all its elements are hashable.

Dictionary keys should correspond to actual identity rules. Using a person's name as a unique key can merge two different people who share a name. Using a normalized course title can accidentally merge distinct courses with similar names. A stable identifier is often preferable when the domain provides one. Where identifiers arrive from outside systems, validate their format and uniqueness and decide what to do when conflicts occur. The data structure makes lookups convenient; it does not establish the correct identity policy by itself.


## Sets and uniqueness

A set holds unique elements. It is useful for membership testing, removing duplicates when multiplicity does not matter, and comparing groups through union or intersection operations. Yet converting a list to a set changes its meaning. If a student attends the same workshop three times, a set of workshop names records only that attendance occurred, not its count. A frequency dictionary is more appropriate when multiplicity matters. If order matters, a plain set may also be unsuitable as a replacement for a sequence.

Consider two registration lists that may contain repeated student identifiers. Converting each list to a set before comparing membership is useful for asking who participated in both events. It is not sufficient for calculating total registrations, because duplicates are removed. Define the question before choosing the representation. Many data-processing mistakes arise from using an operation that is mathematically correct for a different question.


## Choose structures from operations

A practical selection process begins with a table of required operations. Does the application frequently retrieve by index, search by key, append at the end, remove from the front, preserve insertion order, count duplicates, or query sorted ranges? A list is often suitable for indexed access and iteration. A dictionary is suitable for key-based association. A set is suitable for unique membership. A deque is suitable for queue-like operations. Other specialized structures can be justified when the workload requires them. No single container dominates every dimension.

Evaluate both expected complexity and operational costs. A hash map may use extra memory for its internal table, while a linear list scan may be sufficient for a few dozen items. A sorted list supports binary search but insertion can require shifting elements. A tree-based structure may maintain ordering with different trade-offs, although it is not part of Python's basic built-in collection set. Selecting a structure requires an understanding of the application workload, available libraries, and failure modes.



## Lists

## Lists: the computational contract

**Core idea.** Appending is efficient for dynamic arrays, but repeatedly removing the first element shifts remaining values and can be costly. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
items = ['a', 'b']
items.append('c')
print(items.pop(0), items)
```

**Expected result:** `a ['b', 'c']`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For lists, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Test a normal input, an empty input where meaningful, a boundary input and a malformed input. Explain whether the program should return a result, raise an exception or ask for a new value. This separates mathematical domain assumptions from interface behavior. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 3

## Case study: a course library catalogue

Design a catalogue containing course ID, title, department, and publication state. The system must list courses in display order, retrieve a course quickly by ID, and count courses by department. One practical design stores a sequence for display order and a dictionary mapping IDs to course records. The records themselves can be dictionaries or structured objects. A separate dictionary of department counts can be derived when needed or maintained with careful updates. Maintaining two indexes means operations must preserve consistency: adding a course should update both the display sequence and the ID mapping, and deleting one should remove it from both.

Suppose course 201 is added twice by accident. The ID dictionary would keep one entry if the second replaces the first, while the display list might contain two. That inconsistency demonstrates why redundant representations require deliberate invariants. A safe insertion function should check whether the identifier already exists, then update all related structures as one logical operation. In a database-backed catalogue, corresponding constraints and transactions should enforce the relationship. In a small in-memory program, assertions and tests can check that list identifiers are unique and match dictionary keys.

For a search feature, decide whether title matching is exact, prefix-based, or token-based. An exact dictionary lookup works for stable IDs; it is not enough for fuzzy title search. A straightforward case-insensitive substring search over titles may be acceptable for a small catalogue. Before scaling, measure expected searches, collection size, and memory available for an index. Do not describe a search implementation as comprehensive when it cannot account for spelling variants, abbreviations, or multiple languages.


## A frequency counter with independent checks

Consider the input words `['red','blue','red','green','blue','red']`. Initialize an empty dictionary. For each word, read the current count or zero, add one, and store the result. After all six iterations, red has count three, blue two, and green one. The total of all frequency values is six. This provides a simple invariant that every processed token contributes to exactly one count. If the sum differs from input length, a token was ignored or counted twice, assuming the contract is to count every element.

Now change the input to a phrase with punctuation and inconsistent capitalization. Should `"Red"` and `"red"` count as the same word? Should `"red,"` retain the comma as part of its key? The counting algorithm remains a dictionary update, but tokenization and normalization change the reported frequencies. For reproducible analysis, record those decisions as part of the processing pipeline and retain enough input information to audit them. A correct counter can still answer the wrong linguistic question if preprocessing is unspecified.


## Structured records and schema validation

A list of dictionaries is flexible, but flexibility permits missing keys and inconsistent types. One record might have `score` as an integer while another stores the same field as a string. A robust program validates records at entry, including required fields, numeric ranges, and uniqueness constraints. Typed data classes or schema libraries may help express these rules, but the underlying logic remains a domain contract. A schema cannot infer whether an attendance score is supposed to be a percentage or a count; that semantic rule must be provided by the designer.

For a dataset of laboratory observations, represent a reading and its unit together or enforce a documented unit for the entire column. Include a timestamp or sequence number when observation order matters. Missing measurements should have a distinct representation from zero. Downstream functions can then compute aggregates without silently interpreting malformed records as valid numbers. The strongest benefit of structured data is not convenience; it is the ability to check assumptions consistently.



## Dictionaries

## Dictionaries: the computational contract

**Core idea.** Dictionary lookup depends on hashing and equality. Do not rely on hashing as a cryptographic integrity primitive. The primary obligation of a program is to implement an explicit input–output contract. State its accepted inputs, its observable outputs, and assumptions about ordering, numeric ranges or persistence. If a program has side effects, include them in the contract: displaying output, mutating memory and writing to a file are not equivalent to returning a value.

**Executable Python example:**

```python
counts = {}
for word in ['blue','red','blue']:
    counts[word] = counts.get(word, 0) + 1
print(counts['blue'])
```

**Expected result:** `2`. Trace the program without executing it, paying attention to evaluation order, intermediate state, exceptions and the meaning of each name. Then execute it in Python 3. When a snippet contains commented integration lines, place them in the described module context before running.

**Underlying reasoning.** Computational correctness has several layers. A mathematical idea must match the requested problem; the algorithm must implement the idea; the code must implement the algorithm; and the input and output interface must preserve the intended meaning. A failure in any layer can produce a plausible looking result. For dictionaries, first describe the invariant or property that should remain true. Construct a small counterexample that would violate the property if a step were removed or reordered.

**Practical lab.** Compare readability, asymptotic work and memory use with a plausible alternative. For small datasets, clarity may dominate micro-optimization. For huge datasets, count the operations rather than relying on a vague claim that one language construct is faster. Ask a classmate to describe the result using only the contract rather than the implementation. If that description is ambiguous, improve the naming, parameter definitions or documentation. Treat performance as a measurable claim: count iterations, allocations or calls before speculating about speed.

**Reflection.** How would you adapt this example to values supplied through a browser or a file rather than literals in source code? Separate parsing from computation so the central function can be unit tested. Identify a condition under which the present example is intentionally incomplete and what evidence would justify extending it. Understand these limitations before using the same technique in scientific calculations or production applications.

---

### Extended case study, part 4

## Iteration order and reproducibility

Python dictionaries preserve insertion order in modern versions, but insertion order is not automatically a meaningful scientific order. A dataset assembled from several files may reflect file processing order rather than chronological order. When a report requires ranking by score or sorting by time, specify the sort key explicitly. If equal keys are possible, decide whether original order should be preserved or whether a secondary key is needed for deterministic output. Stable, deterministic results make tests and comparisons across runs more reliable.

Parallel processing and distributed systems introduce further challenges. If data arrives from independent workers, arrival order may vary from run to run. An algorithm that produces different results depending on arrival order may require sorting by a stable event timestamp or identifier before aggregation. Sometimes order is irrelevant and a commutative aggregation such as integer counting is safe; sometimes order changes the meaning, as in a financial ledger. Understanding a data structure includes understanding which reorderings preserve the problem's semantics.


## Failure-first exercise: the duplicate-record bug

A student management script stores unique students in a dictionary keyed by lowercase names. Two students have the same name. Adding the second silently overwrites the first, and an attendance report undercounts the class. The dictionary performed exactly the operation requested by its key policy. The error is choosing a key that does not encode unique identity. Repair the representation by introducing stable student identifiers, storing names as ordinary attributes, and verifying that duplicate identifiers are rejected or resolved explicitly. Test two students with the same name and one student whose name spelling changes.

The exercise also exposes why automatic normalization requires judgment. Lowercasing can improve case-insensitive search, but it is not an identity guarantee. Removing punctuation or whitespace can merge otherwise distinct identifiers. For records with legal or personal consequences, keep the original values and the validated identifiers separate. A search index and an identity key may legitimately use different transformations.


## Final synthesis

Strings, lists, dictionaries, sets, and other containers each preserve different properties. The right choice follows from the operations, identity rules, ordering needs, and failure conditions of the application. Data structure correctness includes schema validation, mutation ownership, handling of duplicates, and consistency among related indexes. Big-O notation is useful but does not replace a workload-specific design decision. When a data-processing operation becomes difficult to explain, inspect what information the chosen representation has discarded and what hidden assumptions the algorithm makes about that information.

For practice, represent a small OpenSTEM course catalogue in at least two ways. List the required queries, show the update operations, and write an invariant linking the representations. Then insert a duplicate ID, a duplicate title, and a malformed record. Explain which conditions should be rejected and which are legitimate. The answer should follow from the catalogue's requirements, not merely from the behavior of Python's built-in containers.


### Analyze lookup by linear scan versus dictionary membership for 10,000 keys.

**List**
Worst-case linear search checks all 10,000 keys, so time grows proportionally to n.

**Dictionary**
Hash-table lookup is expected O(1) under typical implementation assumptions, not an unconditional worst-case promise.

**Trade-off**
Hash maps use additional memory and require hashable keys; for small data or order-sensitive workflows a list may remain suitable.

### Trace list operations after append and pop(0).

**Start**
Begin with [a,b]. Append c to obtain [a,b,c].

**Remove**
pop(0) returns a and shifts the remaining items to obtain [b,c].

**Evaluate**
Repeated front removals from Python lists take O(n) per removal; collections.deque supports efficient end operations.

### Compute frequencies of words [red, blue, red, green, blue, red].

**Initialize**
Start with an empty dictionary mapping a word to its integer count.

**Update**
Each observed word increases its existing count by one or starts at one.

**Verify**
Final counts: red=3, blue=2, green=1. Their sum 6 equals the number of tokens processed.


### Applied investigation: Collections, search contracts and hashing

A linear search through n values may inspect every element when the target is absent. In a sorted array, binary search reduces comparison count but relies on the sorted-order invariant. A hash table has a different contract: lookup quality depends on how keys are mapped to buckets, collision resolution and the load factor. An average constant-time claim should explicitly name its hashing assumptions and cannot be transferred to adversarial input uncritically.

Compare a list of eight values with a dictionary indexing those values by unique key. If keys repeat, the dictionary may overwrite a prior value whereas the list retains both occurrences. A stable specification must say whether duplicate keys are allowed and which value wins. Hash equality also does not establish object equality, so collisions still require an equality check. Add a test for insertion, replacement, lookup of a missing key and deletion; merely displaying the current bucket positions would not prove all operations correct.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.
