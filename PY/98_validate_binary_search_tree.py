# 98. Validate Binary Search Tree My Submissions QuestionEditorial Solution
# Total Accepted: 95020 Total Submissions: 451194 Difficulty: Medium
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Definition for a binary tree node.
#
# Inorder traversal
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 12.3.2016 Rewrite

import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate(root, sys.maxint, -sys.maxint-1)
        
    def validate(self, root, maxVal, minVal):
        if not root: return True
        
        if root.val >= maxVal or root.val <= minVal: return False
        
        lres,  rres = True, True
        if root.left: 
            lres = self.validate(root.left, root.val, minVal)
        if root.right:
            rres = self.validate(root.right, maxVal, root.val)
        
        return lres and rres
        

# Recursive
import sys

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root, sys.maxint, -sys.maxint-1)
            
    def isValidBSTHelper(self, root, ltMax, rtMin):
        if not root:
            return True
        
        if root.val >= ltMax or root.val <= rtMin:
            return False
        
        return self.isValidBSTHelper(root.left, root.val, rtMin) and self.isValidBSTHelper(root.right, ltMax, root.val)













# Recursive. It is valid only:
# 1. Left is valid, right is valid
# 2. max left < val and min_right > val
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right): 
            return True
        
        l, r = True, True
        if root.left: 
            max_l = root.left
            while max_l.right: 
                max_l = max_l.right
            l = ((max_l.val < root.val) and self.isValidBST(root.left))
        if root.right:
            min_r = root.right
            while min_r.left: 
                min_r = min_r.left
            r = ((min_r.val > root.val) and self.isValidBST(root.right))
            
        return l and r

import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        t1 = TreeNode(10)
        t2 = TreeNode(5)
        t3 = TreeNode(15)
        t4 = TreeNode(6)
        t5 = TreeNode(20)
        t1.left = t2
        t1.right = t3
        t3.left = t4
        t3.right = t5
        self.assertEqual(Solution().isValidBST(t1), False)

if __name__ == "__main__":
    unittest.main()
