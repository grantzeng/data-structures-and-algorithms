"""
    Binary tree which preserves traversal order
    - Traversal order not ascribed any intrinsic meaning yet
    - Has parent pointers (but also you will need to try implement without parent pointers)
    
    TODOS:
    - ~~Work through insertion~~
    - Work through deletion
        - Easy solution: add overhead of parent pointers
            - hard, refactor to add in parent pointer
        - Hard solution: do without parent pointers

    FUTURE:
    - Implement sequence interface  with the tree you made
    - Ditto set interface

"""

class BinaryNode:
    def __init__(self, x): 
        self.val = x
        self.left, self.right = None, None
        self.parent = None

    """
        Insert before/after current node, while maintaining traversal order
        - Idea is that: if there's nothing, then just insert
        - If there's something, then you need to find predecessor/successor
          of the current node and insert after(right) /before(left) of it

        Idea of pred/succ in this situation only works because we're treating self as the root of a subtree
        rather than looking at the whole tree?

    """
    def subtree_first(self):
        return self if not self.left else self.left.subtree_first()

    def subtree_last(self):
        return self if not self.right else self.right.subtree_last()

    def subtree_insert_before(self, new):
        if not self.left:
            self.left, new.parent = new, self
            return

        targ = self.left.subtree_last()
        targ.right, new.parent = new, targ
        return

    def subtree_insert_after(self, new):
        if not self.right:
            self.right, new.parent = new, self
            return

        targ = self.right.subtree_first()
        targ.left, new.parent = new, targ


    """

        Delete current while maintaining traversal order
        - Uses parent pointers

        Looking for a successor or a predecessor
        - Either it's the left/right most node of the right/left subtree
          or you have to walk up the tree to find the node, whose predecessor/successor
          is the current node

        Re: walking up:
        - if looking for successor, then current node needs to the right most of the left subtree
            - so successor is the first node where you go up left instead of right
    """
    def successor(self):
        if self.right: return self.right.subtree_first()

        # Otherwise need to traverse UP the tree
        curr = self
        while curr.parent and curr.parent.right is curr:
            curr = curr.parent

        # Reached a spot in the tree where parent of curr has curr
        # as a left child (curr is the root of the left subtree of this node)
        return curr.parent

    def predecessor(self):
        if self.left: return self.left.subtree_last()

        curr = self
        while curr.parent and curr.parent.left is curr:
            curr = curr.parent

        # Reached spot in tree where parent of curr has curr as the root
        # of its righb left subtree
        return curr.parent

    def subtree_delete(self, targ):
        pass



    """
        Alternative deletion algorithm _not_ using parent pointers
    """
