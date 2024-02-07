"""
    Implementation of priority queue interface with a (max)binary heap

    The max heap invariant is that for all i (except

    Convention is that root is stored at heap[1] to keep index formulae simpler
    - Exercise: rewrite this to use zero indexing (issues with indexing arrays seem to be unusually frequent)
    - I think this is silly, but just follow this convention for now

    Broken priority queue implementation
"""

class PQ_Heap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = [ None ] * (self.capacity + 1)
        self.size = 0
    #
    #
    #   Insert/delete
    #
    #
    def build(self, A):
        for a in A:
            #print(self.heap)
            self.insert(a)

    def insert(self, x):
        #
        #   Idea, insert the item at the end of the array
        #   - Then fix it up if it violates the heap property (reorganise items on path to root so heap property maintained)
        #
        self.heap[self.size + 1] = x
        self.size += 1
        self._max_heapify_up()

    def delete_max(self):

        #
        #   Remove root value and replace with the last item
        #   - then fix the violation in sizing to restore heap property
        #

        if self.size == 0:
            return

        largest = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1

        self._max_heapify_down()

        return largest
    #
    #
    #   Functions for maintaining max-heap invariant
    #   - for all i except root, which has no parent, A[i] < A[i's parent]
    #   - root is max
    #

    def _max_heapify_up(self):


        # Insert inserts at the end, then we may have to swap values up
        idx = self.size # Start at where newest item was inserted

        while idx > 0:
            parent_idx = self._parent(idx)

            if self.heap[idx] > self.heap[parent_idx]:
                # Violation of max heap property (self > parent), so fix it up
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break

        # print(self.heap)

    def _max_heapify_down(self):
        i = 1

        # while 2 *  i < n
        while self._left_child(i) < self.size:

            # Default is swap with left child, but if right child is bigger, swap with it instead
            j = self._left_child(i)
            if j < self.size and self.heap[j] < self.heap[j + 1]:
                j += 1

            """ Error case when only having 1 item in the heap, something to deal with when you do proper implementation """
            if self.heap[i] >= self.heap[j]:
                break

            # All checks passed
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

        """
            First failed attempt at implementing max heapify down.
            - My main objection apart from it _not working_ is that it's not obvious when the while loop will terminate

            Can you explain _why_ this has gone wrong?
        """
        # """
        #     Iterative implementation
        #     - Exercise: do a recursive implementaiton
        # """
        # # Point of this function is to fix the violation of the (max) heap invariant which happened because we deleted at the root and took the element from end of the list
        # # - the 2521 implementation is confusing, because it's not immediately obvious what all the index operations are doing. But also that's how you'd do it in C
        # # - the 6.006 implementation is recursive...so many of their implementations are recursive!

        # """
        #     Intuition

        # """
        # # Track index of violating element
        # i = 1

        # while True:
        #     left, right = self._left_child(i), self._right_child(i)

        #     # Candidate position
        #     # - default to swapping with left child, but we always want to try swapping with the larger of the two children
        #     # - Also need to keep it a valid index
        #     j = left if self.heap[right] >= self.heap[left] and right < len(self.heap) else right

        #     if self.heap[i] >= self.heap[left]:
        #         # no need for and self.heap[i] > self.heap[right]: # we only need to check if only greater than left value, since they're adjacent
        #         # Element has been pushed down to a position where none of its children are greater than it
        #         break

        #     # Go down one level
        #     i = j
        # print(self.heap)

    #
    #   Indexing like this is only possible because enforce that corresponding binary tree is a complete tree
    #   - i.e. every level is filled, except possibly the last
    #   - Formulae will make sense if you just draw it out
    #   - Tries to keep resulting indexes in bounds
    #

    def _parent(self, i):
        idx = i // 2
        # idx = (i - 1) // 2
        return idx if i > 1 else i

    def _left_child(self, i):
        idx = 2 * i
        # idx = 2 * i + 1
        return idx if idx < self.size else i

    def _right_child(self, i):
        idx = 2 * i + 1
        # idx = 2 * i + 1
        return idx if idx < self.size else i


def main():
    import random
    n = 5
    random.seed(0)
    nums = list(range(n))
    # Simple test function
    # - Basically, make it do heap sort
    pq = PQ_Heap(n)
    pq.build(nums)

    sorted_nums = [ pq.delete_max() for _ in range(n) ]
    assert(sorted(nums, reverse=True) == sorted_nums)



if __name__ == '__main__':
    main()