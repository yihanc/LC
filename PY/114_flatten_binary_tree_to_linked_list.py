# 114. Flatten Binary Tree to Linked List My Submissions QuestionEditorial Solution
# Total Accepted: 83545 Total Submissions: 267206 Difficulty: Medium
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# 
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 12.03.2016 Rewrite
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        cur, pre = root, None
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                pre = cur.left
                
                while pre.right:
                    pre = pre.right
                
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
        
        return

# Iterative. Easy solution..
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                end = cur.left
                while end and end.right:
                    end = end.right
                end.right = cur.right
                cur.right = cur.left
                cur.left = None
            
            cur = cur.right
            
        
            


# Recursive Preorder
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return

        if root.left: self.flatten(root.left)
        if root.right: self.flatten(root.right)

        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
