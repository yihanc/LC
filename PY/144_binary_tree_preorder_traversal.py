# 144. Binary Tree Preorder Traversal My Submissions QuestionEditorial Solution
# Total Accepted: 123003 Total Submissions: 305966 Difficulty: Medium
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Morris Traversal

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = cur
                    res.append(cur.val)
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
                    
        return res

# Iterative
from collections import deque

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        if not root:
            return []
        res = []
        d = deque()
        cur = root

        while d or cur:
            if cur:
                res.append(cur.val)
                if cur.right:
                    d.append(cur.right)
                cur = cur.left
            else:
                cur = d.pop()

        return res
                
            
# Recursive
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.dfs(root.left, res)


















# Iterative with stack

from collections import deque

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        res = []
        if not root: return res
        d = deque()
        d.append(root)
        while d:
            cur = d.pop()
            res.append(cur.val)
            if cur.right: d.append(cur.right)
            if cur.left: d.append(cur.left)

        return res
            

# Recursive
class Solution(object):
    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
