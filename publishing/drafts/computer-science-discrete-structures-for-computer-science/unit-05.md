# Unit 5: Graphs


## Paths

**Core model — Paths**

A path is a sequence of adjacent vertices, and a simple path contains no repeated vertices. Graph directedness determines allowable traversal direction.

**Original worked illustration**

In the directed graph A->B->C there is a path from A to C but no path from C to A unless a reverse route exists.

**Boundary conditions and checks**

A walk may repeat vertices or edges; mixing path and walk definitions causes false claims about cycles.

### Paths, walks and trails in a graph
A graph G=(V,E) represents objects by vertices and selected relationships by edges. In an undirected graph the edge {u,v} has no direction; in a directed graph the arc (u,v) points from u to v. A walk is a sequence of vertices whose consecutive pairs are adjacent, possibly repeating vertices or edges. A trail does not repeat an edge, and a simple path does not repeat a vertex. Definitions differ between texts on whether a length-zero path is allowed, so state conventions when using edge cases.

For an undirected graph with vertices A,B,C,D and edges AB,BC,CD,AD, the sequence A,B,C,D is a simple path of length three; A,D is a simple path of length one. The sequence A,B,C,B repeats vertex B and edge BC, so it is a walk but not a trail or simple path. Counting length means counting edges, not counting visited vertices. This basic distinction controls what shortest-path algorithms actually minimize.

### Reachability through breadth-first search
Breadth-first search on an unweighted graph explores vertices by nondecreasing distance from a start vertex. Initialize a FIFO queue with s, set dist(s)=0 and mark it visited. Whenever a previously unseen neighbor v is found from u, assign dist(v)=dist(u)+1 and enqueue v. The invariant is that vertices leave the queue in nondecreasing distance order. If there were a shorter path to v than the first assigned distance, that path's predecessor would have been explored earlier, a contradiction. Thus BFS finds shortest edge-count distances in an unweighted graph.

This guarantee does not apply to arbitrary positive edge weights. Suppose edges A→B cost 100, A→C cost 1, and C→B cost 1. BFS finds the direct one-edge route A→B, which costs 100, while the two-edge route through C costs 2. Dijkstra's algorithm, with nonnegative weights, handles this cost model. A program that labels BFS output as shortest *travel time* without knowing weights can mislead a user even if its reachability code is correct.

### Euler and Hamilton problems
An Euler trail uses each edge once. In a connected undirected graph, an Euler circuit exists precisely when all vertices have even degree; a nonclosed Euler trail exists with exactly two odd-degree vertices. The reason is that every time a trail passes through an internal vertex, it consumes one entering and one leaving edge, pairing its incident edges. A Hamilton path instead visits each vertex once. The problems sound similar but impose different constraints, and degree parity alone does not characterize Hamiltonicity. Route inspection and visiting-city applications must specify whether roads/edges or locations/vertices must be covered.

### Adversarial input and testing
Test reachability with isolated vertices, a self-loop, two parallel edges if the graph model permits multiedges, disconnected components, and a graph with only one vertex. For a BFS implementation, verify predecessor chains: following predecessors from a reachable target should end at the source in exactly dist(target) steps. A predecessor array that forms a cycle is inconsistent even if the distance labels appear plausible. Record memory costs: adjacency lists use O(|V|+|E|) space, while a dense Boolean adjacency matrix occupies O(|V|²).



## Connectivity

**Core model — Connectivity**

An undirected graph is connected when every pair of vertices has a path. DFS and BFS discover connected components in O(V+E) with adjacency lists.

**Original worked illustration**

On edges (1,2),(2,3),(4,5), the five vertices form two connected components: {1,2,3} and {4,5}.

**Boundary conditions and checks**

A directed graph needs separate weak- and strong-connectivity definitions; an undirected BFS does not solve SCC decomposition.

### Connected components define natural graph partitions
In an undirected graph, two vertices are related when some path joins them. This is an equivalence relation: length-zero paths establish reflexivity, reversing a path establishes symmetry, and concatenating two paths establishes transitivity. Its equivalence classes are the connected components. The graph may have many components, including a singleton isolated vertex. An algorithm that reports one component because it started DFS at one convenient vertex is incorrect when the graph is disconnected.

### Component-labeling algorithm
Initialize all vertices unvisited. For each vertex not yet visited, start DFS or BFS and assign a new component identifier to every vertex reached. Marking a vertex when first discovered prevents revisiting the same region indefinitely in graphs with cycles. With adjacency lists, this labeling requires O(|V|+|E|) time because each vertex is marked once and every undirected edge is inspected at most twice. Component identifiers have no canonical numerical meaning: labeling components in a different traversal order can yield different numbers but the same partition.

### Strongly connected directed graphs
For directed graphs, reachability is not symmetric. A strongly connected component is a maximal subset of vertices where every vertex can reach every other following edge directions. For example, A→B→C→A makes {A,B,C} strongly connected, but adding C→D without a return path does not add D to that component. Collapsing every strongly connected component to one meta-vertex yields a directed acyclic graph. If the condensation graph had a directed cycle among distinct components, those components would be mutually reachable and therefore should have been one component, a contradiction.

Algorithms such as Tarjan's or Kosaraju's find strongly connected components in linear time relative to vertices plus edges. Tarjan's method uses DFS discovery indices, a stack of active vertices, and low-link values. A low-link value summarizes the earliest reachable ancestor in the active DFS context, not the absolute minimum vertex identifier. When implementing the algorithm, test back edges, cross edges, self-loops, and multiple components carefully; low-link updates differ for a newly discovered child versus a neighbor already on the stack.

### Application: dependency cycles
A software build graph should ideally be acyclic: a source target can only be compiled after its prerequisites. If SCC analysis finds a component with more than one target, the build system has a dependency cycle. A single-vertex SCC with a self-loop also represents a cycle. The practical repair is not to delete edges arbitrarily but to identify which dependency was modeled in the wrong direction, or whether two modules should be refactored to depend on a shared interface. SCC detection diagnoses structure; it does not choose the right architectural change for a project.

### Distinguishing connectivity from reliability
Two nodes being connected means at least one path exists. It does not mean that the connection survives failures. Bridges are edges whose removal increases the number of connected components; articulation vertices are vertices whose removal increases that number under the usual definitions. Redundant routes can prevent single-edge failures from disconnecting a network, but path existence alone cannot quantify reliability without a failure model. Study a triangle plus one dangling leaf: its leaf edge is a bridge, while each triangle edge is not.



## Trees

**Core model — Trees**

A tree is a connected acyclic undirected graph. Equivalently, an n-vertex tree contains n-1 edges, and adding any new edge creates a cycle.

**Original worked illustration**

A graph on 6 vertices with 5 edges is not necessarily a tree unless connectivity or acyclicity is also checked.

**Boundary conditions and checks**

The edge-count property alone is insufficient: a cyclic component together with an isolated vertex can still have n-1 edges.

### Trees are connected and acyclic graphs
For a finite undirected graph, several characterizations of a tree are equivalent: it is connected and has no cycles; there is exactly one simple path between each pair of vertices; and it is connected with |E|=|V|−1. One can prove the edge count by removing a leaf and applying induction. Every finite tree with at least two vertices has at least two leaves. This follows by taking a longest simple path: if an endpoint had another neighbor, the path could be extended or a cycle would exist. Both possibilities contradict maximality or acyclicity.

### Spanning trees and network design
A spanning tree of a connected graph includes every vertex and uses a subset of original edges. It has n−1 edges, the minimum possible among connected simple spanning subgraphs. A depth-first or breadth-first exploration produces a spanning tree, but not necessarily a minimum-weight one if edges carry costs. Minimum spanning tree algorithms such as Kruskal's or Prim's use edge weights and exploit a cut property: a minimum-weight edge crossing an appropriate cut can be safely selected for some MST, with careful handling of equal weights.

### A complete small MST example
Let vertices be A,B,C,D and weighted edges AB=1, AC=4, BC=2, BD=5, CD=3, AD=9. Kruskal's algorithm sorts edges by weight. Select AB with cost 1 and BC with cost 2. Next select CD with cost 3, connecting all four vertices without a cycle, for total weight 6. Edge AC would create a cycle among A,B,C and is skipped if encountered after AB and BC. To verify minimality, compare cuts: across {A} the cheapest incident edge is AB; across {A,B} the cheapest crossing edge is BC; across {A,B,C} the cheapest crossing edge is CD. These cut arguments support the chosen tree's optimality.

### Rooted trees and recursive data
Rooting an undirected tree at one chosen vertex gives parent-child relationships and depth values. The shape as an undirected graph does not change, but the parent relation does. A binary tree restricts each node to at most two child positions; it is not simply any tree of maximum undirected degree two. A balanced binary search tree and a binary heap are both rooted-tree-based structures, but their order invariants differ: a search tree organizes keys by left/right comparisons, while a min-heap requires each parent's key to be no greater than its children's keys.

### Counting trees carefully
Cayley's formula says the number of labeled trees on n distinct vertices is n^{n−2} for n≥2. For n=4 it gives 16 distinct labeled trees. The theorem does not count shapes up to graph isomorphism; relabeling vertices generally creates a new object in Cayley's model. Prüfer sequences provide a bijective proof: repeatedly remove the leaf with smallest label, recording its neighbor, until two vertices remain. Each labeled tree maps to a sequence of length n−2 over n labels, and the mapping is reversible. Enumerating the sequences shows why the exponent appears.



## Coloring

**Core model — Coloring**

A proper vertex coloring assigns different colors to endpoints of every edge. Chromatic number is the minimum count required.

**Original worked illustration**

A triangle needs three colors because its vertices are pairwise adjacent, whereas a nonempty bipartite graph needs at most two.

**Boundary conditions and checks**

A high maximum degree provides an upper bound in many settings, not necessarily an exact chromatic number.

### Proper coloring expresses conflict constraints
A proper vertex coloring assigns colors so that adjacent vertices receive different colors. The chromatic number χ(G) is the smallest number of colors that allows such an assignment. Colors are abstract labels, not physical paint. In a conflict scheduling application, two exams joined by an edge cannot share a time slot. A valid coloring therefore yields a feasible assignment under that pairwise-conflict model. The minimum number of slots equals χ(G) only if no further constraints such as room capacity or student travel time apply.

### Fundamental examples and bounds
An edgeless graph has chromatic number one if it contains at least one vertex. A complete graph Kn has chromatic number n because every pair of vertices conflicts. A bipartite graph with at least one edge has chromatic number two: color one partition red and the other blue. An odd cycle needs three colors, while an even cycle needs two. The maximum-degree bound χ(G)≤Δ(G)+1 follows from a greedy process: when coloring a vertex, at most Δ colors are forbidden by already colored neighbors, so one of Δ+1 colors remains.

### Greedy coloring and ordering
Greedy coloring visits vertices in a chosen order and assigns the smallest available color at each step. It always outputs a valid coloring if the algorithm checks all previously colored neighbors. But it need not be optimal. For a path on four vertices, an unfortunate order can make greedy use three colors even though the graph is bipartite and requires only two. This shows that validity and optimality are different obligations. A test suite should separately confirm that no edge has equal endpoint colors and compare the number of colors against known optima for small standard graphs.

### Worked scheduling model
Four courses A,B,C,D have conflicts AB,BC,CD,DA, forming a 4-cycle. Assign A and C to slot 1, B and D to slot 2. Every conflict edge joins different slots, so two suffice. Now add diagonal AC. Courses A,B,C form a triangle, so at least three colors are needed. A three-color assignment exists: A=1, B=2, C=3, D=2, with D adjacent to A and C only. Thus χ=3. The lower bound came from the triangle; the upper bound came from the explicit assignment.

### Edge coloring and register allocation caveat
Edge coloring assigns colors to edges so incident edges differ, a different problem from vertex coloring. In compiler register allocation, a graph's vertices may represent live ranges and edges may represent simultaneous liveness conflicts; colors represent registers. Actual compilers also account for register classes, spills, architecture restrictions and control-flow details, so the interference graph is a useful abstraction but not the entire optimization problem. A model is most instructive when its missing constraints are stated.

### Extended laboratory: planning paths through a campus network
Represent buildings A,B,C,D,E as vertices and walkways as undirected edges AB,BC,CD,DA,CE. The graph is connected: every building is reachable from A, including E through A→B→C→E or A→D→C→E. The degree of C is three and the degree of E is one. The handshake lemma predicts total degree 2|E|=10 because there are five edges. Counting locally gives deg(A)=2, deg(B)=2, deg(C)=3, deg(D)=2, deg(E)=1, summing to ten. This provides an independent consistency check of the representation.

Run BFS from A. Initially distance(A)=0. Discover B and D at distance one; from either route discover C at distance two; then discover E at distance three. With a fixed alphabetic tie-breaking order the predecessor path to E may be A,B,C,E. The shortest edge-count distance is three regardless of tie order. If some walkways are significantly longer than others, the claim changes: the minimum number of walkways need not minimize travel time, and weighted shortest-path methods are required.

A spanning tree could use AB,BC,CD,CE, connecting all five vertices with four edges. The original graph has a cycle A-B-C-D-A, so it is not itself a tree. Removing edge DA breaks that cycle while keeping the graph connected. If instead edge CE is removed, building E becomes isolated; CE is a bridge. This matters for robustness: a planner who removes any one redundant-looking walkway without checking bridges may disconnect part of the network.

Assign walkway repair costs AB=4, BC=2, CD=3, DA=5 and CE=1. To produce a minimum-cost connected maintenance backbone, apply Kruskal's algorithm. Pick CE for one cost unit, BC for two, CD for three, and AB for four. All five vertices are connected and no cycle has formed; the total is ten. Edge DA at cost five is unnecessary for connectivity. The argument assumes the selected walkways can be maintained independently and that cost is additive; capacity and safety constraints could change the engineering decision.

Now add a scheduling problem. Two maintenance jobs conflict when they share a narrow junction and cannot occur simultaneously. Construct a *conflict graph whose vertices are jobs*, not buildings. A valid vertex coloring assigns jobs to time slots. This conflict graph is a different object from the original campus graph even though both use edges. If the jobs for AB and BC conflict, add an edge between those job vertices; if jobs on distant walkways do not conflict, omit the edge. A proper coloring gives a feasible schedule only with respect to these modeled conflicts.

Suppose the campus is updating emergency access rules. Buildings reachable from an entrance form a connected component; if a gate closes, the edge set changes. Precomputing a route once is not sufficient for dynamic availability. A system can rerun BFS for small graphs or maintain dynamic connectivity information for larger ones, but it must ingest current edge states. A simulation that merely draws routes without reflecting closures is not a functioning access-planning model.

For software testing, use three graph fixtures: the original graph, the graph after removing DA, and the graph after removing CE. Confirm that vertex E remains reachable in the first two but not in the third. Confirm that a spanning tree on five vertices uses exactly four edges, and that its connectedness is checked separately from the edge count. A disconnected graph with four edges can exist, so counting edges alone does not prove a tree. This laboratory connects traversals, components, trees and coloring while keeping the different mathematical models explicit.

### Experiment card: trees, degree sums and graph invariants
The primary graph model reports the edge count of a path on n vertices, n−1. At n=1 the path consists of one isolated vertex and zero edges. At n=2 it has exactly one edge. At n=12 it has eleven edges. A student can construct the path adjacency list directly by connecting consecutive integers, enumerate its edges and confirm that every nontrivial path is connected and acyclic. The formula is not enough to classify arbitrary graphs: a disconnected graph can also have n−1 edges, and graph theory proofs always depend on the stated structure.

The second graph model constructs the cycle C_n and counts the sum of vertex degrees as 2n. A simple undirected cycle requires at least three vertices, so this slider has a minimum of three rather than one. At n=3 each vertex has degree two, the sum is six and the number of edges is three. At n=4 the sum is eight and the number of edges four. The handshake lemma holds more generally for every finite undirected graph, not only cycles, because every edge contributes two incidences.

Cross-check the cycle model by building adjacency sets where vertex i is connected to (i−1) mod n and (i+1) mod n. For n≥3 these neighbors are distinct, so every degree is exactly two. The sum of degrees should equal twice the number of distinct undirected edges. The same construction at n=2 collapses its two supposed neighbors into the same vertex and violates the simple-cycle premise; rejecting that input is an intentional modeling boundary, not a defect.

For interactive testing, move the cycle slider from its minimum to its maximum and verify that the value grows by two for each added vertex. Reset should return it to five by the current model definition. The primary path model should grow by one edge for each added vertex, also reflecting its own reset value. The two models give different outputs because the added closing edge in a cycle changes the degree and edge-count structure. Keeping them side by side illustrates a mathematical invariant more effectively than two unrelated pictures.



## Fully worked questions

### Question 1: Paths: worked application 1

Find the components of undirected graph with edges (1,2),(2,3),(4,5).


**Set up the model and conditions:** Vertices 1,2,3 are connected by paths.


**Carry out the calculation or proof:** Vertices 4,5 form a separate component with no interconnecting edge.


**State the result and its scope:** The components are {1,2,3} and {4,5}.


**Independent reasoning check and edge conditions:** The edges 1–2 and 2–3 join vertices 1,2,3 into one reachable group. Edge 4–5 joins vertices 4 and 5 into another. No listed edge connects these groups, so with vertex set {1,2,3,4,5} the components are {1,2,3} and {4,5}. A BFS started at vertex one discovers only the first component; a complete component algorithm must launch another traversal from an unvisited vertex. This conclusion assumes the graph has exactly the five named vertices and no additional edges.


**Answer:** The components are {1,2,3} and {4,5}.


### Question 2: Connectivity: worked application 2

A connected graph on six vertices has no cycles. How many edges must it have?


**Set up the model and conditions:** A connected acyclic graph is a tree.


**Carry out the calculation or proof:** Every finite tree on n vertices has exactly n−1 edges.


**State the result and its scope:** Therefore it has five edges.


**Independent reasoning check and edge conditions:** A finite connected undirected graph without cycles is a tree. Every tree on n vertices has n−1 edges; prove this by removing a leaf, which reduces vertex count and edge count by one while preserving the tree property. With n=6, the edge count is 5. Checking only that a graph has five edges would not suffice to prove it is a tree, because disconnected graphs can also have five edges. In the question, connectedness and acyclicity are supplied, so applying the theorem is justified.


**Answer:** Therefore it has five edges.


### Question 3: Trees: worked application 3

Find the chromatic number of a triangle.


**Set up the model and conditions:** Its three vertices are pairwise adjacent, so each requires a different color.


**Carry out the calculation or proof:** Three colors trivially suffice by assigning one unique color per vertex.


**State the result and its scope:** The chromatic number is 3.


**Independent reasoning check and edge conditions:** A triangle is the complete graph K3, so every pair of its three vertices is joined by an edge. Each pair must have distinct colors in a proper coloring, requiring at least three colors. Assign three different colors, one per vertex, to demonstrate that three suffice. This establishes matching lower and upper bounds χ(K3)=3. A two-color assignment would force some adjacent pair to share a color by the pigeonhole principle. The result is for vertex coloring; edge coloring is a different problem.


**Answer:** The chromatic number is 3.

