# 270. Closest Binary Search Tree Value Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 32448
# Total Submissions: 83212
# Difficulty: Easy
# Contributor: LeetCode
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
# 
# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.


# 2017.05.21
# Inorder traversal
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def dfs(node):
            if not node or res == [target, target]: return
            if node.val == target:
                res[0], res[1] = node.val, node.val
            elif target < node.val:
                res[1] = node.val
                dfs(node.left)
            else:
                res[0] = node.val
                dfs(node.right)
                
        res = [float('-inf'), float('inf')]
        dfs(root)
        return res[0] if abs(res[0] - target) < abs(res[1] - target) else res[1]

