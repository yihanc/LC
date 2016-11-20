# 124. Binary Tree Maximum Path Sum  QuestionEditorial Solution  My Submissions
# Total Accepted: 75337
# Total Submissions: 309410
# Difficulty: Hard
# Given a binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.
# 
# For example:
# Given the below binary tree,
# 
#        1
#       / \
#      2   3
# Return 6.
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

# Recursive
class Solution(object):
    res = -sys.maxint -1
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumRtl(root)
        return self.res
        
    def sumRtl(self, root):
        if not root:
            return 0
        lMax = max(0, self.sumRtl(root.left))
        rMax = max(0, self.sumRtl(root.right))
        self.res = max(self.res, lMax + rMax + root.val)
        return max(lMax, rMax) + root.val
