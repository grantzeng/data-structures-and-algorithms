"""
    Implementation of priority queue interface with a (max)binary heap

    The max heap invariant is that for all i (except

    Convention is that root is stored at heap[1] to keep index formulae simpler
    - Exercise: rewrite this to use zero indexing (issues with indexing arrays seem to be unusually frequent)

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

    def insert(self, x):
        #
        #   Idea, insert the item at the end of the array
        #   - Then fix it up if it violates the heap property (reorganise items on path to root so heap property maintained)
        #
        self.heap[self.size + 1] = x
        self.size += 1
        self.max_heapify_up()

    def delete_max(self):

        #
        #   Remove root value and replace with the last item
        #   - then fix the violation in sizing to restore heap property
        #

        if self.size == 0:
            return

        largest = self.heap[1]
        self.heap[1] = self.heap[self.size]
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
            parent_idx = self.parent(idx)

            if self.heap[idx] > self.heap[parent_idx]:
                # Violation of max heap property so fix it up
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break

    def _max_heapify_down(self):
        # Delete inserts last element at root
        # - Then we need to push this down
        idx = 1  # element causing violation is at root

        pass
        #
        #
        #   Not so sure about how to do this
        #
        #

    #
    #   Indexing like this is only possible because enforce that corresponding binary tree is a complete tree
    #   - i.e. every level is filled, except possibly the last
    #
    #   - Keeps resulting indexes in bounds

    def _parent(i):
        idx = i // 2
        # idx = (i - 1) // 2
        return idx if i > 0 else i

    def _left_child(i, n):
        idx = 2 * i
        # idx = 2 * i + 1
        return idx if idx < n else i

    def _right_child(i, n):
        idx = 2 * i + 1
        # idx = 2 * i + 1
        return idx if idx < n else i


def main():
    pass

if __name__ == '__main__':
    main()