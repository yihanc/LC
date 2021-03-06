# 112. Path Sum  QuestionEditorial Solution  My Submissions
# Total Accepted: 122984
# Total Submissions: 381187
# Difficulty: Easy
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 12.03.2016 BFS Rewrite
from collections import deque
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        d = deque()
        d.append([root, root.val])
        summ = 0
        while d:
            cur, summ  = d.pop()
            
            if not cur.left and not cur.right and summ == sum: 
                return True
            
            if cur.left:
                d.appendleft([cur.left, cur.left.val + summ])
            if cur.right:
                d.appendleft([cur.right, cur.right.val + summ])
            
        return False
            
        

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
