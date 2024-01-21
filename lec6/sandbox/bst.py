"""

    Basic binary search tree
    - Implement set operations

    Things we've changed
    - No parent pointer
    - No subtree doing in order traversal
    - To do: implement any recursive solution, iteratively
    - Slightly more readable variable names (questionable...)

    Implement basic tree functionality and then use later to implement a set
    or a sequence interface

"""

"""
    Change of plan:
    - BSTree class should just be a container and most logic implemented at subtree level
    - IF I want to, I could do it iteratively later, but from what I can tell solutions are ugly

    - do basic tree class (forget about parent pointers, we can add parent pointers when we have an operation we need to modify)


    BST invariant:
        left < curr < right



"""

class BSTNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    """
        Some operations for maintaining traveral order
        - which we will give semantic meanings later
    """

    def subtree_right(self):
        return self.subtree_right(self.right) if self.right else self

    def subtree_first(self):
        return self.subtree_first(self.left) if self.left else self

    def subtree_insert_after(self, new):

        if not self.right:
            self.right = new
            return

        # Preserve traversal order by inserting "left" to be lower than the "minimal element for the subtree
        self.subtree_first(self).left = new


    def subtree_insert_before(self, new):
        # Problem is symmetric to subtree_insert_after
        if not self.left:
            self.left = new
            return

        self.subtree_last(self.left).left = new

    def delete(self, x):
        pass

    """
        Mostly query operations (e.g. traverse, find height of tree etc.)
    """

class BSTree:

    def __init__(self):
        self.root = None
        self.size = 0


class Set_BST:
    pass
    """
        Implement set interface with BST

    """


"""

    Todo:
    - focus on insert + delete
    - write some plans about how you're gonna clean this code up


"""