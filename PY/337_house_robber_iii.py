# 337. House Robber III Add to List
# Description  Submission  Solutions
# Total Accepted: 36659
# Total Submissions: 87135
# Difficulty: Medium
# Contributors: Admin
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
# 
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
# 
# Example 1:
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DP solution.
# res[0]. if root not robbed
# res[1]. if root is robbed

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.robsub(root)
        return max(res)
        
    def robsub(self, root):
        if not root: return [0, 0]
        
        l = self.robsub(root.left)
        r = self.robsub(root.right)
        
        res = [0, 0]
        res[0] = max(l[0], l[1]) + max(r[0], r[1])
        res[1] = root.val + l[0] + r[0]
        return res
        
        

