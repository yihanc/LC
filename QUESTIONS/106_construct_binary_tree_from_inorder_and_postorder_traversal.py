# 106. Construct Binary Tree from Inorder and Postorder Traversal  QuestionEditorial Solution  My Submissions
# Total Accepted: 66057
# Total Submissions: 218150
# Difficulty: Medium
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeHelper(inorder, postorder, 0, len(inorder), 0, len(postorder))
        
    def buildTreeHelper(self, inorder, postorder, inS, inE, postS, postE):
        if inS >= inE or postS >= postE:
            return None
            
        root = TreeNode(postorder[postE-1])
        i = inorder.index(root.val)
        root.left = self.buildTreeHelper(inorder, postorder, inS, i, postS, postS + i - inS )
        root.right = self.buildTreeHelper(inorder, postorder, i+1, inE, postS + i - inS, postE-1)
        return root
