# Data Structures — Unit 6: Graph structures

**DRAFT — length threshold and independent review outstanding.**

## 6.1 Adjacency Lists

### Adjacency Lists

Adjacency lists store neighbors of each vertex using O(V+E) total entries for a graph with V vertices and E edges, modulo directedness conventions. Sparse graphs usually favor this representation.

## 6.2 Adjacency Matrices

### Adjacency Matrices

An adjacency matrix uses a V by V table to record edges. Edge existence can be tested in constant time, but space is quadratic. The representation is attractive for dense graphs or matrix-based algorithms.

## 6.3 Graph Traversal

### Graph Traversal

BFS uses a FIFO queue to explore vertices in nondecreasing shortest-edge distance in unweighted graphs. DFS explores one branch deeply using recursion or an explicit stack.

## 6.4 Connectivity

### Connectivity

Connected components partition an undirected graph into maximal sets with paths between members. BFS, DFS, or disjoint-set unions can identify component membership for different workloads.

### Extended design study: reachability on a campus network

Model a campus network as a graph: vertices represent routers or buildings, and edges represent available communication links. The graph can be directed when a connection works only in one direction, or undirected for symmetric links. In an adjacency list, each vertex maintains its neighboring vertices; an undirected edge usually appears in both endpoint lists. In an adjacency matrix, a Boolean cell records whether an edge exists. The list costs O(V+E) storage under conventional accounting, whereas a full matrix costs O(V squared), which may be reasonable for a small dense graph but wasteful for a very sparse one.

Breadth-first search determines which vertices are reachable from a chosen start and gives minimum edge counts in an unweighted graph. Initialize a queue with the start, mark it discovered, and repeatedly dequeue one vertex. For each previously unseen neighbor, mark it immediately and enqueue it. Marking on enqueue avoids adding the same vertex repeatedly when several edges converge. The resulting distance is the number of edges in the first discovered path to each vertex. If edges have different travel times, this distance is not a minimum weighted travel-time result; an appropriate shortest-path algorithm is needed instead.

Depth-first search uses an explicit stack or recursion and follows one branch until it cannot continue, then backtracks. It can find connected components and support cycle detection with suitable state tracking, but its visitation order does not generally encode shortest paths. Starting only from vertex A cannot discover a component disconnected from A. To count all connected components in an undirected graph, loop over every vertex and start a new traversal whenever a vertex has not been visited. Each such start defines one newly discovered component. With an adjacency-list representation, this full traversal examines each vertex and edge only a constant number of times.

Correctness tests must include isolated vertices and disconnected inputs, not only strongly connected examples. For an undirected graph, every neighbor relationship should have a symmetric counterpart unless the representation intentionally stores edges in a canonical single-sided form. Invalid edge endpoints should be rejected before indexing arrays. Duplicate edges may be permitted, but a traversal must still avoid duplicate discovery. A graph with no edges and V vertices has V components; a connected tree has one. These simple properties are useful independent oracles for test construction. The broader lesson is that representation, algorithm, and graph interpretation must agree, or mathematically sound traversal code may answer the wrong real-world question.

## Worked problem 6.1

An undirected graph has 6 vertices and 5 edges. Compare the main storage terms for an adjacency list and a 6×6 matrix.

**Define the data and method**
An adjacency matrix reserves 6*6=36 Boolean slots. A standard undirected adjacency-list representation stores 2*5=10 neighbor entries plus six collection headers and implementation overhead.

**Derive and interpret the result**
The matrix is O(V^2) space while the lists are O(V+E). Exact byte usage depends on object and pointer representation.

## Worked problem 6.2

Run BFS from A with adjacency A:[B,C], B:[A,D], C:[A,E], D:[B], E:[C]. Assume neighbor order as listed.

**Define the data and method**
The initial queue is [A]. Visit A and enqueue B,C. Visit B and enqueue D. Visit C and enqueue E; subsequently visit D then E.

**Derive and interpret the result**
BFS discovery/visit order is A,B,C,D,E, and shortest edge distances are 0,1,1,2,2. A FIFO queue is central to the breadth-first property.

## Worked problem 6.3

Graph vertices {1,2,3,4,5,6} have edges (1,2),(2,3),(4,5). Find connected components.

**Define the data and method**
Starting BFS at 1 reaches 1,2,3. The next unseen vertex 4 reaches 4,5. Vertex 6 has no incident edges and forms a singleton.

**Derive and interpret the result**
There are three components: {1,2,3}, {4,5}, and {6}. A traversal over all start vertices finds disconnected components.


### Applied investigation: Graphs, BFS and disjoint-set structures

Breadth-first search explores vertices in nondecreasing distance from a chosen source when every edge has equal weight. On a full binary tree the frontier at depth d has 2^d vertices; total vertices through level n−1 equal 2^n−1. This exponential growth is a property of the artificial tree, not a claim that every real-world graph expands without overlap.

A disjoint-set union structure tracks connected components under edge insertions. The number of components starts at the number of isolated vertices and decreases only when an edge joins two previously separate components. Union by rank with path compression makes operations efficient across long sequences, but the toy model’s component counts do not show the internal parent array. Tests should ensure redundant edges do not decrease the component count and union is symmetric with respect to the partition result.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.


### Graph representations and traversal invariants

A graph can be stored as an adjacency list, an adjacency matrix or an edge list. The tradeoff depends on the number of vertices V, the number of edges E, and the queries performed. An adjacency matrix uses quadratic space, but testing whether an edge (u,v) exists takes constant time. An adjacency list uses space proportional to V+E and can enumerate neighbors efficiently in a sparse graph. The exact constants depend on whether edges are weighted, directed and stored in one or both endpoints' lists.

Breadth-first search (BFS) uses a queue and discovers reachable vertices in nondecreasing distance from the source in an unweighted graph. The invariant is that when a vertex is first dequeued, its stored distance equals the length of a shortest path from the source. This follows by induction on the queue layers: every newly discovered vertex is one edge from a previously processed vertex, and FIFO order ensures earlier layers are exhausted first. DFS, by contrast, explores an available path deeply before backtracking. It can discover the same reachable set but does not generally give shortest-path distances in an unweighted graph.

Consider an undirected graph with edges (A,B), (A,C), (B,D), (C,D), (D,E) and (F,G). Starting BFS at A, the first layer is {A}, the second is {B,C}, the third is {D}, and the fourth is {E}; F and G are unreachable from A. To find all connected components, restart a traversal at each unvisited vertex. There are two components in the example: {A,B,C,D,E} and {F,G}. The order of vertices within a layer can vary with adjacency iteration order without changing distances.

A correct implementation marks vertices visited when they are enqueued, not when they are eventually dequeued, if it intends to avoid duplicate enqueues. Suppose D is adjacent to both B and C. If it is not marked upon discovery, both parents may schedule D, wasting work and potentially confusing distance or predecessor assignments. An implementation can still be made correct with later marking and duplicate checks, but that requires a different invariant.

Disjoint-set union offers another way to maintain components under a stream of edge additions. Initially every vertex is its own component. Each union between previously different roots decreases the component count by one. Path compression and union by size or rank give very efficient amortized operations. This structure does not directly support deletions; removing an edge from a dynamically changing graph can split a component, and the earlier union history cannot simply be undone in a basic DSU.

Test a graph library with an isolated vertex, a self-loop, multiple edges, a disconnected graph, a chain and a cycle. Decide whether the API treats parallel edges as separate items or forbids them. For directed graphs, weak and strong connectivity are not interchangeable. Such cases clarify the mathematical object being represented before any claims are made about traversal performance.


### Graph traversals with concrete correctness checks

### Breadth-first distances and discovery policy

A BFS implementation maintains a queue, a visited set, optional predecessors and distances measured in edges. Begin by assigning the source distance zero and enqueueing it. When exploring an edge from u to a previously unseen v, set distance[v]=distance[u]+1, set predecessor[v]=u if paths are needed, mark v visited and enqueue it. Marking at discovery avoids duplicate enqueues in graphs with converging paths. As a result, the queue processes vertices in nondecreasing distance from the source. This monotonic property can be asserted during testing; it is stronger than merely checking that all reachable vertices appear somewhere in the output.

For a graph with vertices 0 through 6 and edges (0,1), (0,2), (1,3), (2,3), (3,4) and (5,6), BFS from 0 visits five vertices. Distances are 0 for vertex zero; 1 for vertices one and two; 2 for vertex three; and 3 for vertex four. Vertices five and six have no path from zero. The predecessor of three might be one or two depending on adjacency iteration, but its shortest distance remains two. A correct test should not demand an arbitrary choice of predecessor when several equally short paths exist.

### DFS and cycle detection

Depth-first search marks a vertex on entry and explores outgoing edges recursively or using an explicit stack. For directed graphs, use at least three states: unvisited, active in the current recursion path and finished. An edge to an active vertex indicates a directed cycle; an edge to a finished vertex does not by itself. For undirected graphs a visited neighbor that is not the traversal parent indicates a cycle in the simple-graph setting. Mixing those criteria causes false reports, especially when an undirected edge is stored in both adjacency lists.

A topological ordering exists only for directed acyclic graphs. Kahn's algorithm repeatedly removes a vertex of indegree zero and deletes its outgoing edges from the remaining graph. If all vertices can be removed, their removal order is topological. If some remain when no indegree-zero vertex exists, the remaining directed graph contains a cycle. A test can verify every original edge u→v has u before v in the returned order. There may be multiple valid topological orders, so comparing to a single hardcoded list is unnecessarily strict.

### Storage and traversal complexity

Adjacency lists allow BFS and DFS to visit each vertex and inspect each edge a constant number of times, giving O(V+E) under a suitable representation. An adjacency matrix costs O(V²) space and may require scanning all V possible neighbors per visited vertex, even for sparse graphs. In a compressed sparse row representation, vertex v's outgoing neighbors occupy a contiguous slice between offsets[v] and offsets[v+1]. This supports compact sequential traversal but makes dynamic edge insertion more expensive. The representation changes performance without changing the mathematical BFS invariant.

### Connected components with DSU

For an undirected graph processed as a stream of edge insertions, disjoint-set union begins with one singleton per vertex. Each successful union of different roots decreases component count by one. Path compression and union by rank provide excellent amortized performance. If a repeated edge connects vertices already in the same component, component count does not change. That gives a direct invariant for randomized tests: the count should equal the number of connected components computed from scratch with a reference traversal on the currently inserted edges.

### Laboratory cases

Build tests with a one-vertex graph, an isolated vertex, parallel edges, self-loops, a disconnected pair of cycles and a long path. Check that BFS distances agree with a simple exhaustive dynamic-programming or queue reference, that topological order is rejected when a directed cycle is introduced, and that DSU handles repeated unions. For directed graphs, clearly distinguish reachability from strong connectivity: a vertex can reach another without being reachable in return. A trustworthy simulator identifies its graph model before drawing conclusions from colored nodes.


## Additional original authored teaching sections

# Graph representations and what they imply for algorithms

A graph contains vertices and edges, but the meaning of 'edge' depends on whether connections are directed, weighted, duplicated, or labeled. An adjacency matrix stores a value for each ordered vertex pair, requiring space proportional to the square of the vertex count. An adjacency list stores outgoing neighbors for each vertex, typically using space proportional to the number of vertices plus the number of stored edges. For a simple undirected graph represented by lists, each edge is usually stored twice, once at each endpoint. Comparing raw adjacency counts without recognizing that convention can lead to errors in complexity reasoning and memory estimates.

Consider five vertices and directed edges A to B, A to C, B to D, C to D, and D to E. The adjacency list for A contains B and C, while D contains E. A matrix representation would use a five-by-five table of possible directed connections, many of which are absent. If the graph is sparse and becomes large, storing only present edges avoids allocating an entire quadratic matrix. If the graph is dense or the application repeatedly asks whether a particular edge exists, a matrix can be attractive because a direct index checks adjacency in constant time. List-based adjacency checks may require scanning a vertex's neighbor collection unless each collection is separately indexed.

Breadth-first search discovers vertices in layers by maintaining a queue. In an unweighted graph, the first discovery of a vertex corresponds to a path with the fewest edges from the start under the chosen traversal assumptions. To reconstruct a path, store the predecessor of each discovered vertex. A common failure is to mark vertices visited only when they leave the queue; the same vertex can then be inserted repeatedly through different predecessors, wasting work or corrupting parent information. Marking a vertex when it is enqueued prevents duplicate discoveries in a standard traversal.

Depth-first search explores recursively or through an explicit stack. It can identify connected components, compute finish orders, and support cycle detection with suitable bookkeeping. In a directed graph, an edge to a currently active recursion-stack vertex identifies a back edge and a cycle. Merely encountering any previously visited vertex does not suffice: a previously completed vertex may be part of another finished branch. In an undirected graph, the edge back to the immediate parent must be ignored in the usual DFS cycle test. These distinctions demonstrate that one `visited` boolean may be insufficient for every graph property.

Traversal order is often nondeterministic unless adjacency iteration order is defined. BFS can return different valid predecessor trees if A lists C before B instead of B before C. Distance in edges remains correct, but the displayed shortest path may differ when alternatives tie. A teaching test should compare shortest distances or accept any valid minimum path unless it explicitly fixes neighbor ordering. Demanding one exact traversal trace from implementations that expose no ordering contract can reject otherwise correct algorithms.

Graph data must also be validated. If vertices use dense integer identifiers, arrays permit compact storage. If identifiers are strings or sparse large integers, a dictionary mapping external identifiers to local integer indices can reduce storage costs and simplify adjacency arrays. Importers must decide what to do with edges referencing missing vertices, self-loops, parallel edges, and negative edge weights. Negative weights do not invalidate a graph representation, but they invalidate some shortest-path algorithm assumptions. Separating data-model validity from algorithm applicability prevents the parser from silently discarding meaningful inputs.

# Connectivity, dynamic changes, and route constraints

In an undirected graph, connected components partition the vertices into maximal groups reachable from one another. Running a graph traversal from each unvisited vertex finds every component in overall time proportional to vertices plus edges for adjacency-list storage. The result can be checked independently: every pair of vertices assigned to the same component should be mutually reachable, and no stored edge should cross two purportedly distinct components. These properties test the output semantically, rather than relying on a particular component numbering chosen by traversal order.

A disjoint-set union structure supports a related but narrower task: incrementally adding undirected connections and querying whether two vertices are in the same connected component. Start with each vertex in its own set and union the endpoints of each new edge. Path compression and union-by-size produce extremely efficient sequences of operations under standard analysis. However, deleting an edge is not supported by the basic structure because the representation does not remember enough information to determine whether a former component should split. In a transportation network with road closures, a disjoint-set structure alone is insufficient for fully dynamic connectivity.

Imagine roads A–B, B–C, and A–C forming a triangle. Removing B–C leaves B connected to C through A; removing A–B afterward can isolate B. A simplistic deletion policy that always splits the endpoints' sets after removing an edge will fail on the first deletion, while a policy that never splits will fail on the second. Correct fully dynamic connectivity requires richer algorithms or recomputation strategies. This is a useful example of how an efficient representation can omit an operation that initially seems natural from the application description.

Graph traversal algorithms must report what 'path' means. BFS minimizes edge count in an unweighted graph. It does not minimize total road distance when edges have different costs. Dijkstra's algorithm handles nonnegative weighted edges under its standard assumptions; algorithms that must handle negative edges require other techniques and attention to negative cycles. A route application may also include constraints such as wheelchair accessibility, timed closures, or maximum transfer count. Those constraints are not automatically represented by a plain edge weight. Some can be encoded by expanding state to include time or resource usage, but the resulting state graph may be much larger than the original map.

A path-finding simulation should expose not just a glowing route but also the frontier of vertices pending exploration, the predecessor links, and the discovery order. For weighted problems, display tentative distances and the assumption about admissible edge weights. Add a toggle that changes one edge cost and predict which shortest path should change before running the algorithm. In a simple four-vertex network with edges S–A of cost one, A–T of cost six, S–B of cost three, and B–T of cost two, the shortest weighted route is S–B–T with total cost five, although both candidate routes contain two edges. BFS cannot distinguish them by edge count alone.

Testing should include disconnected graphs, an isolated start vertex, self-loops, parallel edges, missing destination, and a graph with several equally short routes. For undirected adjacency lists, assert that every stored connection has a reverse adjacency entry when the graph is declared undirected. For directed graphs, avoid imposing that symmetry. Verify distances with a small independent Floyd–Warshall implementation or exhaustive search on tiny graphs when appropriate. Check predecessor paths by summing their edges and confirming that they lead to the requested destination. This combination of structural and semantic checks is stronger than visually inspecting one demonstration graph.
