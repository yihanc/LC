# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 2015.9.3

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.inorderTraversalHelper(root, res)
        return res
    
    def inorderTraversalHelper(self, root, res):
        if root.left:
            self.inorderTraversalHelper(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorderTraversalHelper(root.right, res)
