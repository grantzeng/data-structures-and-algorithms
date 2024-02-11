"""
    Idea: 
    - Most operations for a binary search tree we can get to be O(h)
        e.g. find (binary search is logn), insert, delete, findmin,find max find prev, find x

    - Maintain balance to ensure O(logn) by locally fixing any violations
        - want to maintain traversal order

    Can add in iterators later but the point here was trying to grok the balance maintenance algorithm


    Main things to get done today:
    - Recapping how rotations work
    - Recap how rotations are used by AVL Tree to maintain height balance
"""

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    #
    #   Static operations/mostly just searching on subtree rooted at this node
    #
    def subtree_first(self):
        return self.left.subtree_first() if self.left else self

    def subtree_last(self):
        return self.right.subtree_last() if self.right else self

    def predecessor(self):
        if self.left: return self.left.subtree_last()
        else:
            curr = self
            while self.parent and self.parent.left is curr:
                curr = curr.parent
            return curr.parent

    def successor(self):
        if self.right: return self.right.subtree_first()
        else:
            curr = self
            while self.parent and self.parent.right is curr:
                curr = curr.parent
            return curr.parent


    #
    #   Dynamic operations on subtree rooted at this node
    #
    def insert_after(self, node):
        if not self.right:
            self.right = node
            node.parent = self
        else:
            insert_at = self.right.subtree_first()
            insert_at.left = node
            node.parent = insert_at

    def insert_before(self, node):
        if not self.left:
            self.left = node
            node.parent = self
        else:
            insert_at = self.left.subtree_last()
            insert_at.right = node
            node.parent = insert_at

    def delete(self):
        # Deletes the current node

        #
        #   TODO
        #
        pass


class BSTree:
    def __init__(self):
        self.root = None

    def build(self, X):
        pass

    def find(self, x):
        pass

    def insert(self, x):
        pass


    def delete(self, x):
        pass


class AVLNode(BSTNode):

    def update_heights(self):
        """
            Recursively updates heights
            - If nodes have not already been augmented with a height instance variable, it will add it
        """
        if not self:
            return -1
        else:
            self.height = 1 + max(
                self.update_heights(self.left),
                self.update_heights(self.right)
            )
        return self.height

    def skew(self):
        self.update_heights() # Refresh heights
        return self.right.height - self.left.height


    #
    #   Rotations are to reduce the height of the offending subtree
    #   - but still maintain BST invariant (so traversal order, which is the linear ordering of elems is the same)
    #       - "should not change data represented by the tree"
    #   - there's added complication of fixing up all the parent pointers
    #
    def rotate_left(self):
        if not self.right:
            print('Nothing to rotate')
            return






        self.update_heights()

    def rotate_right(self):
        if not self.left:
            print('Nothing to rotate')
            return

        # Just give names to all the things to make traversal order obvious
        # - Draw the diagram out!
        A, x, B, y, C = self.left.left, self.left, self.left.right, self, self.right


        x.right, y.left = y, B

        # How to fix parent pointers?

    def rebalance(self):
        # Also updates all the heights
        pass

class AVLTree(BSTree):
    def __init__(self):
        pass

    def insert(self, x):
        pass

    def insert(self, right):
        pass




