# 95. Unique Binary Search Trees II My Submissions QuestionEditorial Solution
# Total Accepted: 56069 Total Submissions: 192960 Difficulty: Medium
# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# 
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# 
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)
    
    def dfs(self, start, end):
        res = []
        if start > end:
            res.append(None)
        
        for i in xrange(start, end+1):
            lcs = self.dfs(start, i - 1)
            rcs = self.dfs(i+1, end)
            
            for lc in lcs:
                for rc in rcs:
                    cur = TreeNode(i)
                    cur.left = lc
                    cur.right = rc
                    res.append(cur)
        
        return res
            
            
    













#
# Pretty Hard to think. 
# Trick is for start, end, generate left and right list for each level
# Then after dfs call. Loop through all left and right and get all the possible combination
# for i in xrange(1, n+1)
# left and right. generate left, generate right 
#
class Solution(object):
    def dfs(self, start, end):
        res = []
        if start > end: return []
        
        for i in xrange(start, end+1):
            left_children = self.dfs(start, i-1)
            right_children = self.dfs(i+1, end)
            
            for left_child in left_children or [None]:
                for right_child in right_children [None]:
                    cur = TreeNode(i)
                    cur.left = left_child
                    cur.right = right_child
                    res.append(cur)
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1, n)
