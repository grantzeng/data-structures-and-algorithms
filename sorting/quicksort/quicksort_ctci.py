"""
    Implementation from  CTCI 
    - This one also has indexing problems, but it's not clear to me why


"""

def partition(A, left, right):
    pivot = A[(left + right) // 2]

    while left <= right:
        while A[left] < pivot: left += 1
        while A[right] > pivot: right -= 1

        if left <= right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 1, right - 1

    return left

def quicksort(A, left, right):
    index = partition(A, left, right)
    if left < index - 1:
        quicksort(A, left, index -1)

    if index < right:
        quicksort(A, index, right)




def main():
    import random
    random.seed(0)
    arr = [ random.randint(0, 100) for _ in range(100) ]

    assert (quicksort(arr, 0, 100) == sorted(arr))


if __name__ == '__main__':
    main()

