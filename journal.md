# 2023-12-20
Stubbed dynamic array in C.


# 2023-12-28
Trying to get myself to debug the dynamic array with gdb instead of by inspection.
- Issue seems to happen with resizing, some problems with array bounds, especially when cap ends up at zero.

```
ARRAY RESIZING POLICY

    "Cookies are a _sometimes_ food...according to modern Cookie Monster" - Lec 2

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