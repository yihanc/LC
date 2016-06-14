# 114. Flatten Binary Tree to Linked List My Submissions QuestionEditorial Solution
# Total Accepted: 83545 Total Submissions: 267206 Difficulty: Medium
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# 
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """


# Recursive Preorder
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return

        if root.left: self.flatten(root.left)
        if root.right: self.flatten(root.right)

        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
