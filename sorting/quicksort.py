"""
    Broken implementations

"""


def lomuto_partition(A, lo, hi):
    pivot = A[lo]
    i = lo

    for j in range(lo + 1, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[lo] = A[lo], A[i]
    return i

def hoare_partition(A, lo, hi):
    pivot = A[lo]
    left, right = lo + 1, hi - 1

    while True:
        while left < right and A[left] < pivot: left  += 1
        while left < right and A[right] > pivot: right -= 1

        if left >= right:
            break

        A[left], A[right] = A[right], A[left]

    A[lo], A[right] = A[right], A[lo]
    return right

def quicksort(A, lo, hi): 
    if lo < hi: 
        pivot = lomuto_partition(A, lo, hi)
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