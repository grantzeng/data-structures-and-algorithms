"""
    Convention for specifying array slices I'm using is: 
    - Upper bounds are EXCLUSIVE
    - Indexing starts at 0 
"""

def partition(A, lo, hi):
    """
        Lomuto partitioning scheme
        CLRS strategy
        - due to Lomuto
        - Easier to understand. but slower to implement

        Assume hi is NOT INCLUSIVE!

        The inclusive array index version of things forces i = lo - 1, which isn't a valid index, I'd
        prefer i was always a valid index'

        The strategy here is to "find where to put the pivot"
    """

    pivot = A[hi - 1]  # Pick pivot as last element of array
    i = lo # Init possible position to put i: put it on the far left

    for j in range(lo, hi - 1): # Check all possible positions to put pivot (i.e. everything except last element)
        if A[j] <= pivot: # Found an element smaller, so swap it with where pivot would be
            A[i], A[j] = A[j], A[i]
            i += 1

    # Put the pivot value at position i
    A[i], A[hi - 1] = A[hi - 1], A[i]
    return i


def hoare_partition(A, lo, hi):
    """
        Hoare's original strategy:
        - swap elements that are supposed to be on the left of the pivot with those supposed to be on the right
        of the pivot (essentially a two pointer search)

        - It's less obviously correct (i.e. can you tell by inspection you won't accidentally make things out of bounds?)
    """

    pivot = A[lo]
    # left and right index (this is basically a two pointer strategy; anyhow force them to be valid indicies)
    # - I dislike the inclusive indexing strategy because you end up with invalid array indices for Python
    left, right = lo + 1, hi - 1
    while True:
        # This is correct because right is initted at hi - 1 which is a valid index and lower bounded by left which is a valid index (so right is always valid)
        while right >= left and A[right] >= pivot:  right -= 1
        # Symmetric argument to above as to why left will always be a valid index
        while left <= right and A[left] <= pivot:   left += 1

        if left > right: break

        # Two elements on the wrong side: swap with each other
        A[left], A[right] = A[right], A[left]


    # Put pivot in its pivot position
    A[lo], A[right] = A[right], A[lo]

    return right


def quicksort(A, lo, hi):
    if lo < hi:
        #pivot = partition(A, lo, hi)
        pivot = hoare_partition(A, lo, hi)
        quicksort(A, lo, pivot)
        quicksort(A, pivot + 1, hi)

    return A


def main():
    import random
    random.seed(0)
    arr = [ random.randint(0, 100) for _ in range(100) ]

    for a, b, in zip(sorted(arr), quicksort(arr, 0, len(arr))):
        print(f'{a} : {b}')

    assert(sorted(arr) == quicksort(arr, 0, len(arr)))

if __name__ == '__main__':
    main()