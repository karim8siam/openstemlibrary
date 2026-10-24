# Unit 4: Intermediate representations

*Draft; not approved for public deployment. Eight-unit manuscript with source-specific cases and independent verification pending.*

## Abstract Syntax Trees
**Abstract Syntax Trees: conceptual explanation**

An AST represents the language’s essential operations rather than every punctuation mark. For the concrete string `x + 2 * y`, a typical AST has an Add node whose children are Identifier(x) and Multiply(Number(2),Identifier(y)). Parentheses appear through tree shape; their source spans may remain in metadata for formatting and diagnostics. Typed AST nodes can carry resolved symbols, inferred types, and explicit conversion nodes. Do not smuggle arbitrary runtime values into a source AST: the compiler should distinguish syntax, semantic annotations and runtime state.

A concrete syntax tree may retain whitespace, comments and exact delimiters, making it preferable for formatters and code transformation tools. Some compilers keep a lossless tree for editing and derive a simplified AST for analysis. Tree traversals require stable invariants: expression nodes evaluate to values, statement nodes alter control flow, every identifier reference binds to a valid declaration or a recorded error, and spans nest or overlap in documented ways. Serialization requires a versioned schema if compiler caches persist across releases. Test tree invariants with random nested expressions, round-trip printing when appropriate, and mutation tests that delete a child or swap operator precedence. AST shape matters because later optimizers make assumptions about effect order; representing a call as a pure operator would make reordering unsound.

### Design investigation: AST invariants under refactoring
Specify AST classes for literals, identifiers, binary operations, assignments, calls and conditionals. Parse `a + b*c` into an Add node with Multiply on its right branch. Give every node a source span and children with consistent ranges. Rename bound variable a to q and verify that only references resolved to the same symbol identifier change. Do not rewrite an unrelated a in a nested scope or a string literal. A lossless concrete syntax representation may be necessary if a formatter must preserve comments and whitespace exactly. Intentionally delete a child from a binary node and require an AST validator to reject the malformed structure before type checking. Run a pretty-printer and reparser, then compare structure after normalizing harmless formatting differences. Explain why this is stronger than checking that the pretty-printed source merely parses without crashing.

## Control-Flow Graphs
**Control-Flow Graphs: conceptual explanation**

A control-flow graph models the paths execution might take within a procedure. A basic block is a maximal straight-line sequence with entry at its first instruction and control leaving at its terminator. A conditional branch has two successors, a return none, and an unconditional jump one. Construct blocks at function entry, branch targets and positions immediately following a transfer. The CFG should preserve unreachable blocks long enough to support diagnostics, then a reachability pass can identify dead regions. Exception edges and coroutine suspension complicate the graph and should be represented rather than ignored when those language features are supported.

Dominance formalizes path constraints. Block D dominates B when every path from entry to B passes through D. The entry block dominates all reachable blocks. A dominator tree supports SSA construction and loop analysis. Natural-loop detection typically uses a back edge from a block to one of its dominators; irreducible graphs need more general handling. Compute reachability and dominators on a small six-block example, then introduce an early return and compare the results. The CFG is not a performance graph: an edge’s existence does not specify its probability or frequency. Profile-guided compilation may add weights, but it must keep semantic correctness independent of those measurements.

### Design investigation: dominance on a diamond CFG
Create entry block B0 branching to B1 and B2, both leading to B3; B3 returns. List predecessor and successor sets. Entry B0 dominates all reachable blocks; B1 does not dominate B3 because there is a route through B2. Add a block B4 following B3 and compute its dominators. Then insert an unreachable block B5 with an edge back to B3. Depending on graph conventions, do not allow unreachable predecessors to corrupt dominance of reachable execution paths without explicitly specifying treatment. Run a fixed-point dominator algorithm initialized with entry’s set and the universe for other reachable blocks. Explain why convergence produces a graph property independent of block order. Add a loop back edge B4->B3 and identify the natural loop if B3 dominates B4. A textual source line appearing earlier is not by itself evidence of a back edge.

## Ssa
**Ssa: conceptual explanation**

Static single assignment form assigns each variable version exactly once. Suppose branches each assign `x`: the then branch writes x1 = 5, the else branch x2 = 9, and their join defines x3 = phi(x1,x2). The phi operation selects the value corresponding to the actual predecessor edge; it is not an ordinary function call that evaluates both arguments. A loop-carried value often needs a phi at the loop header, combining an initial value with a value from the back edge. Careless phi insertion either loses updates or creates operands with no incoming definition.

SSA greatly simplifies use-definition chains and sparse analyses because each use has one known definition. Common construction algorithms insert phis using dominance frontiers and rename definitions while traversing the dominator tree. Pruned SSA avoids phis for values that are not live at a join. Memory is harder: aliases and loads from mutable objects are not captured by scalar variable SSA alone. Memory SSA or explicit effect tokens can represent ordering constraints. When lowering from SSA, phi nodes become moves on CFG edges, with special care for critical edges and parallel-copy cycles. Build a test program with two branches and a loop, and verify its result before and after SSA conversion and lowering. The runtime never executes a phi instruction in the abstract sense without choosing a predecessor.

### Design investigation: phi placement and lowering
For `if test then x=11 else x=19; return x+1`, draw two branch blocks and a join block with `x3=phi(x1,x2)`. The return is twelve or twenty according to the taken branch. Show how an interpreter chooses the incoming operand by predecessor edge rather than evaluating both branch results. Extend the program to a loop updating x and introduce a loop-header phi. Verify that each phi has exactly one operand for every incoming predecessor and that its operands are defined along the relevant edges. Lower phi to copies: on the then predecessor assign x3=x1; on the else predecessor assign x3=x2. If an edge is critical, split it as needed. Construct a pair of parallel copies x1<-x2 and x2<-x1 and show why using a temporary is essential. A correctness checker should catch a swap regression through the returned values.

## Symbol Tables
**Symbol Tables: conceptual explanation**

Symbol tables connect names, declarations, types, linkage and storage to the appropriate part of a source program. A front end may use nested hash maps or persistent scopes; the important invariant is that a lookup returns the nearest visible declaration permitted by the language. Function overloading requires a set of candidates, often filtered by arity and type compatibility rather than a single mapped declaration. Separate a source spelling `count` from a stable symbol identifier so shadowing does not cause accidental merges during optimization.

Symbols may pass through several identities. A local source variable becomes a resolved binding, then an SSA value, then perhaps a stack slot or machine register. A linker-visible external name follows a different path and requires visibility, versioning and name-mangling rules. Incremental compilers must invalidate dependent symbol resolutions after an edit while reusing unaffected work. A source rename should not change references outside its binding scope, and a refactoring tool should detect capture when a new name shadows an existing declaration. Construct two modules that export the same short name, import one with an alias, and define a local name matching the other. Explain each lookup using namespace, module scope and local scope, then test the exact diagnostic for an ambiguous import.

### Design investigation: symbol identity and namespace collision
Create a module exporting function `parse`, another module exporting function `parse`, and a client importing one as `parseText`. Add a local variable also spelled parse inside a function. Define precedence among local declarations, explicit imports and qualified module references according to the example language. Assign stable identities `ModuleA.parse`, `ModuleB.parse`, `Client.local.parse` and record every reference’s chosen identity. Change the local variable’s name and check that external imports are untouched. Now import both parse functions without qualification; the resolver should either report ambiguity or apply a documented overload rule based on types. Include tests for an unresolvable name and an illegal duplicate declaration in the same scope. Finally map source identifiers to generated internal labels and demonstrate why symbol identity must survive despite name mangling and register allocation.

## Integrated Case Study and Model Limitations
Translate `if p then x=1 else x=2; print(x)` into basic blocks. The branch produces two definitions, and the merge block needs a phi value `x3 = phi(x1,x2)` under SSA notation. The phi expression selects the value associated with the actual predecessor edge; it does not evaluate both branches at runtime. Identify the control-flow edges and which definitions dominate their uses. A symbol table records whether p and x are in scope and can annotate variable types. If a pointer aliases x through memory, pure SSA for scalar values does not automatically handle writes through that pointer.

### Laboratory: lower an imperative function through multiple IRs

Start with a source function that initializes a sum and loops through an array. Inside the loop, it branches on whether the current element is positive and adds positive values to the sum. Represent this in an AST with explicit statements, expressions and spans. A semantic analyzer resolves the accumulator and loop-index variables and assigns types. Lower the AST to a three-address IR containing basic blocks with a single terminator each. Verify that every block has exactly the declared successors and that each target exists. An omitted branch target is a malformed IR, not a runtime edge case.

Construct a CFG with entry, loop header, condition, then branch, increment and exit blocks. For each block, enumerate predecessors and successors. Compute reachable blocks starting from entry; deliberately insert an unreachable block and check that the reachability pass finds it without changing the behavior of the reachable program. Compute dominators iteratively and draw a dominator tree. Identify the loop back edge from increment to header and explain why its target dominates its source. A compiler treating any edge to an earlier textual block as a back edge is relying on layout rather than graph semantics.

Convert the accumulator and index to SSA. The loop header needs phi nodes that combine entry values with the values from the back edge. The then branch may update the accumulator while the else path leaves it unchanged, requiring a merge or appropriate phi arrangement. Label each definition uniquely, and for every use identify its reaching definition. An SSA validator should reject duplicate definitions, undefined uses, malformed phi arity and incoming operands associated with the wrong predecessor. Demonstrate the validator by intentionally swapping two phi incoming values in a diamond CFG where the two values differ; the resulting program should fail semantic comparison.

Implement a simple constant propagation pass and dead-block elimination. One candidate optimization replaces an always-true comparison with an unconditional jump. Prove the comparison is side-effect-free and its operands fixed at that program point. Another candidate removes a multiplication whose result is unused; if the multiplication is ordinary integer arithmetic it may be safe, but an operator implemented as a call could have effects. Restrict the pass to operations whose semantics the optimizer understands. Dump IR before and after passes and run both through an independent reference interpreter on boundary inputs such as empty arrays and negative values.

Finally lower SSA out of the program. Each phi needs predecessor-specific copies, inserted on edges or in split blocks. Multiple phi copies may need parallel assignment; naively executing copies sequentially can destroy an input value in a cycle. Describe a correct schedule using a temporary where required. Check that control-flow edges, source span mapping, and results survive the full AST -> CFG -> SSA -> optimized CFG -> low-level IR pipeline. The deliverable is not merely a graph drawing: it is a reproducible transformation with invariants, failing tests and a clear account of which statements are allowed to reorder.

### Failure clinic: valid-looking SSA with wrong phi edges

An optimizer converts a branchy source function to SSA. Every variable has one definition, every use points to a defined symbol, and the visual CFG looks reasonable. Yet a join phi uses incoming values in block-name order while the runtime’s predecessor list is in edge-insertion order. The values are swapped on one branch. A simple syntactic SSA validator passes; numerical differential tests on one branch fail. Identify the missing invariant: phi operands are keyed to predecessor edges, not merely listed in an arbitrary order. A correct validator checks correspondence between operands and actual incoming edges.

Build a discriminating source program where one branch defines x=11 and the other x=19, then returns x+1. Both branch conditions must be exercised. Make a parallel copy schedule for phi lowering, including a case where two destinations exchange values. A naive sequence `a=b; b=a` loses the original a. The correct lowering preserves both old operands, possibly using a temporary or scheduling a copy cycle carefully. Explain why critical edges may need to be split before placing predecessor-specific moves.

The project also computes dominators using a faulty initialization that starts every nonentry reachable node with the empty set. A standard iterative must-analysis for dominators starts nonentry nodes with all reachable blocks and intersects predecessor sets. With an incorrect initial value it may converge to an underapproximation and cause missing phi placements. Test a diamond CFG, a simple loop and a graph with unreachable blocks. Compare the result against exhaustive enumeration of entry-to-block paths for small graphs. Graph test cases, not a single hand-drawn flowchart, should justify the implementation.

Finally inspect incremental compilation. A changed source branch invalidates one CFG block but leaves a cached use-definition graph from the previous version. The validator may see internally consistent metadata with stale symbols. Record content hashes or revisions for cached IR stages, and invalidate all dependent analyses when a predecessor, definition or type changes. State precisely which analyses must be recomputed after a CFG edit: reachability, dominance, phi placement and dataflow facts can all change. A source-to-IR pipeline needs identity and lifecycle discipline as much as it needs graph algorithms.

### Worked comparative study: IR invariants across a compiler pipeline

A compiler typically passes through a series of representations, each simplifying one kind of reasoning while preserving enough information for later stages. The source AST distinguishes declarations and expressions. A typed AST assigns symbols and types. A CFG exposes control-flow decisions. SSA gives scalar variables unique definitions. Lower-level IR makes memory effects, stack slots and machine constraints explicit. No single representation is ideal for all analyses. Conflating them leads to errors: a source identifier might map to several SSA versions, while a phi node in SSA has no direct source-language spelling.

Suppose a typed AST contains a loop with a carried counter and an early return. In the CFG the return block has no ordinary successor. At the loop header the counter needs a phi combining its initial and incremented values. A dataflow analysis should consider only reachable predecessor edges under its chosen graph model. If an optimization removes an edge, phi operands must be updated accordingly; an SSA validator that checks unique definitions but ignores predecessor correspondence is incomplete.

Introduce an effectful load from a mutable array. Ordinary scalar SSA can track the index variable but cannot conclude the loaded memory value is constant unless alias and memory-effect information supports that claim. A memory token, memory SSA or explicit ordering edges can encode that a store may invalidate a previous load. An IR design should make such dependencies visible rather than relying on an optimizer to remember unspecified side effects.

Create stage-specific validators. The AST validator checks node arity and source spans. The type validator checks each operator's operand and result types. The CFG validator checks one terminator per block and valid successor IDs. The SSA validator checks definitions, dominance and phi predecessor mapping. The low-level verifier checks register classes, calling convention constraints and legal instruction patterns. Add one deliberately malformed example at each stage and require a localized failure. A pipeline that rejects a malformed IR immediately is easier to debug than one that crashes during code generation long after the original defect. Include content hashes or stage revisions in incremental caches to prevent stale analysis facts from being reused after source edits.

### Unit review: preserve identities through transformation

Trace one source variable from a lexical declaration through its symbol-table identifier, AST use sites, CFG definitions, SSA versions and eventual machine location. These objects are related but not interchangeable: one source binding can have several SSA definitions, and a machine register can hold many unrelated values over time. For every lowering stage, state what information is lost and what metadata must be retained for diagnostics or debugging. Build a validator that catches a wrong phi predecessor and a stale cached dominance relation after a CFG update. Do not equate a well-formed serialization with correct semantics: execution tests must cover both branches of control flow. A careful IR workflow treats each representation as a contract with independently testable invariants.

### Worked question: Build a control-flow merge
Lower `if p then x=4 else x=9; return x` to blocks and give the SSA join expression.

**Set up definitions and premises**
Create an entry/condition block with a conditional branch to Then and Else. Then defines x1=4, Else defines x2=9, and both transfer to Join.

**Derive the result**
At Join define x3=phi(Then:x1, Else:x2) using predecessor-tagged operands. Return x3. The phi selection is conditional on which edge actually reached the join, not a normal function call evaluating both values.

**Validate limits and interpretation**
Test both p=true and p=false: the expected results are four and nine. A bug swapping phi operand order would be detected only if both paths are tested. Phi lowering must insert predecessor-specific copies.

**Answer:** SSA join x3=phi(Then:x1,Else:x2); result 4 or 9.

### Worked question: Compute dominators
For Entry branching to A or B and both feeding Join, name the dominators of Join and explain why A is not one.

**Set up definitions and premises**
By definition D dominates a block X if every entry-to-X path passes through D. There are two paths to Join: Entry->A->Join and Entry->B->Join.

**Derive the result**
Entry lies on both paths and therefore dominates Join. A lies on only one path, so it does not dominate Join. Join trivially dominates itself under the standard reflexive definition.

**Validate limits and interpretation**
Adding a block after Join makes Join a dominator of that later block if all paths to the later block pass through Join. This computation uses graph paths, not textual position or frequency of execution.

**Answer:** Dominators of Join are Entry and Join; A and B do not dominate it.

### Worked question: SSA parallel copies
Explain why lowering simultaneous copies `a_new=b_old; b_new=a_old` as sequential assignments without a temporary is wrong.

**Set up definitions and premises**
Suppose a_old=3 and b_old=8. Simultaneous semantics require a_new=8 and b_new=3. If sequential code first sets a=b, a becomes eight.

**Derive the result**
The next statement b=a reads the already overwritten a, setting b to eight. Both registers now contain eight, losing the original three.

**Validate limits and interpretation**
Use a temporary to preserve an old value: t=a; a=b; b=t. This produces eight and three. More general phi-resolution can require scheduling cycles of parallel copies and splitting critical CFG edges.

**Answer:** Use a temporary or correct parallel-copy scheduling; the required results are a=8,b=3.
