
def selection_sort(A):
    """
        Intuition: for i = 0, ..., n - 1: pick ith highest one + put in position i
        - Kinda like how you might sort your hand when playing cards
        So this maintains a sorted prefix A[:i+1] (making it clear why it works)
    """
    print('\n', '----selection sort----')
    n = len(A)
    for i in range(n):
        min_idx = i

        # A[:i] is sorted, so need to find next elem for A[i]
        for j in range(i, n):
            if A[j] < A[min_idx]:
                min_idx = j

        A[min_idx], A[i] = A[i], A[min_idx]
        print(A)
    print()
    return A


def bubble_sort(A):
    """
        Intuition: repeated passes over array until no out of order elements
        - each pass will "bubble up" higher elements and "bubble down" smaller elements

        It's not formally apparent to me that this algorithm is _correct_ though?
    """
    print('\n', '----bubble sort----')

    n = len(A)

    for i in range(n):

        swapped = False

        for j in range(n - i - 1):
        #
        #   What is going on here???!
        #
        # for j in range(n - 1):
            # Why the n-i-1?
            # -
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
                print(A)

        if not swapped: break

    print()
    return A


def insertion_sort(A):

    """
        Intuition: Maintain a sorted prefix A[:i] for i = 1, ..., n - 1
        so each time we grab i + 1 and insert it into the sorted prefix array somewhere
        so that A[:i+1] is also a sorted prefix
    """
    print('\n', '----insertion sort----')
    n = len(A)
    for i in range(1, n):
        curr = A[i]

        # Insert curr in A[:i] so A[:i+1] is sorted prefix now
        # - need shift elements right to make the space for inserting
        j = i - 1
        while j >= 0 and curr < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = curr
        print(A)

    print()
    return A

def shell_sort(A):
    """
        This one I've actually completely forgot intuition-wise since doing 2521.
        Apparently meant to be an "improved insertion sort"

        CLRS CH2: "Knuth's discussion of insertion sort encompasses several variations of the algorithm. The most important of these is Shell's sort ... which uses insertion sort on periodic subarrays of the input to produce a faster sorting algorithm"
        Intuition about why it works:

        Efficacy depends on the h-sequence used
        - Idea: each h-sequence array we perform insertion sort, until h is >= size of array
        - voila, it's sorted.

    """

    """
        OH, this is not a divide and conquer algorithm at all!
        It's like using a sliding window of size h, and our objective is to swap the two elements at the end if they're out of place!
        - https://www.youtube.com/watch?v=ddeLSDsYVp8 makes it visually obvious what it's doing

        Does a lot of preprocessing to roughly put large elements on one end and small elements on the other
        and then we run insertion sort at the end

        It's basically insertion sort with some preprocessing to minimise large jumps

        When h = 1 we get insertion sort

        TODO: rewrite this to take various gap/h-sequences

    """
    print('\n', '----Shell sort----')

    # Knuth proposed using h-size of 3^k + 1
    # We need to determine a good starting gap size

    # For each gap siz
        # Do insertion sort on each gap


    #
    # Alternative implemenation to make it clear what's happenng
    #
    n = len(A)


    # h_sequence = [
    #     (3 ** k - 1)
    #     for k in range(n)
    #     if (3 ** k - 1) <= (n - 1)/9
    # ]

    # Initialise gap size
    h = 1
    while h < n / 3:
        h = h * 3 + 1


    while h: # for each gap size

        for i in range(h, n): # Start "window" at h
            tmp = A[i] # Save start of window which we may potentialyl ahve to swap
            j = i
            while j >= h and A[j - h] > tmp:
                # Do a swap because end eleements out of order
                A[j] = A[j - h]


                # Decrement h to shift the h-window
                j -= h

        h //= 3 # go to next element in the h-sequence to be our gap
    return A


def main():
    A = [ 63, 62, 61, 1000, 999, -1 ]
    print('input: ', A)
    #print(sorted(A))

    selection_sort(A.copy())
    bubble_sort(A.copy())
    insertion_sort(A.copy())
    shell_sort(A.copy())

if __name__ == '__main__':
    main()