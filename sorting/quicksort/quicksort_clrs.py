"""
    Python implementation of the quicksort in CLRS

"""

def partition(A, p, r):
    print(f'{r} ({len(A)})')
    x = A[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def main():
    import random
    random.seed(0)
    arr = [ random.randint(0, 100) for _ in range(100) ]

    print(sorted(arr))
    quicksort(arr, 0, len(arr))
    print(arr)


if __name__ == '__main__':
    main()
