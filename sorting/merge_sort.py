"""
    Intuition:
        divide and conquer

    Writing it in vaguely C style way.
"""

def merge(A, B):

    # Pythonic merge
    """
    merged = []

    while A and B:
        if A[0] < B[0]:     merged.append(A.pop(0))
        else:               merged.append(B.pop(0))

    if A:   merged.extend(A)
    if B:   merged.extend(B)

    return merged
    """
    # Explicitly manipulating indices (for when (I implement this in C))
    # - issue also here,  needs to store all of A and all of B - why did you put max(len A, lenB)?
    merged = [ None ] * (len(A) + len(B))
    k = 0
    #print(merged)

    # Two pointer merge
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged[k] = A[i]
            i += 1
        else:
            merged[k] = B[j]
            j += 1

        k += 1
    # print(merged)



    # Issue is here:
    # - using k (index variable for the re resulting list, as index for list a)
    while i < len(A):
        merged[k] = A[i]
        i, k = i + 1, k + 1


    while j < len(B):
        merged[k] = B[j]
        j, k = j + 1, k + 1

    return merged


def merge_sort(A):
    # Divide and conquer merging

    if len(A) < 2:
        # Array of one element is sorted
        return A

    mid = len(A) // 2

    left, right = merge_sort(A[:mid]), merge_sort(A[mid:])
    # @post: left and right are sorted arrays

    return merge(left, right)


def main():
    import random
    random.seed(0)
    # Simple debugging tests
    arr = [ random.randint(1, 1000) for _ in range(100) ]
    print(merge_sort(arr))
    assert(merge_sort(arr) == sorted(arr))

    arr = []
    print(merge_sort(arr))

    arr = [1]
    print(merge_sort(arr))

if __name__ == '__main__':
    main()

