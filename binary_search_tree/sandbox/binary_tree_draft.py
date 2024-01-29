"""
	Copy out implementation in Recitation 6 to check I understand it completely
	2024-01-15

	# Okay no more time for this
	# - we've done a cursory review of this, let's just try to work through the leetcodes and be done with this section for today

"""

class Binary_Node():


	def __init__(A, x):
		A.item, A.left, A.right, A.parent = x , None, None, None
		# A.subtree_update()

	# Traversal order
	#   - Easy to understand
	def subtree_iter(A):
		if A.left:
			yield from A.left.subtree_iter()
		yield A
		if A.right:
			yield from A.right.subtree_iter()

	# Keep going left and keep going right
	#   - Also easy to understand
	def subtree_first(A):
		return A.left.subtree_first() if A.left else A

	def subtree_last(A):
		return A.right.subtree_last() if A.right else A

	# Finding before and after nodes in the traversal order
	#   - Not so easy to understand?
	#   - The issue is that you either walk up or walk down to get to it
	#   - Having parent pointers makes this algo easier
	def successor(A):
		# Try walking down to right to get it
		if A.right:
			# Right subtree exists...so the successor (in the linear ordering of values), will be the left most node of the right subtree
			return A.right.subtree_first()

		# Else have to walk up
		# - idea is current node, must be the successor of the predecessor
		# - rewatch the lecture to confirm this
		# - keep walking up the tree, until we walk up let
		while A.parent and (A is A.parent.right):
			A = A.parent
		return A.parent

	def predecessor(A):
		# Problem is symmetric, either walk down left to get pred, or have to go back up the tree
		if A.left:
			return A.left.subtree_last()

		while A.parent and (A is A.parent.left):
			A = A.parent
		return A.parent


	#
	#   Pre, post and level order traversal operations...
	#

	# TODO

	#
	#   Dynamic operations
	#
	def subtree_insert_before(A, B):
		pass
	def subtree_insert_after(A, B):
		pass
	def subtree_delete(A):
		pass


class Binary_Tree():
	def __init__(T, Node_Type = Binary_Node):
		pass
