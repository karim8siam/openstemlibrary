# Unit 2: Search

*Editorial draft; not approved for live publication.*

## Uninformed Search
**Uninformed Search: conceptual explanation**

### Breadth-first, depth-first, and uniform-cost search
A search problem consists of an initial state, a successor function, a goal test and a path-cost rule. The search tree lists paths that an algorithm might examine; the underlying state graph merges paths that reach the same state. These are not equivalent structures when cycles or multiple routes exist. Breadth-first search expands the shallowest unexpanded node and returns a minimum-edge path when every step has equal cost. Its standard graph implementation uses a FIFO queue and a visited set. Over a graph with V vertices and E edges, traversing adjacency lists takes O(V+E) time, assuming constant-time queue operations and hash or indexed membership tests.

A depth-first traversal uses a stack, potentially less frontier memory on a narrow deep tree, but can take a very long route before finding a shallow goal. On an infinite-depth state tree, naive depth-first search can fail to return even when a finite goal exists in another branch. A depth limit prevents endless descent but can miss deeper solutions. Iterative deepening performs depth-limited DFS repeatedly at limits 0,1,2,...; in a uniform branching tree with b>1, most nodes lie near the last depth, so repeated shallow work can be a tolerable cost. These conclusions depend on finite branching and correct goal testing.

Uniform-cost search prioritizes cumulative path cost g(n), rather than depth. In a graph with nonnegative edge weights, Dijkstra's shortest-path method settles nodes in increasing best known cost. If all edge costs are strictly positive with a positive lower bound and branching is finite, search can find a finite-cost solution without endlessly exploring ever-cheaper prefixes. Zero-cost cycles require careful duplicate handling. Negative edge weights invalidate a naive settled-node proof; one may need a different algorithm such as Bellman–Ford for finite graphs without reachable negative cycles.

A test graph with Start–A cost 1, A–Goal cost 20 and Start–B cost 6, B–Goal cost 6 highlights the difference: both paths have two edges, but costs 21 and 12. BFS may return either as a minimum-edge route, while uniform-cost search returns the cost-12 route when implemented correctly. The example also shows that comparing only the first edge's cost is wrong. Track parent pointers and accumulated costs, inspect tie-handling, and test unreachable goals, cycles and a start state that already satisfies the goal.

The phrase 'optimal search' is incomplete without specifying the cost measure, the environment model, completeness assumptions and resource limit. For a course experiment, generate a small graph, independently enumerate simple paths, and verify the result against the search code before benchmarking speed on larger synthetic graphs.

## Heuristic Search
**Heuristic Search: conceptual explanation**

### Heuristics, A*, and admissibility
A heuristic h(n) estimates the cost to reach a goal from n. Greedy best-first search prioritizes h(n) alone, which may appear fast but can ignore the expense already incurred. A* prioritizes f(n)=g(n)+h(n), combining known path cost and estimated remaining cost. A heuristic is admissible when it never exceeds the true minimum remaining cost. It is consistent when h(n)≤c(n,n')+h(n') along every edge and h(goal)=0. Consistency makes f nondecreasing along a path and supports efficient graph-search implementations without reopening settled nodes under standard conditions.

For a four-direction grid with unit move cost and no teleportation, Manhattan distance |x-x_goal|+|y-y_goal| is admissible because any valid route must traverse at least the necessary horizontal and vertical steps. Walls may force longer paths, but cannot make a path shorter than the coordinate lower bound. If diagonal moves are allowed at unit cost, Manhattan distance can overestimate and becomes inadmissible: moving from (0,0) to (1,1) takes one diagonal step but Manhattan distance is two. The correct admissible estimate under eight-direction unit steps is Chebyshev distance max(|Δx|,|Δy|).

Consider a weighted grid where roads differ in travel time. Multiplying Manhattan distance by the smallest possible legal cost per step yields a lower bound if every move covers one grid unit. A heuristic that uses typical rather than minimum edge cost may overestimate. A* with h=0 becomes uniform-cost search; this is a useful control experiment. Weighted A* uses f=g+wh with w>1 to trade optimality for speed and may have approximation guarantees under precise assumptions, but one should not label it optimal merely because it expands fewer nodes.

Heuristic design is often a form of problem relaxation. Remove obstacles or constraints to solve an easier problem and use its optimal cost as a lower bound for the original. In a multi-delivery route, straight-line distance neglects street connectivity, but is valid as a time lower bound only after dividing by a speed upper bound. If speed limits and mode restrictions vary, state the speed assumption. Another source of heuristics is learned prediction; prediction errors can violate admissibility even when average accuracy is good.

For a laboratory, record expanded nodes, solution length, solution cost and heuristic computation cost across the same maps. Add a deliberately overestimating heuristic and capture a counterexample showing suboptimality, rather than assuming every A* result is shortest. Correctness depends on the mathematical bound, not the fact that the function happens to be called 'heuristic'.

## Adversarial Search
**Adversarial Search: conceptual explanation**

### Minimax, alpha–beta pruning and adversarial decisions
Adversarial search models decisions in which one participant's outcome depends on another participant's choices. In a finite deterministic perfect-information zero-sum game, minimax evaluates terminal utilities and backs values upward: MAX nodes choose the largest child value, MIN nodes the smallest. A game tree with branching b and depth d can have O(b^d) leaves before transpositions or pruning. The value is calculated relative to the depth, terminal evaluation rule and assumption that the opponent plays optimally. It is not a forecast of how a human opponent will behave.

At a MAX node with two MIN children, suppose the first has terminal values 3 and 8, and the second 2 and 10. The MIN values are min(3,8)=3 and min(2,10)=2, so MAX selects the first branch with value 3. A greedy player examining only the best visible leaf might incorrectly prefer the second branch because it contains 10. In real games branching can be immense; depth-limited minimax uses a heuristic leaf evaluator. At the cutoff, evaluations such as material balance in chess approximate future utility but do not become exact game-theoretic values.

Alpha–beta pruning keeps a lower bound α on what MAX can secure and an upper bound β on what MIN will allow along the current path. When α≥β, exploring further descendants cannot change the decision at the ancestor, so they can be skipped without altering the minimax result for the explored finite game. Ordering good moves first can make pruning much stronger; poor ordering may provide little benefit. Test pruning by comparing returned root values to an exhaustive unpruned implementation on random small trees. The set of inspected nodes may differ, but the root minimax value must agree.

Chance nodes extend game trees to stochastic outcomes. A chance node's value is a probability-weighted expectation, not a minimum or maximum. This expectiminimax setting needs explicitly normalized probabilities. Hidden information changes the problem again, requiring beliefs, information sets or policy strategies rather than pretending the board is fully observed. Treating a multiplayer negotiation as a two-player zero-sum game can be analytically convenient but may erase cooperation and external impacts.

Practical adversarial systems require evaluation beyond win rates against one scripted opponent. Include opponents with different policies, test symmetry and player-swap cases, control time per move, and record performance under distribution shift. An agent that wins against a weak greedy baseline may still fail against a strategic adversary or reward loopholes in the environment.

## Constraint Satisfaction
**Constraint Satisfaction: conceptual explanation**

### Constraint satisfaction, consistency and search ordering
A constraint-satisfaction problem specifies variables X_1,...,X_n, domains D_i and constraints restricting permitted joint assignments. Examples include timetable scheduling, map coloring, staff assignment and puzzle solving. Constraint satisfaction differs from pathfinding because order of assignments is often irrelevant to the final solution, while the assignment constraints must all hold simultaneously. A general binary CSP can be represented by a constraint graph; a constraint between variables is an edge, though higher-arity constraints may require richer representation.

Backtracking search chooses an unassigned variable, tries a candidate value, checks violated constraints and recurses. Forward checking removes values from neighboring domains that conflict with the latest assignment. Arc consistency requires that for each value of X in a binary constraint, some value of Y supports it. The AC-3 algorithm repeatedly revises arcs until none change; it can detect impossible assignments early but does not guarantee a global solution. A classic counterexample is a triangle of variables each with domain {red,blue}, constrained so adjacent vertices differ. Every binary arc can have support locally, yet the triangle has no valid two-coloring.

The minimum-remaining-values heuristic chooses the variable with fewest legal values; the degree heuristic often breaks ties by favoring variables constraining many others. The least-constraining-value heuristic tries values leaving the most options for neighboring variables. These heuristics change the search order, not which assignments count as solutions. In a timetable, assigning an instructor available only in one slot before an instructor with many slots may avoid exploring dead ends. But constraint propagation must reflect all requirements, such as capacity, room equipment and consecutive-session rules, or the final schedule may appear valid while violating a real-world condition.

To work a small problem, give courses A and B the allowed rooms {R1,R2}, course C only {R2}, and forbid B and C from sharing a room in the same slot. Assign C=R2 first; forward checking removes R2 from B, forcing B=R1. A may still select either room if no other constraint applies. This illustrates how domains shrink. A solver returning 'no solution' should provide either a proof through exhaustive search of a finite space or a conflict explanation; hitting a time limit is not a proof of infeasibility.

For testing, construct random satisfiable instances from an initial valid assignment and then remove some options while preserving that assignment. Compare the CSP solver against brute-force enumeration for very small domains. Add deliberately impossible instances, duplicate constraints, empty domains and inconsistent input types. The simulation's displayed 'possible combinations' should distinguish the raw Cartesian upper bound from assignments that survive propagation and from actual solutions.

## Integrated Case Study and Model Limitations
**Integrated investigation for Search.** The examples below illustrate the precise mathematical and operational constraints of the unit.

### Search laboratory: emergency routing and adversarial congestion
Imagine an ambulance dispatch system choosing a route across intersections. The map is a weighted directed graph, not a simple grid: travel time varies by road, one-way restrictions matter, and predicted congestion is uncertain. First implement BFS to minimize edge count and Dijkstra to minimize the sum of nonnegative expected travel times. Create a graph where the fewest intersections is not the fastest route. Verify the two outcomes by enumerating all simple paths for a six-node toy instance. Then add A* with a lower bound calculated from straight-line distance and a verified upper speed.

For one scenario, routes through A take 12 minutes with probability 0.8 and 25 minutes otherwise, giving expected time 14.6. Routes through B take 16 minutes surely. Expected-time minimization chooses A, but a policy targeting a high probability of arrival within 20 minutes prefers B if the acceptable failure probability is less than 0.2. The choice depends on the performance measure and not merely the path algorithm. In an emergency service, policy approval, route restrictions and human oversight matter alongside computation.

Next add a constraint that one bridge is closed and a planning limit of 50 milliseconds. Report whether the planner returned a proven optimal path, a feasible but not proven optimal path, or no feasible path found within the limit. Never label a timeout 'no route exists'. Compare node expansions and path cost across BFS, Dijkstra and A* and record the heuristic's admissibility argument. For a human operator, explain why the route was chosen using actual edge weights, not a fictional causal explanation generated after the decision.

A further experiment treats congestion reports as adversarial: an attacker can falsify one segment's reported travel time. The experiment illustrates fragility but is not a full security evaluation. A robust system should cross-check reports, bound their influence and fall back to verified maps. Record the attacker capability explicitly; without that boundary, the word 'adversarial' means little. The final technical report should separate algorithmic guarantees on the modeled graph from reliability claims about real roads, sensors and people.

### Search-research exercise: admissibility and inconsistency in practice
Formal optimality results are conditional. Consider A* search on a graph with nodes S,A,B,G and directed edges S→A cost 2, S→B cost 1, A→G cost 2, B→A cost 0.5, and B→G cost 8. The optimal route is S→B→A→G with total cost 1+0.5+2=3.5, while S→A→G costs 4. Choose heuristic values h(G)=0, h(A)=2, h(B)=2.5 and h(S)=3.5. These equal true cost-to-go distances for this graph, so h is admissible and consistent. A* using them can find the optimal route while avoiding unnecessary detours, though tie behavior depends on the queue.

Now deliberately change h(B) to 8. That estimate exceeds the true remaining cost 2.5, so it is not admissible. In some implementations A* may return S→A→G with cost 4 before exploring B, losing optimality. The fact that a particular tie ordering still finds the best path would not restore the theoretical guarantee. To test admissibility independently, compute exact cost-to-go from every vertex on a tiny graph using reverse Dijkstra, then compare h(v)≤h*(v) for all v. A runtime check on finite test graphs can detect overestimation in those cases, but it does not prove that a learned heuristic remains admissible on all possible future graphs.

### Search completeness and duplicate detection
In a graph with cycles, a tree-search implementation may add the same state indefinitely through paths of increasing length. Consider S→A→S, alongside S→G. A depth-first procedure that always explores A first and lacks cycle detection can get trapped alternating S and A. A graph-search visited set prevents revisiting settled states under the appropriate algorithm, while a cost-based search may need to update a state when a cheaper route arrives. Treating visited as a universal immutable flag is incorrect for every graph and cost model. In Dijkstra's algorithm, a node is settled when its minimum tentative distance is removed from the queue under nonnegative weights. Before settling, its distance may be decreased multiple times.

A lab can compare four implementations: BFS with visited-on-enqueue, naive DFS with no cycle check, uniform-cost search with tentative distances and A* with explicitly documented reopening policy. Use a small set of graphs with known shortest paths and include unreachable goals, zero-cost cycles, duplicate parallel edges, negative input costs and start-equals-goal. Negative costs should be rejected where the algorithm's contract excludes them, not silently processed with a success-looking answer.

### Constraint-solving verification experiment
Search and CSP solving often share backtracking but differ in what constitutes a solution. Design a four-exam timetable with periods Morning and Afternoon. Exams E1 and E2 share students, so they cannot use the same period; E2 and E3 share students; E3 and E4 share students. If no other conflicts apply, an assignment Morning, Afternoon, Morning, Afternoon satisfies all constraints. Add a conflict between E1 and E3, forcing them to differ, and examine whether a feasible two-period assignment still exists. This graph includes a triangle among E1,E2,E3, so two colors are insufficient. Arc-consistency tests alone need not detect the global odd-cycle impossibility for the uniform two-value domains.

Write a brute-force checker that tests all 2^4=16 period assignments and uses a separate list of conflict edges. Compare its answer with forward checking and AC-3 plus backtracking. For a small instance, the reference checker is simple enough to inspect manually. Report the number of nodes visited by each solver and the reason why a particular branch is pruned. A bar chart of speed without correctness and input definitions is insufficient evidence.

### Boundary between search and real decisions
In an emergency-routing example, the mathematically shortest path may cross a road whose travel estimate came from an unreliable feed. A planner can optimize perfectly over false input and produce a poor real-world choice. Treat data freshness, connectivity assumptions and override rules as part of the system boundary. Distinguish algorithmic verification from environment verification: the former establishes that the implementation finds the optimum on a declared graph, while the latter concerns whether the graph is a faithful model. A credible report states both limitations and gives a concrete counterexample in which the best modeled route is not the best observed route.

### Independent correctness oracle for bounded search
For a graph of at most six nodes with strictly nonnegative weights, enumerate every simple path from Start to Goal, compute its total weight, and record the minimum. Compare the resulting value with Dijkstra and A* on the same graph under admissible heuristic settings. Enumeration is exponential in the worst case but perfectly acceptable as a tiny reference oracle. Inject duplicate edges, a disconnected goal, a zero-cost edge and equal-cost routes. The solver may return either of two optimal routes if their costs tie; compare costs rather than hard-coding one parent-pointer sequence. For A*, separately verify the heuristic lower bound on every state. When the heuristic is intentionally too large, record any suboptimal return as an instructive counterexample rather than an arbitrary failed test.

### Worked question: Minimum edges versus minimum cost
A graph has routes Start→X→Goal with costs 1 and 20, Start→Y→Goal with costs 6 and 6, and Start→Goal with cost 16. Identify the BFS route and the minimum-cost route.

**Model the question**
BFS optimizes edge count for an unweighted graph. The direct edge Start→Goal uses one edge, while the other two routes each use two. BFS therefore selects the direct route if it is permitted.

**Calculate or derive**
The route costs are 21 through X, 12 through Y and 16 direct. Uniform-cost search or Dijkstra with nonnegative weights selects Start→Y→Goal with cost 12.

**Check assumptions and boundaries**
The path with the fewest edges need not have the smallest sum of weights. A BFS implementation that uses travel-time weights yet claims cost optimality has an invalid specification.

**Answer:** BFS selects the direct one-edge path (cost 16); minimum-cost search selects Start→Y→Goal (cost 12).

### Worked question: A-star heuristic validity
On a grid allowing diagonal moves of cost 1, start (0,0) and goal (3,4) are given. Evaluate Manhattan distance and the actual shortest path length if all eight neighboring moves are legal.

**Model the question**
Manhattan distance is |3-0|+|4-0|=7, a lower bound only for cardinal moves with unit costs. With diagonal moves a single action may reduce both coordinate differences.

**Calculate or derive**
Take three diagonal moves and one vertical move: (0,0)→(1,1)→(2,2)→(3,3)→(3,4). This uses four unit-cost moves, and no path can use fewer than max(3,4)=4.

**Check assumptions and boundaries**
The Manhattan estimate 7 exceeds true cost 4, so it is not admissible for this move set. A Chebyshev heuristic would return 4 and be exact on an empty grid.

**Answer:** Manhattan h=7 is inadmissible; shortest path cost is 4.

### Worked question: Minimax root selection
MAX chooses between two MIN children. The first child has leaves with utilities 4, 8 and 9; the second has utilities 3, 6 and 12. What minimax value does MAX obtain?

**Model the question**
Each MIN child anticipates its lowest-valued outcome under optimal play. Thus the first child is valued at min(4,8,9) and the second at min(3,6,12).

**Calculate or derive**
These child values are 4 and 3. MAX chooses the first child and secures the minimax value max(4,3)=4 under the specified finite zero-sum game.

**Check assumptions and boundaries**
Selecting the leaf with utility 12 ignores the opponent. The conclusion assumes utilities are from MAX’s perspective, that MIN chooses adversarially and that there are no hidden stochastic outcomes.

**Answer:** MAX chooses the first child; minimax root value is 4.
