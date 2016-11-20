# 108. Convert Sorted Array to Binary Search Tree  QuestionEditorial Solution  My Submissions
# Total Accepted: 90069
# Total Submissions: 229378
# Difficulty: Medium
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Similar to pre + inorder to bst
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums))
    
    def helper(self, nums, s, e):
        if s >= e:
            return None
            
        mid = s + (e - s) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, s, mid)
        root.right = self.helper(nums, mid+1, e)
        return root
        

