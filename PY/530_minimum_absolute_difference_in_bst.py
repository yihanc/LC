# 530. Minimum Absolute Difference in BST Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 13959
# Total Submissions: 29591
# Difficulty: Easy
# Contributors:
# nagasupreeth
# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
# 
# Example:
# 
# Input:
# 
#    1
#     \
#      3
#     /
#    2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# Note: There are at least two nodes in this BST.


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: return
            dfs(node.left)
            if lastval[0] != None: 
                res[0] = min(res[0], abs(node.val - lastval[0]))
            lastval[0] = node.val
            dfs(node.right)
        
        res, lastval = [float('inf')], [None]
        dfs(root)
        return res[0]
