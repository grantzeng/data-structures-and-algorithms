"""

    Merge sort

"""

# TODO: implement in place mergesort
def merge(A, B):
    merged = []

    while A and B:
        if A[0] <= B[0]:   merged.append(A.pop(0))
        else:              merged.append(B.pop(0))

    if A:   merged.extend(A)
    if B:   merged.extend(B)

    return merged


def mergesort(A):
    if len(A) < 2:  return A
    mid = len(A) // 2
    left, right = mergesort(A[:mid]), mergesort(A[mid:])

    return merge(left, right)

"""

    Quick sort
    - Currently my codce is broken

"""

def partition(A, lo, hi):
    pivot = A[lo]

    left, right = lo + 1, hi
    while True:
        while left <= right and 1 <= right < len(A) and A[right] >= pivot: right -= 1
        while left <= right and 0 <= left < len(A) - 1 and A[left] <= pivot: left += 1

        if left > right: break

        # Swap two out of place elements with each other
        A[left], A[right] = A[right], A[left]

    # Put pivot at end of the left range
    # left > right
    # - right is at where pivot should go
    # - left has exceeded it
    A[lo], A[right] = A[right], A[lo]
    return right

def naive_quicksort(A, lo, hi):
    if lo >= hi: return A

    pivot = partition(A, lo, hi)
    naive_quicksort(A, lo, pivot - 1)
    naive_quicksort(A, pivot + 1, hi)

    return A

quicksort = lambda A: naive_quicksort(A, 0, len(A))




def main():
    import random
    random.seed(0)
    arr = [ random.randint(0, 100) for _ in range(100) ]

    assert (mergesort(arr) == sorted(arr))
    print(quicksort(arr))
    print(sorted(arr))

    assert (quicksort(arr) == sorted(arr))


if __name__ == '__main__':
    main()

    