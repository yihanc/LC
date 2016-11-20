# 100. Same Tree My Submissions QuestionEditorial Solution
# Total Accepted: 131037 Total Submissions: 301443 Difficulty: Easy
# Given two binary trees, write a function to check if they are equal or not.
# 
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
# 
# Subscribe to see which companies asked this question
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Both None. True
        if not p and not q: return True
        
        # Only one exists, False
        if (not p and q ) or (p and not q): return False
        
        # Both exists. Test Value
        res_l = self.isSameTree(p.left, q.left)
        res_r = self.isSameTree(p.right, q.right)
        
        return (p.val == q.val) and res_l and res_r
