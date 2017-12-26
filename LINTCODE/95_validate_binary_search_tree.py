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
    @return: True if the binary tree is BST, or false
    """
    
    def isValidBST(self, root):
        # write your code here
        if not root: return True
        return self.isValidBSTHelper(root, float('inf'), float('-inf'))
        
    def isValidBSTHelper(self, root, maxx, minn):
        if not root: return True
        lres = self.isValidBSTHelper(root.left, root.val, minn)
        rres = self.isValidBSTHelper(root.right, maxx, root.val)
        return root.val < maxx and root.val > minn and lres and rres
        
            
