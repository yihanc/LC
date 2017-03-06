# 173. Binary Search Tree Iterator Add to List
# Description  Submission  Solutions
# Total Accepted: 79512
# Total Submissions: 200401
# Difficulty: Medium
# Contributors: Admin
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = deque()
        self.pushAll(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop()
        self.pushAll(cur.right)
        return cur.val
    
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

