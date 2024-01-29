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


"""
    This is a binary tree, but do preserve a linear/total ordering of elements
    - we're not just inserting willy nilly

"""


class BinaryNode:
    def __init__(self, x): 
        self.val = x
        self.left, self.right = None, None
        self.parent = None

    # Helpers used in functions for finding predecessors and successors etc.
    def subtree_first(self):
        return self if not self.left else self.left.subtree_first()

    def subtree_last(self):
        return self if not self.right else self.right.subtree_last()


    """
        Insert before/after current node, while maintaining traversal order
        - Idea is that: if there's nothing, then just insert
        - If there's something, then you need to find predecessor/successor
          of the current node and insert after(right) /before(left) of it

        Idea of pred/succ in this situation only works because we're treating self as the root of a subtree
        rather than looking at the whole tree?

    """

    def subtree_insert_before(self, new):
        if not self.left:
            self.left, new.parent = new, self
            return

        targ = self.left.subtree_last()
        targ.right, new.parent = new, targ
        return

    def subtree_insert_after(self, new):
        # Case 1:
        # - there's no right subtree, so we can just put the new node there
        if not self.right:
            self.right, new.parent = new, self
            return

        # Case 2:
        # need to find the successor, and then we need to put the node left of it
        # - treat self as root of the subtree
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

        # If we have a left subtree, then it's just the last node in that subtree
        if self.left: return self.left.subtree_last()

        # Otherwise need to go up the tree
        # - we need to find the node, where the current node is the _successor_
        #   of the node we're looking for (so relative to it, we're the subtree first of its right subtree)
        curr = self
        while curr.parent and curr.parent.left is curr:
            curr = curr.parent

        # Reached spot in tree where parent of curr has curr as the root
        # of its righb left subtree
        return curr.parent



    """
        Different ways of deleting current node
        - data swaps
        - four possible cases node can be at
        - recursive solution
    """

    def subtree_delete_by_data_swap_to_leaf(self):
        #
        #   The 6.006 way
        #
        #   Intuition:
        #   - Deleting a leaf? easy, just delete it and maintain parent pointers
        #   - Deleting root or anything else? Not so easy
        #       - have to do data swaps preserving traversal order, until at leaf and you can just remove
        #         want to push the data to a leaf and keep walking down
        #       - We don't modify the tree structure
        #
        if not self.parent:
            print('You will mess up the tree if you try to delete root node because no data structure to point to new root')
            return

        # Case 1: node is in middle of a tree
        # - need to swap data with successor or predecessor and recurse until data ends up a a leaf
        #
        if self.left or self.right:
            # We need to keep walking down the tree doing data swaps
            swap_data_with = self.predecessor() if self.left else self.successor()
            self.val, swap_data_with.val = swap_data_with.val, self.val
            return swap_data_with.subtree_delete()
        #
        # Case 2: node is a leaf
        # - just delete it (need to maintain parent's pointers)
        if self.parent:
            # Maintain parent pointers
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None

        return self

    def subtree_delete_by_cases(self):
        #
        #   See: https://www.youtube.com/watch?v=8K7EO7s_iFE
        #   Intuition: there's four possible cases of how this node can sit in a tree
        #   - leaf -> just remove it
        #   - has only right subtree/only left subtree
        #   - has both left and right subtrees
        #
        #   This involves actual pointer swaps\

        # After a bit more reading, this is similar to the algorithm in CLRS, we'll have a look at it tonight

        if not self.left and not self.right:
            if self.parent:
                if self.parent.right is self: self.parent.right = None
                if self.parent.left is self: self.parent.left = None

            self.parent = None

        elif not self.left and self.right:
            # Stick current right subtree as right subtree of predecessor
            pred = self.predecessor()
            pred.right, self.right.parent = self.right, pred

            # Clean up pointers on this node
            self.parent, self.right = None, None

        elif self.left and not self.right:
            # Symmetric problem to above
            succ = self.successor()
            succ.left, self.left.parent = self.left, succ
            self.parent, self.left = None, None

        elif self.left and self.right:
            # The node is in the middle of the tree
            # TODO: I don't really understand the algorithm here
            # ????
            # - join algorithm (I think)

            # See here: you need to perform a tree join
            # https://cgi.cse.unsw.edu.au/~cs2521/23T3/lectures/slides/week03wed-bsts.pdf
            #

            #
            #    I can't tell if this algorithm preserves traversal order or not
            #

            # Strategy:
            #  1.  "t_1 < t_2", so find left most of t_2, and stick t_1 as its left subchild
            least = self.right.subtree_first()
            least.left = self.left
            self.left.parent = least

            # Stick root of t2 on to parent
            if self.parent.left is self:
                self.parent.left = least
                least.parent = self.parent.left

            elif self.parent.right is self:
                self.parent.right = least
                least.parent = self.parent.right

            self.parent, self.left, self.right = None, None, None
            #
            #   Problems with this code:
            #    - If you call delete on root with this, you'll lose the pointer to the whole tree
            #   - but okay so long as the node you're deleting isn't root

        return self
