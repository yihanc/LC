# 107. Binary Tree Level Order Traversal II My Submissions QuestionEditorial Solution
# Total Accepted: 81920 Total Submissions: 239829 Difficulty: Easy
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
# 
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative. Use reverse?
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return [[]]
        res, dep = [[]], 0
        d = deque()
        d.append((root, dep))
        while d:
            (cur, dep) = d.pop()
            while len(res) <= dep: res.append([])
            res[dep].append(cur.val)
            print(res)
            if cur.left: d.appendleft((cur.left, dep+1))
            if cur.right: d.appendleft((cur.right, dep+1))
        return res[::-1]

import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        t1 = TreeNode(1)
        self.assertEqual(Solution().levelOrderBottom(t1), [[1]])
        
if __name__ == "__main__":
    unittest.main()
