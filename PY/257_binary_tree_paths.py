# 257. Binary Tree Paths Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 96677
# Total Submissions: 266874
# Difficulty: Easy
# Contributors: Admin
# Given a binary tree, return all root-to-leaf paths.
# 
# For example, given the following binary tree:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
# 
# ["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2017.03.25 Rewrite
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(line, node):
            line = line + "->" + str(node.val) if line else str(node.val)
            if not node.left and not node.right:
                res.append(line)
                return
            if node.left: dfs(line, node.left)
            if node.right: dfs(line, node.right)
        if not root: return
        res = []
        dfs("", root)
        return res

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        res = []
        self.dfs(res, [], root)
        return res
        
    def dfs(self, res, line, node):
        line = line + [str(node.val)]
        
        if not node.left and not node.right:
            res.append("->".join(line))
            return
        
        if node.left:
            self.dfs(res, line, node.left)
        
        if node.right:
            self.dfs(res, line, node.right)
        
        
        
