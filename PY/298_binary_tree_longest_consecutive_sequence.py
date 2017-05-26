# 298. Binary Tree Longest Consecutive Sequence Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 27860
# Total Submissions: 68709
# Difficulty: Medium
# Contributor: LeetCode
# Given a binary tree, find the length of the longest consecutive sequence path.
# 
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
# 
# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

# 2017.05.21
# Preorder Traversal
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, lastval, last):
            res[0] = max(res[0], last)
            if not node: return
            next = last + 1 if node.val == lastval + 1 else 1
            left = helper(node.left, node.val, next)
            right = helper(node.right, node.val, next)

        if not root: return 0
        res = [0]
        helper(root, root.val, 1)
        return res[0]
    
