"""
    Priority queue interface + implementations from recitation 8
    - Typing them out to understand how they work 

"""

# Base class
# - Really I want this to be an interface, but Python don't do no interfaces
class PriorityQueue:
    def __init__(self):
        self.A =[]

    def insert(self, x):
        self.A.append(x)

    def delete_max(self):
        #pass
        # Doesn't promise you the max yet
        # - leaves it to subclasses to sort things and dump max element at end
        if len(self.A) < 1: raise IndexError('Cannot pop from empty priority queue')
        return self.A.pop()

    @classmethod
    def sort(Queue, A):
        # Idea of pq sort is: shove it all in a max/minheap
        # - and we get sorted list out by repeatedly delete max/min
        pq = Queue()
        for x in A: pq.insert(x)
        out = [ pq.delete_max() for _ in A ].reverse()
        return out

class PQ_Array(PriorityQueue):
    """
        Implementation of PQ interface with array and selection sort
    """
    # Insert already correct

    # Delete only correct when we find maximal elem and swap to back for deletion
    def delete_max(self):
        # Swap max element with the end and call delete from super
        max_idx = 0

        #
        #   Not sure why he's implemented like values of A are key/value pairs?
        #   - So have rewritten some stuff to match this
        #
        for i, (key, _) in enumerate(self.A):
            if self.A[i].key < key:
                max_idx = i

        n = len(self.A)

        self.A[max_idx], self.A[n] = self.A[n], self.A[max_idx]

        return super().delete_max()


class PQ_SortedArray(PriorityQueue):
    """
        Imeplements PQ interface with a sorted aray and insertion sort
    """
    # Insert not correct because basic insert doesn't maintain sorting
    def insert(self, *args):
        # Shove into array (will cause invariant of being sorted to break)
        super().insert(*args)

        # Insertion sort the whole array to restore invariant
        #  - I think maybe implement all the sorting algorithms first and come back to this
        #    I don't understand what's going on
        i = len(self.A) - 1
        A = self.A

        while i >= 0 and A[i + 1].key < A[i].key:
            A[i + 1], A[i] = A[i], A[i+ 1]
            i -= 1


    # Delete already correct because invariant of being sorted guarantees last elem maximal


class PQ_Heap(PriorityQueue):
    """
        Implements PQ interface with heap sort and a binary heap
    """
    def insert(self, *args):
        pass

    def delete_max(self):
        pass


    #
    #   Navigating the heap
    #
    def parent(i):
        pass
    def left(i, n):
        pass
    def righ(i, n): 
        pass 

    #
    #   Maintaining heap invariant
    #
    def max_heapify_up():
        pass

    def max_heapify_down():
        pass

    #
    #   Container
    #
    def build_max_heap(A):
        pass
