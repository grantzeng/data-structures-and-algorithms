"""
    Implementing the BST specified in CLRS Ch 12
    - Difference is that for the binary tree implementation, we were more focused on
      maintaining the linear order

    NOTES:
    - The hardest thing to implement is actually subtree delete (if you don't cheat
      by just shuffling the data to a clean and decide you want to fiddle with pointers)
        - Problem with understanding the algorithm is _HOW_ to maintain the tree invariant
    - successor/predcessor/subtree_min/subtree_max are fairly obvious drawing it out

    TODO:
    - Single letter variable names probably could be replaced
    - Sanity check that you actually understand intuition of subtree delete
"""

class BSTNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
        # Easier to find a successor/predecessor with parent pointers (otherwise do
        # a find with trailing pointer for a cost of O(h))

    def delete(self):
        pass

    def subtree_min(self):
        return self.left.subtree_min() if self.left else self

    def subtree_max(self):
        return self.right.subtree_max() if self.right else self

    def successor(self):
        # If right subtree exists, then successor must be the minimal element in it
        # Otherwise, find node whose predecessor is this node

        if self.right: return self.right.subtree_min()

        y, x = self, self.parent
        while x and x.right == y:   y, x = x, x.parent

        return y

    def predecessor(self):
        if self.left: return self.left.subtree_max()

        y, x = self, self.parent
        while x and x.left == y:    y, x = x, x.parent

        return y

class BSTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        z = BSTNode(val)
        if not self.root: self.root = z; return

        # Traverse to a leaf node
        # - maintain trailing pointer to capture the node to insert at when x falls off the tree
        x, y = self.root, None
        while x:
            y = x
            x = x.left if z.val < x.val else x.right

        # Fiddle with pointers to _insert_ the new node
        z.parent = y
        if z.val < y.val:           y.left = z
        else:                       y.right = z

    def find(self, val):
        x = self.root
        while x:
            if x.val == val: return x
            x = x.left if val < x.val else x.right

        # Traversed off tree, meaning value not found
        return None

    def _transplant(self, u, v):
        # Replace subtree rooted at node u, with subtree rooted at node v
        # only jiggles parent pointers, caller must make sure children don't get lost :|
        #   - Pre:  u is not None

        if not u.parent:            self.root = v
        elif u == u.parent.left:    u.parent.left = v
        elif u == u.parent.right:   u.parent.right = v

        if v:                       v.parent = u.parent

    def delete(self, n):
        # Caller must give the reference to the node to be deleted
        # - Intuition: want to replace node, with its successor (but without screwing up tree
        #   invariant

        # Case 1: 0 children
        if not n.left and not n.right: n.parent = None

        # Case 2: 1 child
        if not n.left:              self._transplant(n, n.right)
        elif not n.right:           self._transplant(n, n.left)

        # Case 3: 2 children
        else:
            # Find successor to this node; we want to _replace_ n with its successor
            # - We know n has a right subtree, so this is really just a call to subtree_min()
            s = n.successor()

            if s is not n.right:
                # Problem: successor isn't immediate right
                # - replace successor with its right subtree
                #
                self._transplant(s, s.right)

                # This makesthe right subtree of n the right subtree of successor
                # now that we've torn it out of its original context
                s.right = n.right
                s.right.parent = s

            # Now ready to replace n with successor
            self._transplant(n, s)
            # Attach left subtree to successor
            s.left = n.left
            s.left.parent = s

            # Transplant is confusin
            # - really we want to combine the two subtrees into one tree
