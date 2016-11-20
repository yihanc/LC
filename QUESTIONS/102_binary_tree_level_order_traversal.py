# 102. Binary Tree Level Order Traversal My Submissions QuestionEditorial Solution
# Total Accepted: 105249 Total Submissions: 318501 Difficulty: Easy
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# 
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Iterative, Stack
from collections import deque

class Solution(object):
    def levelOrder(self, root):
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
            node = cur[1]

            while len(res) <= dep:
                res.append([])
            res[dep].append(node.val)

            if node.left:
                d.appendleft([dep+1, node.left])
            if node.right:
                d.appendright([dep+1, node.right])

        return res
                
# Recursive
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """












# Iterative. FIFO Append left and pop right
from collections import deque

class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return [[]]
        res = [[]]
        d, dep = deque(), 0
        d.append((root, 0))
        while d:
            (cur, dep) = d.pop()
            while len(res) <= dep: res.append([])
            res[dep].append(cur.val)
            if cur.left: d.appendleft((cur.left, dep+1))
            if cur.right: d.appendleft((cur.right, dep+1))
        return res

# Recursive. Use Dep. This is Pre-order..
class Solution(object):
    def dfs(self, root, dep, res):
        while len(res) <= dep:
            res.append([])
        res[dep].append(root.val)
        if root.left: self.dfs(root.left, dep+1, res)
        if root.right: self.dfs(root.right, dep+1, res)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res
        
import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        t1 = TreeNode(3)
        t2 = TreeNode(9)
        t3 = TreeNode(20)
        t4 = TreeNode(15)
        t5 = TreeNode(7)
        t1.left = t2
        t1.right = t3
        t3.left = t4
        t3.right = t5
        self.assertEqual(Solution().levelOrder(t1), [ [3], [9, 20], [15, 7]])

    def test_1(self):
        t1 = TreeNode(3)
        t2 = TreeNode(9)
        t3 = TreeNode(20)
        t4 = TreeNode(15)
        t5 = TreeNode(7)
        t1.left = t2
        t1.right = t3
        t3.left = t4
        t3.right = t5
        self.assertEqual(Solution2().levelOrder(t1), [ [3], [9, 20], [15, 7]])

if __name__ == "__main__":
    unittest.main()
