# 235. Lowest Common Ancestor of a Binary Search Tree Add to List
# Description  Submission  Solutions
# Total Accepted: 124251
# Total Submissions: 323857
# Difficulty: Easy
# Contributors: Admin
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
# 
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# 
# Subscribe to see which companies asked this question.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2018.10.06
# self-write
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if root == p: return p
        if root == q: return q
        ll = self.lowestCommonAncestor(root.left, p, q)
        rr = self.lowestCommonAncestor(root.right, p, q)
        if not ll and not rr: return None
        if not ll: return rr
        if not rr: return ll
        return root

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q: return root
        lres = self.lowestCommonAncestor(root.left, p, q)
        rres = self.lowestCommonAncestor(root.right, p, q)
        return root if lres and rres else lres or rres
