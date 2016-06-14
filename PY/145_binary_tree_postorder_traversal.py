# 145. Binary Tree Postorder Traversal My Submissions QuestionEditorial Solution
# Total Accepted: 98882 Total Submissions: 276642 Difficulty: Hard
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative using deque
# Use one variable to check last node visited
from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, d = [], deque()
        cur = root
        lastNodeVisit = None
        while d or cur:
            if cur:
                d.append(cur)
                cur = cur.left
            else:
                peekNode = d.pop()
                if peekNode.right and peekNode.right != lastNodeVisit:
                    d.append(peekNode)
                    cur = peekNode.right
                else:
                    res.append(peekNode.val)
                    lastNodeVisit = peekNode
        return res


# Iterative using deque and isVisit
from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res, isVisit = [], {}
        d = deque()
        d.append(root)
        while d:
            cur = d.pop()   
            d.append(cur)   # no peek in deque
            if cur.right and cur.right not in isVisit: 
                d.append(cur.right)
            if cur.left and cur.left not in isVisit: 
                d.append(cur.left)
            if (not cur.right or cur.right in isVisit ) and (not cur.left or cur.left in isVisit):
                cur = d.pop()
                res.append(cur.val)
                isVisit[cur] = True
        
        return res

# Recursive
class Solution(object):
    def dfs(self, root, res):
        if not root: return 
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
