#!/usr/bin/env python3.10

"""
    Implementation with functional programming to make code cleaner to look at
    - Lots of recursion
    - (Basically see if you can come up with the same solution listed in the recitation without reading it
"""
class Linked_List_Node: 
    def __init__(self, data):
        self.item = data
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)


class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, items):
        for item in reversed(items):
            self.insert_first(item)

    def get_at(self, index):
        # assert self.head
        node = self.head.later_node(index)
        return node.item

    def set_at(self, index, item):
        # assert self.head
        node = self.head.later_node(index)
        node.item = item

    def insert_first(self, item):
        node = Linked_List_Node(item)
        node.next = self.head
        self.head = node
        self.size += 1

    def delete_first(self):
        # assert self.head
        item = self.head(item)
        self.head = self.head.next
        self.size -= 1

    def insert_at(self, index, item):
        # assert self.head
        if index == 0:
            self.insert_first(item)
            return
        new_node = Linked_List_Node(item)
        node = self.head.later_node(index - 1)

        new_node.next = node.next
        node.next = new_node

        self.size += 1

    def delete_at(self, index):
        if index == 0:
            return self.delete_first()

        # assert self.head
        node = self.head.later_node(index - 1)
        # assert node
        # assert node.next
        item = node.next.item
        node.next = node.next.next
        self.size -= 1
        return item

    def insert_last(self, item):
        self.insert_at(self.size, item)
        # self.insert_at(len(self), item) # Why not this?

    def delete_last(self):
        return self.delete_at(self.size - 1)

    def display(self):
        # Not recursive

        print(f'size: {self.size}')

        curr = self.head
        while curr:
            print(f'{curr.item} -> ', end='')
            curr = curr.next
        print('X')