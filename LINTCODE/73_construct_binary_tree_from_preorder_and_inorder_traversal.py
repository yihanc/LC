"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if len(preorder) == 0: return None
        return self.buildTreeHelper(preorder, 0, len(preorder), inorder, 0, len(inorder))
    
    def buildTreeHelper(self, preorder, prel, prer, inorder, inl, inr):
        if prel == prer: return None
        
        node = TreeNode(preorder[prel])
        index = inorder[inl:inr].index(node.val)
        
        node.left = self.buildTreeHelper(preorder, prel+1, prel+1+index, inorder, inl, inl+index)
        node.right = self.buildTreeHelper(preorder, prel+1+index, prer, inorder, inl+index+1, inr)
        return node
