"""
    Intuition behind quicksort

    - divide and conquer algorithm
    - for a partition
        - pick a pivot to make all elements to the left of it less than it and all elements of the right of it greater than it

    Pseduocode strategy
    1. Pick some pivot elem in A
    2. Partition arr into subarrs: (like median finding)
        - less than pivot
        - greater than pivot
    3. Recursively sort on subarrays l and g
    4. merge is trivial because you just concat the arrays (so can just do in place)


    Basically picking pivot is the isue here:
        - if you pick lo or hi of subarray you end up with unbalanced partitions and O(n^2)
        - ideally you pick the median to have roughly equally sized subarrays to consider

    Implementing better ways to pick pivots
"""

def partition(A, lo, hi):
    """
        Idea: need to reshuffule elements around the pivot so that the array looks like
        [ lt_pivot[:] pivot gt_pivot[:] ] and return WHERE the pivot is
    """


    # Say we pick do a simple/dumb way of picking pivot -> just pick lo eleme
    pivot = A[lo]

    # two pointers which go "inward" towards where pivot will be
    # - idea is that if they cross then we've done swapping things on either side -> can put our pivot in
    # - we want to swap elements that are on the wrong side of the pivot

    l, r = lo + 1, hi
    while True:

        # Increment l and r to a point where we find two elements that are on wrong side of pivot (so want to swap them) s
        while l <= r and A[r] >= pivot: r -= 1
        while l <= r and A[l] <= pivot: l += 1



        if l > r: break
        #if l == r:
        #    # Nothing left to fix
        #    break

        # Swap the elements (so they are on "the right side of the array")
        A[l], A[r] = A[r], A[l]
        #print(A)

    # Pivot goes to right of lo side
    # - only condition we want is "everything to left of pivot is less than it", and no other order constraints (hence no need to
    #   move any other elements)
    A[lo], A[r] = A[r], A[lo]
    return r



def naive_quicksort(A, lo, hi):
    #
    #   Sorting happens in-place
    #
    if lo >= hi:
        # print(f'Error: {lo} >= {hi}')
        return

    pivot = partition(A, lo, hi) # ???  Need to clarify why partitioning works
    naive_quicksort(A, lo, pivot - 1) # sort left subarray
    naive_quicksort(A, pivot + 1, hi) # sort right subarray

    return A


def main():
    import random
    random.seed(0)
    # Simple debugging tests
    arr = [ random.randint(1, 1000) for _ in range(100) ]
    # print(naive_quicksort(arr, 0, len(arr) - 1))
    assert(naive_quicksort(arr, 0, len(arr) - 1) == sorted(arr))

    # arr = []
    # print(naive_quicksort(arr, 0, 0))

    #arr = [1]
    #print(naive_quicksort(arr, 0, 1))


if __name__ == '__main__':
    main()