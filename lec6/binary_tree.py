"""
    Binary tree which preserves traversal order (traversal order currently has
    no meaning e.g. is a linear order if we were using it to implement a sequence
    interface)
    
    TODOS:
    - Work through insertion
    - Work through deletion
        - Easy solution: add overhead of parent pointers
        - Hard solution: do without parent pointers

    FUTURE:
    - Implement sequence interface  with the tree you made
    - Ditto set interface

"""

class BSTNode:
    def __init__(self, x): 
        self.val = x
        self.left, self.right = None, None 

    """
        Insert before/after current node, while maintaining traversal order
        - Idea is that: if there's nothing, then just insert
        - If there's something, then you need to find predecessor/successor
          of the current node and insert after(right) /before(left) of it

    """
    # These two sit a bit awkardly because there's other functions we'll want to implement that use them
    def subtree_first(self): return self if not self.left else self.left.subtree_first()
    def subtree_last(self): return self if not self.right else self.right.subtree_last()

    def subtree_insert_before(self, new):
        if self.left:
            self.left.subtree_last().right = new
            return

        self.left = new

    def subtree_insert_after(self, new):
        if self.right:
            self.right.subtree_first().left = new
            return

        self.right = new

    """
        Delete current while maintaining traversal ordr
    """

