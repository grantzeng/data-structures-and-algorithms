from linked_list import Linked_List

def run_linked_list_tests():
    numbers = [3, 4, 6, 788, 88, 8]

    # Test basic display
    ll = Linked_List()
    ll.build(numbers)
    ll.display()

    # Test basic getting
    ll.get_at(-1)
    ll.get_at(0)
    ll.get_at(6)
    ll.get_at(3)

    # Test basic setting
    ll.set_at(-1, 2323)
    ll.set_at(6, 2222)
    ll.set_at(0, 1)
    ll.set_at(2, 3)
    ll.display()

    # Insert first
    ll.insert_first(0)
    ll.insert_first(0)
    ll.insert_first(0)
    ll.display()

    # Delete first
    for i in range(3):
        ll.delete_first()
    ll.display()


if __name__ == '__main__':
    run_linked_list_tests()