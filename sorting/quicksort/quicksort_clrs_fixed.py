"""
    Python implementation of the quicksort in CLRS

    Rewrite all this assuming EXCLUSIVE bounds

"""

def partition(A, p, r):
    #print(f'{r} ({len(A)})')
    x = A[r - 1]
    i = p - 1

    # Alternative solution as using two pointers and slotting in the pivot at the end
    #
    for j in range(p, r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r - 1] = A[r - 1], A[i + 1]

    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q + 1, r)
    return A

def main():
    import random
    random.seed(0)
    arr = [ random.randint(0, 100) for _ in range(100) ]

    #for a, b, in zip(sorted(arr), quicksort(arr, 0, len(arr))):
    #    print(f'{a} : {b}')

    assert(sorted(arr) == quicksort(arr, 0, len(arr)))




if __name__ == '__main__':
    main()
