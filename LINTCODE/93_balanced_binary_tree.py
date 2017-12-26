"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root: return True
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        return abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, root):
        if not root: return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
