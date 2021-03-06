# 129. Sum Root to Leaf Numbers  QuestionEditorial Solution  My Submissions

# Total Accepted: 89353
# Total Submissions: 260777
# Difficulty: Medium
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# For example,
# 
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# Return the sum = 12 + 13 = 25.
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Note. Use instance var for res. 

# 1.1.2017 No static var.
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = [0]
        self.dfs(root, res, 0)
        return res[0]
    
    def dfs(self, root, res, cursum):
        if not root.left and not root.right:
            res[0] += 10 * cursum + root.val
            return
        
        if root.left: self.dfs(root.left, res, 10 * cursum + root.val)
        if root.right: self.dfs(root.right, res, 10 * cursum + root.val)

# DFS template..
class Solution(object):
    res = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, 0)
        return self.res
        
    def dfs(self, root, sum):
        if not root:
            return

        if not root.left and not root.right:
            self.res += 10 * sum + root.val
            return 
        
        self.dfs(root.left, 10 * sum + root.val)
        self.dfs(root.right, 10 * sum + root.val)
        
