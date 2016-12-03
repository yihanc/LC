# 113. Path Sum II  QuestionEditorial Solution  My Submissions
# Total Accepted: 96051
# Total Submissions: 319674
# Difficulty: Medium
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 12.03.2016 Rewrite BFS
from collections import deque
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        d = deque()
        d.append([root, [root.val], root.val])
        
        while d:
            cur, line, summ = d.pop()
            
            if not cur.left and not cur.right and summ == sum:
                res.append(line)
            
            if cur.left:
                d.appendleft([cur.left, line + [cur.left.val], summ + cur.left.val])
                
            if cur.right:
                d.appendleft([cur.right, line + [cur.right.val], summ + cur.right.val])
        
        return res

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, sum, res, [])
        return res
        
    def dfs(self, root, sum, res, line):
        if not root:
            return
        if not root.left and not root.right and sum == root.val:
            res.append(line + [root.val])
            return
        if root.left:
            self.dfs(root.left, sum - root.val, res, line + [root.val])
        if root.right:
            self.dfs(root.right, sum - root.val, res, line + [root.val])
        

