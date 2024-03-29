# 6.006-ocw

Repo for revising DSA stuff.

Mostly try to implement everything in both C and Python (not just Python)

Also: think about test writing/writing some tests (especially for C, or well at least think of test cases...even if you don't implement them...)


# Things to implement
> This is just the minimal set to focus on first

### Structures
Interfaces
- sequence interface (stack + queue)
- set interface (dict)

Data structures
- arrays
    - static array (skip)
    - ~~**dynamic array**~~ (DONE 2023-12-28; revise resizing behaviour)
    - sorted dynamic array
- linked list
    - **singly linked list**
    - doubly linked list
- hash tables
    - direct-access array
    - **hash table**
- trees
    - ~~**binary tree**/**balanced binary tree**~~ (DONE 2024-01-27; revise `subtree_delete()` to make sure you get it though)
- heaps
    - **binary heap**

> Point here is that: stack/queues etc. are really just interfaces on some of these structures "in memory"; so this seems like the minimal set I should implement

> Implement them in Python, then think about testing (on a separate day) from mindset of trying to break your implementation. Then implement them in C...with tests.

> Then move on to all the variations e.g. doubly linked list, splay trees, tries etc. go scout out the 2521 notes for what gets covered.

### Sorting algorithms
- insertion sort
- selection sort
- merge sort
- counting sort
- radix sort
- AVL sort
- heap sort

### Graph algorithms
- BFS
- DAG relaxation
    - DFS
    - Toposort
- Bellman-Ford
- Dijkstra
- Johnson
- Floyd-Warshall


# What we care about?

Design trade-offs (what is this optimized for?)

Performance (mostly time complexity, but also space complexity in passing )

Correctness/proofs of correctness
- also informal explanations of "why it works"


# Change of plan 2024-01-28

Implement all the data structures first

Then implement all the algorithms

It's not really 6.006 but there's bits and pieces of it

Implement everything in Python first - because I'm trying to grok the algorithm's correctness (and time complexity, but mostly point of this exercise is that it should be obvious to me why a solution is/isn't correct)
- then we'll reimplement everything in C so can I do stuff with memory

