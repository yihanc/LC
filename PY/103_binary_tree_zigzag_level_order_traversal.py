# 103. Binary Tree Zigzag Level Order Traversal My Submissions QuestionEditorial Solution
# Total Accepted: 61652 Total Submissions: 213308 Difficulty: Medium
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# 
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        d = deque()
        d.append([0, root])
        
        while d:
            cur = d.pop()
            dep = cur[0]
            cur = cur[1]
            
            while len(res) <= dep:
                res.append([])
            if dep % 2 == 0:
                res[dep].append(cur.val)
            else:
                res[dep] = [cur.val] + res[dep]
            
            if cur.left:
                d.appendleft([dep+1, cur.left])
            if cur.right:
                d.appendleft([dep+1, cur.right])    
        
        return res



#

from collections import deque

class Solution2(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        d = deque()
        res = [[]]
        dep = 0
        d.append((root, 0))
        
        while d:
            (cur, dep) = d.pop()
            while len(res) <= dep:
                res.append([])
            res[dep].append(cur.val)

            if cur.left: d.appendleft((cur.left, dep+1))
            if cur.right: d.appendleft((cur.right, dep+1))
        
        # After level order traversal then reverse
        for i, line in enumerate(res):
            if i % 2 == 1:
                line.reverse()
        
        return res
