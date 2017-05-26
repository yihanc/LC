# 543. Diameter of Binary Tree Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 13092
# Total Submissions: 30666
# Difficulty: Easy
# Contributors:
# nagasupreeth
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# 
# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# Note: The length of path between two nodes is represented by the number of edges between them.
# 
# Show Company Tags
# Show Tags
# 

# 2017.05.25
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = [0]
        self.maxpath(root, res)
        return res[0]
    
    def maxpath(self, root, res):
        if not root: return 0
        left = self.maxpath(root.left, res) if root.left else 0
        right = self.maxpath(root.right, res) if root.right else 0
        res[0] = max(res[0], left + right)
        return max(left, right) + 1
