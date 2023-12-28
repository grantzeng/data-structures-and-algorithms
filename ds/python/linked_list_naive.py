#!/usr/bin/env python3.10

"""
    C-style implementation of a linked list
    - Purely if/for/while/else type structured constructs

    TODO:
    - Check if there's out of bounds errors here...I feel like there might be
"""
class Linked_List_Node: 
    def __init__(self, data):
        self.item = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    # def __iter__(self):

    def build(self, items):

        if not items:
            print('No items to build list with')
            return

        self.head = Linked_List_Node(items[0])
        curr = self.head
        self.size += 1

        for item in items[1:]:
            next = Linked_List_Node(item)
            curr.next = next
            curr = next
            self.size += 1

    def validate_index(self, index):
        if not(index < 0 or index > self.size - 1):
            return True

        print(f'Invalid index: {index}')
        return False


    def get_at(self, index):

        if not self.validate_index(index):
            return

        curr = self.head
        for i in range(index):
            curr = curr.next
        print(f'Item at {index}: {curr.item}')
        return curr.item

    def set_at(self, index, item):

        if not self.validate_index(index):
            return
            
        curr = self.head
        for i in range(index):
            curr = curr.next
        print(f'Item at {index} currently is {curr.item}')
        curr.item = item
        print(f'Item at {index} currently is now {curr.item}')


    def insert_first(self, item):
        new_node = Linked_List_Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1


    def delete_first(self):
        if not self.head:
            print('Nothing to delete')
            return

        temp = self.head
        self.head = temp.next
        self.size -= 1
        del temp


    def insert_at(self, index, item):
        if not self.validate_index(index):
            return

        if index == 0:
            self.insert_first(item)
            return

        # Normal case
        curr = self.head
        for i in range(index - 1):
            curr = curr.next

        new_node = Linked_List_Node(item)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def delete_at(self, index):
        if not self.validate_index(index):
            return

        if index == 0:
            return self.delete_first()

        curr = self.head
        for i in range(index - 1):
            curr = curr.next

        temp = curr.next
        curr.next = temp.next
        self.size -= 1
        return temp.item

    def insert_last(self, item):
        self.insert_at(self.size - 1, item)

    def delete_last(self):
        return self.delete_at(self.size - 1)

    def display(self):
        print(f'size: {self.size}')

        curr = self.head
        while curr:
            print(f'{curr.item} -> ', end='')
            curr = curr.next
        print('X')