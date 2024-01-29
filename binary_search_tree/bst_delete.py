"""
    Try to implement BST delete from memory
    - intution is: 
        - three cases
        - two child case: 
            - has right subtree
            - no right subtree 

"""
class BSTNode:
    def __init__(self, val):
        self.x = val
        self.left = None
        self.right = None
        self.parent = None

    def subtree_min(self):
        return self.right.subtree_min() if self.right else self

    def successor(self):
        if self.right: return self.right.subtree_min()

        y, x = self, self.parent
        while x and x.right == y:
            y = x
            x = x.parent

        return y


class BSTree:
    def __init__(self):
        self.root = None

    def _transplant(self, u, v):
        """ Transplant subtree rooted at u with subtree rooted at v """
        if not u:                   self.root = v
        elif u.parent.left == u:    u.parent.left = v
        elif u.parent.right == u:   u.parent.right = v

        if v:                       v.parent = u.parent

    def _join(self, u, v):
        """ Given roots of two trees, join them into one tree """
        if not u or not v:          return u or v

        x = v.subtree_min()



    # def delete_incorrect(self, n):
    #     """ Delete node n in the tree """
    #     if not n.left:              self._transplant(n, n.right)
    #     elif not n.right:           self._transplant(n, n.left)
    #     else:

    #         s = n.successor()

    #         if s.right: # I'm not 100% sure this is correct?
    #             # This doens't work:
    #             # - try the example where the successor is n.right
    #             #   the pointers go everywhere and it's a bloody mess
    #             self._transplant(s, s.right)
    #             s.right = n.right
    #             s.right.parent = s

    #         self._transplant(n, s)
    #         s.left = n.left
    #         s.left.parent = s

    def delete(self, n):
        if not n.left:
            self._transplant(n, n.right)
        elif not n.right:
            self._transplant(n, n.left)
        else:
            s = n.successor()

            if n.right is not s:
                # successor is further down tree,
                # - need to extract it from its location and replace with its right child
                # - successor can't have left child (else that would be the successor!)
                self._transplant(s, s.right)
                s.right = n.right # Attach n's right children to s
                s.right.parent = s

            self._transplant(n, s)
            s.left = n.left  # Attach n's left children to n
            s.left.parent = s

        # n is now free
        # - if this was C, this would cause a memory leak

    # TODO
    # - Implement alternative bst_delete using 'tree_join'as a primitive
    # - Implement recursive bst_delete
    # - Implement bst_delete where you do data swaps to a leaf node, and delete the leaf instead of all this pointer stuff




