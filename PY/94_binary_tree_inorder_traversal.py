# 94. Binary Tree Inorder Traversal My Submissions QuestionEditorial Solution
# Total Accepted: 126454 Total Submissions: 316388 Difficulty: Medium
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# 
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Recursive
class Solution(object):
    def inorderTraversal(self, root):
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
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)


# Iterative 
from collections import deque
class Solution(object):
    def inorderTraversal(self, root):
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
                d.append(cur)
                cur = cur.left
            else:
                cur = d.pop()
                res.append(cur.val)
                cur = cur.right
        return res
        













# Iterative 
from collections import deque

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        d = deque()     #queue only save parent node
        cur = root
        while d or cur:
            if cur:
                d.append(cur)
                cur = cur.left
            else:
                cur = d.pop()
                res.append(cur.val)
                cur = cur.right
        return res

# Recursive
class Solution(object):
    def dfs(self, root, res):
        if not root: return 
        if root.left: self.dfs(root.left, res)
        res.append(root.val)
        if root.right: self.dfs(root.right, res)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res) 
        return res
