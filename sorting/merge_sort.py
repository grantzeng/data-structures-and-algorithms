"""
    Intuition:
        divide and conquer

    Writing it in vaguely C style way.
"""

def merge(A, B):

    # Allocate result array
    merged = [ None ] * max(len(A), len(B))
    k = 0

    # Two pointer merge
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged[k] = A[i]
            i += 1
        else:
            merged[k] = B[j]
            j += 1

        k += 1

    if k < len(A):
        for k in range(k, len(A)):
            merged[k] = A[k]

    if k < len(B):
        for k in range(k, len(B)):
            merged[k] = B[k]

    return merged




def merge_sort(A):
    # Divide and conquer merging

    if len(A) < 2:
        # Array of one element is sorted
        return A

    mid = len(A) // 2

    left, right = merge_sort(A[:mid]), merge_sort(A[:mid])
    # Post, left and right are sorted arrays

    return merge(left, right)


def main():
    # Simple debugging tests
    arr = [ 66, 4, 3234,2, 123213, 669, -23]
    print(merge_sort(arr))

    arr = []
    print(merge_sort(arr))

    arr = [1]
    print(merge_sort(arr))

if __name__ == '__main__':
    main()

