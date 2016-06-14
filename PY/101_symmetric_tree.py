# 101. Symmetric Tree My Submissions QuestionEditorial Solution
# Total Accepted: 109502 Total Submissions: 320630 Difficulty: Easy
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# 
# For example, this binary tree is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Analysis:
# left.val == right.val
# isSym(left.left, right.right) and isSym(left.right, r

# Iterative

# Recursive
class Solution(object):
    def isSym(self, p, q):
        # Case p or q is None
        if not p and not q: 
            return True
        elif not p or not q:
            return False
        
        # Compare p.left and q.right
        if (not p.left and not q.right) or self.isSym(p.left, q.right):
            res_1 = True
        else:
            res_1 = False

        # Compare p.right and q.left
        if (not p.right and not q.left) or self.isSym(p.right, q.left):
            res_2 = True
        else:
            res_2 = False

        return res_1 and res_2 and (p.val == q.val)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isSym(root.left, root.right)
