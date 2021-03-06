# 111. Minimum Depth of Binary Tree  QuestionEditorial Solution  My Submissions
# Total Accepted: 127309
# Total Submissions: 402081
# Difficulty: Easy
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
