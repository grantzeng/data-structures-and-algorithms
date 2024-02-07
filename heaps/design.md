# Design

Distinction between sequence vs. set interface: whether ordering is _intrinsic_ (stored values have a (total) order) or _extrinsic_ (keys have a (total) order but the values don't)


Priority queue interface possible implementations (see 6.006 Recitation 8)
- (selection sort + array)
- (insertion sort + sorted array)
- (heap sort + binary heap)

Interface needs to offer:
```python
build(n)

insert(x)

delete_max()
```

I'm not entirely sure what's going on, so going to type up all the code in Recitation 8 to see what they're trying to do.


> INTERRUPT: Going to implement sorts first before I come back to this, because this depends on knowing them (2024-01-31)


# Priority queues reconsidered (2024-02-06)

> https://cgi.cse.unsw.edu.au/~cs2521/23T3/lectures/slides/week09mon-priority-queues.pdf
Basically the naive data structures (arrays, linkedlists and their ordered versions), you trade off O(1) insert for O(n) delete max or vice versa

Better idea is we can _store_ a binary tree in an array as its level order traversal. This avoid having to literally have a tree. I.e. implement pq with a binary heap


# Finalising implementation of heaps (2024-02-07)
Implement whatever is easiest first of the iterative or recursive versions, then come back and do a proper implementation. Grok their correctness first, before coming back to analyse trade-offs and time complexity.

Max heapify up works, trying to debug max heapify down, which isn't working.

Test case is basically make it do heapsort. It works now.

### Things
Can you explain _why_ your non-working solutions doesn't work? Seems to have a lot to do with error cases on array indexing.