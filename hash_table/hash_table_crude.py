"""
    A crude hash table that can deal with integers:
    - hash function is just modulus
    - collision resolution by chaining
    - (does not resize based on load)
    - (does not offer order operations)
    - (implicitly assumes values to be inserted are from a set, but does not check this)
"""


# For implementing separate chaining
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class OrderedLinkedList:
    def __init__(self, vals):
        self.head = None
        self.size = 0
        for val in vals:
            self.insert(val)

    def insert(self, x):
        if not self.head:
            self.head = Node(x)
            return

        prev, curr = None, self.head
        while curr and curr.val < x:
            prev, curr = curr, curr.next

        new = Node(x)
        new.next = prev.next

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
        elems = []
        curr = self.head
        while curr:
            elems.append(str(curr.val))
            curr = curr.next
        return ' -> '.join(elems)


class HashTable:
    def __init__(self, cap=10):
        self.size = 0
        self.cap = 10
        self.table = [ None ] * self.cap

    def _hash(self, x):
        # Division hash is bad because not guaranteed inputs will be spread out
        # - e.g. if I insert 10, 20, 30, 40 ... you just get a linked list at index 0
        return x % self.cap

    def insert(self, x):
        key = self._hash(x)

        if self.table[key] is None:
            self.table[key] = x
        elif isinstance(self.table[key], OrderedLinkedList):
            self.table[key].insert(x)
        else:
            self.table[key] = OrderedLinkedList([self.table[key], x])

        self.size += 1

    def delete(self, x):
        key = self._hash(x)

        if self.table[key] is None:
            print(f'{x} does not exist in table')
            return
        elif isinstance(self.table[key], OrderedLinkedList):
            self.table[key].delete(x)
            self.size -= 1 # I think this will cause problems if try to delete non-existent element
            # Really the linked list should have a set interface on top of it

            # Might not exist in the linked list, which this doesn't handle
        else:
            if self.table[key] == x:
                self.table[key] = None
                self.size -= 1
            else:
                print(f'{x} does not exist in table')

    def search(self, k):
        return self.table[k] # May be an int, maybe be a linked list

    def __repr__(self):
        res = ''
        for i in range(self.cap):
            res += f'{i}: {self.table[i]}\n'
        return res

def main():
    ht = HashTable()
    for i in range(0, 100, 10):
        ht.insert(i)
    print(ht)
    #print(ht.search(0))
    for i in range(0, 100, 10):
        ht.delete(i)

    for i in range(10):
        ht.insert(i)

    #print(ht.search(1))
    #print(ht.search(0))
    print(ht)

if __name__ == '__main__':
    main()