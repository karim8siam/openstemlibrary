# Data Structures — Unit 3: Search structures

**DRAFT — length threshold and independent review outstanding.**

## 3.1 Binary Search Trees

### Binary Search Trees

In a binary search tree, every key in the left subtree precedes the node key, while right-subtree keys follow it. Search cost is proportional to height, so an unbalanced tree may take linear time.

## 3.2 Balanced Trees

### Balanced Trees

AVL and red-black trees constrain height using structural invariants. Rotations rebalance local links while preserving sorted inorder order. Height or color metadata must remain synchronized with pointer updates.

## 3.3 Search Operations

### Search Operations

Ordered search structures support exact lookup, predecessor, successor, lower bound, and interval reports. The comparator must be stable and transitive. Range reporting cost includes the number of results returned.

## 3.4 Traversal

### Traversal

Preorder, inorder, and postorder traversals differ in their placement of each parent visit relative to its children. An inorder traversal visits binary-search-tree keys in sorted order.

### Extended design study: ordered lookup for a changing catalog

An online catalog maintains products with numerical identifiers and must support exact lookup, listing a range of identifiers, and finding the next larger identifier. A plain hash map supports expected fast exact lookup, but a balanced search tree also supports sorted order and interval queries. The selection follows the interface requirements, not a blanket rule that one implementation is faster. If the records arrive in sorted identifier order, an ordinary unbalanced BST can degenerate into a one-sided chain. Each future lookup near the end then traverses most of the inserted nodes. A self-balancing tree prevents this worst-case geometry by enforcing height restrictions.

For an AVL tree, the height of an empty subtree can be defined as negative one and the height of a leaf as zero. Each node's balance factor is the height of its left subtree minus the height of its right subtree, and the permitted values are -1, 0, and 1. After inserting one key, update height information from the insertion point toward the root. If a node becomes unbalanced, apply the appropriate single or double rotation. The choice is determined by the direction of the two relevant edges, not by the numerical magnitude of the keys. Rotations preserve the inorder sequence, which is essential because the tree must remain a search structure after balancing.

Range queries illustrate the tree's distinctive value. Suppose the catalog contains keys 11, 19, 23, 28, 34, and 52. To list keys in [20,40), a lower-bound search finds the least stored key not below 20, namely 23. Following inorder successors yields 23, 28, and 34 and stops at 52. In a balanced tree this takes logarithmic setup work plus work proportional to the number of reported records. A traversal that always visits every key would be correct but unnecessarily costly when the requested interval is narrow.

Deletion is a stronger invariant test than insertion. Removing a BST node with two children commonly replaces it with its inorder successor or predecessor, then repairs the affected link. A careless implementation may forget to remove the replacement from its old position, accidentally duplicating a key. In a balanced tree, rebalancing can propagate upward after deletion. An effective validation strategy compares the complete inorder sequence with an independent sorted set after thousands of deterministic random insertions and removals. Additional checks inspect the stored heights and balance factors of every node. The broad lesson is that a comparison-based search structure is best understood through ordering invariants, tree geometry, and the exact queries the client needs.

## Worked problem 3.1

Insert 8,3,10,1,6,14,4,7 into a basic BST. Record the search path for key 7 and the number of comparisons.

**Define the data and method**
Compare 7<8, so go left to 3; compare 7>3, so go right to 6; compare 7>6, so go right to 7, which matches.

**Derive and interpret the result**
The visited nodes are 8,3,6,7, giving four comparisons. General BST search is O(h), not automatically O(log n).

## Worked problem 3.2

An AVL tree becomes the chain 30(left)→20(left)→10 after insertion. State the rebalancing rotation and resulting tree.

**Define the data and method**
The root 30 has left-left imbalance. Rotate right at 30: 20 becomes root, 10 its left child, 30 its right child. Inorder order remains 10,20,30.

**Derive and interpret the result**
The resulting tree has edge-height one instead of two; each subtree satisfies the AVL balance condition. A left rotation would not repair this example.

## Worked problem 3.3

For the binary tree with root 5, children 2 and 8, and children 1 and 3 under node 2, find its preorder, inorder and postorder traversals.

**Define the data and method**
Preorder visits root before subtrees: 5,2,1,3,8. Inorder visits left subtree, root, then right subtree: 1,2,3,5,8.

**Derive and interpret the result**
Postorder visits children before root: 1,3,2,8,5. Every traversal visits five nodes exactly once; only inorder is guaranteed sorted for a BST.


### Applied investigation: Binary search trees and search correctness

A binary search tree requires every key in the left subtree to be smaller and every key in the right subtree to be larger, subject to an explicit duplicate policy. Inserting already sorted keys into a plain unbalanced tree gives height n−1 edges. A balanced implementation instead maintains structural invariants, for example AVL height balance or red–black color rules, to avoid this degeneration.

Searching a BST compares the target against a node and chooses a single subtree at each step. An unsuccessful search can terminate at a null child without examining all stored keys. Trace the fixed tree for targets below, above and between existing keys. For a correct search, the skipped subtree cannot contain the target by the ordering invariant. The demo is a static search tree and must not be mistaken for an implementation of balancing during insertion or deletion.

**Verification exercise.** Compute a small valid case by hand, compare it with both interactive models in this unit, then reset them. Write the boundary case that violates a stated assumption and explain why the implementation should reject it rather than silently returning a misleading result.


### Search trees, order, and correctness under updates

A binary search tree stores an ordering invariant: keys in the left subtree are smaller than the node's key, and keys in the right subtree are larger, under a chosen comparator. This says nothing by itself about height. Inserting the values 1 through 8 in ascending order into a plain unbalanced tree builds a chain with seven edges from root to deepest leaf. Searching for 8 performs eight key comparisons. By contrast, a nearly complete tree with eight nodes can achieve a height of three edges. Logarithmic behavior is a property of balance guarantees or favorable input, not an automatic property of binary search tree terminology.

Insertion follows the comparator until it reaches a missing child link. The new leaf preserves search order if equal-key handling is specified consistently. If duplicates are allowed, options include storing a count at each key, placing equal elements on a chosen side, or storing a list of values in the node. Those policies affect deletion, iteration and equality checks. For a map, replacing the value for an existing key is often more useful than inserting a duplicate node. Test all of these choices explicitly.

Deletion has three structurally different cases. A leaf can be detached. A node with one child can be replaced by that child. A node with two children can be replaced logically by its inorder successor, the smallest key in its right subtree, followed by deletion of the successor's original node. The successor has no left child, so that second removal is simpler. Copying only the key while leaving associated payload data behind is a serious map bug: the key and value must move together.

An inorder traversal recursively visits the left subtree, the node and the right subtree. Given the search-order invariant and a total comparator, its output is sorted. That observation provides an independent test oracle: insert a set of known distinct keys, compare inorder output to an independently sorted list, perform several deletions and compare again. This tests preservation of the ordering invariant, not merely whether individual searches happen to succeed.

Self-balancing trees add metadata or structural constraints. An AVL tree maintains a bounded balance-factor difference between child heights and uses rotations to repair violations. A red-black tree instead uses coloring and black-height conditions to control the longest path within a constant factor of the shortest. A rotation changes local parent-child pointers while preserving inorder key order; its correctness can be checked on a three-node example before studying rebalance cases. Do not assume a particular rotation schedule is shared between AVL and red-black algorithms.

When should a student use a tree rather than a hash table? Suppose a user frequently requests all keys between 400 and 460. A balanced ordered map can locate the lower bound in logarithmic time and then traverse the matching keys in order, giving a bound depending on the number of returned items. An unordered hash map cannot generally support that range query without an auxiliary ordering structure. Conversely, exact-key lookups in a well-sized hash table may be faster in practice. A correct design follows the query semantics rather than a blanket rule that logarithmic is always superior or inferior to expected constant time.


### From search trees to order statistics

### Reconstruct a tree from its insertion history

Consider the keys 8,3,10,1,6,14,4,7,13 inserted into a plain binary search tree. Root eight sends three left and ten right. Inserting six descends eight-left to three-right; inserting four descends through six-left. The shape is determined by insertion order, not just the set of keys. To search for seven, compare at eight, move left to three, right to six and right again to seven. The search takes four visited nodes. A different insertion order could produce a shorter or longer path while representing the same set. This is why balanced-tree implementations promise height control, rather than relying on an expected-looking drawing.

### Rotate without losing the ordering invariant

A left rotation at node x with right child y rearranges three subtrees A, B and C. Initially x has left subtree A and right child y; y has left subtree B and right subtree C. After rotation, y is the local parent, x its left child, with x's children A and B. Since all A keys are less than x, B keys lie between x and y, and C keys exceed y, inorder order is preserved. The rotation modifies a constant number of local links and is therefore constant-time in a pointer-based tree, but the surrounding metadata—parent pointers, subtree sizes or heights—must also be repaired. An incorrect parent-link update can create a cycle that a simple key-search test fails to detect immediately.

### Why balance conditions matter

An AVL tree requires the left and right subtree heights of every node to differ by at most one. Following insertion, retrace the affected path toward the root, update heights and rotate at the first violation according to the imbalance case. A left-left case may use one right rotation, while a left-right case needs a left rotation on the child followed by a right rotation on the parent. Demonstrating these operations with three small keys is valuable, but correctness depends on keeping height metadata valid after all future deletions as well as insertions.

Red-black trees use a different invariant system. Each node has a color, the root is black under the usual formulation, red nodes cannot have red children, and every path from a node to descendant null leaves passes through the same number of black nodes. That black-height property limits total height to a logarithmic function of node count. Red-black rotations resemble binary search tree rotations but may be paired with recoloring. There is no guarantee that an AVL tree and a red-black tree built from the same input will have identical shapes.

### Rank and select queries

Augment each node with subtree_size = 1 + left_size + right_size. The size must be updated during insertion, deletion and rotations. To find the key of rank k in ascending order, compare k with the number of keys in the left subtree. If k equals left_size+1 in one-based indexing, the current node is the answer; if smaller, search left; otherwise subtract left_size+1 and search right. The traversal follows one root-to-leaf path, so a balanced tree supports select in logarithmic time. A rank query computes how many stored keys precede a target using the same metadata.

For example, given keys [2,4,6,8,10,12,14], select(4) returns eight. A tree lacking subtree-size fields can still answer by complete inorder traversal, but then the worst-case work is linear. This demonstrates the broader theme of data structure augmentation: maintain extra information at update time to accelerate queries later. The tradeoff is not free; every mutation must keep the augmented invariant synchronized.

### Trees on disk and in memory

A B-tree stores several keys per node and keeps all leaves at the same depth. A B+ tree usually stores payload references at leaves and uses internal separator keys for navigation, making range scans efficient through linked leaves. Both are important for external-memory settings because fetching a disk or storage page can be much more expensive than comparing several keys already in memory. A binary tree with pointer-sized nodes may have reasonable CPU comparisons yet incur many cache or storage misses.

### Test plan

Generate insertion and deletion sequences while maintaining a separate sorted reference array. After each mutation, confirm inorder traversal equals the reference, each key's search result agrees, subtree sizes add up and balance invariants hold. Include deleting a leaf, a root with one child, a root with two children and repeated key insertion under the selected duplicate policy. A height animation alone is not sufficient to certify any of these structural invariants.


## Additional original authored teaching sections

# Search trees as maintained invariants rather than pictures

A search tree is correct only when every node respects the ordering rule implied by the comparator. For a binary search tree without duplicate keys, all keys in a node's left subtree are smaller than the node's key, and all keys in its right subtree are larger. The condition must hold over entire subtrees, not merely between a parent and its immediate children. A tree whose root is ten and whose left child is five appears reasonable, but if the left child has a right descendant twelve, the root's global invariant has already been violated. Searching for twelve will proceed to the right subtree of ten and miss the misplaced value. A validator that checks only direct children can pass this invalid tree.

A stronger recursive validator carries an allowed lower and upper key bound into each subtree. At the root, the bounds are unbounded. Visiting a left child tightens the upper bound to its parent's key; visiting a right child tightens the lower bound. If the current key violates either bound, the validation fails. Equal keys need a deliberate policy: reject, count duplicates at one node, or use a stable composite key. Without that decision, the inequality in the recursive validator is ambiguous and deletion behavior may depend on insertion history.

The height of a binary tree is the maximum number of edges on a root-to-leaf path, under one common convention. A balanced tree with n nodes has height proportional to the logarithm of n; a degenerate chain has height proportional to n. The complexity of searching an ordinary binary search tree is proportional to its height because one comparison chooses which subtree to search next. Inserting sorted keys without rotations constructs a chain in a naïve implementation, showing that the search-tree property itself does not imply the height guarantee. A height guarantee is provided by the invariants of AVL trees, red-black trees, or another balancing scheme, not by the vocabulary of tree navigation.

An AVL tree stores or computes subtree heights and maintains their difference at no more than one at every node. After insertion, only nodes along the path from the new leaf to the root can have changed height. Rotations restore the local balance without altering inorder sequence. Consider keys 30, 10, 20 inserted into an empty AVL tree. The root 30 becomes left-heavy, while its left child 10 is right-heavy. Rotating left at 10 and then right at 30 yields root 20 with children 10 and 30. Both local rotations update child links, and any cached heights or parent links must be repaired. An implementation that rotates pointers but leaves the height metadata stale may behave correctly for this insertion and fail after the next one.

Deletion deserves separate reasoning because removing a node can shorten a subtree and trigger balancing at multiple ancestors. In a plain binary search tree, a node with two children is often replaced logically by its inorder successor, which has no left child. For a map, copying the successor's key without its associated value corrupts key–value pairing. In a balanced tree, deleting the successor may change heights or colors and require additional transformations. Test deletion of roots, leaves, nodes with one child, and nodes with two children; also test repeated deletion and the empty state. Correct inorder traversal after each operation is necessary but not sufficient to prove height balance.

An order-statistic tree augments each node with the size of its subtree. If a node has left subtree size L, then it is the element of rank L+1 in its own subtree, using one-based ranks. To select rank k, move left if k is at most L; return the current node if k equals L+1; otherwise move right after subtracting L+1 from k. The augmentation permits select and rank queries along one search path, provided all subtree sizes remain correct after every insertion, deletion, and rotation. The additional metadata costs storage and maintenance work but can replace a full inorder scan per query.

# Multiway trees, block access, and disk-conscious index design

Binary search trees are a natural mental model for pointer-based data structures, but storage engines often prioritize fewer page reads over fewer comparisons. A B-tree groups many sorted keys into each node. One page read can reveal dozens or hundreds of separator keys and direct the search into one of several child pages. If a page holds many keys, tree height can remain small even for millions of entries. The search cost should then be separated into page transfers and in-memory comparisons within a page. A larger node can increase comparisons slightly while reducing expensive page transfers substantially.

A B+ tree commonly keeps complete key–record references at leaves while internal nodes act primarily as navigation indexes. Leaf pages are often linked in key order so that a range query can scan neighboring pages without returning to the root. Suppose a database asks for all invoices with dates within one month. A B+ tree indexed by date can descend to the first matching leaf and scan sequentially, while a hash table keyed by invoice identifier offers no comparable ordered access. The choice follows the query semantics: equality-only lookups and ordered range scans have different requirements.

Tree search must handle the distinction between key comparison and collation. Two strings may be compared lexicographically by bytes, case-folded text, normalized Unicode, or locale-sensitive collation rules. Changing the comparator after constructing an index can invalidate its ordering invariant even though the stored bits have not changed. The index therefore needs a stable comparator definition and, in durable storage, potentially a version of the collation policy. A user-visible 'sort order' change is not merely a visual preference when persisted search trees rely on that order internally.

Page splits illustrate why update paths matter. When a B-tree page is too full to accept another key, it may be split into two pages and a separator inserted into the parent. If the parent is also full, splitting can propagate toward the root, increasing tree height. A correct implementation must preserve key ordering, node occupancy constraints, and reachable references despite the split. In a database, an interrupted update can leave pages inconsistent unless the storage engine provides logging, atomic page updates, or a copy-on-write strategy. The in-memory correctness proof is not the entire durability proof.

A prefix trie solves a different search problem by branching on symbols of a key instead of comparing complete keys at each node. Looking up a string of length L visits positions along the string, with time proportional to L under fixed-time transition access. A naïve trie can allocate many sparse nodes, especially when its alphabet is large. Radix trees compress chains of single-child nodes by storing substrings on edges. Prefix search and autocomplete often benefit, but memory cost depends on child representation, alphabet, and key distribution. It is important not to describe every trie as memory-efficient or to assume that all words of the same length visit the same number of allocated objects.

A high-quality search index assessment uses operations, not labels. Measure point lookups, sequential range scans, insertions, deletions, and prefix queries separately. Verify every result against a sorted reference collection. Inject duplicate keys, empty strings, long common prefixes, out-of-range rank requests, and deleted keys. For external-memory trees, simulate or measure storage page reads and the frequency of page splits and merges. For tries, count allocated nodes and outgoing transitions. Only then can you justify which representation fits a real application, such as a course directory, product autocomplete, or historical event archive.
