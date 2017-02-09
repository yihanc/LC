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

# Recursive
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
        print(root.val, lres, rres)
        
        return lres and rres

class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root, None, None)
        
    def isValidBSTHelper(self, root, lmax, rmin):
        if not root: return True
        if not root.left and not root.right: return True
        
        l = True if lmax == None else False
        r = True if rmin == None else False
        
        if lmax != None and root.val < lmax: l = True
        if rmin != None and root.val > rmin: r = True
        
        return ( l and r and 
                self.isValidBSTHelper(root.left, root.val, rmin) and 
                self.isValidBSTHelper(root.right, lmax , root.val) )

import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        t1 = TreeNode(4)
        t2 = TreeNode(2)
        t3 = TreeNode(6)
        t4 = TreeNode(1)
        t5 = TreeNode(7)
        t6 = TreeNode(5)
        t7 = TreeNode(7)
        t1.left = t2
        t1.right = t3
        t2.left = t4
        t2.right = t5
        t3.left = t6
        t3.right = t7
        self.assertEqual(Solution2().isValidBST(t1), False)

if __name__ == "__main__":
    unittest.main()

