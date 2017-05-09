# 222. Count Complete Tree Nodes Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 58408
# Total Submissions: 215167
# Difficulty: Medium
# Contributor: LeetCode
# Given a complete binary tree, count the number of nodes.
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# 
# Subscribe to see which companies asked this question.

# Simple morris traversal TLS
# 2017.05.04 recursive
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        height = 0
        left, right = root, root
        while right:
            left = left.left
            right = right.right
            height += 1
        if not left:
            return (1 << height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
