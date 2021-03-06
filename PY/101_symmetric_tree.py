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

# 2018.02.21
# Is symmetric

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, r1, r2):
        if not r1 and not r2: return True
        if not r1 or not r2: return False
        return r1.val == r2.val and self.isSymmetricHelper(r1.left, r2.right) and self.isSymmetricHelper(r1.right, r2.left)
        

# 2016.12.31 Rewrite
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, lc, rc):
        if not lc and not rc: return True
        if not lc or not rc: return False
        
        if ( lc.val == rc.val and 
            self.isSymmetricHelper(lc.left, rc.right) and
            self.isSymmetricHelper(lc.right, rc.left) ):
            return True
        else:
            return False

# 2016.09.21
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetricHelper(root.left, root.right)
        
    def isSymmetricHelper(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if not right and left:
            return False
        return left.val == right.val and self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)


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
