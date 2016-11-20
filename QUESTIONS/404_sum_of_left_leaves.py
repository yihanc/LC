# 404. Sum of Left Leaves   QuestionEditorial Solution  My Submissions
# Total Accepted: 19529
# Total Submissions: 42991
# Difficulty: Easy
# Contributors: Admin
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        d = deque()
        d.append(root)
        res = 0
        
        while d:
            cur = d.pop()
            
            if cur.left and not cur.left.left and not cur.left.right:
                res += cur.left.val
            elif cur.left:
                d.appendleft(cur.left)
            
            if cur.right and (cur.right.left or cur.right.right):
                d.appendleft(cur.right)
            
        return res

