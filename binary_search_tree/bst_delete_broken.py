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

        if not u:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        elif u.parent.right == u:
            u.parent.right = v

        if v:
            v.parent = u.parent


    def delete(self, n):
        """ Delete node n in the tree """
        if not n.left or not n.right:
            if n.parent.left == n:      n.parent.left = None
            elif n.parent.right == n:   n.parent.right = None
            # free n
        elif not n.left:
            self._transplant(n, n.right)
        elif not n.right:
            self._transplant(n, n.left)
        else:
            s = n.successor()

            if s.right: # I'm not 100% sure this is correct?
                self._transplant(s, s.right)
                s.right = n.right
                s.right.parent = s

            self._transplant(n, s)
            s.left = n.left
            s.left.parent = s



