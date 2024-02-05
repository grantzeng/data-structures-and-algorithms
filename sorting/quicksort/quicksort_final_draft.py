"""
    Convention for specifying array slices I'm using is: 
    - Upper bounds are EXCLUSIVE
    - Indexing starts at 0 
"""

def partition(A, lo, hi):
    """
        CLRS strategy
        - due to Lomuto
        - Easier to understand. but slowe
    """

    pivot = A[hi - 1]  # Pick pivot as last element of array
    i = lo # Candidate position to put the pivot at

    for j in range(lo, hi - 1):
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
    left, right = lo + 1, hi # inclusive

    while True:
        while left <= right and A[right] >= pivot:
            right -= 1

        while left <= right and A[left] <= pivot:
            left += 1

        if left <= right:
            # Two elements on the wrong side: swap with each other
            A[left], A[right] = A[right], A[left]
        else:
            break

    # Put pivot in its pivot position
    A[lo], A[right] = A[right], A[lo]

    return right


def quicksort(A, lo, hi):
    if lo < hi:
        pivot = partition(A, lo, hi)
        # pivot = hoare_partition(A, lo, hi)
        quicksort(A, pivot, lo)
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