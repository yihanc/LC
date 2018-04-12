# 110. Balanced Binary Tree  QuestionEditorial Solution  My Submissions
# Total Accepted: 133064
# Total Submissions: 375787
# Difficulty: Easy
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 2018.04.07 With Cache 80ms
class Solution:
    def __init__(self):
        self.cache = {}
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        return abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
     
    def getHeight(self, root):
        if not root: return 0
        if root in self.cache: 
            return self.cache[root]
        
        if root.left in self.cache:
            l = self.cache[root.left]
        else:
            l = self.getHeight(root.left)
            self.cache[root.left] = l
        
        if root.right in self.cache:
            r = self.cache[root.right]
        else:
            r = self.getHeight(root.right)
            self.cache[root.right] = r
            
        self.cache[root] = max(l, r) + 1
        return max(l, r) + 1

# Without cache

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if ( abs(self.height(root.left) - self.height(root.right)) <= 1 and
            self.isBalanced(root.left) and self.isBalanced(root.right)):
            return True
        else:
            return False

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
