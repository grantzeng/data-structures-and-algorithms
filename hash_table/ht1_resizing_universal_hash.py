"""
    Main changes:
    - Every slot is a "pointer" to a chain (recall I'm just prototyping)
    - Better hash function instead of modulus


    Crude resizing:
    - We keep the modulo hash
    - But instead just resize the array to a prime number
    - Force all entries to be linked lists, rather than mishmash of {None, {an integer}, {an ordered linked list pointer}}


    Resizing strategy:
    - Basically same as for dynamic array:
        - If it's "too full" i.e. > # elements exceed size of array, then double + reinsert (want to maintain O(1a) lookup)
        - If it's "too empty" i.e. elements is only occupying a quarter of the memory we've allocated, we can just halve it

    There are more subtleties to this, but that is something you'll have to come back to.


    Objectives are to:
    - Study resizing policy
    - Study hash function choice

    Heck I'm adding in the better hash function

    What to focus on: basic implementation/know how it works. We will have to do a more detailed analysis in to how to optimize this
    structure later and what tradeoffs you make. But you need a mental model first of how things work

    We _could_ resize table to be a prime number each time, but in practice we'd want memory blocks to be multiples of 2 to get then to line up
    (remember the _point_ of this Python is to prototype how all these data structures work)

"""
from math import ceil
from random import randint
# For implementing separate chaining
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class OrderedLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, x):
        if not self.head:
            self.head = Node(x)
            return

        prev, curr = None, self.head
        while curr and curr.val < x:
            prev, curr = curr, curr.next

        new = Node(x)
        new.next = prev.next if prev else None

        if prev:        prev.next = new
        else:           self.head = new
        # free curr if C

        self.size += 1

    def delete(self, x):
        prev, curr = None, self.head

        while curr and curr.val != x:
            prev, curr = curr, curr.next

        if not curr:
            print('Error: value does not exist')
            return

        if prev:        prev.next = curr.next
        else:           self.head = curr.next
        # free curr if C

        self.size -= 1

    def __repr__(self):
        return ' -> '.join(str(val) for val in self)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

class HashTable:

    def __init__(self, r = 200):
        self.table = []

        # Tracking usage
        self.count = 0

        # For nice hash functions
        self.large_prime = 2 ** 31 - 1        # Pick the biggest integer prime (which also happens to be a Mersenne prime)
        self.random_integer = randint(1, self.large_prime - 1)

        # For resizing
        self.fill_ratio = 0.5          # For arguments sake, say we always want to have double the amount of memory to number of items
        self._compute_bounds()
        self._resize(0)

    def __iter__(self):
        for chain in self.table:
            yield from chain

    def _hash(self, val,  table_size):
        # Universal hashes are in the form ((ak + b) mod p) mod m
        # - We will figure out later the theoretical reasons for why this is likely to spread out values in table
        # - mod m is to contain the resulting val to be a valid index for the table
        return ((self.random_integer * val) % self.large_prime) % table_size

    def _compute_bounds(self):
        self.upper_bound = len(self.table)
        self.lower_bound = len(self.table) * (self.fill_ratio ** 2)

    def _resize(self, required_size):

        if self.lower_bound < required_size < self.upper_bound:
            # print(f'Resizing not needed: {len(self.table)} memory usage is within [{self.lower_bound}, {self.upper_bound}]')
            return

        expansion_factor = ceil(1 / self.fill_ratio)
        new_size = max(required_size, 1) * expansion_factor
        table =  [ OrderedLinkedList() for _ in range(new_size) ]

        for elem in self:
            # Reinsert all existing elements
            table[self._hash(elem, new_size)].insert(elem)

        self.table = table
        self._compute_bounds()
        print(self)

    def insert(self, value):
        self._resize(self.count + 1)
        key = self._hash(value, len(self.table))
        self.table[key].insert(value)
        self.count += 1

    def delete(self, value):

        key = self._hash(value, len(self.table))
        self.table[key].delete(value)
        self.count -= 1

        self._resize(self.count - 1)


    def __repr__(self):
        return ''.join( f'{i}: {self.table[i]}\n' for i in range(len(self.table)))

def test():
    ht = HashTable()
    print(ht)
    for i in range(0, 1000, 10):
        ht.insert(i)
    # Try to get it to blow up

    for i in range(0, 1000, 10):
        ht.delete(i)

    # Try to get it table halve

    # Try to get it to keep halving






if __name__ == '__main__':
    test()
