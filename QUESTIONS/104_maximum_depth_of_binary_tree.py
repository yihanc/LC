# 104. Maximum Depth of Binary Tree My Submissions QuestionEditorial Solution
# Total Accepted: 147459 Total Submissions: 306278 Difficulty: Easy
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, dep):
        if not root: return dep
        dep_l = self.dfs(root.left, dep+1)
        dep_r = self.dfs(root.right, dep+1)
        return max(dep_l, dep_r)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)
