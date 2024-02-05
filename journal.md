# 2023-12-20
Stubbed dynamic array in C.


# 2023-12-28
> "Cookies are a _sometimes_ food...according to modern Cookie Monster" - Lec 2, 6.006 Erik Demaine

Trying to get myself to debug the dynamic array with gdb instead of by inspection.
- Issue seems to happen with resizing, some problems with array bounds, especially when cap ends up at zero.

```
ARRAY RESIZING POLICY


    Idea:
    - Make it s.t. if we do n inserts, it should cost us at most O(n) time, i.e.
      amortized O(1) versus the original policy with the dumb array where we do +1
      each time (so 1 insert costs O(n) time because of all the copying, which is
      the expensive operation we want to make rare)

    - If we're not really _using_ the allocated memory e.g. popped a lot of elements,
      we want to _deallocate_ extra space. But we also want to do this in amortized O(1).

    Resizing policy:
    - if items same as size, trigger table doubling.
    - if items < half of size, trigger table halving.

    Proof results in amortized O(1) insert_last:
    - Suppose we insert_last n items 1, 2, 3, ..., n

    - With table doubling policy, we pay O(n) resize cost (allocation and copying)
      every 1, 2, 4, ..., k=(nearest power of 2 less than n) which is just a geometric
      series \sum_{log k}{i=0} 2^i = 2^{k+1} - 1

    - but this is just O(.) of the highest term which is roughly 2^{\log(n)} so total cost is O(n)

    - voila, O(1) amortized across all n inserts

```

Just lots and lots of array index problems.

Definitely: set aside the code for a bit and come back to look at it from a different perspective (e.g. safety, time complexity etc., add ability to init data structure give static array etc. But for now just focus on making sure you understand the algorithm)

# 2024-01-02
Implemented singly linked list. But it's leaking memory like crazy. Exercise: uset tools to debug.


# 2024-01-23 Tue

Binary tree delete a node proving to be a bit tricky if you want do it by shuffling pointers around (I've spent 90 mins on this thing and I don't think it's 100% sunk in)
- New algo seems to _preserve_ traversal order but can you _prove_ it does?
- issue of deleting root

# 2024-01-28 Sun
Still not sure about delete algorithm when you have two children. It's not _obviously_ correct in some ways.

We're just going to move on to hashtables and come back to this later.


# 2024-01-29 Mon
Leetcode is down.

This morning:
- reimplemented bst delete
- implemented a crude hashtable

To do: take a break, then figureout how to use python debugger to debug my crappy hashtable.
- Debugging wasn't too hard

# 2024-01-30 Tue
Prototyped hash table with resizing, universal hashing and
- The point of having a large prime is to try to spread the elements out.

Need to think about theoretical considerations when it came to design. The more you look into it, the more subtleties there actually are to consider


# 2024-01-31 Wed
I'm tired of doing trees, so I'm just going to move on to heaps and come back to self balancing binary trees later.

PQ needed a better understanding of sorts, so moved on to implementing quadratic sorts

Correctness of quadratic sorts
- insertion, selection sort - correctness is clear because each round maintains `A[:i]` as a sorted prefix
- bubblesort - not quite so clear why it's correct (Is is correct because each suffix `A[n-i-1:]` array is sorted? idea is we bubble max up to `A[n-i-1]`?)
- Shellsort - give up for today, I can't recall why it worked.

# 2024-02-01 Thu

Implemented shell sort.
- "preprocessing" with gap in a gap sequence
- When gap = 1, we end up with insertion sort which we _know_ is correct.


# 2024-02-04 Sun

Implement (naive) mergesort (non-inplace - do this later)

Implementing (naive) quicksort (pivot is "pick left element of subarray")
- Trying to figure out partitioning
- Some issues with indexing array elems
- Currently ends up in an infinite loop?

Quick sort implementation is broken, but I can't quite see where it's gone wrong (seem like different implementations might have different array indexing?)

# 2024-02-05 Mon
Quicksort implementation is running into _a lot_ of array indexing problem. Actually, make that some _serious_ issues with why the array indexing is going out bounds for all my implementations of quicksort! Opportunity to learn how to use a debugger and analyse the algorithm/invariants etc.

Can't figure outwhy my implementations of partitioning weren't working, just have to come back to it later.
### After lunch around 3:21pm
Came back, fixed the Lomuto and Hoare partitioning schemes (issue was informally reasoning about invarinant of indicies being valid). Reimplement this tomorrow, and then implement it with inclusive indexing in function calls