# Algorithms — Unit 6: Graph algorithms


## Shortest Paths

**Core model — Shortest Paths**

A shortest-path algorithm must match edge-weight conditions. BFS handles unweighted edges, Dijkstra requires nonnegative weights, and Bellman–Ford handles negative edges when no reachable negative cycle defeats finite distances.

**Original worked illustration**

On edges A->B=2, A->C=10, B->C=3, the shortest distance from A to C is 5 through B. Dijkstra settles A, then B, then C.

**Boundary conditions and checks**

A negative edge can make an already settled Dijkstra distance wrong; always state the weight-domain assumption.

**Connections in this unit**

The adjacent subjects are Flows, Matching, Graph Decomposition. They are studied alongside Shortest Paths because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

A shortest-path algorithm solves a precisely specified graph problem: find a minimum-total-weight route under the chosen directedness and edge-weight assumptions. Breadth-first search finds minimum-edge-count paths in unweighted graphs, while Dijkstra's algorithm handles nonnegative weighted edges. Bellman–Ford permits negative edge weights and can detect negative cycles reachable from the source. A path tree computed from one source is not a minimum spanning tree. The former optimizes distances from a root; the latter optimizes the sum of installed undirected edges across a connected graph. Mixing the two objectives leads to incorrect network-design decisions.

### Derivation and worked trace

Let directed edges be A→B with cost 2, A→C with cost 9, B→C with cost 3, B→D with cost 8, and C→D with cost 1. Dijkstra begins with distance A=0 and other distances infinite. Relaxing A gives B=2 and C=9. Settling B improves C to 5 and sets D to 10. Settling C improves D to 6. The best A-to-D path is A-B-C-D with weight 2+3+1=6. Trace both tentative and settled states to distinguish a candidate bound from a final optimal distance; the nonnegative-edge assumption ensures settled distances cannot later decrease.

### Counterexample and failure diagnosis

Negative edges can invalidate Dijkstra's finalization rule. Consider A→B of cost 2, A→C of cost 5, and C→B of cost -10. Dijkstra may finalize B at distance two before visiting C, even though the true shortest path to B has cost -5 through C. Bellman–Ford's repeated relaxations can find that improvement if there is no relevant negative cycle. When a reachable negative cycle can be traversed arbitrarily many times before reaching the target, a finite shortest-route optimum may not exist at all. Your algorithm should report that limitation, not a fabricated finite path.

### Applications, engineering constraints and validation

In real routing, weights can represent travel time, monetary cost or reliability transformations. Time-dependent road conditions may violate a static-weight model. Multiple objectives such as minimizing both latency and toll create Pareto frontiers rather than one scalar shortest path. For testing, independently enumerate simple paths on a tiny directed graph when no negative cycles exist, then compare computed distances and parent pointers. Confirm that the parent chain actually reconstructs a valid route and handles unreachable vertices explicitly.

## Flows

**Core model — Flows**

A flow network has directed capacities, flow conservation at internal vertices, and a source and sink. Augmenting paths improve feasible flow; the max-flow/min-cut theorem certifies optimality.

**Original worked illustration**

If s->a has capacity 3, a->t has 2, s->b has 2 and b->t has 2, then total flow 4 is feasible and the t-side cut has capacity 4.

**Boundary conditions and checks**

Residual reverse edges are not decorative: without them an algorithm may be unable to undo an earlier routing choice to reach the maximum.

**Connections in this unit**

The adjacent subjects are Shortest Paths, Matching, Graph Decomposition. They are studied alongside Flows because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

A flow network assigns nonnegative capacities to directed edges, fixes a source and sink, and asks for the largest feasible rate transported through the network. Every internal vertex conserves flow: the sum entering equals the sum leaving. The max-flow/min-cut theorem states that the maximum achievable source-sink flow equals the capacity of a minimum source-sink cut. An augmenting-path algorithm maintains a residual network whose edges record where flow can increase and where previously sent flow may be canceled. Reverse residual edges are essential; omitting them can trap an algorithm in a nonoptimal routing choice.

### Derivation and worked trace

Consider edges s→a capacity 3, s→b capacity 2, a→t capacity 2, a→b capacity 1, and b→t capacity 3. Sending two units s-a-t and two units s-b-t achieves four. One additional unit can use s-a-b-t, yielding total five. The outgoing capacity of the source is 3+2=5, so no flow can exceed five; this constructive feasible flow meets the cut bound and is optimal. Verify conservation at a: three units enter, two leave to t and one to b. At b, two enter from s and one from a; three leave to t.

### Counterexample and failure diagnosis

Do not infer maximum flow from the sum of capacities on arbitrary paths, because paths may share bottleneck edges. Likewise, a saturated edge does not prove the whole network is optimally saturated. For Ford–Fulkerson with real irrational capacities, arbitrary augmenting-path choices require care; Edmonds–Karp's breadth-first residual paths give a polynomial bound when capacities are represented suitably. A reverse residual edge is not an extra original pipeline. It encodes permission to undo part of an earlier flow assignment while maintaining feasibility.

### Applications, engineering constraints and validation

Flow models serve bandwidth allocation, bipartite matching, transportation and image segmentation, but capacity interpretation is central. If edges have costs as well as capacities, a min-cost flow formulation may be necessary. If indivisible units are required, integrality of solutions follows for integer-capacity standard networks under appropriate algorithms, but this property may fail in generalized multicommodity problems. Test conservation, capacity bounds and cut equality on tiny graphs rather than trusting only the final numeric value returned by an implementation.

## Matching

**Core model — Matching**

A matching is a set of edges with no shared endpoints. In bipartite graphs, augmenting-path search grows the matching by alternating between unused and used edges.

**Original worked illustration**

With left vertices L1,L2 and right R1,R2, edges L1-R1, L1-R2, L2-R1 admit matching {L1-R2,L2-R1} of size two.

**Boundary conditions and checks**

Selecting each left vertex's first available neighbor without revisiting earlier choices may stop at size one; augmenting paths correct that failure.

**Connections in this unit**

The adjacent subjects are Shortest Paths, Flows, Graph Decomposition. They are studied alongside Matching because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

A matching is a set of graph edges with no shared endpoint. In a bipartite graph it can represent assignments between applicants and positions, machines and tasks, or students and projects. An augmenting path alternates unmatched and matched edges and begins and ends at unmatched vertices. Flipping the membership of its edges increases matching cardinality by one. Berge's characterization says a matching is maximum if and only if there is no augmenting path. Greedily accepting an available edge gives a maximal matching but not necessarily a maximum matching.

### Derivation and worked trace

Let left vertices be L1,L2 and right vertices R1,R2. Available edges are L1-R1, L1-R2, L2-R1. A naive greedy rule choosing L1-R1 first leaves L2 unmatched if it does not revisit choices, producing size one. An augmenting path L2-R1-L1-R2 switches the first assignment to L1-R2 and assigns L2-R1, producing a matching of size two. All vertices are now matched, so two is clearly optimal. This small example shows why alternating paths are not just implementation machinery: they supply the essential global correction to local decisions.

### Counterexample and failure diagnosis

Hall's theorem gives another structural view of perfect matching on the left: every subset S of left vertices must collectively have at least |S| neighboring right vertices. If three students can only choose the same two projects, no perfect assignment exists for those three, regardless of how clever the search is. When capacities allow a position to serve multiple people, the model becomes a b-matching or flow network. When preferences carry costs, maximum cardinality alone may fail to express the objective; maximum-weight bipartite matching is different.

### Applications, engineering constraints and validation

A matching implementation should maintain symmetry between mate pointers, never assign one endpoint twice, and verify every selected edge is present in the input graph. Test empty sides, isolated vertices, complete bipartite graphs, multiple possible maximum matchings and a graph requiring a nontrivial augmenting path. Enumeration over all edge subsets is feasible for tiny graphs and provides an independent optimal-cardinality oracle. Document whether duplicate edges are permitted and whether the graph is directed or undirected in storage.

## Graph Decomposition

**Core model — Graph Decomposition**

Graph decomposition separates a large problem into structural pieces such as connected components, strongly connected components or biconnected blocks. The definition of connectivity depends on directedness.

**Original worked illustration**

Edges 1->2,2->1,2->3 produce SCCs {1,2} and {3}; the condensation graph has one arrow from the first component to the second.

**Boundary conditions and checks**

A DFS traversal forest alone does not identify strongly connected components unless finishing order or low-link invariants are used correctly.

**Connections in this unit**

The adjacent subjects are Shortest Paths, Flows, Matching. They are studied alongside Graph Decomposition because a complete solution must distinguish the mathematical model, the algorithm or mechanism, and what the example actually establishes. Use the named assumptions above, rather than silently transferring a guarantee from one setting to another.

**Study task**

Reconstruct the example without looking at its conclusion. Identify the input quantities, the rule that transforms those inputs, and the final conclusion. Then challenge one stated assumption using the boundary condition. This gives a falsifiable check rather than a memorized slogan.

## Extended technical treatment

### Conceptual foundations and exact assumptions

Graph decomposition reveals reusable structure in a large network. Connected components partition an undirected graph into maximal mutually reachable vertex groups. Strongly connected components partition a directed graph so that every pair of vertices in a component can reach each other in both directions. Contracting each strongly connected component produces a directed acyclic condensation graph. Depth-first discovery and finishing times support Kosaraju's and Tarjan's algorithms with linear O(V+E) traversal work under adjacency-list representation.

### Derivation and worked trace

Consider directed edges A→B, B→A, B→C, C→D, D→C, and D→E. Vertices A and B form one strongly connected component, C and D another, and E a singleton. After contraction the condensation graph is {A,B}→{C,D}→{E}, which is acyclic. There is a path from A to E, but no return path from E to A. If one carelessly ignores edge directions and computes ordinary connected components, all five vertices appear connected and the strongly connected structure is lost.

### Counterexample and failure diagnosis

Articulation points and bridges describe a different kind of decomposition in undirected graphs: removing such a vertex or edge increases the number of connected components. On a path of four vertices, both internal vertices are articulation points and every edge is a bridge. In a triangle no single edge is a bridge. Algorithms use DFS discovery indices and low-link values, but parent edges and back edges must be distinguished carefully. Applying undirected low-link rules without adaptation to directed graphs gives incorrect results.

### Applications, engineering constraints and validation

Applications include compiler dependency analysis, web graph clustering, fault localization and network reachability. A component label is not sufficient to claim causal dependence or reliability; it reports a particular graph property under explicit edge semantics. Test with self-loops, parallel edges, disconnected graphs and isolated vertices. For SCC algorithms, verify that the quotient graph is acyclic and that any pair placed in one component is mutually reachable; use BFS from each vertex on a tiny input as an independent oracle.

## Unit 6 integrated computational laboratory

## Integrated laboratory: four graph objectives on one network

Graph data structures encode many incompatible mathematical questions. Given a road network, minimum spanning tree construction asks for low total installation cost; shortest paths ask for minimum route cost from one starting point; maximum flow asks for feasible throughput; connectivity decomposition asks which places can reach which others. Applying the wrong solver can return a mathematically meaningful value that is irrelevant to the decision. A textbook should state whether edges are directed, whether weights may be negative, whether capacities are integral and whether parallel edges are allowed before illustrating the chosen algorithm.

Create a directed transit graph with stops A,B,C,D,E and edges A→B weight 2, A→C weight 9, B→C weight 3, B→D weight 8, C→D weight 1 and D→E weight 4. A shortest route from A to E follows A,B,C,D,E and costs ten. Directly using A→C then C→D then D→E costs fourteen. A Dijkstra trace begins by settling A at zero, then B at two, then C at five, then D at six, then E at ten. The parent pointers B←A, C←B, D←C, E←D reconstruct the route. Verify that the cost stored at each vertex matches the parent-edge sum; a table of correct distances with corrupted parents would still fail the requested route-output contract.

Now add a negative edge D→B weight -10, and analyze why ordinary Dijkstra cannot be trusted. Cycling B→C→D→B has cost 3+1-10=-6, a reachable negative cycle. There is no finite lower bound on the cost of routes that may repeat that cycle before continuing to E. Reporting a finite shortest route in this modified graph would be misleading. Bellman–Ford can detect a reachable negative cycle through an extra relaxation pass, but the meaning of a shortest simple path is a separate problem. The example forces students to distinguish an input violating an algorithm's assumptions from a mere slow implementation.

For flow, use a different graph with source s, sink t and intermediate vertices x,y. Capacities are s→x 4, s→y 3, x→t 2, x→y 2 and y→t 5. A feasible flow of seven sends two through s-x-t, two through s-x-y-t and three through s-y-t. Conservation holds at x: four enter and four leave. Conservation holds at y: five enter and five leave. The cut leaving s has capacity seven, so no feasible flow can exceed seven. A feasible flow matching a cut upper bound is a concise optimality certificate. Make the learner construct both sides of this certificate rather than relying on an algorithm's printed result.

Inspect residual edges. Suppose an augmenting-path method sends traffic along a path that later prevents use of a better routing unless some traffic is canceled. The residual network includes a reverse edge with capacity equal to current flow, allowing reallocation without violating conservation. This is not a literal pipeline operating backwards; it is a bookkeeping device for changes to the tentative solution. A test that verifies only the total flow value can miss local capacity violations. Check every directed edge and every internal node separately, then compare final flow with a minimum cut.

For matching, form left vertices L1,L2,L3 and right vertices R1,R2,R3. Available pairs are L1-R1, L1-R2, L2-R1, L2-R3, L3-R2. Choosing L1-R1, L2-R3 and L3-R2 creates a matching of size three. A greedy routine could instead choose L1-R2 and L2-R1, leaving L3 unmatched unless it rearranges assignments. An augmenting-path search may find a correction depending on the chosen intermediate matching. State the matching invariant explicitly: no vertex is incident to two accepted edges. Use exhaustive enumeration of subsets for at most six edges to verify maximum cardinality.

Strongly connected components answer yet another question. Suppose one-way links are P→Q, Q→P, Q→R, R→S, S→R and S→T. The SCC partition is {P,Q}, {R,S}, {T}. After contraction the resulting graph is a chain of three components, even though the underlying undirected graph is connected. Reachability in one direction does not imply mutual reachability. A graph user interface should visually distinguish the edge orientation; otherwise a correct SCC result can appear unintuitive to a learner.

The final project asks students to build a small test harness that accepts a graph definition and reports four results only when the required assumptions are met. It must reject or specially handle negative weights for Dijkstra, distinguish capacities from distances, preserve directedness and show witness structures. Use a tiny exhaustive oracle where possible: enumerate simple routes, all small edge subsets for matching, and all cuts for flow. No single large randomly generated graph can replace these directed, independently interpretable checks.

### Independent audit exercise: graph invariants and invalid inputs

Build an unweighted graph BFS routine and compare its shortest-path results against Dijkstra with all edge weights set to one. In an unweighted graph a shortest path minimizes the number of edges; with unit positive costs, Dijkstra minimizes the identical objective. The two routines should agree on distance for every reachable vertex. They may produce different equally short routes depending on adjacency-list iteration order, so the oracle should compare route length and validity rather than exact parent pointers when multiple optimum routes exist.

On directed edges A→B, A→C, B→D, C→D, D→E, BFS from A obtains distance zero to A, one to B and C, two to D, and three to E. The algorithm processes vertices in nondecreasing distance layers. Its loop invariant says that when a vertex is first discovered, its recorded distance equals the length of a shortest path from the source, because all shorter candidates would have been explored in previous layers. This claim requires the ordinary FIFO queue and unit-edge interpretation; replacing the queue with a stack yields DFS and destroys the same distance guarantee.

Run tests on a disconnected graph. An unreachable vertex should remain unreachable, not receive distance zero or inherit a stale parent from a prior invocation. Test zero vertices, one isolated vertex, parallel edges, a self-loop and a dense directed graph. Clear mutable state between runs. A route reconstruction procedure should stop at the source, detect missing parent pointers and avoid cycling forever if state was corrupted.

Finally examine weighted and negative edges. BFS is not a shortest-weighted-path method when edge weights vary; choosing fewer hops can cost more than choosing more hops. Dijkstra is valid for nonnegative weights, but a negative edge may undermine the finalized-distance invariant. Bellman–Ford can handle negatives without reachable negative cycles. The appropriate error behavior for unsupported input is not to run the wrong solver and present an unexplained number. Validate edge types and show a meaningful message about the failed assumption.

## Worked questions and solutions

### Question 1: Shortest Paths: worked application 1

Compute a shortest A-to-C path from directed edges A→B=2, B→C=3, A→C=10.

1. **Set up the model and conditions:** Direct A→C costs 10; the path through B costs 2+3=5.

2. **Carry out the calculation or proof:** Both paths are valid and all weights are nonnegative.

3. **State the result and its scope:** The shortest distance is 5 via B.

**Answer:** The shortest distance is 5 via B.


### Question 2: Flows: worked application 2

Find the maximum flow if s→a=3, a→t=2, s→b=2 and b→t=2, with no other edges.

1. **Set up the model and conditions:** Route two units along s-a-t, limited by a→t.

2. **Carry out the calculation or proof:** Route two along s-b-t, limited by s→b and b→t.

3. **State the result and its scope:** Total flow 4 matches the cut into t of capacity 4, proving optimality.

**Answer:** Total flow 4 matches the cut into t of capacity 4, proving optimality.


### Question 3: Matching: worked application 3

Find a maximum matching for bipartite graph L1-R1, L1-R2, L2-R1.

1. **Set up the model and conditions:** Assign L2 to R1, which leaves R2 for L1.

2. **Carry out the calculation or proof:** Both chosen edges are disjoint in endpoints.

3. **State the result and its scope:** Matching {(L2,R1),(L1,R2)} has size 2, which is maximum with only two left vertices.

**Answer:** Matching {(L2,R1),(L1,R2)} has size 2, which is maximum with only two left vertices.

